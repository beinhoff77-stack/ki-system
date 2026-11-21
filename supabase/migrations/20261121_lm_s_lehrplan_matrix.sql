-- Bau-Auftrag LM (21.11.), Schritt 1 LM-S: Daten für die Lehrplan-Matrix „Mathe 5–10“ (Lehrer/Eltern und Kinderseite) in einem Aufruf.
-- Vorgabe: inhalte/AUFTRAEGE.md „Bau-Auftrag LM“, inhalte/pruefung/lehrer/matrix/umsetzung.md (LM-1 bis LM-6).
-- Befund (Live-Text gelesen, 21.11.): api.schule_lehrplan_uebersicht liefert je (Thema × Ort) Titel, Gebiet, Ort, jahrgang, beschreibung, lernbereich, lehrplan,
-- lehrplan_reihenfolge, Etappen-Titel (gliederung), Inhaltsstand und je Kind stand/stufe/geplant. Es FEHLEN für die Matrix: merke („Das muss sitzen“),
-- Etappen mit Pflicht, die Verbindungen aus schule.voraussetzung (Art, Begründung), kurz, Gebiet-Reihenfolge, Pflicht je Schulart, Beispielaufgabe,
-- „Etappe x von y“, „Fehler offen“ – und ein Zugang für Kinder (die Übersicht ist nur für Eltern/Lehrer).
-- Neu (die Übersicht bleibt unverändert, die App 0.83 nutzt sie weiter):
--   schule.lehrplan_matrix(p_kinder bigint[], p_kindsicht boolean) – innere Funktion (Rauchtest), liefert themen, verbindungen, gebiete, kinder, lernstand.
--   api.schule_lehrplan_matrix(schlüssel, daten) – Eltern/Lehrer: alle aktiven Kinder (Testkind nur mit daten.mit_testkind = true);
--     Kind (Lern-Zugang ohne Eltern-/Lehrer-Rolle oder sonstiger Zugang): nur das eigene Kind (daten.lernender_id, schule.zugriff), Kindsicht:
--     ohne Lehrplan-Wortlaut, ohne Lernbereiche, ohne Klassen je Schulart, ohne Pflicht-Kennzeichen, ohne Begründungen, ohne andere Kinder.
-- Funktioniert mit dem heutigen Stand von schule.voraussetzung (70 Verbindungen, Arten hart/empfohlen); fehlt eine Verbindung, ist die Liste leer.
-- Nicht ausgeführt – der Haupt-Chat spielt ein (dazu lernen-api: Aktion schule_lehrplan_matrix). Kein DROP, kein DELETE, keine Bestandsänderung. Wiederholt ausführbar.

-- Zeile (Klasse) eines Themas für eine Schulart: eigene Klasse, sonst die der anderen bayerischen Schulart, sonst IB-MYP-Jahr + 5 (Annahme MYP 1 ≈ Kl. 6)
create or replace function schule.thema_klasse_fuer(p_jahrgang jsonb, p_sa text)
 returns jsonb language sql immutable set search_path to ''
as $function$
  select case
    when p_jahrgang ? p_sa and p_sa <> 'ib_myp' then jsonb_build_object('klasse', (p_jahrgang->>p_sa)::int, 'eingeordnet', false)
    when p_sa = 'ib_myp' and p_jahrgang ? 'ib_myp' then jsonb_build_object('klasse', (p_jahrgang->>'ib_myp')::int + 5, 'eingeordnet', false)
    when p_jahrgang ? (case p_sa when 'gym_by' then 'rs_by' else 'gym_by' end) then jsonb_build_object('klasse', (p_jahrgang->>(case p_sa when 'gym_by' then 'rs_by' else 'gym_by' end))::int, 'eingeordnet', true)
    when p_jahrgang ? 'gym_by' then jsonb_build_object('klasse', (p_jahrgang->>'gym_by')::int, 'eingeordnet', true)
    when p_jahrgang ? 'ib_myp' then jsonb_build_object('klasse', (p_jahrgang->>'ib_myp')::int + 5, 'eingeordnet', true)
    else jsonb_build_object('klasse', null, 'eingeordnet', true) end;
$function$;

