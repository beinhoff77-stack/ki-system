-- Bau-Auftrag WD-4, Teil b: den vorhandenen Stau einmalig und verlustfrei strecken (Stand WD-S 3, 22.11.).
-- NUR nach Probelauf und Sebastians Okay einspielen (Haupt-Chat), nach 20261122_wd_s_wiederholungen.sql und 20261122_wd_s3_frische_aufgaben.sql.
--
-- Was passiert – in Worten:
--   Betroffen sind nur Etappen, die über „Kann er – aber wiederholen“ gesetzt wurden, noch auf Stufe 0 stehen (erste Wiederholung offen),
--   keinen Wiederholungs-Fehler haben und heute fällig sind. Genau diese Etappen kamen alle auf einmal in den Takt (Stau).
--   Ausgenommen (ChatGPT 919 MUSS 2): Etappen, die in einer noch offenen Wiederholungs-Runde von heute stehen – sie bleiben heute fällig und zählen
--   auf den heutigen Platz an.
--   Je Kind höchstens 6 (Regel wdh_gesetzt_je_lerntag) erste Wiederholungen je Lerntag (MUSS 3): heute bleiben so viele fällig, wie Plätze frei sind;
--   die übrigen kommen auf den nächsten Lerntag mit freiem Platz – schon von WD-4 geplante erste Wiederholungen gesetzter Etappen belegen ihre Tage mit.
--   Reihenfolge: ein Flug nach dem anderen in Plan-Reihenfolge, im Flug die Etappen-Reihenfolge.
--   Gezählt wird in Lerntagen, nicht Kalendertagen (wdh_ab + wdh_lerntage wie überall im Takt): Reisetage ohne Lernen verschieben nichts nach vorn.
--   Geändert werden nur die drei Felder der Fälligkeit (faellig_am, wdh_ab, wdh_lerntage). Landung, Stufe, Belege, Sterne, Lernstände, Plan bleiben;
--   das wird am Ende geprüft (sonst Abbruch). Natürlich gelandete Etappen und Etappen mit Fehler bleiben unberührt – den Rest löst die Runde nach WD-1 auf.
--   Einmalig: Ein zweiter Lauf tut nichts (es gibt schon Sicherungen).
--   Die alten Werte stehen in schule.wdh_staffel_sicherung. Zurück nur, solange keine dieser Etappen seitdem geübt wurde:
--     select schule.wdh_staffel_zurueck();   -- lehnt ab, wenn eine Etappe inzwischen beantwortet wurde, und ändert dann nichts
--   Ausgabe (NOTICE) je Kind nur mit Nummer: Verteilung auf Lerntage und heute fällig nachher. Kein DROP, kein DELETE.

create table if not exists schule.wdh_staffel_sicherung (
  lernender_id bigint not null, einheit_id bigint not null, lernziel text not null,
  faellig_am timestamptz, wdh_ab timestamptz, wdh_lerntage smallint,
  gesichert_am timestamptz not null default now(),
  primary key (lernender_id, einheit_id, lernziel)
);
alter table schule.wdh_staffel_sicherung add column if not exists richtig integer;          -- Stand beim Strecken (Rückweg nur ohne Zwischenübung)
alter table schule.wdh_staffel_sicherung add column if not exists falsch integer;
alter table schule.wdh_staffel_sicherung add column if not exists wdh_ab_neu timestamptz;
alter table schule.wdh_staffel_sicherung add column if not exists zurueck_am timestamptz;
comment on table schule.wdh_staffel_sicherung is 'WD-4b: Fälligkeit gesetzter Etappen vor dem einmaligen Strecken (zum Zurücksetzen, nur ohne Zwischenübung)';
alter table schule.wdh_staffel_sicherung enable row level security;
revoke all on table schule.wdh_staffel_sicherung from public, anon, authenticated;

-- Strecken (je Kind oder alle); liefert die Zahl gestreckter Etappen
create or replace function schule.wdh_staffel_strecken(p_l bigint default null)
 returns integer language plpgsql set search_path to ''
