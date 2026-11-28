"""TEMPO-S1: Pakete für supabase/migrations/20261207_tempo_s1.sql (schule.etappen_stand schneller, Ergebnis byte-gleich; zwei Indizes).

Schreibt nach tools/tests/aus/ (je Schritt EINE Datei, in einem `execute` lauffähig: kein psql-Meta, kein eigenes BEGIN/COMMIT):
  tempo_s1_probe.sql      Probelauf: misst vorher, spielt ein, misst nachher, vergleicht je Kind × Einheit (etappen_stand) und je Kind (Merkheft-Kopie)
                          per md5; endet IMMER mit „PROBELAUF bestanden, ALLES zurückgerollt …“ (oder „TEMPO-S1 ABBRUCH …“ bei einer Abweichung).
  tempo_s1_einspielen.sql dasselbe, bleibt bei Gleichheit eingespielt (Hinweis „TEMPO-S1 eingespielt: …“); bei einer Abweichung Abbruch, nichts geändert.
  tempo_s1_messen.sql     nach dem Einspielen (neue Transaktion): nur Laufzeiten, ändert nichts (endet mit „MESSUNG … nichts geändert“).
Die Merkheft-Kopie: api.schule_merkheft liegt nicht im Repo; das Paket legt aus ihrem eingespielten Text eine Kopie in pg_temp an, deren Zugriffsprüfung
(schule.zugriff) durch eine Funktion ohne Prüfung ersetzt ist – nur für den Vergleich und die Messung in dieser Sitzung (on commit weg).

Aufruf:  python3 -I tools/tests/tempo_einspielen.py             -> schreibt die Dateien, druckt Größe und md5
         python3 -I tools/tests/tempo_einspielen.py --pruefen   -> schreibt nichts; Rückgabe 1, wenn eine Datei nicht dem Stand entspricht
         python3 -I tools/tests/tempo_einspielen.py --alt-sql   -> druckt create-Anweisung der ALTEN etappen_stand (für den lokalen Nachbau)
"""
import hashlib
import re
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
MIG = WURZEL / 'supabase/migrations'
AUS = WURZEL / 'tools/tests/aus'
MIGRATION = MIG / '20261207_tempo_s1.sql'


def alter_text():
    """Funktionstext (prosrc) von schule.etappen_stand nach allen Migrationen im Repo, in ihrer Reihenfolge nachgerechnet."""
    s = (MIG / '20261114_w150_lernkarten_meisterschaft.sql').read_text(encoding='utf-8')
    i = s.index('create or replace function schule.etappen_stand(')
    j = s.index('as $$', i) + 5
    b = s[j:s.index('$$;', j)]

    def rep(b, alt, neu, datei):
        assert b.count(alt) == 1, (datei, alt[:50])
        return b.replace(alt, neu)
    # 20261116_w150_r3_wiederholung_lerntage.sql
    b = rep(b, 'k.sitzt and k.faellig_am <= now()', 'schule.karte_faellig(k)', '20261116_w150_r3_wiederholung_lerntage.sql')
    # 20261116_w150_sitzt_regel_6_mit_schwer.sql
    b = rep(b, "'sitzt', coalesce(k.sitzt, false),", "'sitzt', coalesce(k.sitzt, false), 'schwer_ok', coalesce(k.schwer_ok, false), 'schwer_noetig', schule.karte_schwer_noetig(p_einheit, z.lz),",
            '20261116_w150_sitzt_regel_6_mit_schwer.sql')
    # 20261118_w176_t1_punkteregel.sql
    b = rep(b, "'wdh_stufe', coalesce(k.wdh_stufe, 0),", """'wdh_stufe', coalesce(k.wdh_stufe, 0),
           'eigene_loesungen', coalesce(k.eigene_loesungen, 0), 'folge', coalesce(k.folge, 0), 'folge_ziel', least(3, schule.karte_ziel(p_einheit, z.lz)),
           'typen_anzahl', coalesce(array_length(k.typen, 1), 0), 'typen_noetig', schule.karte_typen_noetig(p_einheit, z.lz),
           'fehler_folge', coalesce(k.fehler_folge, 0), 'stufe_senkung', coalesce(k.stufe_senkung, 0), 'sicher', coalesce(schule.karte_sicher(k), false),""",
            '20261118_w176_t1_punkteregel.sql')
    # 20261118_w176_t3_mischkarten.sql
    b = rep(b, "'sicher', coalesce(schule.karte_sicher(k), false),", "'sicher', coalesce(schule.karte_sicher(k), false), 'misch_ok', k.misch_ok_am is not null,",
            '20261118_w176_t3_mischkarten.sql')
    # 20261119_w176_h_muss.sql
    b = rep(b, "'fertig', coalesce(k.sitzt, false) or coalesce(s.status in ('nachgewiesen','korrigiert','gesichert'), false)",
            "'fertig', schule.etappe_fertig(k, s.status), 'test_nachgewiesen', coalesce(s.status in ('nachgewiesen','korrigiert','gesichert'), false), 'wieder_offen', not coalesce(k.sitzt, false) and k.sitzt_am is not null, 'gezaehlt', coalesce((select jsonb_agg(x::bigint) from jsonb_object_keys(k.gezaehlt) x), '[]'::jsonb)",
            '20261119_w176_h_muss.sql')
    b = rep(b, "'misch_ok', k.misch_ok_am is not null,",
            "'misch_ok', k.misch_ok_am is not null and k.misch_ok_am >= coalesce(k.sitzt_am, k.misch_ok_am), 'flug_nachtest', schule.flug_nachtest(p_lernender, p_einheit),",
            '20261119_w176_h_muss.sql')
    # 20261203_ft_s_form_takt.sql
    b = rep(b, "'schwer_ok', coalesce(k.schwer_ok, false), 'schwer_noetig'", """'schwer_ok', coalesce(k.schwer_ok, false), 'anwenden_noetig', schule.karte_anwenden_pflicht(k, p_einheit, z.lz), 'anwenden_ok', coalesce(schule.karte_anwenden_ok(k), false),
           'bearbeitungen', schule.karte_bearbeitungen(p_lernender, p_einheit, z.lz), 'schwer_noetig'""", '20261203_ft_s_form_takt.sql')
    return b


