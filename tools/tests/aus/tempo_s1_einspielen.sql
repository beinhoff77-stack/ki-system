-- TEMPO-S1 Einspiel-Paket (erzeugt von tools/tests/tempo_einspielen.py). Ein Aufruf, eine Transaktion. Fehler = alles zurück.
-- Laufzeit: zweimal alle Kinder × Einheiten und je Kind das Merkheft (live vorher ≈ 4 s je Kind) – mit einigen zehn Sekunden rechnen.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '300s', true);
do $p$ begin
  if to_regprocedure('schule.etappen_stand(bigint, bigint)') is null or to_regclass('schule.aufgabe') is null or to_regclass('schule.versuch') is null then
    raise exception 'TEMPO-S1 ABBRUCH, Vorbedingung: schule.etappen_stand / schule.aufgabe / schule.versuch fehlt – nichts geändert';
  end if;
end $p$;
create temp table tempo_mig on commit drop as select $tempomig$-- TEMPO-S1 (Bau-Auftrag Ladezeiten, ENTWURF – nicht eingespielt): schule_merkheft schneller, Ergebnis byte-gleich.
-- Analyse: inhalte/plan/ladezeiten.md. Einspielen NUR über das Paket tools/tests/aus/tempo_s1_einspielen.sql (eine Transaktion, prüft sich selbst:
-- vergleicht vorher/nachher je Kind und Einheit per md5 und bricht bei jeder Abweichung ab); Probe: tools/tests/aus/tempo_s1_probe.sql (rollt alles zurück).
--
-- Befund (live gemessen vom Projektleiter): api.schule_merkheft ruft je Einheit schule.etappen_stand auf, 95 Einheiten ≈ 3,7 s (≈ 39 ms je Einheit).
-- etappen_stand rechnet je Etappe (Lernziel) bis zu zehn Unterabfragen über schule.aufgabe und schule.versuch:
--   gesamt, geloest, karte_ziel (zweimal: ziel und folge_ziel), karte_typen_noetig, karte_schwer_noetig, karte_anwenden_pflicht → karte_anwenden_noetig,
--   karte_bearbeitungen, karte_sicher, dazu flug_nachtest(Kind, Einheit) – das ist je Einheit gleich, wurde aber je Etappe neu gerechnet.
--   Im Repo gibt es keinen Index auf schule.aufgabe(einheit_id …) und keinen auf schule.versuch(lernender_id, aufgabe_id) (live bekannt sind nur die
--   eindeutigen Indizes, supabase/tests/nachbau_live_constraints.sql). Ohne sie ist jede dieser Unterabfragen ein Lauf über die ganze Tabelle.
--
-- WAS:
--  1. Index schule.aufgabe (einheit_id, pool, variante_gruppe) – für alle Etappen-Hilfen (alle filtern einheit_id, pool, variante_gruppe).
--  2. Index schule.versuch (lernender_id, aufgabe_id) – für geloest und karte_bearbeitungen (Versuche eines Kindes zu Aufgaben einer Einheit).
--  3. schule.etappen_stand neu (create or replace), gleiches Ergebnis:
--     - flug_nachtest(Kind, Einheit) einmal je Aufruf statt je Etappe (Unterabfrage mit offset 0, damit der Planer sie nicht je Zeile einsetzt),
--     - karte_ziel einmal je Etappe (für ziel und folge_ziel),
--     - gesamt und geloest je Einheit in EINER gruppierten Abfrage statt je Etappe,
--     - alle übrigen Hilfsfunktionen unverändert dieselben (Regeln bleiben an einer Stelle).
--     Nur wenn die eingespielte Fassung genau die aus dem Repo ist (md5 des Funktionstexts, nachgerechnet aus den Migrationen 20261114 … 20261203);
--     sonst Abbruch ohne Änderung. Schon umgestellt (Marke TEMPO-S1) → nichts tun.
-- WAS NICHT: keine Tabelle, keine Spalte, kein Trigger, keine andere Funktion; kein DROP, kein DELETE, kein UPDATE; api.schule_merkheft bleibt, wie sie ist
--   (Antwort unverändert; Vorschlag für eine schlankere Antwort nur in der Analyse). Wiederholbar: ein zweiter Lauf ändert nichts.
-- Hinweis Index im selben Lauf: Postgres nutzt einen neuen Index in der anlegenden Transaktion u. U. noch nicht (indcheckxmin); die Laufzeit „nachher“
--   in Probe/Einspiel-Paket ist dann zu hoch. Maßgeblich ist die Messung danach (tools/tests/aus/tempo_s1_messen.sql, nur lesend).

select set_config('lock_timeout', '3s', true);

create index if not exists aufgabe_einheit_pool_lz_idx on schule.aufgabe (einheit_id, pool, variante_gruppe);
create index if not exists versuch_kind_aufgabe_idx on schule.versuch (lernender_id, aufgabe_id);

