-- RK-D (Prüfung Gestalter RK-App, Punkt K4): schule_reise_karte liefert je Flug und je Stadt zusätzlich „gesperrt“ mit Grund und „abgelegt“.
-- Nur lesend; alle bisherigen Felder bleiben gleich (Rauchtest: md5 der übrigen Felder). Keine Tabelle, kein Trigger, kein DROP, kein DELETE.
-- Eingebaut in schule.reise_karte (Text-Patch, Anker geprüft): einmal je Aufruf schule.rk_d_basis (Visum, Klassen, abgelegt); die Felder
-- entstehen direkt beim Aufbau von Flug und Stadt. Wiederholbar.
--
-- Festlegungen (Daten wie bisher, keine neue Regel):
--   Visum: der Ort des Flugs hat eine harte Voraussetzung (schule.v_ort_visum, Gruppe des Kindes), deren Ort noch nicht erledigt ist
--          (route fertig oder „kann schon“, oder Visum-Übergang) – dieselbe Bedingung wie in schule.reiseoptionen.
--   ab Klasse: Klasse des Flugs (Thema) in der Schulart des Kindes (thema_jahrgang, wie Lehrplan-Matrix und schuljahr_stand; IB: MYP-Jahr + 5);
--          die Städte erben sie (Klassen je Etappe aus thema_lage wären genauer, kosten aber rund 30 ms je Aufruf – siehe Meldung).
--   Flug gesperrt nur ohne eigenen Fortschritt (kein Stempel, nicht golden, nicht gesetzt, Stufe nicht dran/wiederholung/komplett):
--     'visum'  – Visum fehlt (auch wenn im Plan),
--     'klasse' – nicht im Plan und ab_klasse > Klasse des Kindes.
--   Stadt gesperrt (nur Stand 'offen'): Grund des Flugs.
--   abgelegt: Etappe endgültig aus der Wiederholung (schule.abgelegt, art 'etappe'), mit Datum; je Flug: Flug abgelegt (art 'flug').
-- Neue Felder: Flug  gesperrt, gesperrt_grund ('visum' | 'klasse' | null), ab_klasse, visum_fehlt [{block_id, ort, kontinent}], abgelegt
--              Stadt gesperrt, gesperrt_grund, ab_klasse, abgelegt, abgelegt_am

do $$ begin
  if to_regprocedure('schule.reise_karte(bigint)') is null or to_regclass('schule.abgelegt') is null
     or to_regclass('schule.v_ort_visum') is null then raise exception 'RK-D: Voraussetzungen fehlen (RD-S, LK-S, WD-S, TL-S)'; end if;
end $$;

-- Grundlage je Kind (einmal je Aufruf der Reisekarte)
create or replace function schule.rk_d_basis(p_l bigint)
 returns jsonb language plpgsql stable set search_path to ''
as $$
declare v_sa text; v_kl int; v_gr text; v_plus int; v_t bigint[]; v_visum jsonb; v_lage_f jsonb; v_abg jsonb;
begin
  select coalesce(l.schulart, 'gym_by'), l.klasse, schule.kind_gruppe(l.id) into v_sa, v_kl, v_gr from schule.lernender l where l.id = p_l;
  v_plus := case when v_sa = 'ib_myp' then 5 else 0 end;
  select coalesce(array_agg(distinct rl.thema_id), '{}') into v_t from schule.reise_land rl where rl.art = 'flug' and rl.thema_id is not null;
  -- Visum je Thema: fehlende Voraussetzungs-Orte (wie schule.reiseoptionen)
  select coalesce(jsonb_object_agg(x.thema_id::text, x.fehlt), '{}'::jsonb) into v_visum from (
    select t.thema_id, jsonb_agg(distinct jsonb_build_object('block_id', bb.id, 'ort', bb.titel, 'kontinent', kk.titel)) fehlt
      from unnest(v_t) t(thema_id) join schule.block_thema bt on bt.thema_id = t.thema_id
      join schule.v_ort_visum v on v.ort_id = bt.block_id and v.gruppe = v_gr
      join schule.block bb on bb.id = v.braucht_ort_id left join schule.kontinent kk on kk.id = bb.kontinent_id
     where not exists (select 1 from schule.route r where r.lernender_id = p_l and r.block_id = v.braucht_ort_id and (r.status = 'fertig' or r.kann_schon))
       and not exists (select 1 from schule.visum_uebergang u where u.lernender_id = p_l and u.block_id = v.braucht_ort_id)
     group by t.thema_id) x;
  -- Klasse je Flug: Klasse des Themas in der Schulart des Kindes (dieselbe Quelle wie schule.thema_jahrgang, hier für alle Flüge auf einmal;
  -- feste Klasse thema.klasse_fest geht vor; IB: MYP-Jahr + 5)
  select coalesce(jsonb_object_agg(t.id::text, coalesce((t.klasse_fest->>v_sa)::int, j.jahr) + v_plus) filter (where coalesce((t.klasse_fest->>v_sa)::int, j.jahr) is not null), '{}'::jsonb)
    into v_lage_f
    from schule.thema t
    left join (select z.thema_id, min(q.jahr_von)::int jahr from schule.zuordnung z join schule.eintrag e on e.id = z.eintrag_id join schule.quelle q on q.id = e.quelle_id
                where z.thema_id = any(v_t) and q.aktiv and q.rolle = 'basis' and not e.archiviert and q.schulart = v_sa group by z.thema_id) j on j.thema_id = t.id
   where t.id = any(v_t);

  -- abgelegt (Etappen und Flüge)
  select coalesce(jsonb_object_agg(a.bezug, a.am), '{}'::jsonb) into v_abg from schule.abgelegt a where a.lernender_id = p_l and a.art in ('etappe', 'flug');
  return jsonb_build_object('klasse', v_kl, 'visum', v_visum, 'lage_flug', v_lage_f, 'abgelegt', v_abg);