def alter_sql():
    return ("create or replace function schule.etappen_stand(p_lernender bigint, p_einheit bigint) returns jsonb\n"
            "language sql stable set search_path to '' as $$" + alter_text() + "$$;\n")


def migration():
    m = MIGRATION.read_text(encoding='utf-8')
    soll = re.search(r"v_soll constant text := '([0-9a-f]{32})'", m).group(1)
    ist = hashlib.md5(alter_text().encode('utf-8')).hexdigest()
    assert soll == ist, f'md5 in der Migration ({soll}) passt nicht zum nachgerechneten Repo-Stand ({ist})'
    assert '$tempomig$' not in m and '$rbpaket$' not in m
    return m


HILFEN = r"""
-- Hilfen dieser Sitzung (pg_temp, verschwinden mit dem Ende der Transaktion)
create or replace function pg_temp.tempo_zugriff(p_schluessel text, p_lernender bigint) returns bigint language sql as $$ select null::bigint $$;
-- Merkheft-Kopie ohne Zugriffsprüfung (nur zum Vergleichen und Messen); fehlt die Stelle, bleibt der Merkheft-Vergleich aus (wird gemeldet)
create or replace function pg_temp.tempo_merkheft_anlegen() returns text language plpgsql as $f$
declare d text;
begin
  if to_regprocedure('api.schule_merkheft(text, jsonb)') is null then return 'api.schule_merkheft fehlt'; end if;
  d := pg_get_functiondef('api.schule_merkheft(text, jsonb)'::regprocedure);
  if position('schule.zugriff(' in d) = 0 then return 'keine Stelle schule.zugriff( in api.schule_merkheft'; end if;
  d := replace(d, 'CREATE OR REPLACE FUNCTION api.schule_merkheft(', 'CREATE OR REPLACE FUNCTION pg_temp.tempo_merkheft(');
  d := replace(d, 'schule.zugriff(', 'pg_temp.tempo_zugriff(');
  d := replace(d, ' SECURITY DEFINER', '');
  execute d;
  return 'ok';
exception when others then return 'Kopie nicht angelegt: ' || sqlerrm;
end $f$;
-- Ein Lauf: alle Kinder × alle Einheiten (etappen_stand) und je Kind die Merkheft-Kopie; md5 und Laufzeit. Was die Funktionen dabei schreiben
-- (keine bekannt), wird am Ende des Laufs zurückgerollt; die Ergebnisse bleiben in den Variablen.
create or replace function pg_temp.tempo_lauf(p_merk text) returns jsonb language plpgsql as $f$
declare h jsonb; mh jsonb := '{}'; t0 timestamptz; t1 timestamptz; ms_es numeric; ms_mh numeric; je jsonb := '{}'; status text := p_merk; r record; ms numeric;
begin
  begin
    perform setseed(0.5);
    t0 := clock_timestamp();
    select coalesce(jsonb_object_agg(l.id::text || '/' || e.id::text, md5(coalesce(schule.etappen_stand(l.id, e.id)::text, 'NULL'))), '{}') into h
      from schule.lernender l cross join schule.einheit e;
    ms_es := round(extract(epoch from clock_timestamp() - t0) * 1000, 1);
    ms_mh := 0;
    if p_merk = 'ok' then
      begin
        for r in select l.id from schule.lernender l order by l.id loop
          perform setseed(0.5);
          t1 := clock_timestamp();
          mh := mh || jsonb_build_object(r.id::text, md5(coalesce(pg_temp.tempo_merkheft(null, jsonb_build_object('lernender_id', r.id))::text, 'NULL')));
          ms := round(extract(epoch from clock_timestamp() - t1) * 1000, 1); ms_mh := ms_mh + ms;
          je := je || jsonb_build_object(r.id::text, ms);
        end loop;
        status := 'verglichen';
      exception when others then status := 'nicht verglichen: ' || sqlerrm; mh := null; je := null;
      end;
    end if;
    raise exception using errcode = 'TP999', message = 'zurueck';
  exception when sqlstate 'TP999' then null;
  end;
  return jsonb_build_object('h', h, 'mh', mh, 'ms_etappen_stand_alle', ms_es, 'ms_merkheft_summe', ms_mh, 'ms_merkheft_je_kind', je, 'merkheft', status);
end $f$;
create or replace function pg_temp.tempo_indizes() returns jsonb language sql as $f$
  select coalesce(jsonb_agg(jsonb_build_object('name', c.relname, 'tabelle', t.relname, 'def', pg_get_indexdef(c.oid), 'indcheckxmin', i.indcheckxmin) order by t.relname, c.relname), '[]')
    from pg_index i join pg_class c on c.oid = i.indexrelid join pg_class t on t.oid = i.indrelid join pg_namespace n on n.oid = t.relnamespace
   where n.nspname = 'schule' and t.relname in ('aufgabe', 'versuch');
$f$;
"""