create or replace function schule.lehrplan_matrix(p_kinder bigint[], p_kindsicht boolean)
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare v_themen jsonb; v_vb jsonb; v_geb jsonb; v_kinder jsonb; v_stand jsonb; v_sa text;
begin
  -- für die Kindsicht: Schulart des Kindes (Zeile je Thema), keine Kennzeichen je Schulart
  if p_kindsicht then select coalesce(l.schulart, 'gym_by') into v_sa from schule.lernender l where l.id = p_kinder[1]; end if;

  select coalesce(jsonb_agg(x.j order by x.gr, x.tr, x.id), '[]'::jsonb) into v_themen from (
    select t.id, coalesce(k.reihenfolge, 999) gr, coalesce(t.reihenfolge, 0) tr,
      jsonb_strip_nulls(jsonb_build_object(
        'thema_id', t.id, 'schluessel', t.schluessel, 'titel', t.unterthema, 'kurz', t.kurz,
        'gebiet', k.titel, 'gebiet_id', k.id, 'ort', b.stadt, 'block_id', b.id,
        'was_gefordert', t.beschreibung,                                           -- „Was gefordert ist“ (umfang)
        'jahrgang', case when p_kindsicht then null else schule.thema_jahrgang(t.id) end,
        'lehrplan_reihenfolge', case when p_kindsicht then null else t.lehrplan_reihenfolge end,
        'lernbereich', case when p_kindsicht then null else t.lernbereich end,
        'lehrplan', case when p_kindsicht then null else t.lehrplan end,           -- Lehrplan-Wortlaut je Schulart
        -- Pflicht je Schulart: Thema ist einem Eintrag einer Basis-Quelle (Lehrplan) dieser Schulart zugeordnet
        'pflicht', case when p_kindsicht then null else (select coalesce(jsonb_agg(distinct ql.schulart), '[]'::jsonb) from schule.zuordnung z join schule.eintrag e on e.id = z.eintrag_id
                      join schule.quelle ql on ql.id = e.quelle_id where z.thema_id = t.id and ql.aktiv and ql.rolle = 'basis' and not coalesce(e.archiviert, false)) end,
        'zeile', case when p_kindsicht then schule.thema_klasse_fuer(schule.thema_jahrgang(t.id), v_sa) end, -- Kindsicht: Klasse für die Schulart des Kindes
        'reihenfolge_kind', case when p_kindsicht then (t.lehrplan_reihenfolge->>v_sa)::int end,
        'eigenstaendig', case when p_kindsicht then null else to_jsonb(t)->'eigenstaendig' end, -- noch keine Spalte: bleibt leer, bis schule.thema.eigenstaendig eingeführt ist (Vorschlag im Bericht)
        'einheit_id', ein.id,
        'merke', ein.inhalt->'merke',                                              -- „Das muss sitzen“
        'etappen', (select coalesce(jsonb_agg(jsonb_build_object('lernziel', et.x->>'lernziel', 'titel', et.x->>'titel',
                      'pflicht', coalesce(ein.inhalt->'bewertung'->'lernziele_pflicht', '[]'::jsonb) ? (et.x->>'lernziel')) order by et.nr), '[]'::jsonb)
                      from jsonb_array_elements(coalesce(ein.inhalt->'etappen', '[]'::jsonb)) with ordinality et(x, nr)),
        'beispiel', (select q.f from (select a.frage->>'text' f, a.reihenfolge, a.id from schule.aufgabe a
                      where a.einheit_id = ein.id and a.pool = 'uebung' and a.freigegeben) q where length(q.f) < 160 order by q.reihenfolge, q.id limit 1)
      )) j
    from schule.thema t
    left join lateral (select bt2.block_id from schule.block_thema bt2 join schule.block b2 on b2.id = bt2.block_id where bt2.thema_id = t.id
                        order by b2.reihenfolge, bt2.reihenfolge limit 1) bt on true
    left join schule.block b on b.id = bt.block_id
    left join schule.kontinent k on k.id = b.kontinent_id
    left join schule.einheit ein on ein.id = schule.thema_einheit(t.id)        -- nur die freigegebene Einheit
    where t.fach = 'Mathematik') x;

  -- Verbindungen: thema_id braucht braucht_id (Art hart/empfohlen). Kindsicht ohne Begründung.
  select coalesce(jsonb_agg(jsonb_strip_nulls(jsonb_build_object('thema_id', v.thema_id, 'braucht_id', v.braucht_id, 'art', v.art,
           'begruendung', case when p_kindsicht then null else v.begruendung end)) order by v.thema_id, v.braucht_id), '[]'::jsonb)
    into v_vb from schule.voraussetzung v join schule.thema a on a.id = v.thema_id and a.fach = 'Mathematik' join schule.thema b on b.id = v.braucht_id and b.fach = 'Mathematik';

  select coalesce(jsonb_agg(jsonb_build_object('gebiet_id', k.id, 'titel', k.titel, 'reihenfolge', k.reihenfolge, 'zusatz', coalesce(k.zusatz, false)) order by k.reihenfolge), '[]'::jsonb)
    into v_geb from schule.kontinent k where coalesce(k.fach, 'Mathematik') = 'Mathematik';

  select coalesce(jsonb_agg(jsonb_strip_nulls(jsonb_build_object('id', l.id, 'name', l.anzeigename, 'klasse', l.klasse, 'schulart', case when p_kindsicht then null else l.schulart end)) order by l.id), '[]'::jsonb)
    into v_kinder from schule.lernender l where l.id = any(p_kinder);

  -- Lernstand je Kind und Thema: Stufe (thema_stufe: stufe, zeichen, gesetzt, im_plan, etappen, begonnen, gelandet, sicher, wieder_offen, wdh_nr, naechste_in …),
  -- dazu etappe_jetzt („Etappe x von y“ beim ▶-Thema) und – nur Eltern/Lehrer – fehler_offen (eine Pflicht-Etappe steht nach einem Test auf „fehler“)
  select coalesce(jsonb_object_agg(l.id, (
           select coalesce(jsonb_object_agg(t.id, s.st
             || jsonb_build_object('etappe_jetzt', case when s.st->>'stufe' = 'dran' then least(coalesce((s.st->>'gelandet')::int, 0) + 1, greatest(coalesce((s.st->>'etappen')::int, 1), 1)) end)
             || case when p_kindsicht then '{}'::jsonb else jsonb_build_object('fehler_offen', exists (select 1 from schule.lernziel_stand ls
                  where ls.lernender_id = l.id and ls.einheit_id = schule.thema_einheit(t.id) and ls.pflicht and ls.status = 'fehler')) end), '{}'::jsonb)
             from schule.thema t cross join lateral (select schule.thema_stufe(l.id, t.id) st) s where t.fach = 'Mathematik')), '{}'::jsonb)
    into v_stand from schule.lernender l where l.id = any(p_kinder);

  return jsonb_build_object('ok', true, 'kindsicht', p_kindsicht, 'themen', v_themen, 'verbindungen', v_vb,
    'gebiete', v_geb, 'kinder', v_kinder, 'lernstand', v_stand);
