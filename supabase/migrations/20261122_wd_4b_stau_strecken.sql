-- Bau-Auftrag WD-4, Teil b: den vorhandenen Stau einmalig und verlustfrei strecken.
-- NUR nach Probelauf und Sebastians Okay einspielen (Haupt-Chat). Setzt 20261122_wd_s_wiederholungen.sql voraus (Regel wdh_gesetzt_je_lerntag).
--
-- Was passiert – in Worten:
--   Betroffen sind nur Etappen, die über „Kann er – aber wiederholen“ gesetzt wurden, noch auf Stufe 0 stehen (erste Wiederholung offen),
--   keinen Wiederholungs-Fehler haben und heute fällig sind. Genau diese Etappen kamen alle auf einmal in den Takt (Stau).
--   Je Kind bleiben die ersten 6 (Regel wdh_gesetzt_je_lerntag) heute fällig; die übrigen werden auf die nächsten Lerntage verteilt:
--   Nr. 7–12 am 1. Lerntag ab morgen, Nr. 13–18 am 2. usw. Reihenfolge: ein Flug nach dem anderen in Plan-Reihenfolge, im Flug die Etappen-Reihenfolge.
--   Geändert werden nur die drei Felder der Fälligkeit (faellig_am, wdh_ab, wdh_lerntage). Landung, Stufe, Belege, Sterne, Lernstände, Plan bleiben;
--   das wird am Ende geprüft (sonst Abbruch). Natürlich gelandete Etappen und Etappen mit Fehler bleiben unberührt – den Rest löst die Runde nach WD-1 auf.
--   Die alten Werte stehen in schule.wdh_staffel_sicherung. Zurück (falls gewünscht):
--     update schule.karte_stand k set faellig_am = s.faellig_am, wdh_ab = s.wdh_ab, wdh_lerntage = s.wdh_lerntage
--       from schule.wdh_staffel_sicherung s where s.lernender_id = k.lernender_id and s.einheit_id = k.einheit_id and s.lernziel = k.lernziel;
--   Wiederholt ausführbar: ein zweiter Lauf findet höchstens die 6 heute fälligen je Kind und ändert nichts.
--   Ausgabe (NOTICE) je Kind nur mit Nummer: fällig vorher → nachher und die Verteilung auf Lerntage. Kein DROP, kein DELETE.

create table if not exists schule.wdh_staffel_sicherung (
  lernender_id bigint not null, einheit_id bigint not null, lernziel text not null,
  faellig_am timestamptz, wdh_ab timestamptz, wdh_lerntage smallint,
  gesichert_am timestamptz not null default now(),
  primary key (lernender_id, einheit_id, lernziel)
);
comment on table schule.wdh_staffel_sicherung is 'WD-4b: Fälligkeit gesetzter Etappen vor dem einmaligen Strecken (zum Zurücksetzen)';
alter table schule.wdh_staffel_sicherung enable row level security;
revoke all on table schule.wdh_staffel_sicherung from public, anon, authenticated;

do $mig$
declare v_je int := greatest(schule.wd_regel('wdh_gesetzt_je_lerntag', 6), 1); v_vorher text; v_nachher text; r record; v_n int;
begin
  -- Prüfsumme über alles außer den drei Fälligkeits-Feldern
  select md5(coalesce(string_agg((to_jsonb(k) - 'faellig_am' - 'wdh_ab' - 'wdh_lerntage')::text, '|' order by k.lernender_id, k.einheit_id, k.lernziel), ''))
       || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.lernziel_stand x), ''))
       || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.route x), ''))
       || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.sterne x), ''))
    into v_vorher from schule.karte_stand k;

  -- Plan: welche Etappe bekommt welchen Lerntag (0 = bleibt heute fällig)
  create temp table if not exists wd4b_plan (lernender_id bigint, einheit_id bigint, lernziel text, tag int) on commit drop;
  truncate wd4b_plan; -- nur die Hilfstabelle dieser Sitzung
  insert into wd4b_plan (lernender_id, einheit_id, lernziel, tag)
  select q.lernender_id, q.einheit_id, q.lernziel, (q.nr - 1) / v_je as tag
    from (select k.lernender_id, k.einheit_id, k.lernziel,
                 row_number() over (partition by k.lernender_id
                   order by coalesce((select min(ro.position) from schule.route ro where ro.lernender_id = k.lernender_id and ro.block_id = e.block_id and ro.art = 'normal'), 2147483647),
                            e.id,
                            coalesce((select et.nr from jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) with ordinality et(x, nr) where et.x->>'lernziel' = k.lernziel), 999),
                            k.lernziel) nr
            from schule.karte_stand k join schule.einheit e on e.id = k.einheit_id
           where k.sitzt and k.wdh_gesetzt_am is not null and k.wdh_stufe = 0 and k.wdh_fehler = 0 and schule.karte_faellig(k)) q;

  for r in select p.lernender_id, sum(p.c) n, string_agg(p.tag || ':' || p.c, ' ' order by p.tag) verteilung
             from (select lernender_id, tag, count(*) c from wd4b_plan group by 1, 2) p group by 1 order by 1 loop
    raise notice 'WD-4b Kind %: % gesetzte fällige Etappen → je Lerntag (0 = heute): %', r.lernender_id, r.n, r.verteilung;
  end loop;

  insert into schule.wdh_staffel_sicherung (lernender_id, einheit_id, lernziel, faellig_am, wdh_ab, wdh_lerntage)
  select k.lernender_id, k.einheit_id, k.lernziel, k.faellig_am, k.wdh_ab, k.wdh_lerntage
    from schule.karte_stand k join wd4b_plan p on p.lernender_id = k.lernender_id and p.einheit_id = k.einheit_id and p.lernziel = k.lernziel
   where p.tag > 0
  on conflict do nothing;

  update schule.karte_stand k set wdh_ab = now(), wdh_lerntage = p.tag, faellig_am = now() + p.tag * interval '1 day'
    from wd4b_plan p
   where p.lernender_id = k.lernender_id and p.einheit_id = k.einheit_id and p.lernziel = k.lernziel and p.tag > 0;
  get diagnostics v_n = row_count;

  select md5(coalesce(string_agg((to_jsonb(k) - 'faellig_am' - 'wdh_ab' - 'wdh_lerntage')::text, '|' order by k.lernender_id, k.einheit_id, k.lernziel), ''))
       || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.lernziel_stand x), ''))
       || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.route x), ''))
       || md5(coalesce((select string_agg(x::text, '|' order by x::text) from schule.sterne x), ''))
    into v_nachher from schule.karte_stand k;
  if v_nachher <> v_vorher then raise exception 'WD-4b: außer der Fälligkeit hat sich etwas geändert – Abbruch'; end if;

  for r in select l.id, count(*) filter (where schule.karte_faellig(k)) n from schule.lernender l join schule.karte_stand k on k.lernender_id = l.id group by 1 order by 1 loop
    raise notice 'WD-4b Kind %: heute fällig nachher %', r.id, r.n;
  end loop;
  raise notice 'WD-4b: % Etappen gestreckt; Landungen, Stufen, Belege, Lernstände, Plan, Sterne unverändert', v_n;
end $mig$;