end $$;
revoke all on function schule.rk_d_basis(bigint) from public, anon, authenticated;

-- Einbau in schule.reise_karte: je Flug einmal Grund/Klasse/Visum bestimmen, Felder direkt an Stadt und Flug (keine zweite Runde über die Antwort)
do $$
declare d text;
  a1 text := $a$v_offen jsonb; v_zp boolean; -- ZP-S$a$;
  n1 text := $a$v_offen jsonb; v_zp boolean; -- ZP-S
  v_rk jsonb; v_rk_vf jsonb; v_rk_ab int; v_rk_gr text; v_rk_fort boolean; -- RK-D$a$;
  a2 text := $a$begin
  for v_k in select k.id, k.schluessel, k.titel, k.zusatz, k.reihenfolge, rk.reise$a$;
  n2 text := $a$begin
  v_rk := schule.rk_d_basis(p_l); -- RK-D
  for v_k in select k.id, k.schluessel, k.titel, k.zusatz, k.reihenfolge, rk.reise$a$;
  a3 text := $a$      v_st := '[]'; v_offen := null;$a$;
  n3 text := $a$      v_rk_vf := coalesce(v_rk->'visum'->(v_f.thema_id::text), '[]'::jsonb); -- RK-D
      v_rk_ab := (v_rk->'lage_flug'->>(v_f.thema_id::text))::int;
      v_rk_fort := v_stempel is not null or coalesce(v_golden, false) or v_stufe->>'gesetzt' is not null or coalesce(v_stufe->>'stufe', '') in ('dran', 'wiederholung', 'komplett');
      v_rk_gr := case when not v_rk_fort and jsonb_array_length(v_rk_vf) > 0 then 'visum'
                      when not v_rk_fort and not coalesce((v_stufe->>'im_plan')::boolean, false) and v_rk_ab > (v_rk->>'klasse')::int then 'klasse' end;
      v_st := '[]'; v_offen := null;$a$;
  a4 text := $a$                                    || case when v_zp then jsonb_build_object('zaehlt', true) else '{}'::jsonb end); -- ZP-S$a$;
  n4 text := $a$                                    || case when v_zp then jsonb_build_object('zaehlt', true) else '{}'::jsonb end -- ZP-S
                                    || jsonb_build_object('gesperrt', v_rk_gr is not null and v_stand = 'offen', 'gesperrt_grund', case when v_stand = 'offen' then v_rk_gr end,
                                         'ab_klasse', v_rk_ab, 'abgelegt', v_rk->'abgelegt' ? ('etappe:' || v_e || ':' || v_s.lernziel),
                                         'abgelegt_am', v_rk->'abgelegt'->>('etappe:' || v_e || ':' || v_s.lernziel))); -- RK-D$a$;
  a5 text := $a$        'staedte', v_st);$a$;
  n5 text := $a$        'staedte', v_st,
        'gesperrt', v_rk_gr is not null, 'gesperrt_grund', v_rk_gr, 'ab_klasse', v_rk_ab, 'visum_fehlt', v_rk_vf, 'abgelegt', v_rk->'abgelegt' ? ('flug:' || v_f.thema_id)); -- RK-D$a$;
begin
  d := pg_get_functiondef('schule.reise_karte(bigint)'::regprocedure);
  if position('RK-D' in d) > 0 then raise notice 'reise_karte schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a1, ''))) / length(a1) <> 1 then raise exception 'RK-D: Anker 1 in reise_karte nicht genau einmal gefunden'; end if;
  if (length(d) - length(replace(d, a2, ''))) / length(a2) <> 1 then raise exception 'RK-D: Anker 2 in reise_karte nicht genau einmal gefunden'; end if;
  if (length(d) - length(replace(d, a3, ''))) / length(a3) <> 1 then raise exception 'RK-D: Anker 3 in reise_karte nicht genau einmal gefunden'; end if;
  if (length(d) - length(replace(d, a4, ''))) / length(a4) <> 1 then raise exception 'RK-D: Anker 4 in reise_karte nicht genau einmal gefunden'; end if;
  if (length(d) - length(replace(d, a5, ''))) / length(a5) <> 1 then raise exception 'RK-D: Anker 5 in reise_karte nicht genau einmal gefunden'; end if;
  execute replace(replace(replace(replace(replace(d, a1, n1), a2, n2), a3, n3), a4, n4), a5, n5);
end $$;
