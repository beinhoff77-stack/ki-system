-- W150 Phase 3 Schritt D (K3, K4, E-4): Stufe je Schulart je Kind, alle Flüge mit Klasse für den Stand, Bordkarten bis „sitzt“, Lehrplan-Reihenfolge.
--  1. schule.lernender.stufen jsonb – Stufe des Kindes je Schulart, z. B. {"rs_by": 6, "ib_myp": 1}. Fehlt eine Schulart, gilt in der App:
--     eigene Schulart = klasse, andere = gleiche Klasse, IB MYP = Klasse − 4. Setzen über schule_kind_setzen (daten.stufen; null löscht eine Schulart).
--  2. schule.thema.lehrplan_reihenfolge jsonb – Reihenfolge innerhalb der Klasse je Schulart (heute nur gym_by), befüllt aus inhalte/themenliste.json (Feld reihenfolge).
--  3. schule_uebersicht: je Kind „stufen“; neu „themen“ = alle Mathe-Flüge (auch ohne Inhalt) mit Klasse je Schulart, Ort, Kontinent, Einheit –
--     damit zählen Stand und Einstiegs-Check alle Flüge der Klasse (Rechenregel „Stand“), nicht nur die mit Inhalt.
--  4. schule_plan_lesen: kind.stufen; je Flug lehrplan_reihenfolge (für „Neuer Plan aus Lehrplan-Vorlage“, E-4).
--  5. schule_lernstand: je Etappe sitzt_am und bis_sitzt = Zahl der Bordkarten (erste Versuche, ohne Tests) bis zum ersten „sitzt“ (K4).
-- Kein DROP, kein DELETE; bestehende Funktionen nur per create or replace bzw. gezieltem Ersetzen (Stellen im Live-Text vorab geprüft).

alter table schule.lernender add column if not exists stufen jsonb not null default '{}'::jsonb
  check (jsonb_typeof(stufen) = 'object');
comment on column schule.lernender.stufen is 'K3/E-4: Stufe je Schulart (gym_by, rs_by, ib_myp) für den Stand; fehlt eine, gilt die Klasse (IB MYP: Klasse − 4)';
alter table schule.thema add column if not exists lehrplan_reihenfolge jsonb not null default '{}'::jsonb
  check (jsonb_typeof(lehrplan_reihenfolge) = 'object');
comment on column schule.thema.lehrplan_reihenfolge is 'Reihenfolge innerhalb der Klasse je Schulart, z. B. {"gym_by": 3} (Quelle: inhalte/themenliste.json)';

