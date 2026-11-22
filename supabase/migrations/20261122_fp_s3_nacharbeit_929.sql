-- FP-S 3 (22.11.): Nacharbeit aus ChatGPT 929 (inhalte/AUFTRAEGE.md „Nachtrag FP-S 3 – Rückläufer ChatGPT 929“). Nach 20261122_fp_s2_nacharbeit_924.sql
-- einspielen (Reihenfolge: WD-S 2, WD-S 3, WD-4b, WD-S 4, FP-S, FP-S 2, FP-S 3), in einer Transaktion. Gelieferte Migrationen bleiben unverändert.
-- Mischkarte atomar einlösen:
--   1. uebung_pruefen_wd sperrt vor der Prüfung die Etappe (karte_stand, dieselbe Sperre wie karte_buchen) und die offene Ausgabe (misch_ausgabe)
--      und prüft erst danach. Eine zweite Antwort auf dieselbe Karte (andere client_id) wartet und sieht die Ausgabe eingelöst; eine Antwort auf eine
--      andere Aufgabe derselben Etappe ist entweder vorher fertig (dann ungültig) oder wartet bis nach dem Einlösen.
--   2. misch_buchen meldet den tatsächlichen Ausgang (Einstellung schule.misch_ausgang = Aufgabe:t/f). Im Rückfall (keine freie Ausgabe oder Etappe
--      nicht gelandet): normale Buchung OHNE Wiederholungswertung (schule.kein_wdh), versuch.misch = false (versuch_buchen), Sterne wie eine normale
--      Übung (sterne_aus_versuch), Antwort misch.gueltig = false (uebung_pruefen_wd).
-- Kein DROP einer Tabelle/Spalte, kein DELETE. Bestand: Karten, Lernstände, Sterne unverändert (am Ende geprüft). Wiederholt ausführbar.

create temp table if not exists fp3_vorher (t text, s text) on commit drop;
truncate fp3_vorher; -- nur die Hilfstabelle dieser Sitzung
insert into fp3_vorher
  select 'karte', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.karte_stand x
  union all select 'lernziel', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernziel_stand x
  union all select 'sterne', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x
  union all select 'misch', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.misch_ausgabe x;

create or replace function pg_temp.fp3_ersetzen(p_fn text, p_merkmal text, p_alt text[], p_neu text[])
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

-- 2a. misch_buchen: tatsächlichen Ausgang melden; Rückfall ohne Wiederholungswertung
select pg_temp.fp3_ersetzen('schule.misch_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)', 'misch_ausgang',
  array[$a$declare a schule.aufgabe; v_mid bigint;$a$,
        $a$  if v_mid is null or not exists (select 1 from schule.karte_stand k where k.lernender_id = p_l and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe and k.sitzt) then
    perform schule.karte_buchen(p_l, p_aufgabe, p_richtig, p_hilfe, p_zeit); return;
  end if;$a$],
  array[$a$declare a schule.aufgabe; v_mid bigint; v_kw text;$a$,
        $a$  if v_mid is null or not exists (select 1 from schule.karte_stand k where k.lernender_id = p_l and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe and k.sitzt) then
    -- FP-S 3: Rückfall – tatsächlich keine Mischkarte: melden, normal buchen, aber nicht als Wiederholung werten
    perform set_config('schule.misch_ausgang', p_aufgabe || ':f', true);
    v_kw := current_setting('schule.kein_wdh', true);
    perform set_config('schule.kein_wdh', '1', true);
    perform schule.karte_buchen(p_l, p_aufgabe, p_richtig, p_hilfe, p_zeit);
    perform set_config('schule.kein_wdh', coalesce(v_kw, ''), true);
    return;
  end if;
  perform set_config('schule.misch_ausgang', p_aufgabe || ':t', true); -- FP-S 3: eingelöst und als Mischkarte gebucht$a$]);

