-- Bau-Auftrag LM (21.11.), Schritt 1 LM-S (Stand LM-S 2): Daten für die Lehrplan-Matrix „Mathe 5–10“ (Lehrer/Eltern und Kinderseite).
-- Vorgabe: inhalte/AUFTRAEGE.md „Bau-Auftrag LM“ und „Nachbesserung Dreißigste Runde und LM-S (21.11.)“ Teil B, inhalte/pruefung/lehrer/matrix/umsetzung.md (LM-1 bis LM-6).
-- Befund (Live-Text gelesen, 21.11.): api.schule_lehrplan_uebersicht liefert je (Thema × Ort) Titel, Gebiet, Ort, jahrgang, beschreibung, lernbereich, lehrplan,
-- lehrplan_reihenfolge, Etappen-Titel, Inhaltsstand und je Kind stand/stufe/geplant. Es FEHLEN für die Matrix: merke, Etappen mit Pflicht, die Verbindungen aus
-- schule.voraussetzung, Pflicht je Schulart, Beispielaufgabe, „Etappe x von y“, „Fehler offen“ – und ein Zugang für Kinder.
-- Zwei Aktionen (die Übersicht bleibt unverändert, die App 0.83 nutzt sie weiter):
--   api.schule_lehrplan_matrix(schlüssel, daten) – Raster: knappe Themenliste, Verbindungen (ohne Begründung), Gebiete, Kinder, Lernstand. Ziel < 100 KB je Aufruf.
--   api.schule_lehrplan_thema(schlüssel, {thema_id}) – Detail eines Themas: was gefordert, kurz, Ort, merke, Etappen mit Pflicht, Beispiel, Lehrplan-Wortlaut,
--     Verbindungen beider Richtungen mit Begründung, eigenständig (Begründung).
--   Eltern/Lehrer: alle aktiven Kinder (Testkind nur mit daten.mit_testkind = true). Kind: nur es selbst; Kindsicht ohne Lehrplan-Wortlaut, Lernbereiche,
--     Klassen je Schulart, Pflicht-Kennzeichen, Begründungen, eigenständig, Schulart, „Fehler offen“ und ohne andere Kinder.
-- schule.thema.eigenstaendig ist Text (Begründung; null = nicht gekennzeichnet; Spalte kommt mit 20261121_lehrplan_zuordnung_voraussetzungen.sql).
--   Gelesen über to_jsonb(t)->>'eigenstaendig', damit diese Datei auch vor jener Migration läuft (dann überall null).
-- Nicht ausgeführt – der Haupt-Chat spielt ein (dazu lernen-api 0.8.0). Kein DROP, kein DELETE, keine Bestandsänderung. Wiederholt ausführbar.

-- Zeile (Klasse) eines Themas für eine Schulart: eigene Klasse, sonst die der anderen bayerischen Schulart, sonst IB-MYP-Jahr + 5 (Annahme MYP 1 ≈ Kl. 6)
create or replace function schule.thema_klasse_fuer(p_jahrgang jsonb, p_sa text)
 returns jsonb language sql immutable set search_path to ''
as $function$
  select case
    when p_jahrgang ? p_sa and p_sa <> 'ib_myp' then jsonb_build_object('klasse', (p_jahrgang->>p_sa)::int)
    when p_sa = 'ib_myp' and p_jahrgang ? 'ib_myp' then jsonb_build_object('klasse', (p_jahrgang->>'ib_myp')::int + 5)
    when p_jahrgang ? (case p_sa when 'gym_by' then 'rs_by' else 'gym_by' end) then jsonb_build_object('klasse', (p_jahrgang->>(case p_sa when 'gym_by' then 'rs_by' else 'gym_by' end))::int, 'eingeordnet', true)
    when p_jahrgang ? 'gym_by' then jsonb_build_object('klasse', (p_jahrgang->>'gym_by')::int, 'eingeordnet', true)
    when p_jahrgang ? 'ib_myp' then jsonb_build_object('klasse', (p_jahrgang->>'ib_myp')::int + 5, 'eingeordnet', true)
    else jsonb_build_object('eingeordnet', true) end;
$function$;

