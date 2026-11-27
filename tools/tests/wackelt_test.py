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
        aus = T.WURZEL / 'tools/tests/aus'
        lies = lambda n: (aus / n).read_text(encoding='utf-8')
        probe = lies('ww_s_probe.sql')
        out = pg.paket(probe, erwartet_fehler='PROBELAUF bestanden')
        assert '"mit_fehlbild": false' in out and '"tagesgrenze"' in out and '"karte_sitzt_nicht_faellig"' in out and 'laufzeit_ms_testkind' in out, out[-1500:]
        # Karte im Nachbau (karte_buchen wie live laut Repo): 1. Fehler an der sitzenden Karte -> bleibt sitzen (wdh_fehler 1), 2. Fehler -> wieder offen
        assert '"nach_1_fehler": {"sitzt": true, "wdh_fehler": 1}' in out and '"nach_2_fehler": {"sitzt": false, "geoeffnet": true, "wdh_fehler": 0}' in out, out[-1500:]
        assert 'WW-S eingespielt' in pg.paket(lies('ww_s_einspielen.sql'))
        pg.paket(lies('rb_s_einspielen.sql'))   # RB-S nach WW-S (umgekehrte Reihenfolge geht auch)
        for r in T.ALLE:
            pg.paket(lies(f'rb_nachtrag_r{r:02d}.sql'))
        out = pg.paket(probe, erwartet_fehler='PROBELAUF bestanden')
        assert '"mit_fehlbild": true' in out, out[-600:]
        # Rechte über die api-Aktionen mit echten Lern-Schlüsseln (Funktionen aus der Zugangs-Migration)
        pg.sql("""insert into schule.lern_login (name, rolle, lernender_id, code_hash) values ('K1', 'kind', 1, 'c1'), ('K2', 'kind', 2, 'c2'), ('E', 'eltern', null, 'c3');
insert into schule.lern_sitzung (token_hash, login_id, laeuft_ab) select 't' || id, id, now() + interval '1 hour' from schule.lern_login;""")
        kid = lambda n: "(select 'lern:t' || id from schule.lern_login where code_hash = 'c%d')" % n
        pg.sql(f"select api.schule_wackelt_analyse({kid(1)}, '{{\"lernender_id\": 1}}');", erwartet_fehler='Nur Eltern/Lehrer')
        pg.sql(f"select api.schule_nachueben_schicken({kid(1)}, '{{\"lernender_id\": 1, \"versuch_ids\": [1]}}');", erwartet_fehler='Nur Eltern/Lehrer')
        pg.sql(f"select api.schule_nachueben_lesen({kid(2)}, '{{\"lernender_id\": 1}}');", erwartet_fehler='Kein Zugriff')
        assert 'true' in pg.sql(f"\\pset tuples_only on\nselect api.schule_nachueben_lesen({kid(1)}, '{{\"lernender_id\": 1}}')->>'ok';")
        assert 'true' in pg.sql(f"\\pset tuples_only on\nselect api.schule_wackelt_analyse({kid(3)}, '{{\"lernender_id\": 1, \"tage\": 0}}')->>'ok';")
        pg.sql(f"select api.schule_wackelt_analyse({kid(3)}, '{{\"lernender_id\": 1, \"tage\": 3}}');", erwartet_fehler='tage')
        print('WW-S im Nachbau bestanden')
    finally:
        pg.ende()
    print('OK')


if __name__ == '__main__':
    main()