-- 2b. versuch_buchen: Versuch trägt den tatsächlichen Ausgang
select pg_temp.fp3_ersetzen('schule.versuch_buchen(schule.versuch)', 'misch_ausgang',
  array[$a$  if coalesce(v.misch, false) then perform schule.misch_buchen(v.lernender_id, v.aufgabe_id, v.richtig, v.hilfe, now());$a$],
  array[$a$  if coalesce(v.misch, false) then perform schule.misch_buchen(v.lernender_id, v.aufgabe_id, v.richtig, v.hilfe, now());
    if current_setting('schule.misch_ausgang', true) = v.aufgabe_id || ':f' then update schule.versuch set misch = false where id = v.id; end if; -- FP-S 3$a$]);

-- 2c. sterne_aus_versuch: im Rückfall Sterne wie eine normale Übung (nicht die Mischkarten-Regel)
select pg_temp.fp3_ersetzen('schule.sterne_aus_versuch()', 'misch_ausgang',
  array[$a$       or (coalesce(new.misch, false) and (coalesce(new.hilfe, 0) > 0 or coalesce(new.anlauf, 1) = 2)) then$a$],
  array[$a$       or (coalesce(new.misch, false) and coalesce(current_setting('schule.misch_ausgang', true), '') <> new.aufgabe_id || ':f' -- FP-S 3: Rückfall
           and (coalesce(new.hilfe, 0) > 0 or coalesce(new.anlauf, 1) = 2)) then$a$]);

-- 1. Antwort der Übung (wie FP-S 2) mit Gültigkeit unter Sperre und tatsächlichem Ausgang
create or replace function schule.uebung_pruefen_wd(p_l bigint, p_daten jsonb)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_r jsonb; v_w jsonb; v_lb jsonb; v_a schule.aufgabe; v_will boolean := coalesce((p_daten->>'misch')::boolean, false); v_gueltig boolean := false;
  v_gebucht bigint;
begin
  perform set_config('schule.misch_ausgang', '', true);
  if v_will then
    select * into v_a from schule.aufgabe where id = nullif(p_daten->>'aufgabe_id', '')::bigint;
    if v_a.id is not null then
      -- FP-S 3: Gültigkeit und Einlösen unter einer Sperre. Erst die Etappe (dieselbe Sperre wie jede Antwort auf diese Etappe in karte_buchen),
      -- dann die offene Ausgabe (höchstens eine je Kind und Aufgabe). Erst danach prüfen – mit dem Stand nach der Sperre.
      perform 1 from schule.karte_stand k where k.lernender_id = p_l and k.einheit_id = v_a.einheit_id and k.lernziel = v_a.variante_gruppe for update;
      perform 1 from schule.misch_ausgabe m where m.lernender_id = p_l and m.aufgabe_id = v_a.id and m.eingeloest_am is null for update;
      perform set_config('schule.misch_entscheid', '', true);
      v_gueltig := schule.misch_gueltig(p_l, v_a, p_daten);
    end if;
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
  -- FP-S 3: tatsächlicher Ausgang – gültig nur, wenn misch_buchen die Ausgabe wirklich eingelöst und als Mischkarte gebucht hat
  if v_gueltig and coalesce(current_setting('schule.misch_ausgang', true), '') <> v_a.id || ':t' then v_gueltig := false; end if;
  perform set_config('schule.misch_ausgang', '', true);
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

-- Bestand unverändert?
do $mig$
declare v_t text;
begin
  select string_agg(v.t, ', ') into v_t from fp3_vorher v
   where v.s <> (select case v.t
       when 'karte' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.karte_stand x)
       when 'lernziel' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernziel_stand x)
       when 'sterne' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x)
       when 'misch' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.misch_ausgabe x) end);
  if v_t is not null then raise exception 'FP-S 3: Bestand verändert (%)', v_t; end if;
  raise notice 'FP-S 3: Karten, Lernstände, Sterne, Mischkarten unverändert';
end $mig$;