-- Raster (knapp). Lernstand: nur die Felder, die die Matrix zeigt; null und false sind weggelassen (fehlt = nein).
create or replace function schule.lehrplan_matrix(p_kinder bigint[], p_kindsicht boolean)
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare v_themen jsonb; v_vb jsonb; v_geb jsonb; v_kinder jsonb; v_stand jsonb; v_sa text;
begin
  if p_kindsicht then select coalesce(l.schulart, 'gym_by') into v_sa from schule.lernender l where l.id = p_kinder[1]; end if;

  select coalesce(jsonb_agg(x.j order by x.gr, x.tr, x.id), '[]'::jsonb) into v_themen from (
    select t.id, coalesce(k.reihenfolge, 999) gr, coalesce(t.reihenfolge, 0) tr,
      jsonb_strip_nulls(jsonb_build_object(
        'thema_id', t.id, 'schluessel', t.schluessel, 'titel', t.unterthema, 'gebiet_id', k.id, 'block_id', b.id,
        'jahrgang', case when p_kindsicht then null else schule.thema_jahrgang(t.id) end,
        'lehrplan_reihenfolge', case when p_kindsicht then null else t.lehrplan_reihenfolge end,
        'lernbereich', case when p_kindsicht then null else t.lernbereich end,
        'pflicht', case when p_kindsicht then null else (select coalesce(jsonb_agg(distinct ql.schulart), '[]'::jsonb) from schule.zuordnung z join schule.eintrag e on e.id = z.eintrag_id
                      join schule.quelle ql on ql.id = e.quelle_id where z.thema_id = t.id and ql.aktiv and ql.rolle = 'basis' and not coalesce(e.archiviert, false)) end,
        'eigenstaendig', case when not p_kindsicht and to_jsonb(t)->>'eigenstaendig' is not null then true end,  -- Begründung im Detail
        'zeile', case when p_kindsicht then schule.thema_klasse_fuer(schule.thema_jahrgang(t.id), v_sa) end,
        'reihenfolge_kind', case when p_kindsicht then (t.lehrplan_reihenfolge->>v_sa)::int end,
        'einheit_id', ein.id,
        'ohne_flug', case when ein.id is null then true end,                     -- keine freigegebene Einheit (z. B. aufgelöster Entwurf)
        'etappen_anzahl', case when ein.id is not null then jsonb_array_length(coalesce(ein.inhalt->'etappen', '[]'::jsonb)) end
      )) j
    from schule.thema t
    left join lateral (select bt2.block_id from schule.block_thema bt2 join schule.block b2 on b2.id = bt2.block_id where bt2.thema_id = t.id
                        order by b2.reihenfolge, bt2.reihenfolge limit 1) bt on true
    left join schule.block b on b.id = bt.block_id
    left join schule.kontinent k on k.id = b.kontinent_id
    left join schule.einheit ein on ein.id = schule.thema_einheit(t.id)
    where t.fach = 'Mathematik') x;

  -- Verbindungen als [thema_id, braucht_id, art] (art h = hart, e = empfohlen): „thema_id braucht braucht_id“. Begründung im Detail.
  select coalesce(jsonb_agg(jsonb_build_array(v.thema_id, v.braucht_id, case v.art when 'hart' then 'h' else 'e' end) order by v.thema_id, v.braucht_id), '[]'::jsonb)
    into v_vb from schule.voraussetzung v join schule.thema ta on ta.id = v.thema_id and ta.fach = 'Mathematik' join schule.thema tb on tb.id = v.braucht_id and tb.fach = 'Mathematik';

  select coalesce(jsonb_agg(jsonb_build_object('gebiet_id', k.id, 'titel', k.titel, 'reihenfolge', k.reihenfolge, 'zusatz', coalesce(k.zusatz, false)) order by k.reihenfolge), '[]'::jsonb)
    into v_geb from schule.kontinent k where coalesce(k.fach, 'Mathematik') = 'Mathematik';

  select coalesce(jsonb_agg(jsonb_strip_nulls(jsonb_build_object('id', l.id, 'name', l.anzeigename, 'klasse', l.klasse, 'schulart', case when p_kindsicht then null else l.schulart end)) order by l.id), '[]'::jsonb)
    into v_kinder from schule.lernender l where l.id = any(p_kinder);

  -- je Kind und Thema: thema_stufe ohne etappen/gesetzt/ohne_test/wdh_stufe_min, dazu etappe_jetzt (nur „dran“) und – Lehrer – fehler_offen
  select coalesce(jsonb_object_agg(l.id, (
           select coalesce(jsonb_object_agg(t.id, (
               select coalesce(jsonb_object_agg(f.key, f.value), '{}'::jsonb) from jsonb_each(
                 (s.st - array['etappen', 'gesetzt', 'ohne_test', 'wdh_stufe_min'])
                 || jsonb_build_object('etappe_jetzt', case when s.st->>'stufe' = 'dran' then least(coalesce((s.st->>'gelandet')::int, 0) + 1, greatest(coalesce((s.st->>'etappen')::int, 1), 1)) end)
                 || case when p_kindsicht then '{}'::jsonb else jsonb_build_object('fehler_offen', exists (select 1 from schule.lernziel_stand ls
                      where ls.lernender_id = l.id and ls.einheit_id = schule.thema_einheit(t.id) and ls.pflicht and ls.status = 'fehler')) end) f
               where f.value not in ('null'::jsonb, 'false'::jsonb))), '{}'::jsonb)
             from schule.thema t cross join lateral (select schule.thema_stufe(l.id, t.id) st) s where t.fach = 'Mathematik')), '{}'::jsonb)
    into v_stand from schule.lernender l where l.id = any(p_kinder);

  return jsonb_build_object('ok', true, 'kindsicht', p_kindsicht, 'themen', v_themen, 'verbindungen', v_vb,
    'gebiete', v_geb, 'kinder', v_kinder, 'lernstand', v_stand);
