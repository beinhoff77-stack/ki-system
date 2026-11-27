"""Test für WW-S („Was wackelt“, Teil Datenbank) im lokalen NACHBAU (tools/tests/regelbezug_nachbau.sql, nicht die echte Datenbank).
Ablauf: leere Postgres-Instanz, Nachbau mit allen eingespielten Aufgaben; Probelauf WW-S ohne RB-S muss „PROBELAUF bestanden“ melden;
Einspiel-Paket WW-S läuft durch; dann RB-S und die Nachträge, Probelauf WW-S noch einmal (jetzt mit Fehlbild); Kind-Schlüssel bekommt keine Analyse,
Eltern-Schlüssel schon; Kind liest seine Nachübe-Liste, nicht die eines anderen Kindes.
Aufruf: python3 -I tools/tests/wackelt_test.py   (endet mit OK; ohne Postgres: übersprungen)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import regelbezug_sql_test as T  # noqa: E402


def main():
    b = T.pg_bin()
    if not b:
        print('übersprungen (kein Postgres)'); print('OK'); return
    pg = T.PG(b)
    try:
        pg.sql(T.nachbau_sql())
        rc, probe, err = T.py('tools/tests/wackelt_einspielen.py', '--probe'); assert rc == 0, err
        out = pg.sql(probe, erwartet_fehler='PROBELAUF bestanden')
        assert '"mit_fehlbild": false' in out, out[-600:]
        rc, ein, err = T.py('tools/tests/wackelt_einspielen.py'); assert rc == 0, err
        assert 'WW-S eingespielt' in pg.sql(ein)
        rc, rb, err = T.py('tools/tests/regelbezug_einspielen.py'); pg.sql(rb)
        for r in T.ALLE:
            rc, p, err = T.py('tools/regelbezug_sql.py', '--runden', str(r), '--sql'); pg.sql(p)
        out = pg.sql(probe.replace('PROBELAUF bestanden', 'PROBELAUF bestanden'), erwartet_fehler='PROBELAUF bestanden')
        assert '"mit_fehlbild": true' in out, out[-600:]
        # Rechte über die api-Aktionen (Nachbau-Schlüssel: 'eltern:<kind>' / 'kind:<kind>')
        pg.sql("select api.schule_wackelt_analyse('kind:1', '{\"lernender_id\": 1}');", erwartet_fehler='Nur Eltern/Lehrer')
        pg.sql("select api.schule_nachueben_schicken('kind:1', '{\"lernender_id\": 1, \"versuch_ids\": [1]}');", erwartet_fehler='Nur Eltern/Lehrer')
        pg.sql("select api.schule_wackelt_analyse('eltern:2', '{\"lernender_id\": 1}');", erwartet_fehler='Kein Zugriff')
        out = pg.sql("\\pset tuples_only on\nselect api.schule_wackelt_analyse('eltern:1', '{\"lernender_id\": 1, \"tage\": 0}')->>'ok';")
        assert 'true' in out
        pg.sql("select api.schule_nachueben_lesen('kind:2', '{\"lernender_id\": 1}');", erwartet_fehler='Kein Zugriff')
        out = pg.sql("\\pset tuples_only on\nselect api.schule_nachueben_lesen('kind:1', '{\"lernender_id\": 1}')->>'ok';")
        assert 'true' in out
        pg.sql("select api.schule_wackelt_analyse('eltern:1', '{\"lernender_id\": 1, \"tage\": 3}');", erwartet_fehler='tage')
        print('WW-S im Nachbau bestanden')
    finally:
        pg.ende()
    print('OK')


if __name__ == '__main__':
    main()
