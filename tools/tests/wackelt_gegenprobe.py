"""Gegenprobe für WW-S2: erkennt das Probe-Paket einen Eingriff in die Lernlogik? Lokal im NACHBAU (nicht die echte Datenbank).
Die Migration wird absichtlich verdorben (nur im Speicher, die Datei bleibt unberührt), daraus ein Probe-Paket erzeugt und im Nachbau ausgeführt.
Jede Fassung muss mit „WW-S ABBRUCH“ enden; die unveränderte Fassung mit „PROBELAUF bestanden“.
Aufruf: python3 -I tools/tests/wackelt_gegenprobe.py   (endet mit OK; ohne Postgres: übersprungen)
"""
import contextlib
import io
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import regelbezug_sql_test as T  # noqa: E402
import wackelt_einspielen as E  # noqa: E402

ABHAKEN_SCHLEIFE = "    get diagnostics c = row_count; n := n + c;\n  end loop;"
ANALYSE_ENDE = "  return jsonb_strip_nulls(r);\nend $function$;"
LEITER = "  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;\n"


def verdorben(mig):
    i = mig.index('create or replace function api.schule_fehler_abhaken')
    j = mig.index(LEITER, i)
    return {
        'Abhaken schreibt in die Karte': mig.replace(ABHAKEN_SCHLEIFE, ABHAKEN_SCHLEIFE.replace('  end loop;',
            "    if to_regclass('schule.karte_stand') is not null then execute 'update schule.karte_stand set wdh_fehler = 0 where lernender_id = $1' using p_l; end if;\n  end loop;")),
        'Analyse schreibt in eine bestehende Tabelle': mig.replace(ANALYSE_ENDE,
            "  update schule.lernender set zeitzone = coalesce(zeitzone, 'Europe/Berlin') where id = p_l;\n" + ANALYSE_ENDE),
        'Migration ändert eine bestehende Funktion': mig + "\ncreate or replace function schule.ist_lern(p_schluessel text) returns boolean language sql immutable as $$ select coalesce(left(p_schluessel, 5) = 'lern:', false) and true $$;\n",
        'neuer Trigger an schule.versuch': mig + "\ncreate or replace function schule.ww_x() returns trigger language plpgsql as $$ begin return new; end $$;\n"
                                                  "drop trigger if exists ww_x on schule.versuch; create trigger ww_x after insert on schule.versuch for each row execute function schule.ww_x();\n",
        'Fremdschlüssel auf schule.versuch': mig.replace('  versuch_id bigint not null,     --', '  versuch_id bigint not null references schule.versuch(id),     --'),
        'Abhaken ohne ist_leiter': mig[:j] + mig[j + len(LEITER):],
    }


def paket(mig, ordner):
    f = Path(ordner) / 'mig.sql'
    f.write_text(mig, encoding='utf-8')
    alt, E.MIG = E.MIG, f
    alt_argv, sys.argv = sys.argv, ['wackelt_einspielen.py', '--probe']
    try:
        b = io.StringIO()
        with contextlib.redirect_stdout(b):
            E.main()
        return b.getvalue()
    finally:
        E.MIG, sys.argv = alt, alt_argv


def fehlerzeile(out):
    z = [x for x in out.splitlines() if 'ERROR:' in x]
    assert len(z) == 1, out[-1500:]
    return z[0]


def main():
    b = T.pg_bin()
    if not b:
        print('übersprungen (kein Postgres)'); print('OK'); return
    mig = E.MIG.read_text(encoding='utf-8')
    pg = T.PG(b)
    try:
        pg.sql(T.nachbau_sql())
        with tempfile.TemporaryDirectory() as d:
            assert 'PROBELAUF bestanden' in fehlerzeile(pg.paket(paket(mig, d), erwartet_fehler='ERROR'))
            faelle = verdorben(mig)
            for name, m in faelle.items():
                assert m != mig, name
                z = fehlerzeile(pg.paket(paket(m, d), erwartet_fehler='ERROR'))
                assert 'WW-S ABBRUCH' in z, (name, z[:500])
                print(f'erkannt: {name}')
        print(f'WW-S2 Gegenprobe bestanden ({len(faelle)} von {len(faelle)} Eingriffen erkannt)')
    finally:
        pg.ende()
    print('OK')


if __name__ == '__main__':
    main()
