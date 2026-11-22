-- FP-S 2 (22.11.): Nacharbeit aus ChatGPT 924 (inhalte/AUFTRAEGE.md „Nachtrag FP-S 2 – Rückläufer ChatGPT 924“). Nach 20261122_fp_s_faire_punkte.sql einspielen
-- (Reihenfolge: WD-S 2, WD-S 3, WD-4b, WD-S 4, FP-S, FP-S 2), in einer Transaktion. Gelieferte Migrationen bleiben unverändert.
--   1. `sterne` (und `misch.sterne`) in der Antwort zählt nur die in diesem Aufruf eingefügten Buchungen: ein Trigger nach jeder neuen Zeile in
--      schule.sterne addiert die Menge auf einen aufruf-lokalen Zähler (Einstellung schule.aufruf_sterne, nur innerhalb der Transaktion dieses Aufrufs).
--      Gleichzeitige Antworten desselben Kindes oder eine gleichzeitige Nachbuchung melden so keine fremden Sterne mehr mit.
--   2. Misch-Gültigkeit einmal entscheiden: uebung_pruefen_wd prüft vor dem Speichern und reicht das Ergebnis durch; misch_gueltig übernimmt es für
--      genau diese Aufgabe (Einstellung schule.misch_entscheid), uebung_pruefen_intern wertet und antwortet damit gleich.
--   3. Nachbuchungs-Hinweis: schule.landung_nachbuchung.gesehen_am; neue Aktion api.schule_landung_nachbuchung_gesehen {lernender_id} (Zugriffsprüfung),
--      schule_konto liefert landung_nachbuchung {etappen, sterne, am, gesehen_am}.
-- Kein DROP einer Tabelle/Spalte, kein DELETE. Bestand: Karten, Lernstände, Sterne unverändert (am Ende geprüft). Wiederholt ausführbar.

create temp table if not exists fp2_vorher (t text, s text) on commit drop;
truncate fp2_vorher; -- nur die Hilfstabelle dieser Sitzung
insert into fp2_vorher
  select 'karte', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.karte_stand x
  union all select 'lernziel', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernziel_stand x
  union all select 'sterne', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x;

-- 1. aufruf-lokaler Sterne-Zähler
create or replace function schule.sterne_aufruf_zaehlen()
 returns trigger language plpgsql set search_path to ''
as $function$
declare v text := current_setting('schule.aufruf_sterne', true);
begin
  if coalesce(v, '') <> '' then perform set_config('schule.aufruf_sterne', (v::bigint + new.menge)::text, true); end if;
  return new;
end $function$;
revoke all on function schule.sterne_aufruf_zaehlen() from public, anon, authenticated;
create or replace trigger sterne_aufruf_zaehlen after insert on schule.sterne for each row execute function schule.sterne_aufruf_zaehlen();

create or replace function pg_temp.fp2_ersetzen(p_fn text, p_merkmal text, p_alt text[], p_neu text[])
 returns void language plpgsql as $f$
declare d text := pg_get_functiondef(p_fn::regprocedure); i int;
begin
  if position(p_merkmal in d) > 0 then raise notice '% schon umgebaut', p_fn; return; end if;
  for i in 1 .. cardinality(p_alt) loop
    if (length(d) - length(replace(d, p_alt[i], ''))) / length(p_alt[i]) <> 1 then
      raise exception '%: Stelle % nicht genau einmal gefunden: %', p_fn, i, left(p_alt[i], 80); end if;
    d := replace(d, p_alt[i], p_neu[i]);
  end loop;
  execute d;
end $f$;

-- 2. misch_gueltig übernimmt die eine Entscheidung des Aufrufs (für genau diese Aufgabe), sonst wie bisher
select pg_temp.fp2_ersetzen('schule.misch_gueltig(bigint, schule.aufgabe, jsonb)', 'misch_entscheid',
  array[$a$  select coalesce(coalesce((p->>'misch')::boolean, false)$a$,
        $a$false); -- Ausgabe aus 0.81.1$a$],
  array[$a$  select case when coalesce(current_setting('schule.misch_entscheid', true), '') like a.id || ':%'   -- FP-S 2: einmal entschieden
              then coalesce((p->>'misch')::boolean, false) and split_part(current_setting('schule.misch_entscheid', true), ':', 2) = 't'
              else coalesce(coalesce((p->>'misch')::boolean, false)$a$,
        $a$false) end; -- Ausgabe aus 0.81.1$a$]);

-- 1./2. Antwort der Übung (wie FP-S) mit aufruf-lokalem Zähler und einmal entschiedener Misch-Gültigkeit
create or replace function schule.uebung_pruefen_wd(p_l bigint, p_daten jsonb)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_r jsonb; v_w jsonb; v_lb jsonb; v_a schule.aufgabe; v_will boolean := coalesce((p_daten->>'misch')::boolean, false); v_gueltig boolean := false;
  v_gebucht bigint;