update schule.thema t set lehrplan_reihenfolge = x.r
  from (values
  (1, '{"gym_by":10}'::jsonb),
  (2, '{"gym_by":5}'::jsonb),
  (3, '{"gym_by":4}'::jsonb),
  (4, '{"gym_by":9}'::jsonb),
  (5, '{"gym_by":8}'::jsonb),
  (6, '{"gym_by":11}'::jsonb),
  (7, '{"gym_by":5}'::jsonb),
  (8, '{"gym_by":4}'::jsonb),
  (9, '{"gym_by":9}'::jsonb),
  (10, '{"gym_by":2}'::jsonb),
  (11, '{"gym_by":7}'::jsonb),
  (14, '{"gym_by":13}'::jsonb),
  (15, '{"gym_by":1}'::jsonb),
  (16, '{"gym_by":2}'::jsonb),
  (17, '{"gym_by":8}'::jsonb),
  (18, '{"gym_by":6}'::jsonb),
  (19, '{"gym_by":4}'::jsonb),
  (20, '{"gym_by":2}'::jsonb),
  (21, '{"gym_by":1}'::jsonb),
  (22, '{"gym_by":2}'::jsonb),
  (23, '{"gym_by":3}'::jsonb),
  (24, '{"gym_by":6}'::jsonb),
  (25, '{"gym_by":11}'::jsonb),
  (26, '{"gym_by":12}'::jsonb),
  (28, '{"gym_by":1}'::jsonb),
  (29, '{"gym_by":2}'::jsonb),
  (30, '{"gym_by":5}'::jsonb),
  (31, '{"gym_by":7}'::jsonb),
  (32, '{"gym_by":1}'::jsonb),
  (33, '{"gym_by":2}'::jsonb),
  (34, '{"gym_by":6}'::jsonb),
  (35, '{"gym_by":3}'::jsonb),
  (36, '{"gym_by":8}'::jsonb),
  (37, '{"gym_by":1}'::jsonb),
  (38, '{"gym_by":5}'::jsonb),
  (39, '{"gym_by":6}'::jsonb),
  (42, '{"gym_by":3}'::jsonb),
  (43, '{"gym_by":5}'::jsonb),
  (44, '{"gym_by":8}'::jsonb),
  (45, '{"gym_by":9}'::jsonb),
  (46, '{"gym_by":3}'::jsonb),
  (47, '{"gym_by":7}'::jsonb),
  (50, '{"gym_by":13}'::jsonb),
  (51, '{"gym_by":12}'::jsonb),
  (52, '{"gym_by":13}'::jsonb),
  (53, '{"gym_by":14}'::jsonb),
  (54, '{"gym_by":11}'::jsonb),
  (55, '{"gym_by":12}'::jsonb),
  (56, '{"gym_by":14}'::jsonb),
  (57, '{"gym_by":8}'::jsonb),
  (58, '{"gym_by":9}'::jsonb),
  (60, '{"gym_by":9}'::jsonb),
  (61, '{"gym_by":10}'::jsonb),
  (62, '{"gym_by":3}'::jsonb),
  (63, '{"gym_by":6}'::jsonb),
  (64, '{"gym_by":4}'::jsonb),
  (67, '{"gym_by":7}'::jsonb),
  (68, '{"gym_by":1}'::jsonb),
  (69, '{"gym_by":3}'::jsonb),
  (71, '{"gym_by":7}'::jsonb),
  (73, '{"gym_by":4}'::jsonb),
  (91, '{"gym_by":8}'::jsonb),
  (92, '{"gym_by":9}'::jsonb),
  (93, '{"gym_by":5}'::jsonb),
  (94, '{"gym_by":6}'::jsonb),
  (95, '{"gym_by":7}'::jsonb),
  (96, '{"gym_by":10}'::jsonb),
  (98, '{"gym_by":4}'::jsonb)
  ) as x(id, r)
 where t.id = x.id and t.lehrplan_reihenfolge is distinct from x.r;

-- Stufen setzen: nur gym_by, rs_by, ib_myp mit ganzen Zahlen 1–13; null entfernt eine Schulart.
create or replace function api.schule_kind_setzen(p_schluessel text, p_daten jsonb)
 returns jsonb
 language plpgsql
 security definer
 set search_path to ''
as $function$
declare v_l bigint := nullif(p_daten->>'lernender_id','')::bigint; v_st jsonb; v_k text; v_v jsonb;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  if p_daten ? 'stufen' then
    if jsonb_typeof(p_daten->'stufen') is distinct from 'object' then raise exception 'stufen muss ein Objekt sein' using errcode = 'P0001'; end if;
    select stufen into v_st from schule.lernender where id = v_l;
    for v_k, v_v in select * from jsonb_each(p_daten->'stufen') loop
      if v_k not in ('gym_by', 'rs_by', 'ib_myp') then raise exception 'Unbekannte Schulart %', v_k using errcode = 'P0001'; end if;
      if jsonb_typeof(v_v) = 'null' then v_st := coalesce(v_st, '{}'::jsonb) - v_k;
      elsif jsonb_typeof(v_v) = 'number' and (v_v::text)::numeric between 1 and 13 and (v_v::text)::numeric = trunc((v_v::text)::numeric) then v_st := coalesce(v_st, '{}'::jsonb) || jsonb_build_object(v_k, (v_v::text)::int);
      else raise exception 'Stufe muss eine Zahl von 1 bis 13 sein' using errcode = 'P0001'; end if;
    end loop;
  end if;
  update schule.lernender set schulart = coalesce(nullif(p_daten->>'schulart',''), schulart),
    klasse = coalesce(nullif(p_daten->>'klasse','')::smallint, klasse),
    stufen = coalesce(v_st, stufen) where id = v_l;
  if not found then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  return jsonb_build_object('ok', true);
end $function$;

