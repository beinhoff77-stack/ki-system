"""Test für RB-S: tools/regelbezug_sql.py, tools/regelbezug_lernkarten.py, Migration 20261204_rb_s_regelbezug.sql, Paket regelbezug_einspielen.py.

Teil 1 (immer): Zuordnung Repo -> eingespielt (alle 2028 Aufgaben gefunden, Z2-02 als Abweichung), Zählungen in sich stimmig,
  Lernkarten-Datei auf dem Stand, je Runde ein Paket erzeugbar.
Teil 2 (nur wenn lokale Postgres-Programme da sind, z. B. /usr/lib/postgresql/16/bin): leere Instanz in /tmp, NACHBAU (regelbezug_nachbau.sql,
  NICHT die echte Datenbank) mit allen eingespielten Aufgaben aus tools/tests/aus/; dann: Probelauf muss „PROBELAUF bestanden“ melden,
  Einspiel-Paket läuft durch, Nachtrags-Pakete aller Runden laufen, zweiter Lauf fügt nichts hinzu, eine Fehlantwort aus einer Datei liefert
  die Beschreibung, eine veränderte Aufgabe lässt das Paket abbrechen.
Aufruf: python3 -I tools/tests/regelbezug_sql_test.py   (endet mit OK; Teil 2 wird übersprungen, wenn kein Postgres da ist)
"""
import glob
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(WURZEL / 'tools'))
import regelbezug_sql as R  # noqa: E402
import rollend_sql  # noqa: E402

ALLE = tuple(range(1, 14))


def py(*args):
    p = subprocess.run([sys.executable, '-I', *args], capture_output=True, text=True, cwd=str(WURZEL))
    return p.returncode, p.stdout, p.stderr


