"""Test für FB-S (Fehler-Bordkarten): tools/tests/fb_einspielen.py, Migration 20261210_fb_s_fehlerkarten.sql, Pakete tools/tests/aus/fb_s_*.sql.

Teil 1 (immer): Pakete und Migration auf dem Stand, Migration = Einspiel-Datei, je geänderter Funktion genau eine Stelle anders, Alt-Hashes = Repo-Stand,
  Wartezeit-Funktion = wdh_sperre_ab bis auf die Einstellung, alle übrigen Pakete unter tools/tests/aus/ byteidentisch zu origin/lernen-app.
Teil 2 (nur mit lokalem Postgres; NACHBAU tools/tests/fb_nachbau.py, NICHT die echte Datenbank) – zweimal: ohne ICU und mit ICU (en-US; RB_PG_ICU setzt eine andere):
  Probelauf (über execute wie der Projektleiter und direkt) rollt alles zurück; Einspielen; Zweitlauf; Verhalten (Schalter aus/an/Testkind, Wartezeit in Lerntagen,
  richtig gelöst, erneut falsch, Obergrenze, Tipp/2. Anlauf, mehrere, gesperrt, Lückenweg/zaehlt nein, Mischkarte Stufe, anderes Kind, wdh_aufgabe_da, Tagesrunde,
  Mischkarten-Einlösung, Zeitzone); Gegenprobe (veränderte Auswahl -> Abbruch); Negativfälle für den Paketschutz.
Aufruf: python3 -I tools/tests/fb_s_test.py   (endet mit OK)
"""
import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(WURZEL / 'tools/tests'))
import fb_einspielen as FB  # noqa: E402
import fb_nachbau as NB  # noqa: E402
import regelbezug_sql_test as T  # noqa: E402

AUS = WURZEL / 'tools/tests/aus'
W = 'schule.wdh_aufgabe_waehlen(bigint, bigint, text, boolean)'
M = 'schule.mischkarten(bigint, bigint, integer)'


def text(pg, sql):
    return pg.sql('\\pset tuples_only on\n\\pset format unaligned\n' + sql).strip()


def teil1():
    p = subprocess.run([sys.executable, '-I', 'tools/tests/fb_einspielen.py', '--pruefen'], capture_output=True, text=True, cwd=str(WURZEL))
    assert p.returncode == 0, p.stderr
    probe = (AUS / 'fb_s_probe.sql').read_text(encoding='utf-8')
    einsp = (AUS / 'fb_s_einspielen.sql').read_text(encoding='utf-8')
    assert FB.MIGRATION.read_text(encoding='utf-8') == einsp
    assert 'PROBELAUF bestanden' in probe and 'PROBELAUF' not in einsp and 'FB-S eingespielt' in einsp
    assert not re.search(r'(?im)^\s*(begin|commit|rollback|savepoint)\s*;', einsp + probe), 'kein BEGIN/COMMIT im Paket'
    assert ' exception when ' not in (einsp + probe).lower() and 'xmin' not in einsp + probe, 'keine Untertransaktion, keine xmin-Zählung'
    assert probe.split('\n')[[i for i, z in enumerate(probe.split('\n')) if not z.startswith('--')][0]].startswith("select set_config('lock_timeout'"), 'Zeitgrenzen zuerst'
    w_alt, w_neu, m_alt, m_neu = FB.waehlen_alt(), FB.waehlen_neu(), FB.mischkarten_alt(), FB.mischkarten_neu()
    assert (FB.md5(w_alt), len(w_alt)) == ('7a6d76c619d1edfb6cdd8ee4a4a5cb1f', 537) and (FB.md5(m_alt), len(m_alt)) == ('1d8a3466c1698cfe9d4d0dd00d5ca638', 5123)
    assert w_neu.replace(FB.W_NEU_STELLE, FB.W_ALT_STELLE) == w_alt and w_neu.count('fehlerkarte') == 1
    assert m_neu.replace(FB.M_NEU_STELLE, FB.M_ALT_STELLE) == m_alt and m_neu.count('fehlerkarte') == 1
    for t in (FB.md5(w_alt), FB.md5(w_neu), FB.md5(m_alt), FB.md5(m_neu)):
        assert t in einsp and t in probe
    ab = [h for h in FB.HILFEN if h[0] == 'schule.fehlerkarte_ab(bigint)'][0][3]
    assert ab.replace("schule.fehlerkarte_regel('fehlerkarten_pause_lerntage', 2)", "schule.wd_regel('wdh_sperre_lerntage', 3) - 1") == FB.sperre_ab_alt(), \
        'Wartezeit = Lerntag-Logik der Sperre (nur die Einstellung anders)'
    # alle übrigen Pakete byteidentisch zu origin/lernen-app
    namen = subprocess.run(['git', 'ls-tree', '--name-only', 'origin/lernen-app', 'tools/tests/aus/'], capture_output=True, text=True, cwd=str(WURZEL), check=True).stdout.split()
    assert len(namen) >= 40
    for n in namen:
        alt = subprocess.run(['git', 'show', f'origin/lernen-app:{n}'], capture_output=True, cwd=str(WURZEL), check=True).stdout
        assert hashlib.md5((WURZEL / n).read_bytes()).hexdigest() == hashlib.md5(alt).hexdigest(), n
    neu = sorted(p.name for p in AUS.iterdir())
    assert sorted(set(neu) - {Path(n).name for n in namen}) == ['fb_s_einspielen.sql', 'fb_s_probe.sql'], neu
    # öffentliches Repo: keine Namen, keine Schlüssel
    alles = einsp + probe + (WURZEL / 'tools/tests/fb_einspielen.py').read_text(encoding='utf-8') + (WURZEL / 'tools/tests/fb_nachbau.py').read_text(encoding='utf-8')
    assert not re.search(r'(?i)(eyJ[a-z0-9]{20}|sk-[a-z0-9]{20}|service_role)', alles)
    print(f'Teil 1 bestanden: Pakete auf dem Stand, je Funktion eine Stelle, {len(namen)} bestehende Pakete byteidentisch')
    return probe, einsp