def paket(probe):
    m = migration()
    kopf = f"""-- TEMPO-S1 {'Probelauf' if probe else 'Einspiel-Paket'} (erzeugt von tools/tests/tempo_einspielen.py{' – Probe' if probe else ''}). Ein Aufruf, eine Transaktion. Fehler = alles zurück.
-- Laufzeit: zweimal alle Kinder × Einheiten und je Kind das Merkheft (live vorher ≈ 4 s je Kind) – mit einigen zehn Sekunden rechnen.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '300s', true);
do $p$ begin
  if to_regprocedure('schule.etappen_stand(bigint, bigint)') is null or to_regclass('schule.aufgabe') is null or to_regclass('schule.versuch') is null then
    raise exception 'TEMPO-S1 ABBRUCH, Vorbedingung: schule.etappen_stand / schule.aufgabe / schule.versuch fehlt – nichts geändert';
  end if;
end $p$;
create temp table tempo_mig on commit drop as select $tempomig${m}$tempomig$::text as sql;
"""
    ende = ("  raise exception 'PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt): %', bericht::text;" if probe
            else "  raise notice 'TEMPO-S1 eingespielt: %', bericht::text;")
    rumpf = r"""
do $p$
declare vorher jsonb; nachher jsonb; merk text; idx_vorher jsonb; idx_nachher jsonb; def_vorher text; def_nachher text; abw jsonb; abw_mh jsonb; bericht jsonb; schon boolean;
begin
  def_vorher := (select p.prosrc from pg_proc p where p.oid = 'schule.etappen_stand(bigint, bigint)'::regprocedure);
  schon := position('TEMPO-S1' in def_vorher) > 0;
  idx_vorher := pg_temp.tempo_indizes();
  merk := pg_temp.tempo_merkheft_anlegen();
  vorher := pg_temp.tempo_lauf(merk);
  execute (select sql from tempo_mig);
  def_nachher := (select p.prosrc from pg_proc p where p.oid = 'schule.etappen_stand(bigint, bigint)'::regprocedure);
  idx_nachher := pg_temp.tempo_indizes();
  nachher := pg_temp.tempo_lauf(merk);
  select coalesce(jsonb_agg(a.key order by a.key), '[]') into abw
    from jsonb_each_text(vorher->'h') a full join jsonb_each_text(nachher->'h') b on b.key = a.key where a.value is distinct from b.value;
  if vorher->'mh' is not null and jsonb_typeof(vorher->'mh') = 'object' and nachher->'mh' is not null and jsonb_typeof(nachher->'mh') = 'object' then
    select coalesce(jsonb_agg(coalesce(a.key, b.key)), '[]') into abw_mh
      from jsonb_each_text(vorher->'mh') a full join jsonb_each_text(nachher->'mh') b on b.key = a.key where a.value is distinct from b.value;
  end if;
  bericht := jsonb_build_object(
    'schon_umgestellt_vorher', schon, 'umgestellt_nachher', position('TEMPO-S1' in def_nachher) > 0, 'md5_funktionstext_vorher', md5(def_vorher),
    'paare_kind_einheit', (select count(*) from jsonb_object_keys(vorher->'h')), 'abweichungen_etappen_stand', jsonb_array_length(abw), 'erste_abweichungen', abw -> 0,
    'merkheft', nachher->>'merkheft', 'merkheft_kinder', (select count(*) from jsonb_object_keys(coalesce(nachher->'mh', '{}'))), 'abweichungen_merkheft', abw_mh,
    'ms_vorher', jsonb_build_object('etappen_stand_alle', vorher->'ms_etappen_stand_alle', 'merkheft_summe', vorher->'ms_merkheft_summe', 'merkheft_je_kind', vorher->'ms_merkheft_je_kind'),
    'ms_nachher', jsonb_build_object('etappen_stand_alle', nachher->'ms_etappen_stand_alle', 'merkheft_summe', nachher->'ms_merkheft_summe', 'merkheft_je_kind', nachher->'ms_merkheft_je_kind'),
    'indizes_vorher', idx_vorher, 'indizes_nachher', idx_nachher,
    'hinweis', 'Laufzeit nachher kann zu hoch sein, wenn ein neuer Index indcheckxmin = true hat (in dieser Transaktion noch nicht nutzbar) – dann tempo_s1_messen.sql danach');
  if jsonb_array_length(abw) > 0 or coalesce(jsonb_array_length(abw_mh), 0) > 0 then
    raise exception 'TEMPO-S1 ABBRUCH, alles zurückgerollt: Ergebnis weicht ab (% Paare, Merkheft %): %', jsonb_array_length(abw), abw_mh, bericht::text;
  end if;
""" + ende + "\nend $p$;\n"
    return kopf + HILFEN + rumpf