def teil1():
    zeilen, abw, fehlt, z, weg, je_typ = R.sammeln(ALLE)
    assert z['aufgaben'] == 2028 and not fehlt, (z, fehlt[:3])
    assert any(a.startswith('Z2-02 ') for a in abw), abw
    assert z['fb_uebernommen'] + sum(weg.values()) == z['fehlbilder'], (z, weg)
    assert sum(c['eindeutig'] for c in je_typ.values()) == z['fb_uebernommen']
    ks = [x['k'] for x in zeilen]
    assert len(ks) == len(set(ks))
    paare = [(x['e'], x['r']) for x in zeilen]
    assert len(paare) == len(set(paare)), 'zwei Aufgaben auf demselben Platz'
    for x in zeilen:
        nrs = [f['nr'] for f in x['fb']]
        assert len(nrs) == len(set(nrs))
        keys = [(f['art'], f['luecke'], f['wert']) for f in x['fb']]
        assert len(keys) == len(set(keys)), x['k']
    z2 = next(x for x in zeilen if x['k'] == 'Z2-02')
    assert z2['fb'] == [] and z2['regel'], z2
    rc, out, err = py('tools/regelbezug_lernkarten.py', '--pruefen')
    assert rc == 0, err
    rc, out, err = py('tools/tests/rb_ww_pakete.py', '--pruefen')
    assert rc == 0, 'Paket-Dateien unter tools/tests/aus nicht auf dem Stand: python3 -I tools/tests/rb_ww_pakete.py\n' + err
    for r in ALLE:
        rc, out, err = py('tools/regelbezug_sql.py', '--runden', str(r), '--sql')
        assert rc == 0 and out.count('$rbf$') % 2 == 0 and 'do $rbnach$' in out, (r, err[-400:])
    # Runde 14: seit 28.11. mit 640 Fehlbildern und ohne Regel eingespielt; die Regel kommt nur über rb_nachtrag_r14.sql. Das alte Paket bleibt byteidentisch.
    z14, abw14, fehlt14, c14, weg14, _ = R.sammeln((14,))
    assert c14['aufgaben'] == 213 and not fehlt14 and not abw14 and c14['mit_regel'] == 195 and c14['fb_uebernommen'] == 640 and not weg14, (c14, abw14, weg14)
    assert len(z14) == 213 and sum(len(x['fb']) for x in z14) == 640 and sum(1 for x in z14 if x['regel']) == 195
    alt14 = (WURZEL / 'tools/tests/aus/rollend14_einspielen.sql').read_bytes()
    assert hashlib.md5(alt14).hexdigest() == 'b2d081b8da216e6d45691f55d0e73569', 'rollend14_einspielen.sql ist nicht mehr das eingespielte Paket'
    rc, out, err = py('tools/rollend_sql.py', '--runden', '14', '--sql')
    assert rc == 0 and out.encode('utf-8') == alt14, 'rollend_sql.py erzeugt für Runde 14 nicht mehr das eingespielte Paket (Regel darf dort nicht stehen)'
    assert 'neue Aufgaben rollend-14: 213 Aufgaben, 0 Regeln, 640 Fehlbilder.' in out
    # Auflage Werkstatt 1177: eine Nur-Lesen-Runde (14) zusammen mit anderen Runden bricht mit klarer Meldung ab (kein gemeinsamer schreibender Block)
    assert R.FEHLBILD_NUR_LESEN_RUNDEN == (14,)
    assert R.gemischte_runden((14,)) is None and R.gemischte_runden((13,)) is None and R.gemischte_runden((12, 13)) is None
    assert R.gemischte_runden((13, 14)) and R.gemischte_runden((1, 5, 14)) and R.gemischte_runden((14, 13))
    for rl in ('13,14', '14,13', '1,2,3,4,14', 'alle'):
        rc, out, err = py('tools/regelbezug_sql.py', '--runden', rl, '--sql')
        assert rc == 1 and out == '' and err.startswith('ABBRUCH: Runde 14 darf nur lesend verglichen werden') and 'getrennt erzeugen' in err, (rl, rc, err[:300])
        rc, out, err = py('tools/regelbezug_sql.py', '--runden', rl, '--sql', '--probe')
        assert rc == 1 and out == '' and 'ABBRUCH' in err, (rl, 'probe')
    rc, out, err = py('tools/regelbezug_sql.py', '--runden', '14', '--sql')
    assert rc == 0 and 'insert into schule.aufgabe_fehlbild' not in out and 'do $rbnach$' in out, err[-300:]
    rc, out, err = py('tools/regelbezug_sql.py', '--runden', '13', '--sql')
    assert rc == 0 and 'insert into schule.aufgabe_fehlbild' in out, err[-300:]
    rc, out, err = py('tools/regelbezug_sql.py', '--runden', '13,14')   # Übersicht (schreibt nichts) bleibt erlaubt
    assert rc == 0 and out.startswith('Runden 13,14:'), err[-300:]
    print('Runde 14 gemischt mit anderen Runden: Abbruch mit Meldung (13,14 / 14,13 / 1,2,3,4,14 / alle), 14 allein und 13 allein unverändert')
    # neue Runden bringen den Block mit, --ohne-regelbezug lässt ihn weg
    rc, out, _ = py('tools/rollend_sql.py', '--runden', '8', '--sql')
    assert rc == 0 and 'do $rbnach$' in out
    rc, out, _ = py('tools/rollend_sql.py', '--runden', '8', '--sql', '--ohne-regelbezug')
    assert rc == 0 and 'rbnach' not in out
    return zeilen


def pg_bin():
    for d in sorted(glob.glob('/usr/lib/postgresql/*/bin'), reverse=True):
        if os.path.exists(d + '/initdb'): return d
    w = shutil.which('initdb')
    return os.path.dirname(w) if w else None


