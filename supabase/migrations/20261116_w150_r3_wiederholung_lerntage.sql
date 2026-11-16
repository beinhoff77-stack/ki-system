-- W150 Rückmeldung & Lernweg, Paket R3 / V9: Wiederholung in Lerntagen statt Kalendertagen (reisetauglich).
alter table schule.karte_stand add column if not exists wdh_ab timestamptz;
alter table schule.karte_stand add column if not exists wdh_lerntage smallint;
comment on column schule.karte_stand.wdh_ab is 'Zeitpunkt, ab dem die Lerntage bis zur nächsten Wiederholung zählen';
comment on column schule.karte_stand.wdh_lerntage is 'So viele Lerntage nach wdh_ab ist die Karte wieder fällig (1/3/7/14/30); null = alte Zählung über faellig_am';

-- Fällig: so viele Lerntage (Tage mit Mathe-Übung) nach wdh_ab; der heutige Tag zählt mit, sobald er ein späterer Kalendertag ist (das Kind ist gerade da).
create or replace function schule.karte_faellig(k schule.karte_stand) returns boolean language sql stable set search_path to '' as $function$
  select coalesce(k.sitzt, false) and case
    when k.wdh_lerntage is null or k.wdh_ab is null then coalesce(k.faellig_am <= now(), false)
    else (select (select count(*) from schule.lerntag t where t.lernender_id = k.lernender_id and t.fach = 'Mathematik'
                    and (t.datum::timestamp at time zone t.zeitzone) > k.wdh_ab and t.datum < (now() at time zone z.tz)::date)
                 + case when (now() at time zone z.tz)::date > (k.wdh_ab at time zone z.tz)::date then 1 else 0 end >= k.wdh_lerntage
            from (select coalesce((select l.zeitzone from schule.lernender l where l.id = k.lernender_id), 'UTC') as tz) z)
  end
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
    if not p_richtig then k.serie := 0;
    elsif coalesce(p_hilfe, 0) = 0 then k.serie := k.serie + 1;
    end if;
    if k.serie >= v_ziel then
      k.sitzt := true; k.sitzt_am := p_zeit; k.wdh_stufe := 0; k.faellig_am := p_zeit + v_abst[1]; k.wdh_fehler := 0;
      k.wdh_ab := p_zeit; k.wdh_lerntage := v_tage[1];
    end if;
  else
    if not p_richtig then
      if k.wdh_fehler >= 1 then
        k.sitzt := false; k.serie := 0; k.wdh_stufe := 0; k.faellig_am := null; k.wdh_fehler := 0; k.wdh_ab := null; k.wdh_lerntage := null;
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
  update schule.karte_stand set serie = k.serie, richtig = k.richtig, falsch = k.falsch, sitzt = k.sitzt, sitzt_am = k.sitzt_am,
    wdh_stufe = k.wdh_stufe, faellig_am = k.faellig_am, wdh_fehler = k.wdh_fehler, wdh_ab = k.wdh_ab, wdh_lerntage = k.wdh_lerntage, zuletzt = p_zeit
   where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe;
end $function$;

-- Die drei Lese-Funktionen fragen jetzt schule.karte_faellig(k) statt „faellig_am <= now()“ (Text-Ersetzung in den bestehenden Definitionen).
do $$
declare r record; d text; n int := 0;
begin
  for r in select p.oid, p.proname from pg_proc p join pg_namespace s on s.oid = p.pronamespace
            where (s.nspname = 'api' and p.proname in ('schule_lernstand', 'schule_wiederholung')) or (s.nspname = 'schule' and p.proname = 'etappen_stand') loop
    d := pg_get_functiondef(r.oid);
    if position('k.sitzt and k.faellig_am <= now()' in d) = 0 then raise exception 'Stelle in % nicht gefunden', r.proname; end if;
    d := replace(d, 'k.sitzt and k.faellig_am <= now()', 'schule.karte_faellig(k)');
    execute d; n := n + 1;
  end loop;
  if n <> 3 then raise exception 'erwartet 3 Funktionen, gefunden %', n; end if;
end $$;
