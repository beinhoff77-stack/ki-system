"""Test für WW-S2 („Was wackelt“, Teil Datenbank, ohne Nachüben) im lokalen NACHBAU (tools/tests/regelbezug_nachbau.sql, nicht die echte Datenbank).
Ablauf: leere Postgres-Instanz, Nachbau mit allen eingespielten Aufgaben; Probelauf WW-S2 ohne RB-S muss „PROBELAUF bestanden“ melden
(mit Nachweis: bestehende Funktionen/Trigger/Spalten und alle Daten außer schule.fehler_erledigt gleich, Abhaken ohne Wirkung auf die Karte);
Einspiel-Paket läuft durch und ein zweites Mal (wiederholbar); dann RB-S und die Nachträge, Probelauf noch einmal (jetzt mit Fehlbild);
Rechte über die api-Aktionen: Kind bekommt keine Analyse und hakt nicht ab, fremdes Kind auch nicht, Eltern schon; Nachüben-Aktionen gibt es nicht.
Aufruf: python3 -I tools/tests/wackelt_test.py   (endet mit OK; ohne Postgres: übersprungen)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import regelbezug_sql_test as T  # noqa: E402


def meldung(out):
    """Nur die Fehlerzeile von psql (der Kontext dahinter enthält den SQL-Text des Pakets und damit jedes Stichwort)."""
    z = [x for x in out.splitlines() if 'ERROR:' in x]
    assert len(z) == 1 and 'PROBELAUF bestanden' in z[0], out[-1500:]
    return z[0]


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
        out = meldung(pg.paket(probe, erwartet_fehler='PROBELAUF bestanden'))
        for teil in ('"mit_fehlbild": false', '"fehler": 0', '"bestand_gleich": true', '"schema_bestehend_gleich": true', '"bestand_gleich_beim_abhaken": true',
                     '"karte_abhaken_ohne_wirkung"', 'laufzeit_ms_testkind'):
            assert teil in out, (teil, out[-1500:])
        assert 'nachueben' not in out and 'tagesgrenze' not in out, out[-1500:]
        # Karte im Nachbau (karte_buchen wie live laut Repo): 1. Fehler an der sitzenden Karte -> bleibt sitzen (wdh_fehler 1), 2. Fehler -> wieder offen,
        # mit und ohne Abhaken gleich
        for lauf in ('mit_abhaken', 'ohne_abhaken'):
            assert f'"{lauf}": {{"nach_1_fehler": {{"sitzt": true, "wdh_fehler": 1}}, "nach_2_fehler": {{"sitzt": false, "geoeffnet": true, "wdh_fehler": 0}}}}' in out, out[-1500:]
        einspielen = lies('ww_s_einspielen.sql')
        for _ in range(2):   # zweiter Lauf: wiederholbar
            hinweis = [z for z in pg.paket(einspielen).splitlines() if 'NOTICE:' in z and 'WW-S eingespielt' in z]
            assert len(hinweis) == 1 and '"fehler": 0' in hinweis[0] and '"bestand_gleich": true' in hinweis[0], hinweis
        assert 'nachueb' not in pg.sql("\\pset tuples_only on\nselect string_agg(proname, ',') from pg_proc where proname like '%nachueb%';")
        assert 'nachueb' not in pg.sql("\\pset tuples_only on\nselect string_agg(relname, ',') from pg_class where relname like '%nachueb%';")
        pg.paket(lies('rb_s_einspielen.sql'))   # RB-S nach WW-S (umgekehrte Reihenfolge geht auch)
        for r in T.ALLE:
            pg.paket(lies(f'rb_nachtrag_r{r:02d}.sql'))
        out = meldung(pg.paket(probe, erwartet_fehler='PROBELAUF bestanden'))
        assert '"mit_fehlbild": true' in out and '"fehler": 0' in out, out[-600:]
        # Rechte über die api-Aktionen mit echten Lern-Schlüsseln (Funktionen aus der Zugangs-Migration)
        pg.sql("""insert into schule.lern_login (name, rolle, lernender_id, code_hash) values ('K1', 'kind', 1, 'c1'), ('K2', 'kind', 2, 'c2'), ('E', 'eltern', null, 'c3');
insert into schule.lern_sitzung (token_hash, login_id, laeuft_ab) select 't' || id, id, now() + interval '1 hour' from schule.lern_login;""")
        kid = lambda n: "(select 'lern:t' || id from schule.lern_login where code_hash = 'c%d')" % n
        pg.sql(f"select api.schule_wackelt_analyse({kid(1)}, '{{\"lernender_id\": 1}}');", erwartet_fehler='Nur Eltern/Lehrer')
        pg.sql(f"select api.schule_wackelt_analyse({kid(2)}, '{{\"lernender_id\": 1}}');", erwartet_fehler='Nur Eltern/Lehrer')
        pg.sql(f"select api.schule_fehler_abhaken({kid(1)}, '{{\"lernender_id\": 1, \"versuch_ids\": [1]}}');", erwartet_fehler='Nur Eltern/Lehrer')
        pg.sql("select api.schule_wackelt_analyse('lern:gibt-es-nicht', '{\"lernender_id\": 1}');", erwartet_fehler='Nicht angemeldet')
        pg.sql(f"select api.schule_nachueben_lesen({kid(1)}, '{{\"lernender_id\": 1}}');", erwartet_fehler='does not exist')
        assert 'true' in pg.sql(f"\\pset tuples_only on\nselect api.schule_wackelt_analyse({kid(3)}, '{{\"lernender_id\": 1, \"tage\": 0}}')->>'ok';")
        pg.sql(f"select api.schule_wackelt_analyse({kid(3)}, '{{\"lernender_id\": 1, \"tage\": 3}}');", erwartet_fehler='tage')
        # Edge-Funktion: genau die zwei Aktionen, keine Nachüben-Aktion, Version 0.9.5
        ts = (T.WURZEL / 'supabase/functions/lernen-api/index.ts').read_text(encoding='utf-8')
        assert "const VERSION = '0.9.5'" in ts and "schule_wackelt_analyse: ['lernender_id', 'tage?', 'erledigt?']," in ts
        assert "schule_fehler_abhaken: ['lernender_id', 'versuch_ids', 'zurueck?']," in ts and 'schule_nachueben' not in ts.split('const AKTIONEN')[1]
        print('WW-S2 im Nachbau bestanden')
    finally:
        pg.ende()
    print('OK')


if __name__ == '__main__':
    main()