class PG:
    def __init__(self, bindir):
        self.bin, self.dir = bindir, tempfile.mkdtemp(prefix='rbpg-')
        self.root = os.geteuid() == 0
        if self.root: shutil.chown(self.dir, 'nobody')
        self.port = '55433'
        self.als(f'{bindir}/initdb -D {self.dir}/d -U postgres -E UTF8 --locale=C.UTF-8 -A trust > {self.dir}/init.log 2>&1')
        self.als(f"{bindir}/pg_ctl -D {self.dir}/d -o '-k {self.dir} -p {self.port} -c listen_addresses=' -l {self.dir}/log -w start > /dev/null")

    def als(self, cmd):
        full = ['su', 'nobody', '-s', '/bin/bash', '-c', cmd] if self.root else ['bash', '-c', cmd]
        subprocess.run(full, check=True)

    def sql(self, text, erwartet_fehler=None):
        f = Path(self.dir) / 'x.sql'
        f.write_text(text, encoding='utf-8')
        os.chmod(f, 0o644)
        p = subprocess.run([f'{self.bin}/psql', '-h', self.dir, '-p', self.port, '-U', 'postgres', '-X', '-q', '-v', 'ON_ERROR_STOP=1',
                            '-1', '-f', str(f)], capture_output=True, text=True)
        if erwartet_fehler is None:
            assert p.returncode == 0, p.stderr[-3000:]
        else:
            assert p.returncode != 0 and erwartet_fehler in p.stderr, (erwartet_fehler, p.stderr[-3000:])
        return p.stdout + p.stderr

    def paket(self, text, erwartet_fehler=None):
        """Wie der Projektleiter: Inhalt einer Paket-Datei in EINEM execute innerhalb eines do-Blocks (eine Transaktion)."""
        assert '$rbpaketinhalt$' not in text
        return self.sql(f'do $rbpaket$ begin execute $rbpaketinhalt${text}$rbpaketinhalt$; end $rbpaket$;', erwartet_fehler)

    def ende(self):
        self.als(f'{self.bin}/pg_ctl -D {self.dir}/d -m immediate stop > /dev/null 2>&1 || true')
        shutil.rmtree(self.dir, ignore_errors=True)


def auszug(datei, anfang, ende='end $function$;'):
    s = (WURZEL / 'supabase/migrations' / datei).read_text(encoding='utf-8')
    i = s.index(anfang)
    return s[i:s.index(ende, i) + len(ende)]