# ---------- Daten ----------
GRUND = """
insert into schule.lernender (id, ist_test, zeitzone, klasse) values (1, false, 'Europe/Berlin', 7), (2, false, 'Europe/Berlin', 8), (3, true, 'Pacific/Kiritimati', 7);
insert into schule.block values (1, 'Ort 1', 1), (2, 'Ort 2', 1);
insert into schule.einheit (id, status, inhalt, block_id) values
  (1, 'freigegeben', '{"etappen": [{"lernziel": "A", "titel": "a"}, {"lernziel": "B", "titel": "b"}]}', 1),
  (2, 'freigegeben', '{"etappen": [{"lernziel": "C", "titel": "c"}]}', 2);
insert into schule.aufgabe (id, einheit_id, variante_gruppe, stufe, form, zaehlt, freigegeben) values
  (11, 1, 'A', 2, null, null, true), (12, 1, 'A', 2, null, null, true), (13, 1, 'A', 2, null, null, true), (14, 1, 'A', 2, null, null, true),
  (15, 1, 'A', 1, null, null, true), (16, 1, 'A', 2, 'lueckenweg', 'nein', true), (17, 1, 'A', 2, 'lueckenweg', null, true), (18, 1, 'A', 2, null, null, false),
  (19, 1, 'A', 3, 'fehler_detektiv', 'ja', true),
  (21, 1, 'B', 2, null, null, true), (22, 1, 'B', 2, null, null, true), (23, 1, 'B', 2, null, null, true),
  (31, 2, 'C', 2, null, null, true), (32, 2, 'C', 2, null, null, true);
insert into schule.karte_stand (lernender_id, einheit_id, lernziel, sitzt, sitzt_am, wdh_stufe, faellig_am) values
  (1, 1, 'A', true, now() - interval '60 days', 1, now() - interval '1 day'), (1, 1, 'B', true, now() - interval '60 days', 1, now() + interval '5 days'),
  (2, 1, 'A', true, now() - interval '60 days', 1, now() - interval '1 day'), (2, 1, 'B', true, now() - interval '60 days', 1, now() - interval '1 day'),
  (3, 1, 'A', true, now() - interval '60 days', 1, now() - interval '1 day');
"""
ALT_RICHTIG = [11, 12, 13, 15, 16, 17, 19, 18]          # Grundlage: lange her selbst gelöst, 11 am längsten -> normale Wahl 11


def v(l, a, d, richtig=True, hilfe=0, anlauf=1, misch=False, uhr='12:00'):
    """Versuch am Lerntag heute+d (Ortszeit des Kindes, Uhrzeit uhr)."""
    return (f"insert into schule.versuch (lernender_id, aufgabe_id, richtig, hilfe, anlauf, misch, am) values ({l}, {a}, {str(richtig).lower()}, {hilfe}, {'null' if anlauf is None else anlauf}, {str(misch).lower()}, "
            f"((schule.heute_tag({l}) + {d})::timestamp + time '{uhr}') at time zone (select zeitzone from schule.lernender where id = {l}));")


def lt(l, tage):
    return '\n'.join(f"insert into schule.lerntag values ({l}, 'Mathematik', schule.heute_tag({l}) + {d}, (select zeitzone from schule.lernender where id = {l})) on conflict do nothing;" for d in tage)


def grund(l):
    return '\n'.join(v(l, a, -40 + i) for i, a in enumerate(ALT_RICHTIG)) + '\n' + v(l, 14, -31) + '\n' + lt(l, range(-41, -30))


def regeln(an=1, pause=None, mx=None):
    s = f"update schule.regel set wert = '{an}' where schluessel = 'fehlerkarten_an';"
    if pause is not None: s += f"\nupdate schule.regel set wert = '{pause}' where schluessel = 'fehlerkarten_pause_lerntage';"
    if mx is not None: s += f"\nupdate schule.regel set wert = '{mx}' where schluessel = 'fehlerkarten_max';"
    return s