def messen():
    return """-- TEMPO-S1 Messung (erzeugt von tools/tests/tempo_einspielen.py). Nach dem Einspielen in einer NEUEN Transaktion ausführen. Ändert nichts:
-- legt nur Hilfen in pg_temp an und endet immer mit „MESSUNG (nichts geändert): …“ (Fehler = alles zurück).
select set_config('statement_timeout', '300s', true);
""" + HILFEN + r"""
do $p$
declare m text := pg_temp.tempo_merkheft_anlegen(); x jsonb;
begin
  x := pg_temp.tempo_lauf(m);
  raise exception 'MESSUNG (nichts geändert): %', jsonb_build_object('umgestellt', position('TEMPO-S1' in (select p.prosrc from pg_proc p where p.oid = 'schule.etappen_stand(bigint, bigint)'::regprocedure)) > 0,
    'merkheft', x->>'merkheft', 'ms_etappen_stand_alle', x->'ms_etappen_stand_alle', 'ms_merkheft_summe', x->'ms_merkheft_summe', 'ms_merkheft_je_kind', x->'ms_merkheft_je_kind',
    'indizes', pg_temp.tempo_indizes())::text;
end $p$;
"""


def pakete():
    out = [('tempo_s1_probe.sql', paket(True)), ('tempo_s1_einspielen.sql', paket(False)), ('tempo_s1_messen.sql', messen())]
    for name, text in out:
        assert len(text.encode('utf-8')) < 1_500_000, name
        assert not re.search(r'^\s*\\', text, re.M), f'{name}: psql-Meta'
        assert not re.search(r'^\s*(begin|commit|rollback|start transaction)\s*;', text, re.M | re.I), f'{name}: eigenes BEGIN/COMMIT'
        assert '$rbpaket$' not in text, name
    return out


def main():
    if '--alt-sql' in sys.argv:
        sys.stdout.write(alter_sql()); return
    out = pakete()
    if '--pruefen' in sys.argv:
        alt = [n for n, t in out if not (AUS / n).exists() or (AUS / n).read_text(encoding='utf-8') != t]
        if alt: print('nicht auf dem Stand:', ', '.join(alt), file=sys.stderr); sys.exit(1)
        print('OK'); return
    print('| Datei | Bytes | md5 |\n|---|---|---|')
    for n, t in out:
        (AUS / n).write_text(t, encoding='utf-8')
        print(f'| `tools/tests/aus/{n}` | {len(t.encode("utf-8")):,} | `{hashlib.md5(t.encode("utf-8")).hexdigest()}` |'.replace(',', ' '))


if __name__ == '__main__':
    main()
