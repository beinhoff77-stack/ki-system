-- W150: Neue Regel für „Lernkarte sitzt“ (Entscheidung Sebastian 16.11.):
--  * 6 Punkte statt 2–4 (bei weniger als 6 Übungen: so viele, wie es gibt, mindestens 2)
--  * richtig ohne Hilfe im ersten Versuch: +1 Punkt; Fehler: −2 Punkte (nicht mehr zurück auf 0)
--  * zusätzlich muss mindestens eine Aufgabe der Stufe 3 im ersten Versuch ohne Hilfe richtig sein (wenn die Karte Stufe-3-Übungen hat)
--  * Wiederholungen: bevorzugt Aufgaben der Stufen 2 und 3
-- Karten, die schon sitzen, bleiben unverändert.
alter table schule.karte_stand add column if not exists schwer_ok boolean not null default false;
comment on column schule.karte_stand.schwer_ok is 'Seit Beginn des Übens mindestens eine Stufe-3-Übung ohne Hilfe im ersten Versuch richtig';

create or replace function schule.karte_ziel(p_einheit bigint, p_lz text)
 returns integer language sql stable set search_path to ''
as $function$
  select least(6, greatest(2, count(*)))::int from schule.aufgabe a
   where a.einheit_id = p_einheit and a.pool = 'uebung' and a.variante_gruppe = p_lz and a.freigegeben;
$function$;

create or replace function schule.karte_schwer_noetig(p_einheit bigint, p_lz text)
 returns boolean language sql stable set search_path to ''
as $function$
  select exists (select 1 from schule.aufgabe a
   where a.einheit_id = p_einheit and a.pool = 'uebung' and a.variante_gruppe = p_lz and a.freigegeben and a.stufe = 3);
$function$;

create or replace function schule.karte_buchen(p_l bigint, p_aufgabe bigint, p_richtig boolean, p_hilfe smallint, p_zeit timestamp with time zone)
 returns void
 language plpgsql
 set search_path to ''
as $function$
declare a schule.aufgabe; k schule.karte_stand; v_ziel int;
  v_abst interval[] := array[interval '1 day', interval '3 days', interval '7 days', interval '14 days', interval '30 days'];
  v_tage smallint[] := array[1, 3, 7, 14, 30];
begin
  select * into a from schule.aufgabe where id = p_aufgabe;
  if a.id is null or a.pool <> 'uebung' then return; end if;
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) values (p_l, a.einheit_id, a.variante_gruppe) on conflict do nothing;
  select * into k from schule.karte_stand where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe for update;
  v_ziel := schule.karte_ziel(a.einheit_id, a.variante_gruppe);
  if p_richtig then k.richtig := k.richtig + 1; else k.falsch := k.falsch + 1; end if;
  if not k.sitzt then
    if not p_richtig then k.serie := greatest(k.serie - 2, 0);
    elsif coalesce(p_hilfe, 0) = 0 then
      k.serie := least(k.serie + 1, v_ziel);
      if a.stufe = 3 then k.schwer_ok := true; end if;
    end if;
    if k.serie >= v_ziel and (k.schwer_ok or not schule.karte_schwer_noetig(a.einheit_id, a.variante_gruppe)) then
      k.sitzt := true; k.sitzt_am := p_zeit; k.wdh_stufe := 0; k.faellig_am := p_zeit + v_abst[1]; k.wdh_fehler := 0;
      k.wdh_ab := p_zeit; k.wdh_lerntage := v_tage[1];
    end if;
  else
    if not p_richtig then
      if k.wdh_fehler >= 1 then
        k.sitzt := false; k.serie := 0; k.schwer_ok := false; k.wdh_stufe := 0; k.faellig_am := null; k.wdh_fehler := 0; k.wdh_ab := null; k.wdh_lerntage := null;
      else
        k.wdh_fehler := 1; k.wdh_stufe := greatest(k.wdh_stufe - 1, 0); k.faellig_am := p_zeit + interval '1 day';
        k.wdh_ab := p_zeit; k.wdh_lerntage := 1;
      end if;
    else
      k.wdh_fehler := 0;
      if schule.karte_faellig(k) then
        k.wdh_stufe := least(k.wdh_stufe + 1, 4); k.faellig_am := p_zeit + v_abst[k.wdh_stufe + 1];
        k.wdh_ab := p_zeit; k.wdh_lerntage := v_tage[k.wdh_stufe + 1];
      end if;
    end if;
  end if;
  update schule.karte_stand set serie = k.serie, richtig = k.richtig, falsch = k.falsch, sitzt = k.sitzt, sitzt_am = k.sitzt_am, schwer_ok = k.schwer_ok,
    wdh_stufe = k.wdh_stufe, faellig_am = k.faellig_am, wdh_fehler = k.wdh_fehler, wdh_ab = k.wdh_ab, wdh_lerntage = k.wdh_lerntage, zuletzt = p_zeit
   where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe;
end $function$;

-- Antworten an die App um schwer_ok / schwer_noetig ergänzen; Wiederholung bevorzugt Stufe 2/3
do $do$
declare v_def text; v_neu text;
begin
  select pg_get_functiondef(p.oid) into v_def from pg_proc p where p.pronamespace = 'schule'::regnamespace and p.proname = 'uebung_pruefen_intern';
  v_neu := replace(v_def, $a$'sitzt', k.sitzt,$a$, $a$'sitzt', k.sitzt, 'schwer_ok', k.schwer_ok, 'schwer_noetig', schule.karte_schwer_noetig(k.einheit_id, k.lernziel),$a$);
  if v_neu = v_def then raise exception 'uebung_pruefen_intern: Stelle nicht gefunden'; end if;
  execute v_neu;

  select pg_get_functiondef(p.oid) into v_def from pg_proc p where p.pronamespace = 'schule'::regnamespace and p.proname = 'etappen_stand';
  v_neu := replace(v_def, $a$'sitzt', coalesce(k.sitzt, false),$a$, $a$'sitzt', coalesce(k.sitzt, false), 'schwer_ok', coalesce(k.schwer_ok, false), 'schwer_noetig', schule.karte_schwer_noetig(p_einheit, z.lz),$a$);
  if v_neu = v_def then raise exception 'etappen_stand: Stelle nicht gefunden'; end if;
  execute v_neu;

  select pg_get_functiondef(p.oid) into v_def from pg_proc p where p.pronamespace = 'api'::regnamespace and p.proname = 'schule_wiederholung';
  v_neu := replace(v_def, $a$order by (select count(*) from schule.versuch vs$a$, $a$order by (coalesce(a.stufe, 2) = 1), (select count(*) from schule.versuch vs$a$);
  if v_neu = v_def then raise exception 'schule_wiederholung: Stelle nicht gefunden'; end if;
  execute v_neu;
end $do$;