def szen(pg, sql, fragen):
    """sql + Fragen in EINER Transaktion, danach zurückgerollt. fragen: {name: sql-Ausdruck} -> {name: text}."""
    q = '\n'.join(f"select '{k}=' || coalesce(({e})::text, 'NULL');" for k, e in fragen.items())
    out = pg.sql('\\pset tuples_only on\n\\pset format unaligned\ndelete from schule.misch_ausgabe; delete from schule.versuch; delete from schule.lerntag;\n'
                 + sql + '\n' + q + '\nrollback;')
    return {k: re.search(rf'^{k}=(.*)$', out, re.M).group(1) for k in fragen}


def wahl(l, misch=False, lz='A'):
    return f"schule.wdh_aufgabe_waehlen({l}, 1, '{lz}', {str(misch).lower()})"


def fingerabdruck(pg):
    return text(pg, "select md5(string_agg(concat(p.oid::regprocedure::text, md5(p.prosrc), p.provolatile, p.prosecdef, p.proisstrict, p.proparallel, p.procost, p.proleakproof, "
                    "coalesce(p.proconfig::text, ''), coalesce(p.proacl::text, '')), '|' order by p.oid::regprocedure::text collate \"C\")) "
                    "|| (select md5(coalesce(string_agg(r::text, '|' order by r.schluessel collate \"C\"), '')) from schule.regel r) "
                    "|| (select md5(coalesce(string_agg(m::text, '|' order by m.id), '')) from schule.misch_ausgabe m) "
                    "|| (select md5(coalesce(string_agg(k::text, '|' order by k::text collate \"C\"), '')) from schule.karte_stand k) "
                    "|| (select count(*)::text from schule.versuch) || (select count(*)::text from pg_proc where pronamespace = pg_my_temp_schema()) "
                    "from pg_proc p where p.pronamespace = 'schule'::regnamespace;")


def bericht(out):
    m = re.search(r'Details: (\{.*\})', out)
    import json
    return json.loads(m.group(1))


def negativ(pg, einsp, aenderung, erwartet, name):
    pg.sql(aenderung + f"\ndo $fbt$ begin execute $fbtinhalt${einsp}$fbtinhalt$; end $fbt$;", erwartet_fehler=erwartet)
    return name


def mit_text(sig_kopf, b, zusatz=''):
    return f"create or replace function {sig_kopf} as $function${b}$function${zusatz};"


W_KOPF = "schule.wdh_aufgabe_waehlen(p_l bigint, p_e bigint, p_lz text, p_misch boolean) returns bigint language sql volatile set search_path to ''"
M_KOPF = "schule.mischkarten(p_lernender bigint, p_einheit bigint, p_anzahl integer default 8) returns jsonb language plpgsql set search_path to ''"


def negativfaelle_alt(pg, einsp):
    f = []
    w, m = FB.waehlen_alt(), FB.mischkarten_alt()
    A = 'FB-S ABBRUCH, Vorbedingung'
    f.append(negativ(pg, einsp, mit_text(W_KOPF, w.replace('limit 1;', 'limit  1;')), 'wdh_aufgabe_waehlen(bigint, bigint, text, boolean) weicht ab', 'Körper wdh_aufgabe_waehlen'))
    f.append(negativ(pg, einsp, f'alter function {W} strict;', A, 'STRICT'))
    f.append(negativ(pg, einsp, f'alter function {W} stable;', A, 'VOLATILE -> STABLE'))
    f.append(negativ(pg, einsp, f'alter function {W} security definer;', A, 'SECURITY DEFINER'))
    f.append(negativ(pg, einsp, f'alter function {W} cost 50;', A, 'Kosten'))
    f.append(negativ(pg, einsp, f'alter function {W} parallel safe;', A, 'Parallelität'))
    f.append(negativ(pg, einsp, f'alter function {W} leakproof;', A, 'leakproof'))
    f.append(negativ(pg, einsp, f"alter function {W} set search_path to public;", A, 'Einstellungen (search_path)'))
    f.append(negativ(pg, einsp, f'drop function {W};', 'Funktion fehlt: ' + W, 'fehlende Funktion'))
    f.append(negativ(pg, einsp, f"drop function {W}; create function schule.wdh_aufgabe_waehlen(p_x bigint, p_e bigint, p_lz text, p_misch boolean) returns bigint language sql volatile set search_path to '' as $function${re.sub(r'\bp_l\b', 'p_x', w)}$function$;",
                     A, 'Argumentname'))
    f.append(negativ(pg, einsp, f"drop function {W}; create function {W_KOPF.replace('returns bigint', 'returns integer')} as $function${w.replace('select c.id', 'select c.id::int')}$function$;", A, 'Ergebnistyp'))
    f.append(negativ(pg, einsp, mit_text(M_KOPF, m.replace('-- 1. verfallen', '-- 1.  verfallen')), 'mischkarten(bigint, bigint, integer) weicht ab', 'Körper mischkarten'))
    f.append(negativ(pg, einsp, f'alter function {M} stable;', A, 'mischkarten VOLATILE -> STABLE'))
    f.append(negativ(pg, einsp, f'alter function {M} immutable;', A, 'mischkarten IMMUTABLE'))
    neu_hilfen = '\n'.join(f"create or replace function {kopf}{art}as $function${t}$function$;" for s, kopf, art, t, c in FB.HILFEN)
    f.append(negativ(pg, einsp, neu_hilfen + '\n' + mit_text(W_KOPF, FB.waehlen_neu()), 'Zwischenzustand', 'Zwischenzustand: wdh_aufgabe_waehlen neu, mischkarten alt'))
    f.append(negativ(pg, einsp, neu_hilfen, 'Zwischenzustand', 'Zwischenzustand: nur die Hilfen neu'))
    h = FB.HILFEN[1]
    f.append(negativ(pg, einsp, f"create or replace function {h[1]}{h[2]}as $function$ select true; $function$;", 'ist vorhanden, aber nicht im neuen Stand', 'Hilfe mit anderem Körper'))
    f.append(negativ(pg, einsp, f"create or replace function schule.wdh_sperre_ab(p_l bigint) returns date language sql stable set search_path to '' as $function$ select current_date; $function$;",
                     'Bezugsfunktion schule.wdh_sperre_ab(bigint) weicht', 'Bezugsfunktion wdh_sperre_ab'))
    f.append(negativ(pg, einsp, f"alter function schule.misch_gueltig(bigint, schule.aufgabe, jsonb) volatile;", A, 'Bezugsfunktion misch_gueltig Eigenschaft'))
    f.append(negativ(pg, einsp, "insert into schule.regel values ('fehlerkarten_an', '\"ja\"', 'x');", 'ungültigen Wert', 'Regel ungültig (Text)'))
    f.append(negativ(pg, einsp, "insert into schule.regel values ('fehlerkarten_max', '99', 'x');", 'ungültigen Wert', 'Regel außerhalb des Bereichs'))
    f.append(negativ(pg, einsp, "alter table schule.versuch rename column anlauf to anlauf_x;", 'Spalte fehlt: schule.versuch.anlauf', 'Spalte fehlt'))
    return f


