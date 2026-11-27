-- FT-S Einspiel-Paket (erzeugt von tools/tests/form_takt_einspielen.py --probe). Ein Aufruf, eine Transaktion. Fehler = alles zurück.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '180s', true);
create temp table ft_mig on commit drop as select m.sql, substr(m.sql, strpos(m.sql, E'do $$\ndeclare\n  f record;'), 6463) as patch, m.alt
from (select $ftmig$do $$ begin
  if to_regprocedure('schule.karte_landet(schule.karte_stand)') is null or to_regprocedure('schule.loesung_sicht(schule.aufgabe)') is null
     or to_regprocedure('schule.wd_regel(text, integer)') is null then raise exception 'FT-S: Voraussetzung fehlt (LB-3 Nachbesserung, WD-S, BD-S2)'; end if;
end $$;
alter table schule.aufgabe add column if not exists form text;
alter table schule.aufgabe add column if not exists zaehlt text;
comment on column schule.aufgabe.form is 'FT-S: neue Aufgabenform (leer = Bestand): lueckenweg|fehler_detektiv|verfahren_waehlen|zwei_wege|umkehren|bruecke|anwenden|viele_antworten';
comment on column schule.aufgabe.zaehlt is 'FT-S: zählt für Karte/„sitzt“ (leer = ja): ja|nein. nein = wird bewertet und gespeichert, ändert an der Karte nichts';
do $$
declare v_ist text; v_soll text; c record;
begin
  if to_regclass('pg_temp.ft_zwilling') is null then
    create temp table ft_zwilling (form text, zaehlt text,
      constraint aufgabe_form_check check (form is null or form in ('lueckenweg', 'fehler_detektiv', 'verfahren_waehlen', 'zwei_wege', 'umkehren', 'bruecke', 'anwenden', 'viele_antworten')),
      constraint aufgabe_zaehlt_check check (zaehlt is null or zaehlt in ('ja', 'nein'))) on commit drop;
  end if;
  for c in select conname, pg_get_constraintdef(oid) d from pg_constraint where conrelid = 'pg_temp.ft_zwilling'::regclass and contype = 'c' order by conname loop
    select pg_get_constraintdef(oid) into v_ist from pg_constraint where conname = c.conname and conrelid = 'schule.aufgabe'::regclass;
    if v_ist is null then execute format('alter table schule.aufgabe add constraint %I %s', c.conname, c.d);
    elsif v_ist <> c.d then raise exception 'FT-S: % hat eine unerwartete Fassung: %', c.conname, v_ist;
    end if;
  end loop;
end $$;
insert into schule.regel (schluessel, wert, hinweis) values ('form_jede', '3'::jsonb, 'FT-S: je Lernkarte jede n-te Bearbeitung eine Aufgabe mit neuer Form (Plätze n, 2n, …), wenn eine ungelöste da ist')
  on conflict (schluessel) do nothing;
create or replace function schule.aufgabe_zaehlt(a schule.aufgabe)
 returns boolean language sql immutable set search_path to ''
as $function$
  select a.zaehlt is distinct from 'nein';
$function$;
comment on function schule.aufgabe_zaehlt(schule.aufgabe) is 'FT-S Regel 5: ist die Aufgabe ein Rechenbeleg (zaehlt leer oder ja)';
create or replace function schule.aufgabe_anwenden(a schule.aufgabe)
 returns boolean language sql immutable set search_path to ''
as $function$
  select coalesce(a.typ in ('einkleidung', 'transfer', 'pruefung'), false);
$function$;
comment on function schule.aufgabe_anwenden(schule.aufgabe) is 'FT-S Regel 6: Art „anwenden“ (Typ g einkleidung, transfer, pruefung – Tabelle in inhalte/mathe-profi/rollend-2/verhaeltnis.md)';
create or replace function schule.karte_anwenden_noetig(p_einheit bigint, p_lz text)
 returns boolean language sql stable set search_path to ''
as $function$
  select exists (select 1 from schule.aufgabe a
   where a.einheit_id = p_einheit and a.pool = 'uebung' and a.variante_gruppe = p_lz and a.freigegeben and schule.aufgabe_zaehlt(a) and schule.aufgabe_anwenden(a));
$function$;
create or replace function schule.karte_anwenden_pflicht(k schule.karte_stand, p_einheit bigint, p_lz text)
 returns boolean language sql stable set search_path to ''
as $function$
  select k.sitzt_am is null and not coalesce(k.sitzt, false) and schule.karte_anwenden_noetig(p_einheit, p_lz);
$function$;
comment on function schule.karte_anwenden_pflicht(schule.karte_stand, bigint, text) is 'FT-S Regel 6: Sachaufgabe nötig – nur für nie gelandete Karten und nur, wenn die Lernkarte eine freigegebene, zählende Übung der Art anwenden hat';
create or replace function schule.karte_anwenden_ok(k schule.karte_stand)
 returns boolean language sql stable set search_path to ''
as $function$
  select exists (select 1 from jsonb_object_keys(coalesce(k.gezaehlt, '{}'::jsonb)) x join schule.aufgabe a on a.id = x::bigint
                  where schule.aufgabe_anwenden(a) and schule.aufgabe_zaehlt(a));
$function$;
comment on function schule.karte_anwenden_ok(schule.karte_stand) is 'FT-S Regel 6: unter den gezählten Aufgaben (gezaehlt) ist eine der Art anwenden';
create or replace function schule.karte_bearbeitungen(p_l bigint, p_e bigint, p_lz text)
 returns integer language sql stable set search_path to ''
as $function$
  select count(*)::int from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
   where v.lernender_id = p_l and a.einheit_id = p_e and a.variante_gruppe = p_lz and a.pool = 'uebung'
     and v.testsitzung_id is null and not coalesce(v.misch, false) and coalesce(v.anlauf, 1) <> 2;
$function$;
comment on function schule.karte_bearbeitungen(bigint, bigint, text) is 'FT-S Regel 2: Bearbeitungen des Kindes an der Lernkarte (ohne Test, ohne Mischkarte; 2. Anlauf derselben Aufgabe zählt nicht extra)';
revoke all on function schule.aufgabe_zaehlt(schule.aufgabe), schule.aufgabe_anwenden(schule.aufgabe), schule.karte_anwenden_noetig(bigint, text),
  schule.karte_anwenden_pflicht(schule.karte_stand, bigint, text), schule.karte_anwenden_ok(schule.karte_stand), schule.karte_bearbeitungen(bigint, bigint, text)
  from public, anon, authenticated;
do $$
declare
  f record; e jsonb; d text; d0 text; n_alt int; n_neu int; soll int; z_alt int; z_fertig int;
  zaehle constant text := 'select (length($1) - length(replace($1, $2, ''''))) / length($2)';
  plan constant jsonb := jsonb_build_array(
    jsonb_build_object('f', 'schule.aufgabe_anzeige(schule.aufgabe, boolean)', 'p', jsonb_build_array(
      jsonb_build_array($a$'typ', a.typ, 'bonus'$a$, $a$'typ', a.typ, 'form', a.form, 'zaehlt', a.zaehlt, 'bonus'$a$, 1))),
    jsonb_build_object('f', 'schule.aufgaben_einfuegen(bigint, jsonb)', 'p', jsonb_build_array(
      jsonb_build_array($a$reihenfolge, pool, typ)$a$, $a$reihenfolge, pool, typ, form, zaehlt)$a$, 1),
      jsonb_build_array($a$x->>'g' from q$a$, $a$x->>'g', x->>'form', x->>'zaehlt' from q$a$, 1))),
    jsonb_build_object('f', 'schule.karte_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)', 'p', jsonb_build_array(
      jsonb_build_array($a$if a.id is null or a.pool <> 'uebung' then return; end if;$a$, $a$if a.id is null or a.pool <> 'uebung' or not schule.aufgabe_zaehlt(a) then return; end if;$a$, 1))),
    jsonb_build_object('f', 'schule.misch_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)', 'p', jsonb_build_array(
      jsonb_build_array($a$if a.id is null or a.pool <> 'uebung' then return; end if;$a$, $a$if a.id is null or a.pool <> 'uebung' or not schule.aufgabe_zaehlt(a) then return; end if;$a$, 1))),
    jsonb_build_object('f', 'schule.expedition_buchen(bigint, bigint, boolean, smallint, smallint, timestamp with time zone)', 'p', jsonb_build_array(
      jsonb_build_array($a$coalesce(p_anlauf, 1) = 1 then$a$, $a$coalesce(p_anlauf, 1) = 1 and schule.aufgabe_zaehlt(a) then$a$, 1),
      jsonb_build_array($a$a.variante_gruppe, p_zeit); -- H8$a$, $a$a.variante_gruppe, p_zeit) where schule.aufgabe_zaehlt(a); -- H8$a$, 1))),
    jsonb_build_object('f', 'schule.karte_landet(schule.karte_stand)', 'p', jsonb_build_array(
      jsonb_build_array($a$least(3, schule.karte_ziel(k.einheit_id, k.lernziel));$a$, $a$least(3, schule.karte_ziel(k.einheit_id, k.lernziel))
     and (schule.karte_anwenden_ok(k) or not schule.karte_anwenden_pflicht(k, k.einheit_id, k.lernziel)); -- FT-S Regel 6$a$, 1))),
    jsonb_build_object('f', 'schule.karte_ziel(bigint, text)', 'p', jsonb_build_array(
      jsonb_build_array($a$where a.einheit_id = p_einheit and$a$, $a$where schule.aufgabe_zaehlt(a) and a.einheit_id = p_einheit and$a$, 1))),
    jsonb_build_object('f', 'schule.karte_typen_noetig(bigint, text)', 'p', jsonb_build_array(
      jsonb_build_array($a$where a.einheit_id = p_einheit and$a$, $a$where schule.aufgabe_zaehlt(a) and a.einheit_id = p_einheit and$a$, 1))),
    jsonb_build_object('f', 'schule.karte_schwer_noetig(bigint, text)', 'p', jsonb_build_array(
      jsonb_build_array($a$where a.einheit_id = p_einheit and$a$, $a$where schule.aufgabe_zaehlt(a) and a.einheit_id = p_einheit and$a$, 1))),
    jsonb_build_object('f', 'schule.folge_nachrechnen(bigint, bigint, text, timestamp with time zone)', 'p', jsonb_build_array(
      jsonb_build_array($a$a.variante_gruppe = p_lz and a.pool = 'uebung'$a$, $a$a.variante_gruppe = p_lz and schule.aufgabe_zaehlt(a) and a.pool = 'uebung'$a$, 1))),
    jsonb_build_object('f', 'schule.landung_zaehlen(bigint, bigint, text)', 'p', jsonb_build_array(
      jsonb_build_array($a$a.variante_gruppe = p_lz and a.pool = 'uebung'$a$, $a$a.variante_gruppe = p_lz and schule.aufgabe_zaehlt(a) and a.pool = 'uebung'$a$, 2))),
    jsonb_build_object('f', 'schule.wdh_aufgabe_waehlen(bigint, bigint, text, boolean)', 'p', jsonb_build_array(
      jsonb_build_array($a$where a.einheit_id = p_e and$a$, $a$where schule.aufgabe_zaehlt(a) and a.einheit_id = p_e and$a$, 1))),
    jsonb_build_object('f', 'schule.wdh_aufgabe_da(bigint, bigint, text)', 'p', jsonb_build_array(
      jsonb_build_array($a$where a.einheit_id = p_e and$a$, $a$where schule.aufgabe_zaehlt(a) and a.einheit_id = p_e and$a$, 1))),
    jsonb_build_object('f', 'schule.wdh_aufgabe_da(bigint, text)', 'p', jsonb_build_array(
      jsonb_build_array($a$where a.einheit_id = p_e and$a$, $a$where schule.aufgabe_zaehlt(a) and a.einheit_id = p_e and$a$, 1))),
    jsonb_build_object('f', 'schule.uebung_pruefen_intern(bigint, jsonb)', 'p', jsonb_build_array(
      jsonb_build_array($a$'schwer_ok', k.schwer_ok, 'schwer_noetig'$a$, $a$'schwer_ok', k.schwer_ok, 'anwenden_noetig', schule.karte_anwenden_pflicht(k, k.einheit_id, k.lernziel), 'anwenden_ok', schule.karte_anwenden_ok(k),
                'bearbeitungen', schule.karte_bearbeitungen(k.lernender_id, k.einheit_id, k.lernziel), 'schwer_noetig'$a$, 1))),
    jsonb_build_object('f', 'schule.etappen_stand(bigint, bigint)', 'p', jsonb_build_array(
      jsonb_build_array($a$'schwer_ok', coalesce(k.schwer_ok, false), 'schwer_noetig'$a$, $a$'schwer_ok', coalesce(k.schwer_ok, false), 'anwenden_noetig', schule.karte_anwenden_pflicht(k, p_einheit, z.lz), 'anwenden_ok', coalesce(schule.karte_anwenden_ok(k), false),
           'bearbeitungen', schule.karte_bearbeitungen(p_lernender, p_einheit, z.lz), 'schwer_noetig'$a$, 1))),
    jsonb_build_object('f', 'schule.einheit_lesen_intern(bigint, bigint)', 'p', jsonb_build_array(
      jsonb_build_array($a$'heute_tag', schule.heute_tag(p_lernender), 'heute_bis'$a$, $a$'heute_tag', schule.heute_tag(p_lernender), 'form_jede', schule.wd_regel('form_jede', 3), 'heute_bis'$a$, 1))));
begin
  for f in select x->>'f' as name, x->'p' as p from jsonb_array_elements(plan) x loop
    if to_regprocedure(f.name) is null then raise exception 'FT-S: Funktion % fehlt', f.name; end if;
    d0 := pg_get_functiondef(to_regprocedure(f.name)); d := d0; z_alt := 0; z_fertig := 0;
    for e in select * from jsonb_array_elements(f.p) loop
      soll := (e->>2)::int;
      execute zaehle into n_alt using d, e->>0;
      execute zaehle into n_neu using d, e->>1;
      if n_alt = soll and n_neu = 0 then d := replace(d, e->>0, e->>1); z_alt := z_alt + 1;
      elsif n_alt = 0 and n_neu = soll then z_fertig := z_fertig + 1;
      else raise exception 'FT-S: % ist weder im alten noch im fertigen Zustand (Stelle „%…“: alt %, neu %, erwartet %)', f.name, left(e->>0, 40), n_alt, n_neu, soll;
      end if;
    end loop;
    if z_alt > 0 and z_fertig > 0 then raise exception 'FT-S: % ist halb umgestellt (% Stellen alt, % fertig)', f.name, z_alt, z_fertig; end if;
    if d is distinct from d0 then execute d; end if;
  end loop;
end $$;
$ftmig$::text as sql, $ftalt$do $x$
declare k bigint := (select id from schule.lernender where ist_test order by id limit 1); a schule.aufgabe; o jsonb := '{}';
begin
  select * into a from schule.aufgabe where id = (select min(id) from schule.aufgabe where pool = 'uebung' and antworttyp = 'zahl' and freigegeben);
  if k is null or a.id is null then raise exception 'FT-S: Testkind oder Vergleichsaufgabe fehlt'; end if;
  begin
    perform schule.offene_entscheiden(k);
    o := o || jsonb_build_object('start', jsonb_build_object('m', pg_temp.ft_k(k, a.einheit_id, a.variante_gruppe)));
    o := o || jsonb_build_object('falsch-1', jsonb_build_object('r', pg_temp.ft_ant(k, a.id, false, 1, 'ft-b-1'), 'm', pg_temp.ft_k(k, a.einheit_id, a.variante_gruppe)));
    o := o || jsonb_build_object('falsch-2', jsonb_build_object('r', pg_temp.ft_ant(k, a.id, false, 2, 'ft-b-2'), 'm', pg_temp.ft_k(k, a.einheit_id, a.variante_gruppe)));
    raise exception using errcode = 'FT999', message = 'zurueck';
  exception when sqlstate 'FT999' then null;
  end;
  begin
    perform schule.offene_entscheiden(k);
    o := o || jsonb_build_object('richtig', jsonb_build_object('r', pg_temp.ft_ant(k, a.id, true, 1, 'ft-b-3'), 'm', pg_temp.ft_k(k, a.einheit_id, a.variante_gruppe)));
    raise exception using errcode = 'FT999', message = 'zurueck';
  exception when sqlstate 'FT999' then null;
  end;
  insert into ft_aus values ('PHASE', o);
end $x$;$ftalt$::text as alt) m;
do $chk$ begin if (select strpos(patch, 'plan constant jsonb') = 0 or right(patch, 7) <> 'end $$;' or length(patch) <> 6463 from ft_mig) then raise exception 'FT-S: Patch-Block nicht gefunden'; end if; end $chk$;
-- Hilfen nur für diese Sitzung (pg_temp)
create function pg_temp.ft_k(p_k bigint, p_e bigint, p_lz text) returns text language sql stable as $f$
  select coalesce((select md5(x::text) from schule.karte_stand x where x.lernender_id = p_k and x.einheit_id = p_e and x.lernziel = p_lz), 'keine') $f$;
create function pg_temp.ft_ant(p_k bigint, p_id bigint, p_ok boolean, p_anlauf int, p_cid text) returns jsonb language plpgsql as $f$
declare a schule.aufgabe;
begin
  select * into a from schule.aufgabe where id = p_id;
  return schule.uebung_pruefen_wd(p_k, jsonb_build_object('aufgabe_id', p_id, 'client_id', p_cid, 'antwort',
           case when p_ok then jsonb_build_object('wert', replace(a.loesung->>'wert', '.', ',')) else '{"wert":"987654"}'::jsonb end)
         || case when p_anlauf is null then '{}'::jsonb else jsonb_build_object('anlauf', p_anlauf) end);
end $f$;
create function pg_temp.ft_kopie(p_basis bigint, p_lz text, p_typ text, p_stufe int, p_form text, p_zaehlt text, p_nr int) returns bigint language plpgsql as $f$
declare v bigint;
begin
  execute 'insert into schule.aufgabe (einheit_id, thema_id, teilfaehigkeit, art, stufe, variante_gruppe, antworttyp, frage, antworten, loesung, tipp, loesungsweg,
      punkte_max, reihenfolge, pool, freigegeben, typ, form, zaehlt)
    select einheit_id, thema_id, teilfaehigkeit, art, coalesce($2, stufe), coalesce($3, variante_gruppe), antworttyp, frage || jsonb_build_object(''ft_probe'', $4), antworten,
      loesung, tipp, loesungsweg, punkte_max, 90000 + $4, pool, true, coalesce($5, typ), $6, $7 from schule.aufgabe where id = $1 returning id'
    into v using p_basis, p_stufe, p_lz, p_nr, p_typ, p_form, p_zaehlt;
  return v;
end $f$;
create temp table ft_aus (phase text, o jsonb) on commit drop;
create temp table ft_bericht on commit drop as select null::jsonb as b where false;
create temp table ft_kvor on commit drop as select (select md5(coalesce(string_agg(concat_ws('|', x.lernender_id, x.einheit_id, x.lernziel, x.sitzt, x.sitzt_am, x.eigene_loesungen, x.gezaehlt, x.folge), '#' order by x.lernender_id, x.einheit_id, x.lernziel), '')) from schule.karte_stand x) as spalten,
       (select md5(coalesce(string_agg(x::text, '#' order by x.lernender_id, x.einheit_id, x.lernziel), '')) from schule.karte_stand x) as ganz,
       (select count(*) from schule.karte_stand x where x.sitzt), (select count(*) from schule.aufgabe) as sitzend;
create temp table ft_vor on commit drop as
  select f, pg_get_functiondef(to_regprocedure(f)) as def, (select proacl::text from pg_proc where oid = to_regprocedure(f)) as acl from unnest(array['schule.aufgabe_anzeige(schule.aufgabe, boolean)', 'schule.aufgaben_einfuegen(bigint, jsonb)', 'schule.karte_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)', 'schule.misch_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)', 'schule.expedition_buchen(bigint, bigint, boolean, smallint, smallint, timestamp with time zone)', 'schule.karte_landet(schule.karte_stand)', 'schule.karte_ziel(bigint, text)', 'schule.karte_typen_noetig(bigint, text)', 'schule.karte_schwer_noetig(bigint, text)', 'schule.folge_nachrechnen(bigint, bigint, text, timestamp with time zone)', 'schule.landung_zaehlen(bigint, bigint, text)', 'schule.wdh_aufgabe_waehlen(bigint, bigint, text, boolean)', 'schule.wdh_aufgabe_da(bigint, bigint, text)', 'schule.wdh_aufgabe_da(bigint, text)', 'schule.uebung_pruefen_intern(bigint, jsonb)', 'schule.etappen_stand(bigint, bigint)', 'schule.einheit_lesen_intern(bigint, bigint)', 'schule.aufgabe_zaehlt(schule.aufgabe)', 'schule.aufgabe_anwenden(schule.aufgabe)', 'schule.karte_anwenden_noetig(bigint, text)', 'schule.karte_anwenden_pflicht(schule.karte_stand, bigint, text)', 'schule.karte_anwenden_ok(schule.karte_stand)', 'schule.karte_bearbeitungen(bigint, bigint, text)']::text[]) f;
do $$ begin execute replace((select alt from ft_mig), 'PHASE', 'vor'); end $$;
do $$ begin execute (select sql from ft_mig); end $$;
create temp table ft_nach1 on commit drop as
  select f, pg_get_functiondef(to_regprocedure(f)) as def, (select proacl::text from pg_proc where oid = to_regprocedure(f)) as acl from unnest(array['schule.aufgabe_anzeige(schule.aufgabe, boolean)', 'schule.aufgaben_einfuegen(bigint, jsonb)', 'schule.karte_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)', 'schule.misch_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)', 'schule.expedition_buchen(bigint, bigint, boolean, smallint, smallint, timestamp with time zone)', 'schule.karte_landet(schule.karte_stand)', 'schule.karte_ziel(bigint, text)', 'schule.karte_typen_noetig(bigint, text)', 'schule.karte_schwer_noetig(bigint, text)', 'schule.folge_nachrechnen(bigint, bigint, text, timestamp with time zone)', 'schule.landung_zaehlen(bigint, bigint, text)', 'schule.wdh_aufgabe_waehlen(bigint, bigint, text, boolean)', 'schule.wdh_aufgabe_da(bigint, bigint, text)', 'schule.wdh_aufgabe_da(bigint, text)', 'schule.uebung_pruefen_intern(bigint, jsonb)', 'schule.etappen_stand(bigint, bigint)', 'schule.einheit_lesen_intern(bigint, bigint)', 'schule.aufgabe_zaehlt(schule.aufgabe)', 'schule.aufgabe_anwenden(schule.aufgabe)', 'schule.karte_anwenden_noetig(bigint, text)', 'schule.karte_anwenden_pflicht(schule.karte_stand, bigint, text)', 'schule.karte_anwenden_ok(schule.karte_stand)', 'schule.karte_bearbeitungen(bigint, bigint, text)']::text[]) f;
do $$ begin execute (select sql from ft_mig); end $$;
do $$ begin execute replace((select alt from ft_mig), 'PHASE', 'nach'); end $$;

-- Prüfblock
do $pruef$
declare
  fehler text[] := '{}'; f record; n int; v_txt text; v_c text; i int; v_id bigint; v_id2 bigint; v_ids bigint[] := '{}'; v_r jsonb; v_m text; ks schule.karte_stand;
  k constant bigint := (select id from schule.lernender where ist_test order by id limit 1);
  v_basis constant bigint := (select min(id) from schule.aufgabe where pool = 'uebung' and antworttyp = 'zahl' and freigegeben);
  a schule.aufgabe; v_e bigint; v_lz text; v_status text; v_patch text := (select patch from ft_mig);
  o jsonb := '{}'; p jsonb := '{}'; v_vor jsonb; v_nach jsonb;
begin
  select * into a from schule.aufgabe where id = v_basis; v_e := a.einheit_id; v_lz := a.variante_gruppe;
  select status into v_status from schule.einheit where id = v_e;

  -- 1. zweiter Lauf, Rechte, Spalten, Prüfbedingungen, Regel
  for f in select v.f, v.def as vor, v.acl as acl_vor, n1.def as nach1, n1.acl as acl1, pg_get_functiondef(to_regprocedure(v.f)) as jetzt,
                  (select proacl::text from pg_proc where oid = to_regprocedure(v.f)) as acl_jetzt, v.f = any(array['schule.aufgabe_zaehlt(schule.aufgabe)', 'schule.aufgabe_anwenden(schule.aufgabe)', 'schule.karte_anwenden_noetig(bigint, text)', 'schule.karte_anwenden_pflicht(schule.karte_stand, bigint, text)', 'schule.karte_anwenden_ok(schule.karte_stand)', 'schule.karte_bearbeitungen(bigint, bigint, text)']::text[]) as neu from ft_vor v join ft_nach1 n1 using (f) loop
    if f.nach1 is null then fehler := fehler || (f.f || ': fehlt nach der Migration')::text;
    elsif not f.neu and f.vor = f.nach1 then fehler := fehler || (f.f || ': erster Lauf hat nichts geändert')::text; end if;
    if f.nach1 is distinct from f.jetzt then fehler := fehler || (f.f || ': zweiter Lauf hat die Definition geändert')::text; end if;
    if (not f.neu and f.acl_vor is distinct from f.acl_jetzt) or f.acl1 is distinct from f.acl_jetzt then fehler := fehler || (f.f || ': Rechte geändert')::text; end if;
    if f.neu and (has_function_privilege('anon', f.f, 'execute') or has_function_privilege('authenticated', f.f, 'execute')) then fehler := fehler || (f.f || ': für App-Rollen aufrufbar')::text; end if;
  end loop;
  if (select count(*) from pg_attribute where attrelid = 'schule.aufgabe'::regclass and attname in ('form', 'zaehlt') and not attisdropped and not attnotnull and not atthasdef) <> 2
    then fehler := fehler || ('Spalten form/zaehlt fehlen oder sind nicht nullable ohne Vorgabe')::text; end if;
  if (select count(*) from pg_constraint where conrelid = 'schule.aufgabe'::regclass and conname in ('aufgabe_form_check', 'aufgabe_zaehlt_check') and convalidated) <> 2
    then fehler := fehler || ('Prüfbedingungen fehlen')::text; end if;
  if exists (select 1 from schule.aufgabe x where x.form is not null or x.zaehlt is not null) then fehler := fehler || ('Bestand hat form/zaehlt')::text; end if;
  if not exists (select 1 from schule.regel where schluessel = 'form_jede') then fehler := fehler || ('Regel form_jede fehlt')::text; end if;
  if (select row(t.*)::text from ft_kvor t) is distinct from (select row((select md5(coalesce(string_agg(concat_ws('|', x.lernender_id, x.einheit_id, x.lernziel, x.sitzt, x.sitzt_am, x.eigene_loesungen, x.gezaehlt, x.folge), '#' order by x.lernender_id, x.einheit_id, x.lernziel), '')) from schule.karte_stand x),
       (select md5(coalesce(string_agg(x::text, '#' order by x.lernender_id, x.einheit_id, x.lernziel), '')) from schule.karte_stand x),
       (select count(*) from schule.karte_stand x where x.sitzt), (select count(*) from schule.aufgabe))::text) then fehler := fehler || ('Karten oder Aufgabenzahl nach der Migration anders als vorher')::text; end if;

  -- 2. Mischstand und Gegenprobe
  for i in 1 .. 2 loop
    begin
      v_txt := case i when 1 then pg_get_functiondef('schule.expedition_buchen(bigint, bigint, boolean, smallint, smallint, timestamp with time zone)'::regprocedure) else pg_get_functiondef('schule.karte_ziel(bigint, text)'::regprocedure) end;
      v_c := case i when 1 then replace(v_txt, 'p_zeit) where schule.aufgabe_zaehlt(a); -- H8', 'p_zeit); -- H8')
                    else replace(v_txt, 'where schule.aufgabe_zaehlt(a) and a.einheit_id = p_einheit and', 'where a.einheit_id in (p_einheit) and') end;
      if v_c = v_txt then raise exception using errcode = 'FT998', message = 'Probe-Stelle nicht gefunden'; end if;
      execute v_c;
      execute v_patch;
      raise exception using errcode = 'FT999', message = 'kein Abbruch';
    exception
      when sqlstate 'FT999' then fehler := fehler || ('Mischstand ' || i || ' wurde nicht abgewiesen')::text;
      when others then
        if sqlerrm like (case i when 1 then 'FT-S:%halb umgestellt%' else 'FT-S:%weder im alten noch im fertigen%' end) then p := p || jsonb_build_object('mischstand_' || i, 'abgewiesen');
        else fehler := fehler || ('Mischstand ' || i || ' unerwartet: ' || sqlerrm)::text; end if;
    end;
  end loop;
  begin
    for f in select v.def from ft_vor v where v.def is not null and not (v.f = any(array['schule.aufgabe_zaehlt(schule.aufgabe)', 'schule.aufgabe_anwenden(schule.aufgabe)', 'schule.karte_anwenden_noetig(bigint, text)', 'schule.karte_anwenden_pflicht(schule.karte_stand, bigint, text)', 'schule.karte_anwenden_ok(schule.karte_stand)', 'schule.karte_bearbeitungen(bigint, bigint, text)']::text[])) loop execute f.def; end loop;
    execute v_patch;
    select count(*) into n from ft_nach1 n1 where pg_get_functiondef(to_regprocedure(n1.f)) is distinct from n1.def;
    raise exception using errcode = 'FT999', message = 'gegenprobe:' || n;
  exception
    when sqlstate 'FT999' then if sqlerrm = 'gegenprobe:0' then p := p || '{"gegenprobe":"ok"}'; else fehler := fehler || ('Gegenprobe: Einbau aus dem alten Stand ergibt nicht die neuen Definitionen (' || sqlerrm || ')')::text; end if;
    when others then fehler := fehler || ('Gegenprobe unerwartet: ' || sqlerrm)::text;
  end;
  if exists (select 1 from ft_nach1 n1 where pg_get_functiondef(to_regprocedure(n1.f)) is distinct from n1.def) then fehler := fehler || ('nach den Proben sind die Definitionen nicht wieder die neuen')::text; end if;

  -- 3. Bestand: dieselbe Übung antwortet wie vorher, die Karte bleibt gleich
  select t.o into v_vor from ft_aus t where t.phase = 'vor'; select t.o into v_nach from ft_aus t where t.phase = 'nach';
  if (select count(*) from jsonb_object_keys(coalesce(v_vor, '{}')) ) <> 4 or (select count(*) from jsonb_object_keys(coalesce(v_nach, '{}'))) <> 4 then fehler := fehler || ('Bestand: Vergleich unvollständig')::text;
  else
    for v_txt in select key from jsonb_object_keys(v_vor) key loop
      if v_vor->v_txt->'m' is distinct from v_nach->v_txt->'m' then fehler := fehler || ('Bestand: Karte anders nach ' || v_txt)::text; end if;
      if (v_vor->v_txt->'r') is distinct from ((v_nach->v_txt->'r') #- '{karte,anwenden_noetig}' #- '{karte,anwenden_ok}' #- '{karte,bearbeitungen}') then fehler := fehler || ('Bestand: Antwort anders bei ' || v_txt)::text; end if;
      if v_nach->v_txt->'r' ? 'karte' and not (v_nach->v_txt->'r'->'karte' ?& array['anwenden_noetig', 'anwenden_ok', 'bearbeitungen']) then fehler := fehler || ('Bestand: neue Felder fehlen in karte bei ' || v_txt)::text; end if;
    end loop;
    if not (v_nach->'falsch-1'->'r' @> '{"format_ok":true,"richtig":false,"nochmal":true}') or not (v_nach->'falsch-2'->'r' @> '{"richtig":false}') or not (v_nach->'falsch-2'->'r' ? 'loesung')
       or not (v_nach->'richtig'->'r' @> '{"format_ok":true,"richtig":true}') then fehler := fehler || ('Bestand: fachlich unerwartete Antwort')::text; end if;
  end if;

  -- 4. zaehlt = nein / form + ja / Bearbeitungen / Ausgaben (alles nur in dieser Untertransaktion)
  begin
    perform schule.offene_entscheiden(k);
    v_m := pg_temp.ft_k(k, v_e, v_lz);
    v_id := pg_temp.ft_kopie(v_basis, null, null, null, 'lueckenweg', 'nein', 1);
    o := o || jsonb_build_object('anzeige', (select jsonb_build_object('form', z->'form', 'zaehlt', z->'zaehlt') from (select schule.aufgabe_anzeige(x, true) z from schule.aufgabe x where x.id = v_id) q));
    o := o || jsonb_build_object('nein_richtig', pg_temp.ft_ant(k, v_id, true, 1, 'ft-n-1'));
    if pg_temp.ft_k(k, v_e, v_lz) is distinct from v_m then fehler := fehler || ('zaehlt = nein, richtig: bestehende Karte verändert')::text; end if;
    v_id2 := pg_temp.ft_kopie(v_basis, null, null, null, 'fehler_detektiv', 'nein', 2);
    o := o || jsonb_build_object('nein_falsch_1', pg_temp.ft_ant(k, v_id2, false, 1, 'ft-n-2'), 'nein_falsch_2', pg_temp.ft_ant(k, v_id2, false, 2, 'ft-n-3'));
    if pg_temp.ft_k(k, v_e, v_lz) is distinct from v_m then fehler := fehler || ('zaehlt = nein, endgültig falsch: bestehende Karte verändert')::text; end if;
    if (select count(*) from schule.versuch v where v.lernender_id = k and v.aufgabe_id in (v_id, v_id2)) <> 3 then fehler := fehler || ('zaehlt = nein: Versuche nicht gespeichert')::text; end if;
    -- neue Lernkarte: nein richtig, ja richtig, nein zweimal falsch
    v_ids := array[pg_temp.ft_kopie(v_basis, 'ft-probe-d', null, null, 'zwei_wege', 'nein', 3), pg_temp.ft_kopie(v_basis, 'ft-probe-d', 'direkt', 1, 'umkehren', 'ja', 4),
                   pg_temp.ft_kopie(v_basis, 'ft-probe-d', null, null, 'bruecke', 'nein', 5)];
    v_r := pg_temp.ft_ant(k, v_ids[1], true, 1, 'ft-d-1');
    if not (v_r @> '{"format_ok":true,"richtig":true}') or exists (select 1 from schule.karte_stand x where x.lernender_id = k and x.einheit_id = v_e and x.lernziel = 'ft-probe-d') then fehler := fehler || ('zaehlt = nein auf neuer Karte: ' || left(v_r::text, 200))::text; end if;
    o := o || jsonb_build_object('ja_richtig', pg_temp.ft_ant(k, v_ids[2], true, 1, 'ft-d-2'));
    ks := (select x from schule.karte_stand x where x.lernender_id = k and x.einheit_id = v_e and x.lernziel = 'ft-probe-d'); v_m := pg_temp.ft_k(k, v_e, 'ft-probe-d');
    if ks.lernender_id is null or ks.eigene_loesungen <> 1 or ks.folge <> 1 or not ks.gezaehlt ? v_ids[2]::text or ks.gezaehlt ? v_ids[1]::text then fehler := fehler || ('form + zaehlt = ja zählt nicht wie erwartet')::text; end if;
    perform pg_temp.ft_ant(k, v_ids[3], false, 1, 'ft-d-3'); perform pg_temp.ft_ant(k, v_ids[3], false, 2, 'ft-d-4');
    if pg_temp.ft_k(k, v_e, 'ft-probe-d') is distinct from v_m then fehler := fehler || ('zaehlt = nein, falsch: Folge oder Karte verändert')::text; end if;
    p := p || jsonb_build_object('bearbeitungen_d', schule.karte_bearbeitungen(k, v_e, 'ft-probe-d'));
    if schule.karte_bearbeitungen(k, v_e, 'ft-probe-d') <> 3 then fehler := fehler || ('Bearbeitungen: ' || schule.karte_bearbeitungen(k, v_e, 'ft-probe-d') || ' statt 3')::text; end if;
    v_r := schule.einheit_lesen_intern(k, v_e);
    p := p || jsonb_build_object('form_jede', v_r->'form_jede', 'uebung_form', (select jsonb_build_object('form', u->'form', 'zaehlt', u->'zaehlt') from jsonb_array_elements(v_r->'uebungen') u where (u->>'id')::bigint = v_ids[2]),
                                 'etappen_felder', (select count(*) from jsonb_each(v_r->'etappen_stand') s where s.value ?& array['anwenden_noetig', 'anwenden_ok', 'bearbeitungen']),
                                 'etappen', (select count(*) from jsonb_each(v_r->'etappen_stand')));
    if (v_r->>'form_jede')::int is distinct from schule.wd_regel('form_jede', -1) or p->'uebung_form' is distinct from '{"form":"umkehren","zaehlt":"ja"}'::jsonb
       or (p->>'etappen_felder')::int <> (p->>'etappen')::int or (p->>'etappen')::int = 0 then fehler := fehler || ('einheit_lesen_intern: form_jede oder neue Felder fehlen: ' || left(p::text, 300))::text; end if;
    raise exception using errcode = 'FT999', message = 'zurueck';
  exception
    when sqlstate 'FT999' then null;
    when others then fehler := fehler || ('zaehlt-Proben: ' || sqlerrm)::text;
  end;
  if o->'anzeige' is distinct from '{"form":"lueckenweg","zaehlt":"nein"}'::jsonb then fehler := fehler || ('Anzeige ohne form/zaehlt: ' || coalesce((o->'anzeige')::text, 'leer'))::text; end if;
  if not (o->'nein_richtig' @> '{"format_ok":true,"richtig":true}') or not (o->'nein_falsch_1' @> '{"nochmal":true}') or not (o->'nein_falsch_2' ? 'loesung')
     or not (o->'ja_richtig' @> '{"richtig":true,"karte":{"eigene_loesungen":1,"bearbeitungen":2}}') then fehler := fehler || ('zaehlt-Proben: unerwartete Antworten: ' || left(o::text, 400))::text; end if;

  -- 5. Prüfbedingungen
  for i in 1 .. 2 loop
    v_c := null;
    begin
      perform pg_temp.ft_kopie(v_basis, 'ft-probe-x', null, null, case i when 1 then 'quatsch' end, case i when 2 then 'folge' end, 40 + i);
      raise exception using errcode = 'FT999', message = 'angenommen';
    exception
      when check_violation then get stacked diagnostics v_c = constraint_name;
      when sqlstate 'FT999' then v_c := 'angenommen';
      when others then v_c := 'unerwartet: ' || sqlerrm;
    end;
    if v_c is distinct from (case i when 1 then 'aufgabe_form_check' else 'aufgabe_zaehlt_check' end) then fehler := fehler || ('Prüfbedingung ' || i || ': ' || coalesce(v_c, '-'))::text;
    else p := p || jsonb_build_object('pruefbedingung_' || i, v_c); end if;
  end loop;
  begin
    n := schule.aufgaben_einfuegen(v_e, jsonb_build_array(jsonb_build_object('t', a.teilfaehigkeit, 'p', 'uebung', 's', 2, 'l', 'ft-probe-e', 'y', a.antworttyp, 'f', a.frage || '{"ft_probe":50}',
           'o', a.loesung, 'h', 'Probe', 'w', 'Probe', 'r', 90050, 'g', 'umkehr', 'form', 'umkehren', 'zaehlt', 'nein') || jsonb_strip_nulls(jsonb_build_object('a', a.antworten))));
    p := p || jsonb_build_object('einfuegen', n, 'einfuegen_ok', exists (select 1 from schule.aufgabe x where x.einheit_id = v_e and x.variante_gruppe = 'ft-probe-e' and x.form = 'umkehren' and x.zaehlt = 'nein'));
    raise exception using errcode = 'FT999', message = 'zurueck';
  exception
    when sqlstate 'FT999' then null;
    when others then fehler := fehler || ('aufgaben_einfuegen: ' || sqlerrm)::text;
  end;
  if not coalesce((p->>'einfuegen_ok')::boolean, false) or (p->>'einfuegen')::int <> 1 then fehler := fehler || ('aufgaben_einfuegen übernimmt form/zaehlt nicht')::text; end if;

  -- 6. Sachaufgaben-Pflicht: A mit Sachaufgabe (zählt), B mit Sachaufgabe zaehlt = nein
  begin
    perform schule.offene_entscheiden(k);
    for i in 1 .. 6 loop
      v_ids[i] := pg_temp.ft_kopie(v_basis, 'ft-probe-a', case when i <= 3 then 'direkt' else 'mehrschritt' end, case when i <= 3 then 1 else 2 end, null, null, 10 + i);
      v_ids[6 + i] := pg_temp.ft_kopie(v_basis, 'ft-probe-b', case when i <= 3 then 'direkt' else 'mehrschritt' end, case when i <= 3 then 1 else 2 end, null, null, 20 + i);
    end loop;
    v_id := pg_temp.ft_kopie(v_basis, 'ft-probe-a', 'einkleidung', 2, 'anwenden', 'ja', 17);
    perform pg_temp.ft_kopie(v_basis, 'ft-probe-b', 'einkleidung', 2, 'anwenden', 'nein', 27);
    for i in 1 .. 6 loop v_r := pg_temp.ft_ant(k, v_ids[i], true, 1, 'ft-a-' || i); end loop;
    p := p || jsonb_build_object('a_ohne', v_r->'karte' - 'gezaehlt');
    v_r := pg_temp.ft_ant(k, v_id, true, 1, 'ft-a-7');
    p := p || jsonb_build_object('a_mit', v_r->'karte' - 'gezaehlt');
    for i in 7 .. 12 loop v_r := pg_temp.ft_ant(k, v_ids[i], true, 1, 'ft-b-' || i); end loop;
    p := p || jsonb_build_object('b', v_r->'karte' - 'gezaehlt');
    raise exception using errcode = 'FT999', message = 'zurueck';
  exception
    when sqlstate 'FT999' then null;
    when others then fehler := fehler || ('Sachaufgaben-Pflicht: ' || sqlerrm)::text;
  end;
  if not (p->'a_ohne' @> '{"sitzt":false,"eigene_loesungen":6,"anwenden_noetig":true,"anwenden_ok":false}') then fehler := fehler || ('Pflicht: Karte ohne Sachaufgabe: ' || coalesce((p->'a_ohne')::text, 'leer'))::text; end if;
  if not (p->'a_mit' @> '{"sitzt":true,"anwenden_ok":true}') then fehler := fehler || ('Pflicht: Karte mit Sachaufgabe: ' || coalesce((p->'a_mit')::text, 'leer'))::text; end if;
  if not (p->'b' @> '{"sitzt":true,"anwenden_noetig":false,"ziel":6}') then fehler := fehler || ('Pflicht entfällt nicht (Sachaufgabe zaehlt = nein): ' || coalesce((p->'b')::text, 'leer'))::text; end if;

  -- 7. Wiederholung und Mischkarte ziehen keine Aufgabe mit zaehlt = nein
  begin
    v_id := pg_temp.ft_kopie(v_basis, 'ft-probe-c', null, 2, 'bruecke', 'nein', 30);
    p := p || jsonb_build_object('wdh_nur_nein', jsonb_build_array(schule.wdh_aufgabe_waehlen(k, v_e, 'ft-probe-c', false), schule.wdh_aufgabe_waehlen(k, v_e, 'ft-probe-c', true),
                                 schule.wdh_aufgabe_da(k, v_e, 'ft-probe-c'), schule.wdh_aufgabe_da(v_e, 'ft-probe-c')));
    v_id2 := pg_temp.ft_kopie(v_basis, 'ft-probe-c', null, 2, null, null, 31);
    p := p || jsonb_build_object('wdh_mit_ja', jsonb_build_array(schule.wdh_aufgabe_waehlen(k, v_e, 'ft-probe-c', false) = v_id2, schule.wdh_aufgabe_waehlen(k, v_e, 'ft-probe-c', true) = v_id2,
                                 schule.wdh_aufgabe_da(k, v_e, 'ft-probe-c'), schule.wdh_aufgabe_da(v_e, 'ft-probe-c')));
    raise exception using errcode = 'FT999', message = 'zurueck';
  exception
    when sqlstate 'FT999' then null;
    when others then fehler := fehler || ('Wiederholung: ' || sqlerrm)::text;
  end;
  if p->'wdh_nur_nein' is distinct from '[null, null, false, false]'::jsonb
     or p->'wdh_mit_ja' is distinct from (case when v_status in ('geprueft', 'freigegeben') then '[true, true, true, true]' else '[true, true, false, false]' end)::jsonb
    then fehler := fehler || ('Wiederholung/Mischkarte: ' || coalesce((p->'wdh_nur_nein')::text, '-') || ' / ' || coalesce((p->'wdh_mit_ja')::text, '-'))::text; end if;

  -- 8. Am Ende: Karten (alle Kinder) und Aufgabenzahl wie vorher; keine sitzende Karte mit Sachaufgaben-Pflicht
  if (select row(t.*)::text from ft_kvor t) is distinct from (select row((select md5(coalesce(string_agg(concat_ws('|', x.lernender_id, x.einheit_id, x.lernziel, x.sitzt, x.sitzt_am, x.eigene_loesungen, x.gezaehlt, x.folge), '#' order by x.lernender_id, x.einheit_id, x.lernziel), '')) from schule.karte_stand x),
       (select md5(coalesce(string_agg(x::text, '#' order by x.lernender_id, x.einheit_id, x.lernziel), '')) from schule.karte_stand x),
       (select count(*) from schule.karte_stand x where x.sitzt), (select count(*) from schule.aufgabe))::text) then fehler := fehler || ('Karten oder Aufgabenzahl am Ende anders als vorher')::text; end if;
  select count(*) into n from schule.karte_stand x where x.sitzt and schule.karte_anwenden_pflicht(x, x.einheit_id, x.lernziel);
  if n <> 0 then fehler := fehler || (n || ' sitzende Karten hätten eine Sachaufgaben-Pflicht')::text; end if;
  if exists (select 1 from schule.aufgabe x where x.variante_gruppe like 'ft-probe-%' or x.frage ? 'ft_probe') then fehler := fehler || ('Probe-Aufgaben sind nicht zurückgerollt')::text; end if;

  if array_length(fehler, 1) > 0 then raise exception 'FT-S ABBRUCH, alles zurückgerollt: %', array_to_string(fehler, ' | '); end if;
  insert into ft_bericht select jsonb_build_object('ergebnis', 'FT-S eingespielt, alle Prüfungen bestanden', 'funktionen_geaendert', 17, 'funktionen_neu', 6,
    'karten', (select count(*) from schule.karte_stand), 'karten_sitzend', (select t.sitzend from ft_kvor t), 'pruefsumme_karten', (select t.spalten from ft_kvor t),
    'proben', p, 'antworten', (select jsonb_object_agg(key, value - 'loesung' - 'loesungsweg') from jsonb_each(o) where jsonb_typeof(value) = 'object'));
  raise exception 'PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt): %', (select b::text from ft_bericht);
end $pruef$;
select b from ft_bericht;
