-- W150 Rückmeldung & Lernweg, Paket R1 / V6 (inhalte/pruefung/rueckmeldung/umsetzung.md):
-- Ein Fehler bei einer Karte, die „sitzt“, wirft sie nicht mehr sofort auf „üben“ zurück.
-- 1. Fehler: Wiederholstufe um 1 kleiner (mindestens 0), morgen wieder fällig, „sitzt“ bleibt (die Karte bleibt in schule_wiederholung).
-- 2. Fehler hintereinander: zurück auf „üben“ (bisheriges Verhalten). Ein richtiger Versuch dazwischen setzt den Zähler zurück.
alter table schule.karte_stand add column if not exists wdh_fehler smallint not null default 0;
comment on column schule.karte_stand.wdh_fehler is 'Fehler hintereinander, seit die Karte sitzt (0 oder 1); beim 2. Fehler geht die Karte zurück auf üben';

create or replace function schule.karte_buchen(p_l bigint, p_aufgabe bigint, p_richtig boolean, p_hilfe smallint, p_zeit timestamp with time zone)
 returns void
 language plpgsql
 set search_path to ''
as $function$
declare a schule.aufgabe; k schule.karte_stand; v_ziel int;
  v_abst interval[] := array[interval '1 day', interval '3 days', interval '7 days', interval '14 days', interval '30 days'];
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
    end if;
  else
    if not p_richtig then
      if k.wdh_fehler >= 1 then
        k.sitzt := false; k.serie := 0; k.wdh_stufe := 0; k.faellig_am := null; k.wdh_fehler := 0;
      else
        k.wdh_fehler := 1; k.wdh_stufe := greatest(k.wdh_stufe - 1, 0); k.faellig_am := p_zeit + interval '1 day';
      end if;
    else
      k.wdh_fehler := 0;
      if k.faellig_am is null or k.faellig_am <= p_zeit then
        k.wdh_stufe := least(k.wdh_stufe + 1, 4); k.faellig_am := p_zeit + v_abst[k.wdh_stufe + 1];
      end if;
    end if;
  end if;
  update schule.karte_stand set serie = k.serie, richtig = k.richtig, falsch = k.falsch, sitzt = k.sitzt, sitzt_am = k.sitzt_am,
    wdh_stufe = k.wdh_stufe, faellig_am = k.faellig_am, wdh_fehler = k.wdh_fehler, zuletzt = p_zeit
   where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe;
end $function$;