def teil2(probe, einsp, icu):
    if icu: os.environ['RB_PG_ICU'] = icu
    else: os.environ.pop('RB_PG_ICU', None)
    pg = T.PG(T.pg_bin())
    erg = []
    try:
        if icu: assert text(pg, "select datlocprovider from pg_database where datname = current_database();") == 'i'
        pg.sql(NB.nachbau_sql() + GRUND)
        z0 = fingerabdruck(pg)
        # --- Probelauf auf Daten ohne Versuche, dann mit Daten (Kind 1: Aufgabe 14 vor 3 Lerntagen falsch)
        out = pg.paket(probe, erwartet_fehler='FB-S PROBELAUF bestanden')
        assert 'Abweichungen AUS 0' in out and 'alt -> neu' in out and fingerabdruck(pg) == z0, out[-800:]
        pg.sql(grund(1) + grund(2) + grund(3) + v(1, 14, -3, False) + lt(1, [-3, -2, -1]) + v(2, 13, -2, False) + lt(2, [-2, -1]) + v(1, 21, -3, True, 1) + v(1, 16, -3, False))
        z0 = fingerabdruck(pg)
        out = pg.paket(probe, erwartet_fehler='FB-S PROBELAUF bestanden')
        kopf = re.search(r'FB-S PROBELAUF bestanden – (.*?) – ALLES', out).group(1)
        assert kopf.startswith('Kinder 3, Etappen 5, Vergleiche 10, Abweichungen AUS 0 | AN heute: Etappen mit fälliger Fehler-Bordkarte je Kind {"1": 2} (davon heute fällig {"1": 1}), Mischkarten-Etappen 2, Fehler-Aufgaben offen 3 (heute fällig 2)'), kopf
        b = bericht(out)
        assert b['davon_heute_in_der_wiederholung_faellig_je_kind'] == {'1': 1} and b['mischkarten_etappen_mit_fehlerkarte'] == 2, b
        assert b['fehler_aufgaben_offen'] == 3 and b['fehler_aufgaben_heute_faellig'] == 2 and b['lueckenwege_ausgenommen'] == 0, b   # 14, 21 (Tipp) bei Kind 1; 13 bei Kind 2 noch in der Pause; 16 zählt nicht
        assert b['schalter'] == 0 and b['zustand_vorher'][W] == 'alt' and b['da_ungleich_auswahl_info'] == 0, b
        assert fingerabdruck(pg) == z0, 'Probelauf hat etwas zurückgelassen'
        pg.sql(probe, erwartet_fehler='FB-S PROBELAUF bestanden')          # auch direkt (psql, eine Transaktion)
        assert fingerabdruck(pg) == z0
        erg.append(f'Probelauf: bestanden, zurückgerollt, Bericht am Anfang ({kopf[:90]}…)')
        # --- Gegenprobe: neue Auswahl, die schon mit Schalter AUS anders sortiert -> Abbruch
        bad = FB.paket(False, waehlen_variante='   order by schule.fehlerkarte_faellig(p_l, c.id, c.zuletzt) desc, c.zuletzt desc nulls first, (c.stufe = 1), random() limit 1;')
        out = pg.paket(bad, erwartet_fehler='mit Schalter AUS weicht die Auswahl in')
        assert fingerabdruck(pg) == z0
        erg.append('Gegenprobe (Auswahl mit Schalter AUS verändert): Abbruch, nichts geblieben')
        # --- Mischkarte im alten Stand: schon beantwortete Aufgabe verfällt beim nächsten Laden (Grund für die zweite Stelle)
        misch_fall = (grund(1) + v(1, 14, -3, False) + lt(1, [-3, -2, -1]) +
                      "update schule.karte_stand set faellig_am = now() + interval '5 days' where lernender_id = 1 and lernziel = 'A';"
                      "update schule.karte_stand set faellig_am = now() - interval '1 day' where lernender_id = 1 and lernziel = 'B';"
                      "insert into schule.misch_ausgabe (lernender_id, aufgabe_id, einheit_id, lernziel, ausgegeben_am) values (1, 14, 2, 'C', now() - interval '2 minutes');"
                      "select schule.mischkarten(1, 2, 2);")
        fr = {'g1': "schule.misch_gueltig(1, (select a from schule.aufgabe a where a.id = 14), '{\"misch\": true}')",
              'reload': "jsonb_array_length(schule.mischkarten(1, 2, 1))",
              'g2': "schule.misch_gueltig(1, (select a from schule.aufgabe a where a.id = 14), '{\"misch\": true}')",
              'verf': "(select verfallen_am is not null from schule.misch_ausgabe where aufgabe_id = 14)"}
        r = szen(pg, misch_fall, fr)
        assert r['g1'] == 'false' and r['verf'] == 'true', r      # alt: schon beim ersten Laden verfallen (vorher beantwortet), Antwort zählt nicht als Mischkarte
        # --- Negativfälle (Zustand alt)
        neg = negativfaelle_alt(pg, einsp)
        assert fingerabdruck(pg) == z0
        # --- Einspielen, Zweitlauf
        out = pg.sql(f"do $fbt$ begin execute $fbtinhalt${einsp}$fbtinhalt$; end $fbt$;\n\\pset tuples_only on\nselect 'TEMP=' || count(*) from pg_proc where pronamespace = pg_my_temp_schema();")
        assert 'TEMP=0' in out, 'Hilfen im temporären Schema nicht aufgeräumt'
        assert 'FB-S eingespielt' in out and 'alt -> neu' in out and 'Abweichungen AUS 0' in out, out[-800:]
        z1 = fingerabdruck(pg)
        assert text(pg, f"select md5(prosrc) from pg_proc where oid = '{W}'::regprocedure;") == FB.md5(FB.waehlen_neu())
        assert text(pg, "select string_agg(schluessel || '=' || wert::text, ',' order by schluessel collate \"C\") from schule.regel where schluessel like 'fehlerkarten%';") == \
            'fehlerkarten_an=0,fehlerkarten_max=3,fehlerkarten_pause_lerntage=2'
        assert text(pg, "select bool_and(not has_function_privilege('anon', p.oid, 'execute') and not has_function_privilege('authenticated', p.oid, 'execute')) from pg_proc p where proname like 'fehlerkarte%';") == 't'
        pg.sql(regeln(1))
        out = pg.paket(einsp)                                                # Zweitlauf mit Schalter AN: nichts geändert, Schalter bleibt
        assert 'neu -> neu' in out and 'Abweichungen AUS 0' in out, out[-600:]
        assert text(pg, "select wert::text from schule.regel where schluessel = 'fehlerkarten_an';") == '1'
        pg.sql(regeln(0))
        assert fingerabdruck(pg) == z1
        out = pg.paket(probe, erwartet_fehler='FB-S PROBELAUF bestanden')
        assert 'neu -> neu' in out and fingerabdruck(pg) == z1
        erg.append('Einspielen alt -> neu, Zweitlauf neu -> neu (Schalter bleibt), Probe danach: nichts geändert; Hilfen ohne Rechte für anon/authenticated')
        # Negativfälle im Zustand neu
        h = FB.HILFEN[4]
        neg.append(negativ(pg, einsp, f"create or replace function {h[1]}{h[2]}as $function$ select false; $function$;", 'ist vorhanden, aber nicht im neuen Stand', 'neu: Hilfe verändert'))
        neg.append(negativ(pg, einsp, mit_text(W_KOPF, FB.waehlen_alt()), 'Zwischenzustand', 'neu: wdh_aufgabe_waehlen zurück auf alt'))
        neg.append(negativ(pg, einsp, f'alter function schule.fehlerkarte_serie(bigint, bigint) volatile;', 'FB-S ABBRUCH, Vorbedingung', 'neu: Hilfe VOLATILE'))
        assert fingerabdruck(pg) == z1
        assert len(neg) >= 12
        erg.append(f'Negativfälle Paketschutz: {len(neg)} (alle Abbruch, nichts geändert): ' + '; '.join(neg))
        pg.sql(NB.rang_sql())
        verhalten(pg, erg, misch_fall, fr)
    finally:
        pg.ende()
    return erg