end $function$;
comment on function schule.lehrplan_matrix(bigint[], boolean) is 'LM-S: Raster der Lehrplan-Matrix (knappe Themen, Verbindungen, Gebiete, Kinder, Lernstand); Detail: schule.lehrplan_thema';

-- Detail eines Themas (beim Antippen nachladen)
create or replace function schule.lehrplan_thema(p_thema bigint, p_kindsicht boolean)
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare v_t schule.thema; v_ein schule.einheit; v_ort text;
begin
  select * into v_t from schule.thema t where t.id = p_thema and t.fach = 'Mathematik';
  if v_t.id is null then raise exception 'Thema nicht gefunden' using errcode = 'P0001'; end if;
  select * into v_ein from schule.einheit e where e.id = schule.thema_einheit(p_thema);
  select b.stadt into v_ort from schule.block_thema bt join schule.block b on b.id = bt.block_id where bt.thema_id = p_thema order by b.reihenfolge, bt.reihenfolge limit 1;
  return jsonb_strip_nulls(jsonb_build_object('ok', true, 'kindsicht', p_kindsicht,
    'thema_id', v_t.id, 'titel', v_t.unterthema, 'kurz', v_t.kurz, 'ort', v_ort,
    'was_gefordert', v_t.beschreibung,                                             -- „Was gefordert ist“
    'lehrplan', case when p_kindsicht then null else v_t.lehrplan end,             -- Lehrplan-Wortlaut je Schulart
    'eigenstaendig', case when p_kindsicht then null else to_jsonb(v_t)->>'eigenstaendig' end, -- Begründung (gesetzt ⇒ eigenständig)
    'ohne_flug', case when v_ein.id is null then true end,
    'einheit_id', v_ein.id,
    'merke', v_ein.inhalt->'merke',                                                -- „Das muss sitzen“
    'etappen', case when v_ein.id is not null then (select coalesce(jsonb_agg(jsonb_strip_nulls(jsonb_build_object('lernziel', et.x->>'lernziel', 'titel', et.x->>'titel',
                  'pflicht', case when p_kindsicht then null else coalesce(v_ein.inhalt->'bewertung'->'lernziele_pflicht', '[]'::jsonb) ? (et.x->>'lernziel') end)) order by et.nr), '[]'::jsonb)
                  from jsonb_array_elements(coalesce(v_ein.inhalt->'etappen', '[]'::jsonb)) with ordinality et(x, nr)) end,
    'beispiel', (select q.f from (select a.frage->>'text' f, a.reihenfolge, a.id from schule.aufgabe a
                  where a.einheit_id = v_ein.id and a.pool = 'uebung' and a.freigegeben) q where length(q.f) < 160 order by q.reihenfolge, q.id limit 1),
    -- Verbindungen beider Richtungen („Braucht vorher“, „Darauf baut auf“); „weiter zurück“ rechnet die App aus dem Raster
    'braucht', (select coalesce(jsonb_agg(jsonb_strip_nulls(jsonb_build_object('thema_id', v.braucht_id, 'titel', tb.unterthema, 'art', v.art,
                  'begruendung', case when p_kindsicht then null else v.begruendung end)) order by v.braucht_id), '[]'::jsonb)
                  from schule.voraussetzung v join schule.thema tb on tb.id = v.braucht_id and tb.fach = 'Mathematik' where v.thema_id = p_thema),
    'baut_darauf', (select coalesce(jsonb_agg(jsonb_strip_nulls(jsonb_build_object('thema_id', v.thema_id, 'titel', ta.unterthema, 'art', v.art,
                  'begruendung', case when p_kindsicht then null else v.begruendung end)) order by v.thema_id), '[]'::jsonb)
                  from schule.voraussetzung v join schule.thema ta on ta.id = v.thema_id and ta.fach = 'Mathematik' where v.braucht_id = p_thema)));