as $function$
declare v_je int := greatest(schule.wd_regel('wdh_gesetzt_je_lerntag', 6), 1); v_kind bigint; k record; v_belegt int[]; v_heute int; d int; v_n int := 0;
begin
  for v_kind in select l.id from schule.lernender l where (p_l is null or l.id = p_l) order by l.id loop
    -- schon geplante erste Wiederholungen gesetzter Etappen je künftigem Lerntag (1 = nächster Lerntag)
    select coalesce(array_agg(schule.karte_wdh_in(x)), '{}') into v_belegt from schule.karte_stand x
     where x.lernender_id = v_kind and x.sitzt and x.wdh_gesetzt_am is not null and x.wdh_stufe = 0 and x.wdh_fehler = 0 and not schule.karte_faellig(x);
    -- heute belegt: gesetzte fällige Etappen in der offenen Runde von heute
    select count(*) into v_heute from schule.karte_stand x
      join schule.wdh_runde_etappe r on r.lernender_id = x.lernender_id and r.einheit_id = x.einheit_id and r.lernziel = x.lernziel and r.tag = schule.heute_tag(v_kind)
      join schule.wdh_runde w on w.lernender_id = r.lernender_id and w.tag = r.tag and w.fertig_am is null
     where x.lernender_id = v_kind and x.sitzt and x.wdh_gesetzt_am is not null and x.wdh_stufe = 0 and x.wdh_fehler = 0 and schule.karte_faellig(x);
    for k in
      select x.einheit_id, x.lernziel, x.faellig_am, x.wdh_ab, x.wdh_lerntage, x.richtig, x.falsch
        from schule.karte_stand x join schule.einheit e on e.id = x.einheit_id
       where x.lernender_id = v_kind and x.sitzt and x.wdh_gesetzt_am is not null and x.wdh_stufe = 0 and x.wdh_fehler = 0 and schule.karte_faellig(x)
         and not exists (select 1 from schule.wdh_runde_etappe r join schule.wdh_runde w on w.lernender_id = r.lernender_id and w.tag = r.tag and w.fertig_am is null
                          where r.lernender_id = x.lernender_id and r.tag = schule.heute_tag(v_kind) and r.einheit_id = x.einheit_id and r.lernziel = x.lernziel)
       order by coalesce((select min(ro.position) from schule.route ro where ro.lernender_id = x.lernender_id and ro.block_id = e.block_id and ro.art = 'normal'), 2147483647),
                e.id, coalesce((select et.nr from jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) with ordinality et(y, nr) where et.y->>'lernziel' = x.lernziel), 999),
                x.lernziel loop
      if v_heute < v_je then v_heute := v_heute + 1; continue; end if;      -- bleibt heute fällig
      d := 1;
      while (select count(*) from unnest(v_belegt) b where b = d) >= v_je loop d := d + 1; end loop;
      v_belegt := v_belegt || d;
      insert into schule.wdh_staffel_sicherung (lernender_id, einheit_id, lernziel, faellig_am, wdh_ab, wdh_lerntage, richtig, falsch, wdh_ab_neu)
      values (v_kind, k.einheit_id, k.lernziel, k.faellig_am, k.wdh_ab, k.wdh_lerntage, k.richtig, k.falsch, now())
      on conflict do nothing;
      update schule.karte_stand set wdh_ab = now(), wdh_lerntage = d, faellig_am = now() + d * interval '1 day'
       where lernender_id = v_kind and einheit_id = k.einheit_id and lernziel = k.lernziel;
      v_n := v_n + 1;
    end loop;
  end loop;
  return v_n;
end $function$;
revoke all on function schule.wdh_staffel_strecken(bigint) from public, anon, authenticated;

-- Rückweg: nur wenn keine gestreckte Etappe seitdem beantwortet wurde (sonst Ablehnung, nichts geändert); einmal
create or replace function schule.wdh_staffel_zurueck(p_l bigint default null)
 returns integer language plpgsql set search_path to ''