do $tempo$
declare d text := (select p.prosrc from pg_proc p where p.oid = to_regprocedure('schule.etappen_stand(bigint, bigint)'));
  v_soll constant text := 'bf3152e9a378a1d4e41c98965acf738e';   -- md5 des Funktionstexts nach 20261203_ft_s_form_takt.sql (tools/tests/tempo_einspielen.py)
begin
  if d is null then raise exception 'TEMPO-S1: schule.etappen_stand(bigint, bigint) fehlt'; end if;
  if position('TEMPO-S1' in d) > 0 then raise notice 'TEMPO-S1: etappen_stand schon umgestellt'; return; end if;
  if md5(d) <> v_soll then
    raise exception 'TEMPO-S1 ABBRUCH, Vorbedingung: etappen_stand weicht vom Repo-Stand ab (md5 %, erwartet %) – nichts geändert', md5(d), v_soll;
  end if;
  execute $neu$
create or replace function schule.etappen_stand(p_lernender bigint, p_einheit bigint)
 returns jsonb language sql stable set search_path to ''
as $function$
  -- TEMPO-S1: gleiches Ergebnis wie die Fassung nach FT-S; je Einheit einmal: flug_nachtest, gesamt/geloest (gruppiert); je Etappe einmal: karte_ziel
  select coalesce(jsonb_object_agg(z.lz, jsonb_build_object('geloest', z.geloest, 'gesamt', z.gesamt,
           'serie', coalesce(k.serie, 0), 'ziel', z.ziel, 'sitzt', coalesce(k.sitzt, false), 'schwer_ok', coalesce(k.schwer_ok, false), 'anwenden_noetig', schule.karte_anwenden_pflicht(k, p_einheit, z.lz), 'anwenden_ok', coalesce(schule.karte_anwenden_ok(k), false),
           'bearbeitungen', schule.karte_bearbeitungen(p_lernender, p_einheit, z.lz), 'schwer_noetig', schule.karte_schwer_noetig(p_einheit, z.lz),
           'faellig', coalesce(schule.karte_faellig(k), false), 'wdh_stufe', coalesce(k.wdh_stufe, 0),
           'eigene_loesungen', coalesce(k.eigene_loesungen, 0), 'folge', coalesce(k.folge, 0), 'folge_ziel', least(3, z.ziel),
           'typen_anzahl', coalesce(array_length(k.typen, 1), 0), 'typen_noetig', schule.karte_typen_noetig(p_einheit, z.lz),
           'fehler_folge', coalesce(k.fehler_folge, 0), 'stufe_senkung', coalesce(k.stufe_senkung, 0), 'sicher', coalesce(schule.karte_sicher(k), false), 'misch_ok', k.misch_ok_am is not null and k.misch_ok_am >= coalesce(k.sitzt_am, k.misch_ok_am), 'flug_nachtest', fn.v,
           'fertig', schule.etappe_fertig(k, s.status), 'test_nachgewiesen', coalesce(s.status in ('nachgewiesen','korrigiert','gesichert'), false), 'wieder_offen', not coalesce(k.sitzt, false) and k.sitzt_am is not null, 'gezaehlt', coalesce((select jsonb_agg(x::bigint) from jsonb_object_keys(k.gezaehlt) x), '[]'::jsonb))), '{}'::jsonb)
  from (select y.lz, coalesce(g.gesamt, 0) gesamt, coalesce(v.geloest, 0) geloest, schule.karte_ziel(p_einheit, y.lz) ziel
          from (select e->>'lernziel' lz, o.nr
                  from schule.einheit x, jsonb_array_elements(coalesce(x.inhalt->'etappen', '[]'::jsonb)) with ordinality o(e, nr) where x.id = p_einheit) y
          left join (select a.variante_gruppe lz, count(*) gesamt from schule.aufgabe a
                      where a.einheit_id = p_einheit and a.pool = 'uebung' and a.freigegeben group by a.variante_gruppe) g on g.lz = y.lz
          left join (select a.variante_gruppe lz, count(distinct v.aufgabe_id) geloest from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                      where v.lernender_id = p_lernender and v.richtig and v.testsitzung_id is null and a.einheit_id = p_einheit and a.pool = 'uebung'
                      group by a.variante_gruppe) v on v.lz = y.lz
         order by y.nr) z
  cross join (select schule.flug_nachtest(p_lernender, p_einheit) v offset 0) fn
  left join schule.lernziel_stand s on s.lernender_id = p_lernender and s.einheit_id = p_einheit and s.lernziel = z.lz
  left join schule.karte_stand k on k.lernender_id = p_lernender and k.einheit_id = p_einheit and k.lernziel = z.lz;
$function$
$neu$;
end $tempo$;
$tempomig$::text as sql;

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
  raise notice 'TEMPO-S1 eingespielt: %', bericht::text;
end $p$;