def karte_sql():
    """Karte wie live, soweit im Repo: karte_buchen aus H-Muss (19.11.) mit dem FT-S-Filter, karte_faellig aus R3; Trigger mit den Live-Namen
    (versuch_hilfe_merken BEFORE; versuch_karte, versuch_lerntag, versuch_misch_verfall, versuch_sterne AFTER) – vereinfacht, siehe Kommentare."""
    kb = auszug('20261119_w176_h_muss.sql', 'create or replace function schule.karte_buchen(')
    alt = "if a.id is null or a.pool <> 'uebung' then return; end if;"
    assert kb.count(alt) == 1
    kb = kb.replace(alt, "if a.id is null or a.pool <> 'uebung' or not schule.aufgabe_zaehlt(a) then return; end if;")   # FT-S
    kf = auszug('20261116_w150_r3_wiederholung_lerntage.sql', 'create or replace function schule.karte_faellig(', '$function$;\n')
    return f"""
create table schule.karte_stand (lernender_id bigint not null references schule.lernender(id), einheit_id bigint not null references schule.einheit(id), lernziel text not null,
  serie smallint not null default 0, richtig int not null default 0, falsch int not null default 0, sitzt boolean not null default false, sitzt_am timestamptz,
  wdh_stufe smallint not null default 0, faellig_am timestamptz, zuletzt timestamptz, schwer_ok boolean not null default false, wdh_fehler smallint not null default 0,
  wdh_ab timestamptz, wdh_lerntage smallint, eigene_loesungen int not null default 0, typen text[] not null default '{{}}', folge int not null default 0,
  fehler_folge int not null default 0, stufe_senkung smallint not null default 0, gezaehlt jsonb not null default '{{}}', geoeffnet_am timestamptz,
  primary key (lernender_id, einheit_id, lernziel));
create table schule.lerntag (lernender_id bigint, fach text, datum date, zeitzone text, primary key (lernender_id, fach, datum));
create table schule.sterne (id bigserial primary key, lernender_id bigint, menge int, grund text, bezug text, am timestamptz default now(), unique (lernender_id, grund, bezug));
create or replace function schule.karte_ziel(p_einheit bigint, p_lz text) returns int language sql stable set search_path to '' as $$
  select least(4, greatest(2, count(*)))::int from schule.aufgabe a where a.einheit_id = p_einheit and a.pool = 'uebung' and a.variante_gruppe = p_lz and a.freigegeben $$;
create or replace function schule.karte_typen_noetig(p_einheit bigint, p_lz text) returns int language sql stable as $$ select 0 $$;   -- Nachbau: keine Typen-Pflicht
create or replace function schule.karte_schwer_noetig(p_einheit bigint, p_lz text) returns boolean language sql stable as $$ select false $$;
{kf}
{kb}
-- Nachbau der Trigger (Live-Namen). versuch_karte wie R2 (live seit I-2 mit wertung_offen: ein falscher 1. Anlauf wird später nachgebucht).
create or replace function schule.versuch_hilfe_merken() returns trigger language plpgsql as $$ begin new.hilfe := coalesce(new.hilfe, 0); return new; end $$;
create trigger versuch_hilfe_merken before insert on schule.versuch for each row execute function schule.versuch_hilfe_merken();
create or replace function schule.versuch_karte() returns trigger language plpgsql set search_path to '' as $$
begin
  if new.testsitzung_id is null and not (coalesce(new.anlauf, 0) = 1 and not new.richtig) then
    perform schule.karte_buchen(new.lernender_id, new.aufgabe_id, new.richtig, new.hilfe, now());
  end if;
  return new;
end $$;
create trigger versuch_karte after insert on schule.versuch for each row execute function schule.versuch_karte();
create or replace function schule.versuch_lerntag() returns trigger language plpgsql set search_path to '' as $$
begin insert into schule.lerntag values (new.lernender_id, 'Mathematik', (now() at time zone 'Europe/Berlin')::date, 'Europe/Berlin') on conflict do nothing; return new; end $$;
create trigger versuch_lerntag after insert on schule.versuch for each row execute function schule.versuch_lerntag();
create or replace function schule.versuch_misch_verfall() returns trigger language plpgsql as $$ begin return new; end $$;
create trigger versuch_misch_verfall after insert on schule.versuch for each row execute function schule.versuch_misch_verfall();
create or replace function schule.versuch_sterne() returns trigger language plpgsql set search_path to '' as $$
begin
  if new.richtig and new.testsitzung_id is null then insert into schule.sterne (lernender_id, menge, grund, bezug) values (new.lernender_id, 10, 'uebung', 'aufgabe:' || new.aufgabe_id) on conflict do nothing; end if;
  return new;
end $$;
create trigger versuch_sterne after insert on schule.versuch for each row execute function schule.versuch_sterne();
"""