as $function$
declare v_geuebt int; v_n int;
begin
  select count(*) into v_geuebt from schule.wdh_staffel_sicherung s join schule.karte_stand k
      on k.lernender_id = s.lernender_id and k.einheit_id = s.einheit_id and k.lernziel = s.lernziel
   where s.zurueck_am is null and (p_l is null or s.lernender_id = p_l)
     and (k.richtig is distinct from s.richtig or k.falsch is distinct from s.falsch or k.wdh_ab is distinct from s.wdh_ab_neu);
  if v_geuebt > 0 then
    raise exception 'WD-4b Rückweg abgelehnt: % gestreckte Etappen wurden inzwischen geübt', v_geuebt using errcode = 'P0001';
  end if;
  update schule.karte_stand k set faellig_am = s.faellig_am, wdh_ab = s.wdh_ab, wdh_lerntage = s.wdh_lerntage
    from schule.wdh_staffel_sicherung s
   where s.lernender_id = k.lernender_id and s.einheit_id = k.einheit_id and s.lernziel = k.lernziel and s.zurueck_am is null and (p_l is null or s.lernender_id = p_l);
  get diagnostics v_n = row_count;
  update schule.wdh_staffel_sicherung set zurueck_am = now() where zurueck_am is null and (p_l is null or lernender_id = p_l);
  return v_n;
end $function$;
revoke all on function schule.wdh_staffel_zurueck(bigint) from public, anon, authenticated;

do $mig$
declare v_vorher text; v_nachher text; r record; v_n int;
begin
  if exists (select 1 from schule.wdh_staffel_sicherung) then
    raise notice 'WD-4b: schon gelaufen (Sicherungen vorhanden) – kein zweiter Lauf'; return;
  end if;
  -- Prüfsumme über alles außer den drei Fälligkeits-Feldern
  select md5(coalesce(string_agg((to_jsonb(k) - 'faellig_am' - 'wdh_ab' - 'wdh_lerntage')::text, '|' order by k.lernender_id, k.einheit_id, k.lernziel), ''))
       || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.lernziel_stand x), ''))
       || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.route x), ''))
       || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.sterne x), ''))
    into v_vorher from schule.karte_stand k;

  v_n := schule.wdh_staffel_strecken(null);

  select md5(coalesce(string_agg((to_jsonb(k) - 'faellig_am' - 'wdh_ab' - 'wdh_lerntage')::text, '|' order by k.lernender_id, k.einheit_id, k.lernziel), ''))
       || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.lernziel_stand x), ''))
       || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.route x), ''))
       || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.sterne x), ''))
    into v_nachher from schule.karte_stand k;
  if v_nachher <> v_vorher then raise exception 'WD-4b: außer der Fälligkeit hat sich etwas geändert – Abbruch'; end if;

  for r in select q.lernender_id, string_agg(q.d || ':' || q.n, ' ' order by q.d) verteilung
             from (select x.lernender_id, x.wdh_lerntage d, count(*) n from schule.wdh_staffel_sicherung s0
                     join schule.karte_stand x on x.lernender_id = s0.lernender_id and x.einheit_id = s0.einheit_id and x.lernziel = s0.lernziel
                    group by 1, 2) q group by 1 order by 1 loop
    raise notice 'WD-4b Kind %: gestreckt je Lerntag (Lerntag:Anzahl): %', r.lernender_id, r.verteilung;
  end loop;
  for r in select l.id, count(*) filter (where schule.karte_faellig(k)) n from schule.lernender l join schule.karte_stand k on k.lernender_id = l.id group by 1 order by 1 loop
    raise notice 'WD-4b Kind %: heute fällig nachher %', r.id, r.n;
  end loop;
  raise notice 'WD-4b: % Etappen gestreckt; Landungen, Stufen, Belege, Lernstände, Plan, Sterne unverändert', v_n;
end $mig$;