def verhalten(pg, erg, misch_fall, fr):
    g1 = grund(1)
    vor = lt(1, [-3, -2, -1])
    # Schalter AUS / AN / nur Testkind
    r = szen(pg, g1 + v(1, 14, -3, False) + vor, {'aus': wahl(1)})
    assert r['aus'] == '11'
    r = szen(pg, g1 + v(1, 14, -3, False) + vor + regeln(1), {'an': wahl(1), 'misch': wahl(1, True)})
    assert r == {'an': '14', 'misch': '14'}, r
    r = szen(pg, g1 + v(1, 14, -3, False) + vor + regeln(2), {'kind': wahl(1)})
    assert r['kind'] == '11', 'Schalter 2: nur Testkinder'
    erg.append('Schalter: aus -> wie bisher (11), an -> Fehler-Bordkarte zuerst (14, auch Mischkarte), 2 -> nur Testkinder')
    # Wartezeit in Lerntagen (nicht Kalendertagen); Sperre bleibt
    r = szen(pg, g1 + v(1, 14, -3, False) + lt(1, [-3, -1]) + regeln(1), {'w': wahl(1)})
    assert r['w'] == '11', 'nur ein Lerntag dazwischen: noch gesperrt'
    r = szen(pg, g1 + v(1, 14, -6, False) + lt(1, [-6, -2, -1]) + regeln(1), {'w': wahl(1)})
    assert r['w'] == '14', '6 Kalendertage, 2 Lerntage dazwischen: fällig'
    r = szen(pg, g1 + v(1, 14, -4, False) + lt(1, [-4, -3, -2, -1]) + regeln(1, pause=4), {'w': wahl(1), 'rang': "pruef.rang_neu(1, 1, 'A', false)"})
    assert r['w'] == '11' and ',14}' in r['rang'].split('|')[0], r            # Pause 4 länger als die Sperre: wählbar, aber nicht bevorzugt (am Ende)
    r = szen(pg, g1 + v(1, 14, -5, False) + lt(1, [-5, -4, -3, -2, -1]) + regeln(1, pause=4), {'w': wahl(1)})
    assert r['w'] == '14'
    r = szen(pg, g1 + v(1, 14, -1, False) + lt(1, [-1]) + regeln(1, pause=0), {'w': wahl(1)})
    assert r['w'] == '11', 'Pause 0: die Sperre der letzten 3 Lerntage gilt trotzdem'
    erg.append('Wartezeit: nach 2 Lerntagen Pause zuerst, vorher nicht (Kalendertage ohne Lernen zählen nicht); Pause 4 > Sperre wirkt; Pause 0 hebt die Sperre nicht auf')
    # richtig gelöst / erneut falsch / Obergrenze
    r = szen(pg, g1 + v(1, 14, -10, False) + v(1, 14, -3) + lt(1, [-10, -3, -2, -1]) + regeln(1), {'w': wahl(1)})
    assert r['w'] == '11', 'selbst gelöst: erledigt'
    r = szen(pg, g1 + v(1, 14, -12, False) + v(1, 14, -9) + v(1, 14, -3, False) + lt(1, [-12, -9, -3, -2, -1]) + regeln(1), {'w': wahl(1)})
    assert r['w'] == '14', 'erneut falsch: kommt wieder'
    drei = v(1, 14, -9, False) + v(1, 14, -6, False) + v(1, 14, -3, False) + lt(1, [-12, -9, -6, -3, -2, -1])
    r = szen(pg, g1 + drei + regeln(1), {'w': wahl(1), 's': 'schule.fehlerkarte_serie(1, 14)'})
    assert r == {'w': '14', 's': '3'}, r
    r = szen(pg, g1 + v(1, 14, -12, False) + drei + regeln(1), {'w': wahl(1), 's': 'schule.fehlerkarte_serie(1, 14)'})
    assert r == {'w': '11', 's': '4'}, r
    r = szen(pg, g1 + v(1, 14, -12, False) + drei + regeln(1, mx=5), {'w': wahl(1)})
    assert r['w'] == '14'
    r = szen(pg, g1 + v(1, 14, -3, False) + vor + regeln(1, mx=0), {'w': wahl(1)})
    assert r['w'] == '11'
    erg.append('richtig gelöst -> nicht mehr bevorzugt; erneut falsch -> wieder; Obergrenze 3 (viertes Mal normal), einstellbar (5, 0)')
    # Tipp / zweiter Anlauf / selbst
    r = szen(pg, g1 + v(1, 14, -3, True, 1) + vor + regeln(1), {'w': wahl(1)})
    assert r['w'] == '14', 'mit Tipp richtig = nicht selbst'
    r = szen(pg, g1 + v(1, 14, -3, False, 0, 1) + v(1, 14, -3, True, 1, 2, uhr='12:01') + vor + regeln(1), {'w': wahl(1), 's': 'schule.fehlerkarte_serie(1, 14)'})
    assert r == {'w': '14', 's': '1'}, '2. Anlauf richtig = nicht selbst, zählt als eine Bearbeitung'
    r = szen(pg, g1 + v(1, 14, -3, True, 0, 1) + vor + regeln(1), {'w': wahl(1)})
    assert r['w'] == '11'
    r = szen(pg, g1 + v(1, 14, -3, True, 0, None) + vor + regeln(1), {'w': wahl(1)})
    assert r['w'] == '11', 'ohne Anlauf-Angabe richtig ohne Tipp = selbst (wie versuch_wertung)'
    r = szen(pg, g1 + v(1, 14, -3, False, 0, 1, misch=True) + vor + regeln(1), {'w': wahl(1)})
    assert r['w'] == '14', 'falsche Mischkarte ist auch eine Bearbeitung'
    erg.append('Tipp, 2. Anlauf, falsche Mischkarte = nicht selbst gelöst; richtig im 1. Anlauf ohne Tipp = erledigt')
    # mehrere, gesperrt, Lückenweg / zaehlt nein, Stufe
    r = szen(pg, g1 + v(1, 13, -4, False) + v(1, 14, -3, False) + lt(1, [-4, -3, -2, -1]) + regeln(1), {'w': wahl(1)})
    assert r['w'] == '13', 'mehrere: die älteste'
    r = szen(pg, g1 + v(1, 18, -3, False) + vor + regeln(1), {'w': wahl(1), 'rang': "pruef.rang_neu(1, 1, 'A', false)"})
    assert r['w'] == '11' and '18' not in re.findall(r'\d+', r['rang']), r
    r = szen(pg, g1 + v(1, 16, -3, False) + v(1, 17, -3, False) + vor + regeln(1), {'w': wahl(1), 'rang': "pruef.rang_neu(1, 1, 'A', false)"})
    ids = re.findall(r'\d+', r['rang'].split('|')[0])
    assert r['w'] == '11' and '16' not in ids and ids[-1] == '17', r          # zaehlt nein: nie; Lückenweg (zählt): normal, nicht bevorzugt
    r = szen(pg, g1 + v(1, 15, -3, False) + vor + regeln(1), {'w': wahl(1), 'm': wahl(1, True)})
    assert r == {'w': '15', 'm': '11'}, r
    r = szen(pg, g1 + v(1, 19, -3, False) + vor + regeln(1), {'w': wahl(1), 'm': wahl(1, True)})
    assert r == {'w': '19', 'm': '19'}, r
    erg.append('mehrere -> die älteste; gesperrt nie; zaehlt = nein nie; Lückenweg nicht bevorzugt; Stufe 1 nur in der Wiederholung, nicht als Mischkarte')
    # anderes Kind unberührt, alt = neu für alle Kinder/Etappen/beide Arten mit Schalter AUS; wdh_aufgabe_da gleich
    alle = g1 + grund(2) + grund(3) + v(1, 14, -3, False) + vor + v(2, 21, -5, False) + lt(2, [-5, -2, -1])
    fr2 = {f'{x}{l}{lz}{mi}': f"pruef.rang_{'alt' if x == 'a' else 'neu'}({l}, 1, '{lz}', {mi})" for x in 'an' for l in (1, 2, 3) for lz in 'AB' for mi in ('false', 'true')}
    fr2.update({f'da{l}{lz}': f"schule.wdh_aufgabe_da({l}, 1, '{lz}')" for l in (1, 2, 3) for lz in 'AB'})
    aus = szen(pg, alle + regeln(0), fr2)
    an = szen(pg, alle + regeln(1), fr2)
    for l in (1, 2, 3):
        for lz in 'AB':
            for mi in ('false', 'true'):
                assert aus[f'a{l}{lz}{mi}'] == aus[f'n{l}{lz}{mi}'], (l, lz, mi)
                assert an[f'a{l}{lz}{mi}'] == aus[f'a{l}{lz}{mi}']
                if not (l == 1 and lz == 'A') and not (l == 2 and lz == 'B'):
                    assert an[f'n{l}{lz}{mi}'] == aus[f'n{l}{lz}{mi}'], ('anderes Kind/Etappe verändert', l, lz, mi)
                assert set(an[f'n{l}{lz}{mi}'].split('|')[0].strip('{}').split(',')) == set(aus[f'n{l}{lz}{mi}'].split('|')[0].strip('{}').split(',')), 'Kandidatenmenge'
            assert an[f'da{l}{lz}'] == aus[f'da{l}{lz}'] and aus[f'da{l}{lz}'] == ('true' if aus[f'n{l}{lz}false'] != '{}|{}' else 'false')
    assert an['n1Afalse'].startswith('{14,') and an['n2Bfalse'].startswith('{21,')
    leer = szen(pg, g1 + '\n'.join(v(1, a, -1) for a in (11, 12, 13, 14, 15, 17, 19)) + lt(1, [-1]) + regeln(1), {'w': wahl(1), 'da': "schule.wdh_aufgabe_da(1, 1, 'A')"})
    assert leer == {'w': 'NULL', 'da': 'false'}, leer
    erg.append('Schalter AUS: Rangfolge alt = neu (3 Kinder × 2 Etappen × Wiederholung/Mischkarte); AN: nur betroffene Etappen anders, Kandidatenmenge gleich; '
               'anderes Kind unberührt; wdh_aufgabe_da gleich (auch „keine Aufgabe“)')
    # Tagesrunde gleich
    tr = alle + "update schule.karte_stand set faellig_am = now() - interval '1 day';"
    runde = "(select ziel || '/' || faellig || '/' || (select string_agg(nr || ':' || einheit_id || lernziel, ',' order by nr) from schule.wdh_runde_etappe e where e.lernender_id = r.lernender_id) from schule.wdh_runde r where r.lernender_id = {l})"
    fr3 = {}
    for l in (1, 2, 3): fr3[f'r{l}'] = runde.format(l=l)
    hol = ''.join(f"select schule.wdh_runde_holen({l}, schule.heute_tag({l}));" for l in (1, 2, 3))
    a1 = szen(pg, tr + regeln(0) + hol, fr3)
    a2 = szen(pg, tr + regeln(1) + hol, fr3)
    assert a1 == a2 and all(x != 'NULL' for x in a1.values()), (a1, a2)
    erg.append(f'Tagesrunde (wdh_runde_holen) mit Schalter aus/an gleich: {a1}')
    # Mischkarten-Einlösung mit einer Fehler-Bordkarte
    r = szen(pg, misch_fall.replace("insert into schule.misch_ausgabe", regeln(1) + "insert into schule.misch_ausgabe"), fr)
    assert r['g1'] == 'true' and r['g2'] == 'true' and r['verf'] == 'false', r
    r = szen(pg, misch_fall.replace("insert into schule.misch_ausgabe", regeln(0) + "insert into schule.misch_ausgabe"), fr)
    assert r['g1'] == 'false' and r['verf'] == 'true', 'Schalter aus: wie bisher'
    r = szen(pg, g1 + v(1, 14, -3, False) + vor + regeln(1) + "update schule.karte_stand set faellig_am = now() - interval '1 day' where lernender_id = 1;",
             {'ausg': "(select string_agg(x->>'id', ',' order by (x->>'id')::int) from jsonb_array_elements(schule.mischkarten(1, 2, 8)) x)",
              'g': "schule.misch_gueltig(1, (select a from schule.aufgabe a where a.id = 14), '{\"misch\": true}')",
              'nochmal': "(select string_agg(x->>'id', ',' order by (x->>'id')::int) from jsonb_array_elements(schule.mischkarten(1, 2, 8)) x)",
              'g2': "schule.misch_gueltig(1, (select a from schule.aufgabe a where a.id = 14), '{\"misch\": true}')"})
    assert r['ausg'].startswith('14,') and r['g'] == 'true' and r['nochmal'] == r['ausg'] and r['g2'] == 'true', r
    erg.append('Mischkarte: Fehler-Bordkarte wird ausgegeben, bleibt beim erneuten Laden gültig und wird eingelöst (Schalter aus: verfällt wie bisher)')
    # Zeitzone / Lerntag-Grenze (Testkind, UTC+14, Schalter 2 = nur Testkinder)
    g3 = grund(3) + lt(3, [-3, -2, -1]) + regeln(2)
    r = szen(pg, g3 + v(3, 14, -3, False, uhr='23:30'), {'w': wahl(3), 'utc': "(select (am at time zone 'UTC')::date - schule.heute_tag(3) from schule.versuch where aufgabe_id = 14 and not richtig)"})
    assert r['w'] == '14' and r['utc'] == '-3', r
    r = szen(pg, g3 + v(3, 14, -2, False, uhr='00:30'), {'w': wahl(3), 'utc': "(select (am at time zone 'UTC')::date - schule.heute_tag(3) from schule.versuch where aufgabe_id = 14 and not richtig)"})
    assert r['w'] == '11' and r['utc'] == '-3', r                                # in UTC derselbe Tag wie oben, beim Kind schon der nächste Lerntag -> noch gesperrt
    erg.append('Zeitzone: Lerntag nach der Ortszeit des Kindes (23:30 vs. 00:30 bei UTC+14), Testkind-Schalter 2 wirkt')


def main():
    probe, einsp = teil1()
    if not T.pg_bin():
        print('Teil 2 übersprungen (kein Postgres)'); print('OK'); return
    for icu in (None, os.environ.get('RB_PG_ICU') or 'en-US'):
        erg = teil2(probe, einsp, icu)
        print(f'--- Teil 2 {"mit ICU " + icu if icu else "ohne ICU (C.UTF-8)"}: bestanden')
        for e in erg: print('  -', e)
    print('OK')


if __name__ == '__main__':
    main()