begin
  if v_will then
    select * into v_a from schule.aufgabe where id = nullif(p_daten->>'aufgabe_id', '')::bigint;
    v_gueltig := v_a.id is not null and schule.misch_gueltig(p_l, v_a, p_daten);   -- vor dem Speichern prüfen (danach ist die Ausgabe eingelöst)
  end if;
  -- FP-S 2: einmal entschieden – misch_gueltig in uebung_pruefen_intern übernimmt dieses Ergebnis
  perform set_config('schule.misch_entscheid', case when v_will and v_a.id is not null then v_a.id || ':' || case when v_gueltig then 't' else 'f' end else '' end, true);
  perform set_config('schule.aufruf_sterne', '0', true);   -- FP-S 2: Sterne dieses Aufrufs (Trigger sterne_aufruf_zaehlen)
  perform set_config('schule.wdh_ergebnis', '', true);
  perform set_config('schule.landung_ergebnis', '', true);
  perform set_config('schule.kein_wdh', case when v_will and not v_gueltig then '1' else '' end, true);
  v_r := schule.uebung_pruefen_intern(p_l, p_daten);
  perform set_config('schule.kein_wdh', '', true);
  perform set_config('schule.misch_entscheid', '', true);
  v_gebucht := coalesce(nullif(current_setting('schule.aufruf_sterne', true), ''), '0')::bigint;   -- nur die in diesem Aufruf eingefügten Buchungen
  perform set_config('schule.aufruf_sterne', '', true);
  v_w := nullif(current_setting('schule.wdh_ergebnis', true), '')::jsonb;
  v_lb := nullif(current_setting('schule.landung_ergebnis', true), '')::jsonb;
  perform set_config('schule.wdh_ergebnis', '', true);
  perform set_config('schule.landung_ergebnis', '', true);
  if v_w is not null then
    v_r := v_r || jsonb_build_object('wiederholung', jsonb_strip_nulls(jsonb_build_object('bestanden', v_w->'bestanden', 'sterne', v_w->'sterne',
                                       'stufe_neu', v_w->'stufe_neu', 'naechste_in', v_w->'naechste_in', 'mit_hilfe', v_w->'mit_hilfe')))
               || case when v_w ? 'abgelegt' then jsonb_build_object('abgelegt', v_w->'abgelegt') else '{}'::jsonb end;
  end if;
  if v_lb is not null then
    v_r := v_r || jsonb_build_object('landung', coalesce(v_r->'landung', '{}'::jsonb) || v_lb);   -- FP: Bonus zur Landungs-Einblendung
  end if;
  if v_will and coalesce((v_r->>'format_ok')::boolean, false) and not coalesce((v_r->>'nochmal')::boolean, false) and not coalesce((v_r->>'wiederholt')::boolean, false) then
    v_r := v_r || jsonb_build_object('misch', coalesce(v_r->'misch', '{}'::jsonb) || jsonb_build_object('gueltig', v_gueltig, 'sterne', v_gebucht));
  end if;
  if coalesce((v_r->>'format_ok')::boolean, false) and not coalesce((v_r->>'wiederholt')::boolean, false) then
    v_r := v_r || jsonb_build_object('sterne', v_gebucht);                                          -- FP/FP-S 2: in diesem Aufruf tatsächlich gebucht
  end if;
  return v_r;
end $function$;

-- 3. Nachbuchungs-Hinweis „gesehen“ im Server
alter table schule.landung_nachbuchung add column if not exists gesehen_am timestamptz;

create or replace function schule.landung_nachbuchung_gesehen(p_l bigint)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v schule.landung_nachbuchung;
begin
  update schule.landung_nachbuchung set gesehen_am = coalesce(gesehen_am, now()) where lernender_id = p_l returning * into v;
  return jsonb_build_object('ok', true, 'gesehen_am', v.gesehen_am);
end $function$;
revoke all on function schule.landung_nachbuchung_gesehen(bigint) from public, anon, authenticated;

create or replace function api.schule_landung_nachbuchung_gesehen(p_schluessel text, p_daten jsonb default null)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_l bigint := (p_daten->>'lernender_id')::bigint;
begin
  perform schule.zugriff(p_schluessel, v_l);
  return schule.landung_nachbuchung_gesehen(v_l);
end $function$;
grant execute on function api.schule_landung_nachbuchung_gesehen(text, jsonb) to council_mcp;
revoke all on function api.schule_landung_nachbuchung_gesehen(text, jsonb) from public, anon, authenticated;

select pg_temp.fp2_ersetzen('api.schule_konto(text, jsonb)', 'gesehen_am',
  array[$a$'landung_nachbuchung', (select jsonb_build_object('etappen', n.etappen, 'sterne', n.sterne, 'am', n.am) from schule.landung_nachbuchung n where n.lernender_id = v_l), -- FP$a$],
  array[$a$'landung_nachbuchung', (select jsonb_build_object('etappen', n.etappen, 'sterne', n.sterne, 'am', n.am, 'gesehen_am', n.gesehen_am)
                              from schule.landung_nachbuchung n where n.lernender_id = v_l), -- FP, FP-S 2: gesehen_am$a$]);

-- Bestand unverändert?
do $mig$
declare v_t text;
begin
  select string_agg(v.t, ', ') into v_t from fp2_vorher v
   where v.s <> (select case v.t
       when 'karte' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.karte_stand x)
       when 'lernziel' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernziel_stand x)
       when 'sterne' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x) end);
  if v_t is not null then raise exception 'FP-S 2: Bestand verändert (%)', v_t; end if;
  raise notice 'FP-S 2: Karten, Lernstände, Sterne unverändert';
end $mig$;