end $function$;
comment on function schule.lehrplan_thema(bigint, boolean) is 'LM-S: Detail eines Themas der Lehrplan-Matrix (Wortlaut, merke, Etappen, Beispiel, Verbindungen mit Begründung); Kindsicht ohne Lehrer-Felder';

-- Zugang für beide Aktionen: Eltern/Lehrer → null (Lehrer-Sicht); Kind (Lern-Zugang) → es selbst; sonst daten.lernender_id + schule.zugriff
create or replace function schule.lehrplan_sicht(p_schluessel text, p_daten jsonb)
 returns bigint language plpgsql security definer set search_path to ''
as $function$
declare v_l bigint := nullif(p_daten->>'lernender_id', '')::bigint;
begin
  perform schule.wer_tn(p_schluessel);
  if schule.ist_leiter(p_schluessel) then return null; end if;
  if schule.ist_lern(p_schluessel) then select i.lernender_id into v_l from schule.lern_ich(p_schluessel) i; end if;
  if v_l is null then raise exception 'Kind fehlt' using errcode = 'P0001'; end if;
  perform schule.zugriff(p_schluessel, v_l);
  return v_l;
end $function$;
revoke all on function schule.lehrplan_sicht(text, jsonb) from public, anon, authenticated;

create or replace function api.schule_lehrplan_matrix(p_schluessel text, p_daten jsonb default null)
 returns jsonb language plpgsql security definer set search_path to ''  -- nicht stable: ruft schule.zugriff (volatile)
as $function$
declare v_l bigint; v_kinder bigint[];
begin
  v_l := schule.lehrplan_sicht(p_schluessel, p_daten);
  if v_l is null then
    select coalesce(array_agg(l.id order by l.id), '{}') into v_kinder from schule.lernender l
     where l.aktiv and (not l.ist_test or coalesce((p_daten->>'mit_testkind')::boolean, false));
    return schule.lehrplan_matrix(v_kinder, false);
  end if;
  return schule.lehrplan_matrix(array[v_l], true);
end $function$;
grant execute on function api.schule_lehrplan_matrix(text, jsonb) to council_mcp;
revoke all on function api.schule_lehrplan_matrix(text, jsonb) from public, anon, authenticated;

create or replace function api.schule_lehrplan_thema(p_schluessel text, p_daten jsonb default null)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_th bigint := nullif(p_daten->>'thema_id', '')::bigint; v_kind boolean;
begin
  v_kind := schule.lehrplan_sicht(p_schluessel, p_daten) is not null;   -- Zugang zuerst prüfen
  if v_th is null then raise exception 'thema_id fehlt' using errcode = 'P0001'; end if;
  return schule.lehrplan_thema(v_th, v_kind);
end $function$;
grant execute on function api.schule_lehrplan_thema(text, jsonb) to council_mcp;
revoke all on function api.schule_lehrplan_thema(text, jsonb) from public, anon, authenticated;
