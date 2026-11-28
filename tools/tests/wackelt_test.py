"""Test für WW-S2 („Was wackelt“, Teil Datenbank, ohne Nachüben) im lokalen NACHBAU (tools/tests/regelbezug_nachbau.sql, nicht die echte Datenbank).
Ablauf: leere Postgres-Instanz, Nachbau mit allen eingespielten Aufgaben; Probelauf WW-S2 ohne RB-S muss „PROBELAUF bestanden“ melden
(mit Nachweis: bestehende Funktionen/Trigger/Spalten und alle Daten außer schule.fehler_erledigt gleich, Abhaken ohne Wirkung auf die Karte);
Einspiel-Paket läuft durch und ein zweites Mal (wiederholbar); dann RB-S und die Nachträge, Probelauf noch einmal (jetzt mit Fehlbild);
Rechte über die api-Aktionen: Kind bekommt keine Analyse und hakt nicht ab, fremdes Kind auch nicht, Eltern schon; Nachüben-Aktionen gibt es nicht.
WW-S3 (Folgemigration): Probe vor WW-S2 bricht mit „Vorbedingung“ ab; nach WW-S2 (ohne RB-S) „PROBELAUF bestanden“ mit allen Nachweisen
(Parallelfall, ohne Thema auch jenseits der 300, besprochen je Thema, Typen, Karte, Rechte); Einspielen zweimal; nach RB-S noch einmal (mit Fehlbild,
Stand 3 vorher); Rechte und neue Antwortformen über die api-Aktionen; Edge-Liste 0.9.6.
Aufruf: python3 -I tools/tests/wackelt_test.py   (endet mit OK; ohne Postgres: übersprungen)
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import regelbezug_sql_test as T  # noqa: E402


def meldung(out):
    """Nur die Fehlerzeile von psql (der Kontext dahinter enthält den SQL-Text des Pakets und damit jedes Stichwort)."""
    z = [x for x in out.splitlines() if 'ERROR:' in x]
    assert len(z) == 1 and 'PROBELAUF bestanden' in z[0], out[-1500:]
    return z[0]


def bericht(zeile):
    """Bericht (JSON) aus der Zeile „PROBELAUF bestanden …: {…}“ bzw. „WW-S3 eingespielt: {…}“."""
    return json.loads(zeile[zeile.index('{'):])


def ww3_probe(pg, probe, mit_fehlbild, stand_vorher):
    out = meldung(pg.paket(probe, erwartet_fehler='PROBELAUF bestanden'))
    b = bericht(out)
    assert b['fehler'] == 0 and b['schema_bestehend_gleich'] and b['bestand_gleich'] and b['fehler_erledigt_gleich'], b
    assert b['bestand_gleich_beim_markieren'] and b['typen_ok'] and b['mit_fehlbild'] is mit_fehlbild and b['stand_vorher'] == stand_vorher, b
    assert 'hinweis_danach_richtig' not in b and 'hinweis_ohne_thema' not in b and 'hinweis_fremdkind' not in b, b
    # Parallelfall: veralteter Eintrag übersprungen
    pf = b['parallelfall']
    assert pf['antwort']['geaendert'] == 0 and pf['antwort']['uebersprungen'][0]['grund'] == 'überholt' and pf['neu'] != pf['veraltet'], pf
    # ohne Thema: im Nachbau gibt es keine Einheit ohne Thema -> vorübergehend; 300 neue Fehler, die beiden liegen jenseits der 300 und zählen trotzdem
    ot = b['ohne_thema']
    assert ot['weg'] == 'vorübergehend ohne Thema' and ot['neue_fehler'] == 300 and ot['jenseits_300'] is True, ot
    assert ot['offen_ohne_thema'] >= 2 and ot['offen_ohne_thema_danach'] >= 2 and ot['offen_zahl_danach'] >= ot['offen_zahl'] + 300, ot
    bs = b['besprochen_beispiel']
    assert bs['tage'] == 2 and bs['neu_seit'] >= 1 and isinstance(bs['zuletzt'], str), bs
    for lauf in ('mit_markierung', 'ohne_markierung'):
        assert b['karte_markierung_ohne_wirkung'][lauf] == {'nach_1_fehler': {'sitzt': True, 'wdh_fehler': 1}, 'nach_2_fehler': {'sitzt': False, 'geoeffnet': True, 'wdh_fehler': 0}}, b
    assert 'laufzeit_ms_testkind' in b and 'laufzeit_ms_300' in ot, b
    return b


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
        probe3, einspielen3 = lies('ww_s3_probe.sql'), lies('ww_s3_einspielen.sql')
        z = [x for x in pg.paket(probe3, erwartet_fehler='WW-S3 ABBRUCH').splitlines() if 'ERROR:' in x]
        assert len(z) == 1 and 'Vorbedingung: WW-S2 ist nicht eingespielt' in z[0], z   # WW-S3 setzt WW-S2 voraus
        einspielen = lies('ww_s_einspielen.sql')
        for _ in range(2):   # zweiter Lauf: wiederholbar
            hinweis = [z for z in pg.paket(einspielen).splitlines() if 'NOTICE:' in z and 'WW-S eingespielt' in z]
            assert len(hinweis) == 1 and '"fehler": 0' in hinweis[0] and '"bestand_gleich": true' in hinweis[0], hinweis
        assert 'nachueb' not in pg.sql("\\pset tuples_only on\nselect string_agg(proname, ',') from pg_proc where proname like '%nachueb%';")
        assert 'nachueb' not in pg.sql("\\pset tuples_only on\nselect string_agg(relname, ',') from pg_class where relname like '%nachueb%';")
        b3 = ww3_probe(pg, probe3, False, 2)   # WW-S3 auf „WW-S2 eingespielt“, ohne RB-S
        print('WW-S3 Probe (ohne RB-S):', json.dumps({x: b3[x] for x in ('laufzeit_ms_testkind', 'besprochen_beispiel')}, ensure_ascii=False),
              'laufzeit_ms_300', b3['ohne_thema']['laufzeit_ms_300'])
        pg.paket(lies('rb_s_einspielen.sql'))   # RB-S nach WW-S (umgekehrte Reihenfolge geht auch)
        for r in T.ALLE:
            pg.paket(lies(f'rb_nachtrag_r{r:02d}.sql'))
        out = meldung(pg.paket(probe, erwartet_fehler='PROBELAUF bestanden'))
        assert '"mit_fehlbild": true' in out and '"fehler": 0' in out, out[-600:]
        ww3_probe(pg, probe3, True, 2)   # mit Fehlbild
        for _ in range(2):   # WW-S3 echt, zweiter Lauf wiederholbar
            hinweis = [z for z in pg.paket(einspielen3).splitlines() if 'NOTICE:' in z and 'WW-S3 eingespielt' in z]
            assert len(hinweis) == 1 and bericht(hinweis[0])['fehler'] == 0 and bericht(hinweis[0])['bestand_gleich'], hinweis
        ww3_probe(pg, probe3, True, 3)   # Probe auf dem Stand „WW-S3 eingespielt“ (zweiter Lauf ändert nichts)
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
        # WW-S3 über die api-Aktionen (nach dem Einspielen): Markieren liefert markierung_ids, Zurückholen nur diese, Kind darf nichts
        tq = lambda q: pg.sql('\\pset tuples_only on\n' + q).strip()
        pg.sql("insert into schule.lern_login (name, rolle, lernender_id, code_hash) values ('L', 'lehrer', null, 'c4');"
               "insert into schule.lern_sitzung (token_hash, login_id, laeuft_ab) select 't' || id, id, now() + interval '1 hour' from schule.lern_login where code_hash = 'c4';")
        pg.sql("select schule.uebung_pruefen_wd(1, jsonb_build_object('aufgabe_id', (select min(id) from schule.aufgabe where antworttyp = 'zahl'), 'client_id', 'ww3-t', 'antwort', '{\"wert\": \"987654\"}'::jsonb));")
        v = tq("select id from schule.versuch where client_id = 'ww3-t';")
        r = json.loads(tq(f"select api.schule_fehler_abhaken({kid(3)}, '{{\"lernender_id\": 1, \"versuch_ids\": [{v}]}}');"))
        assert r['stand'] == 3 and r['geaendert'] == 1 and r['geaendert_ids'] == [int(v)] and len(r['markierung_ids']) == 1, r
        mid = r['markierung_ids'][0]
        a = json.loads(tq(f"select api.schule_wackelt_analyse({kid(3)}, '{{\"lernender_id\": 1, \"tage\": 0, \"erledigt\": true}}');"))
        e = next(x for x in a['erledigt'] if x['versuch_id'] == int(v))
        assert a['stand'] == 3 and e['erledigt']['id'] == mid and isinstance(e['mit_tipp'], bool) and 'tag' in e['erledigt'], e
        assert any('besprochen' in t for t in a['auswertung']['themen']), a['auswertung']['themen']
        pg.sql(f"select api.schule_fehler_abhaken({kid(1)}, '{{\"lernender_id\": 1, \"markierung_ids\": [{mid}], \"zurueck\": true}}');", erwartet_fehler='Nur Eltern/Lehrer')
        pg.sql(f"select api.schule_fehler_abhaken({kid(3)}, '{{\"lernender_id\": 1, \"markierung_ids\": [{mid}]}}');", erwartet_fehler='markierung_ids nur mit zurueck')
        r = json.loads(tq(f"select api.schule_fehler_abhaken({kid(4)}, '{{\"lernender_id\": 1, \"markierung_ids\": [{mid}], \"zurueck\": true}}');"))
        assert r == {'ok': True, 'stand': 3, 'geaendert': 1, 'geaendert_ids': [mid], 'uebersprungen': []}, r
        r = json.loads(tq(f"select api.schule_fehler_abhaken({kid(4)}, '{{\"lernender_id\": 1, \"markierung_ids\": [{mid}], \"zurueck\": true}}');"))
        assert r['geaendert'] == 0 and r['uebersprungen'] == [{'markierung_id': mid, 'versuch_id': int(v), 'grund': 'schon zurückgeholt'}], r
        print('WW-S3 Antwortformen:', json.dumps(r, ensure_ascii=False))
        # Edge-Funktion: genau die zwei Aktionen, keine Nachüben-Aktion, Version 0.9.6 mit markierung_ids?
        ts = (T.WURZEL / 'supabase/functions/lernen-api/index.ts').read_text(encoding='utf-8')
        assert "const VERSION = '0.9.6'" in ts and "schule_wackelt_analyse: ['lernender_id', 'tage?', 'erledigt?']," in ts
        assert "schule_fehler_abhaken: ['lernender_id', 'versuch_ids', 'zurueck?', 'markierung_ids?']," in ts and 'schule_nachueben' not in ts.split('const AKTIONEN')[1]
        print('WW-S2 im Nachbau bestanden')
        print('WW-S3 im Nachbau bestanden')
    finally:
        pg.ende()
    print('OK')


if __name__ == '__main__':
    main()