def nachbau_sql():
    s = (WURZEL / 'supabase/migrations/20261116_w150_r2_fehlermuster_zweiter_versuch.sql').read_text(encoding='utf-8')
    i = s.index('create or replace function schule.antwort_bewerten')
    ab = s[i:s.index('end $function$;', i) + len('end $function$;')]
    plan = json.loads((WURZEL / 'inhalte/plan/rollend-einheiten.json').read_text(encoding='utf-8'))
    zg = (WURZEL / 'supabase/migrations/20261114_w150_lern_zugaenge_plan.sql').read_text(encoding='utf-8')
    zg = zg[:zg.index('-- Bestehende Funktionen auf die neuen Prüfungen umstellen')]   # Tabellen und Funktionen der Lern-Zugänge, ohne die Umstellung alter api-Funktionen
    teile = [(WURZEL / 'tools/tests/regelbezug_nachbau.sql').read_text(encoding='utf-8'), ab + '\n', karte_sql(), zg]
    for t, e in plan['einheiten'].items():
        teile.append(f"insert into schule.thema values ({e['id']}, '{t}') on conflict do nothing; insert into schule.einheit values ({e['id']}, {e['id']}, 'freigegeben');")
    # Bestand (vor den Runden): je eine Aufgabe zahl / auswahl / luecken an Platz 1-3 der ersten Einheit
    teile.append("""insert into schule.aufgabe (einheit_id, variante_gruppe, antworttyp, frage, antworten, loesung, tipp, loesungsweg, reihenfolge) values
      (4, 'teiler', 'zahl', '{"text": "Bestand zahl"}', null, '{"wert": 12}', 't', 'w', 1),
      (4, 'teiler', 'auswahl', '{"text": "Bestand auswahl"}', '["a", "b", "c"]', '{"index": 1}', 't', 'w', 2),
      (4, 'teiler', 'luecken', '{"text": "Bestand luecken"}', null, '{"werte": [3, 4, 5]}', 't', 'w', 3);""")
    # alles, was laut tools/tests/aus eingespielt ist
    aus, _ = R.eingespielt()
    werte = []
    for (eid, r), row in sorted(aus.items()):
        js = json.dumps(row, ensure_ascii=False)
        werte.append(f"({eid}, $j${js}$j$::jsonb)")
    teile.append('insert into schule.aufgabe (einheit_id, variante_gruppe, antworttyp, frage, antworten, loesung, tipp, loesungsweg, reihenfolge, stufe, typ, form, zaehlt) '
                 "select e, x->>'l', x->>'y', x->'f', x->'a', x->'o', x->>'h', x->>'w', (x->>'r')::int, (x->>'s')::smallint, x->>'g', x->>'form', x->>'zaehlt' from (values "
                 + ',\n'.join(werte) + ') v(e, x);')
    return '\n'.join(teile)


