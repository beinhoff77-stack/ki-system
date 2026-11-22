-- FP-S 4 (22.11.): Sperrreihenfolge Mischkarte (inhalte/AUFTRAEGE.md „Stand 22.11., 15:00 Berlin – Rückläufer ChatGPT 932“, An bau-lehrer, Sollte 1).
-- Nach FP-S 3 einspielen (Reihenfolge: WD-S 2, WD-S 3, WD-4b, WD-S 4, FP-S, FP-S 2, FP-S 3, FP-S 4), in einer Transaktion.
-- Eine Regel für alle Wege: erst die Etappe (schule.karte_stand), dann die Ausgabe (schule.misch_ausgabe).
--   Befund vorher – zwei Stellen fassen die Ausgabe an, ohne die Etappe vorher zu sperren:
--   a) Trigger versuch_misch_verfall (normale Antwort auf eine ausgegebene Aufgabe): Im normalen Ablauf sperrt versuch_karte → karte_buchen die Etappe
--      schon vorher (Trigger in Namensfolge: versuch_karte vor versuch_misch_verfall). Ohne Buchung (1. Anlauf falsch, Wertung offen) sperrt er nur die
--      Ausgabe und wartet danach auf nichts mehr – kein Zyklus, aber keine einheitliche Regel.
--   b) misch_buchen: löst erst die Ausgabe ein und schreibt dann die Karte. Über uebung_pruefen_wd ist die Etappe schon gesperrt (FP-S 3). Bucht aber
--      offene_entscheiden einen früheren, offenen Mischkarten-Versuch aus einer Antwort ohne Misch-Wunsch, hält diese Transaktion die Ausgabe und wartet
--      auf die Karte, während eine gleichzeitige Mischkarten-Antwort die Karte hält und auf die Ausgabe wartet → Zyklus (Deadlock) möglich.
--   Jetzt: beide sperren zuerst die Etappe. Sperren, die die Transaktion schon hält, kosten nichts. mischkarten (Ausgeben/Verfallen) sperrt keine Karte
--   und wartet nach der Ausgabe auf nichts anderes – kein Zyklus mit Karte → Ausgabe.
-- Kein DROP, kein DELETE. Bestand unverändert (am Ende geprüft). Wiederholt ausführbar.

create temp table if not exists fp4_vorher (t text, s text) on commit drop;
truncate fp4_vorher; -- nur die Hilfstabelle dieser Sitzung
insert into fp4_vorher
  select 'karte', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.karte_stand x
  union all select 'sterne', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x
  union all select 'misch', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.misch_ausgabe x;

create or replace function pg_temp.fp4_ersetzen(p_fn text, p_merkmal text, p_alt text[], p_neu text[])
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

-- a) normale Antwort: Ausgabe verfallen lassen – vorher die Etappe sperren (nur wenn es eine offene Ausgabe gibt)
create or replace function schule.versuch_misch_verfall()
 returns trigger language plpgsql set search_path to ''
as $function$
begin
  if not coalesce(new.misch, false)
     and exists (select 1 from schule.misch_ausgabe m where m.lernender_id = new.lernender_id and m.aufgabe_id = new.aufgabe_id
                   and m.eingeloest_am is null and m.verfallen_am is null) then
    -- FP-S 4: Sperrfolge wie im Mischpfad – erst die Etappe, dann die Ausgabe
    perform 1 from schule.karte_stand k join schule.aufgabe a on a.id = new.aufgabe_id
     where k.lernender_id = new.lernender_id and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe for update of k;
    update schule.misch_ausgabe set verfallen_am = now()
     where lernender_id = new.lernender_id and aufgabe_id = new.aufgabe_id and eingeloest_am is null and verfallen_am is null;
  end if;
  return new;
end $function$;

-- b) misch_buchen: erst die Etappe sperren, dann einlösen
select pg_temp.fp4_ersetzen('schule.misch_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)', 'FP-S 4',
  array[$a$  if a.id is null or a.pool <> 'uebung' then return; end if;
  -- I-3/H10$a$],
  array[$a$  if a.id is null or a.pool <> 'uebung' then return; end if;
  -- FP-S 4: Sperrfolge erst Etappe, dann Ausgabe (auch wenn offene_entscheiden einen früheren Mischkarten-Versuch bucht)
  perform 1 from schule.karte_stand k where k.lernender_id = p_l and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe for update;
  -- I-3/H10$a$]);

do $mig$
declare v_t text;
begin
  select string_agg(v.t, ', ') into v_t from fp4_vorher v
   where v.s <> (select case v.t
       when 'karte' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.karte_stand x)
       when 'sterne' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x)
       when 'misch' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.misch_ausgabe x) end);
  if v_t is not null then raise exception 'FP-S 4: Bestand verändert (%)', v_t; end if;
  raise notice 'FP-S 4: Karten, Sterne, Mischkarten unverändert';
end $mig$;