end $function$;
comment on function schule.lehrplan_matrix(bigint[], boolean) is 'LM-S: Daten der Lehrplan-Matrix (Themen, Verbindungen, Gebiete, Kinder, Lernstand je Kind); Kindsicht ohne Lehrplan-Wortlaut und Kennzeichen';

create or replace function api.schule_lehrplan_matrix(p_schluessel text, p_daten jsonb default null)
 returns jsonb language plpgsql security definer set search_path to ''  -- nicht stable: ruft schule.zugriff (volatile)
as $function$
declare v_l bigint := nullif(p_daten->>'lernender_id', '')::bigint; v_kinder bigint[];
begin
  perform schule.wer_tn(p_schluessel);
  if schule.ist_leiter(p_schluessel) then
    -- Eltern/Lehrer: alle aktiven Kinder (wie die Lehrplan-Übersicht); das Testkind nur auf ausdrücklichen Wunsch (App-Tests mit erfundenen Daten)
    select coalesce(array_agg(l.id order by l.id), '{}') into v_kinder from schule.lernender l
     where l.aktiv and (not l.ist_test or coalesce((p_daten->>'mit_testkind')::boolean, false));
    return schule.lehrplan_matrix(v_kinder, false);
  end if;
  -- Kind: nur sich selbst
  if schule.ist_lern(p_schluessel) then
    select i.lernender_id into v_l from schule.lern_ich(p_schluessel) i;
  end if;
  if v_l is null then raise exception 'Kind fehlt' using errcode = 'P0001'; end if;
  perform schule.zugriff(p_schluessel, v_l);
  return schule.lehrplan_matrix(array[v_l], true);
end $function$;
grant execute on function api.schule_lehrplan_matrix(text, jsonb) to council_mcp;
revoke all on function api.schule_lehrplan_matrix(text, jsonb) from public, anon, authenticated;