do $$
declare d text;
begin
  -- schule_uebersicht: stufen je Kind und die Liste aller Flüge
  d := pg_get_functiondef('api.schule_uebersicht(text, jsonb)'::regprocedure);
  if position('''ist_test'', l.ist_test,' in d) = 0
     or position('declare v_tn bigint; v_leiter boolean; v_l jsonb; v_e jsonb; v_orte jsonb;' in d) = 0
     or position('return jsonb_build_object(''ok'', true, ''leitung'', v_leiter, ''lernende'', v_l, ''einheiten'', v_e, ''orte'', v_orte);' in d) = 0 then
    raise exception 'Stellen in schule_uebersicht nicht gefunden';
  end if;
  d := replace(d, '''ist_test'', l.ist_test,', '''ist_test'', l.ist_test, ''stufen'', l.stufen,');
  d := replace(d, 'declare v_tn bigint; v_leiter boolean; v_l jsonb; v_e jsonb; v_orte jsonb;', 'declare v_tn bigint; v_leiter boolean; v_l jsonb; v_e jsonb; v_orte jsonb; v_th jsonb;');
  d := replace(d, 'return jsonb_build_object(''ok'', true, ''leitung'', v_leiter, ''lernende'', v_l, ''einheiten'', v_e, ''orte'', v_orte);',
    $r$select coalesce(jsonb_agg(jsonb_build_object('thema_id', t.id, 'titel', t.unterthema, 'jahrgang', schule.thema_jahrgang(t.id), 'reihenfolge', t.lehrplan_reihenfolge,
        'block_id', bt.block_id, 'stadt', b.stadt, 'kontinent', k.titel, 'erdteil', k.erdteil,
        'einheit_id', (select e.id from schule.einheit e where e.thema_id = t.id and (e.status in ('geprueft','freigegeben') or (v_leiter and e.status = 'entwurf'))
                        order by (e.status in ('geprueft','freigegeben')) desc, e.version desc limit 1))
      order by k.reihenfolge, b.reihenfolge, bt.reihenfolge), '[]'::jsonb) into v_th
  from schule.thema t
  left join lateral (select x.block_id, x.reihenfolge from schule.block_thema x where x.thema_id = t.id order by x.block_id limit 1) bt on true
  left join schule.block b on b.id = bt.block_id left join schule.kontinent k on k.id = b.kontinent_id
  where t.fach = 'Mathematik';

  return jsonb_build_object('ok', true, 'leitung', v_leiter, 'lernende', v_l, 'einheiten', v_e, 'orte', v_orte, 'themen', v_th);$r$);
  execute d;

  -- schule_plan_lesen: Stufen des Kindes, Lehrplan-Reihenfolge je Flug
  d := pg_get_functiondef('api.schule_plan_lesen(text, jsonb)'::regprocedure);
  if position('''schulart'', v_k.schulart, ''ist_test'', v_k.ist_test)' in d) = 0 or position('''stand'', schule.thema_stand(v_l, t.id),' in d) = 0 then
    raise exception 'Stellen in schule_plan_lesen nicht gefunden';
  end if;
  d := replace(d, '''schulart'', v_k.schulart, ''ist_test'', v_k.ist_test)', '''schulart'', v_k.schulart, ''ist_test'', v_k.ist_test, ''stufen'', v_k.stufen)');
  d := replace(d, '''stand'', schule.thema_stand(v_l, t.id),', '''stand'', schule.thema_stand(v_l, t.id), ''lehrplan_reihenfolge'', t.lehrplan_reihenfolge,');
  execute d;

  -- schule_lernstand: wie viele Bordkarten bis „sitzt“ (erste Versuche ohne Tests bis sitzt_am)
  d := pg_get_functiondef('api.schule_lernstand(text, jsonb)'::regprocedure);
  if position('''faellig'', coalesce(schule.karte_faellig(k), false),' in d) = 0 then raise exception 'Stelle in schule_lernstand nicht gefunden'; end if;
  d := replace(d, '''faellig'', coalesce(schule.karte_faellig(k), false),',
    $r$'faellig', coalesce(schule.karte_faellig(k), false), 'sitzt_am', k.sitzt_am,
              'bis_sitzt', case when k.sitzt_am is null then null else (select count(*) from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                 where v.lernender_id = v_l and a.einheit_id = e.id and a.variante_gruppe = et->>'lernziel' and v.testsitzung_id is null
                   and coalesce(v.versuch_nr, 1) = 1 and v.am <= k.sitzt_am) end,$r$);
  execute d;
end $$;
