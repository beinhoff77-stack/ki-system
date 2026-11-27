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
    for r in ALLE:
        rc, out, err = py('tools/regelbezug_sql.py', '--runden', str(r), '--sql')
        assert rc == 0 and out.count('$rbf$') % 2 == 0 and 'do $rbnach$' in out, (r, err[-400:])
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

    def ende(self):
        self.als(f'{self.bin}/pg_ctl -D {self.dir}/d -m immediate stop > /dev/null 2>&1 || true')
        shutil.rmtree(self.dir, ignore_errors=True)


def nachbau_sql():
    s = (WURZEL / 'supabase/migrations/20261116_w150_r2_fehlermuster_zweiter_versuch.sql').read_text(encoding='utf-8')
    i = s.index('create or replace function schule.antwort_bewerten')
    ab = s[i:s.index('end $function$;', i) + len('end $function$;')]
    plan = json.loads((WURZEL / 'inhalte/plan/rollend-einheiten.json').read_text(encoding='utf-8'))
    teile = [(WURZEL / 'tools/tests/regelbezug_nachbau.sql').read_text(encoding='utf-8'), ab + '\n']
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
        rc, probe, err = py('tools/tests/regelbezug_einspielen.py', '--probe')
        assert rc == 0, err
        pg.sql(probe, erwartet_fehler='PROBELAUF bestanden')
        assert 'from schule.aufgabe_fehlbild' in pg.sql("select 'from schule.aufgabe_fehlbild' where to_regclass('schule.aufgabe_fehlbild') is null;")
        rc, ein, err = py('tools/tests/regelbezug_einspielen.py')
        out = pg.sql(ein)
        assert 'RB-S eingespielt' in out, out[-800:]
        # Probe-Lauf eines Nachtrags (rollt zurück), dann alle Runden zweimal
        rc, p5, err = py('tools/regelbezug_sql.py', '--runden', '5', '--sql', '--probe')
        pg.sql(p5, erwartet_fehler='PROBELAUF bestanden')
        for runde in ALLE:
            rc, paket, err = py('tools/regelbezug_sql.py', '--runden', str(runde), '--sql')
            assert rc == 0, err
            out1 = pg.sql(paket)
            out2 = pg.sql(paket)
            assert 'Fehlbilder neu' in out1 and ', 0 Regeln neu, 0 Fehlbilder neu' in out2, (runde, out1[-300:], out2[-300:])
        zahl = pg.sql("\\pset tuples_only on\nselect count(*) || ' ' || (select count(*) from schule.aufgabe_fehlbild) from schule.aufgabe_regel;").split()
        assert int(zahl[0]) == sum(1 for x in zeilen if x['regel']) and int(zahl[1]) == sum(len(x['fb']) for x in zeilen), zahl
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
        rc, pk, _ = py('tools/regelbezug_sql.py', '--runden', 'alle', '--sql')
        pg.sql(pk, erwartet_fehler='ist nicht die erwartete')
        print('Teil 2 (lokaler Nachbau) bestanden')
    finally:
        pg.ende()


def main():
    zeilen = teil1()
    teil2(zeilen)
    print('OK')


if __name__ == '__main__':
    main()