def teil2(zeilen):
    b = pg_bin()
    if not b:
        print('Teil 2 übersprungen (kein Postgres)'); return
    pg = PG(b)
    try:
        pg.sql(nachbau_sql())
        n = pg.sql("select count(*) from schule.aufgabe;")
        aus = WURZEL / 'tools/tests/aus'
        probe = (aus / 'rb_s_probe.sql').read_text(encoding='utf-8')
        pg.paket(probe, erwartet_fehler='PROBELAUF bestanden')
        pg.sql(probe, erwartet_fehler='PROBELAUF bestanden')   # auch direkt (psql) lauffähig
        assert 'from schule.aufgabe_fehlbild' in pg.sql("select 'from schule.aufgabe_fehlbild' where to_regclass('schule.aufgabe_fehlbild') is null;")
        out = pg.paket((aus / 'rb_s_einspielen.sql').read_text(encoding='utf-8'))
        assert 'RB-S eingespielt' in out, out[-800:]
        # Probe-Lauf eines Nachtrags (rollt zurück), dann alle Runden zweimal
        rc, p5, err = py('tools/regelbezug_sql.py', '--runden', '5', '--sql', '--probe')
        pg.sql(p5, erwartet_fehler='PROBELAUF bestanden')
        for runde in ALLE:
            paket = (aus / f'rb_nachtrag_r{runde:02d}.sql').read_text(encoding='utf-8')
            out1 = pg.paket(paket)
            out2 = pg.paket(paket)
            assert 'Fehlbilder neu' in out1 and ', 0 Regeln neu, 0 Fehlbilder neu' in out2, (runde, out1[-300:], out2[-300:])
        # Runde 14: erst der Fehlbild-Block des eingespielten Pakets (0 Regeln, 640 Fehlbilder), dann der Nachtrag der Regeln
        pk14 = (aus / 'rollend14_einspielen.sql').read_text(encoding='utf-8')
        out = pg.paket(pk14[pk14.index('-- RB-S Regelbezug: neue Aufgaben rollend-14'):])
        assert 'RB-S Regelbezug: 213 Aufgaben, 0 Regeln neu, 640 Fehlbilder neu' in out, out[-400:]
        nach14 = (aus / 'rb_nachtrag_r14.sql').read_text(encoding='utf-8')
        assert 'insert into schule.aufgabe_fehlbild' not in nach14, 'rb_nachtrag_r14.sql darf nichts in aufgabe_fehlbild schreiben'
        # Negativtests: der Nachtrag r14 bricht ab, wenn die Fehlbilder nicht genau dem Soll entsprechen; danach steht keine Regel von R14 in der Tabelle
        x0 = R.sammeln((14,))[0][0]
        f0 = x0['fb'][0]
        aid = f"(select id from schule.aufgabe where einheit_id = {x0['e']} and pool = 'uebung' and reihenfolge = {x0['r']})"
        offen = f"update schule.einheit set status = 'geprueft' where id = {x0['e']};\n"
        zu = f"\nupdate schule.einheit set status = 'freigegeben' where id = {x0['e']};"
        regeln_vor = pg.sql("\\pset tuples_only on\nselect count(*) from schule.aufgabe_regel;").split()[0]
        fb_vor = pg.sql("\\pset tuples_only on\nselect count(*) from schule.aufgabe_fehlbild;").split()[0]
        def nichts_geblieben(was):
            assert pg.sql("\\pset tuples_only on\nselect count(*) from schule.aufgabe_regel;").split()[0] == regeln_vor, f'{was}: Regeln von R14 sind zurückgeblieben'
        # 1. ein Fehlbild fehlt
        pg.sql("create table public.fb_sicher as select * from schule.aufgabe_fehlbild where false;\n" + offen
               + f"insert into public.fb_sicher select * from schule.aufgabe_fehlbild where aufgabe_id = {aid} and nr = {f0['nr']};\n"
               + f"delete from schule.aufgabe_fehlbild where aufgabe_id = {aid} and nr = {f0['nr']};" + zu)
        out = pg.paket(nach14, erwartet_fehler='RB-S Regelbezug ABBRUCH')
        assert x0['k'] in out and 'fehlt oder weicht' in out, out[-600:]
        nichts_geblieben('Fehlbild fehlt')
        pg.sql(offen + "insert into schule.aufgabe_fehlbild select * from public.fb_sicher;\ndrop table public.fb_sicher;" + zu)
        # 2. ein zusätzliches Fehlbild
        assert x0['y'] == 'zahl'      # alle Aufgaben der Runde 14 haben eine Zahlantwort
        pg.sql(offen + f"insert into schule.aufgabe_fehlbild (aufgabe_id, nr, art, luecke, wert, beschreibung) values ({aid}, 99, 'zahl', null, '987654', 'zusätzlich');" + zu)
        pg.paket(nach14, erwartet_fehler='RB-S Regelbezug ABBRUCH')
        nichts_geblieben('zusätzliches Fehlbild')
        pg.sql(offen + f"delete from schule.aufgabe_fehlbild where aufgabe_id = {aid} and nr = 99;" + zu)
        # 3. ein abweichendes Fehlbild
        pg.sql(offen + f"update schule.aufgabe_fehlbild set beschreibung = beschreibung || ' (geändert)' where aufgabe_id = {aid} and nr = {f0['nr']};" + zu)
        out = pg.paket(nach14, erwartet_fehler='RB-S Regelbezug ABBRUCH')
        assert 'fehlt oder weicht' in out, out[-600:]
        nichts_geblieben('abweichendes Fehlbild')
        pg.sql(offen + f"update schule.aufgabe_fehlbild set beschreibung = replace(beschreibung, ' (geändert)', '') where aufgabe_id = {aid} and nr = {f0['nr']};" + zu)
        assert pg.sql("\\pset tuples_only on\nselect count(*) from schule.aufgabe_fehlbild;").split()[0] == fb_vor, 'Fehlbilder nicht wiederhergestellt'
        # 4. Teilvorbestand an Regeln (eine Regel von R14 steht schon) -> Abbruch
        pg.sql(f"insert into schule.aufgabe_regel (aufgabe_id, regel) values ({aid}, '{x0['regel']}');")
        out = pg.paket(nach14, erwartet_fehler='Teilvorbestand')
        pg.sql(offen + f"delete from schule.aufgabe_regel where aufgabe_id = {aid};" + zu)
        nichts_geblieben('Teilvorbestand')
        print('Negativtests Nachtrag r14 (Fehlbild fehlt / zusätzlich / abweichend / Teilvorbestand): Abbruch, 0 Regeln von R14 zurückgeblieben')
        out1 = pg.paket(nach14)
        out2 = pg.paket(nach14)
        assert 'RB-S Regelbezug: 213 Aufgaben, 195 Regeln neu, 0 Fehlbilder neu' in out1, out1[-400:]
        assert 'RB-S Regelbezug: 213 Aufgaben, 0 Regeln neu, 0 Fehlbilder neu' in out2, out2[-400:]
        print('Runde 14, Nachtrag, 1. Lauf:', [l for l in out1.splitlines() if 'RB-S Regelbezug' in l][-1].strip())
        print('Runde 14, Nachtrag, 2. Lauf:', [l for l in out2.splitlines() if 'RB-S Regelbezug' in l][-1].strip())
        zahl = pg.sql("\\pset tuples_only on\nselect count(*) || ' ' || (select count(*) from schule.aufgabe_fehlbild) from schule.aufgabe_regel;").split()
        assert int(zahl[0]) == sum(1 for x in zeilen if x['regel']) + 195 and int(zahl[1]) == sum(len(x['fb']) for x in zeilen) + 640, zahl
        # eine echte Fehlantwort aus einer Datei (Zahl mit Kennung) über die Bewertung
        x = next(x for x in zeilen if x['y'] == 'zahl' and any(f['fehlbild'] for f in x['fb']))
        f = next(f for f in x['fb'] if f['fehlbild'])
        out = pg.sql(f"""\\pset tuples_only on
select schule.uebung_pruefen_wd(1, jsonb_build_object('aufgabe_id', (select id from schule.aufgabe where einheit_id = {x['e']} and reihenfolge = {x['r']}),
  'client_id', 'rb-t', 'antwort', jsonb_build_object('wert', '{f['wert'].replace('.', ',')}'), 'anlauf', 2))->'regelbezug';
select fehlbild_nr || ' ' || fehlbild from schule.versuch where client_id = 'rb-t';""")
        assert f['fehlbild'] in out and str(f['nr']) in out and json.dumps(f['text'], ensure_ascii=False)[1:20] in out, out
        # veränderte Aufgabe -> Abbruch
        pg.sql(f"""update schule.einheit set status = 'geprueft' where id = {zeilen[0]['e']};
update schule.aufgabe set frage = frage || '{{"text": "geändert"}}' where einheit_id = {zeilen[0]['e']} and reihenfolge = {zeilen[0]['r']};
update schule.einheit set status = 'freigegeben' where id = {zeilen[0]['e']};""")
        # veränderte Lösung (gleicher Text) -> Abbruch mit „Lösung … statt … wie eingespielt“
        z1 = zeilen[1]
        pg.sql(f"""update schule.einheit set status = 'geprueft' where id = {z1['e']};
update schule.aufgabe set loesung = loesung || '{{"toleranz": 0.5}}' where einheit_id = {z1['e']} and reihenfolge = {z1['r']};
update schule.einheit set status = 'freigegeben' where id = {z1['e']};""")
        rc, pk, _ = py('tools/regelbezug_sql.py', '--runden', ','.join(map(str, ALLE)), '--sql')   # Runden 1-13 (14 nur einzeln, s. gemischte_runden)
        assert rc == 0, rc
        out = pg.sql(pk, erwartet_fehler='ist nicht die erwartete')
        assert f"{z1['k']}: Aufgabe" in out and 'wie eingespielt' in out, out[-1500:]
        print('Teil 2 (lokaler Nachbau) bestanden')
    finally:
        pg.ende()


def main():
    zeilen = teil1()
    teil2(zeilen)
    print('OK')


if __name__ == '__main__':
    main()
