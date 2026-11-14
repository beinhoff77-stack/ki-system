-- W150 (Claude): Jahrgang je Schulart, Zielschulart je Kind, Themenplan nur aus Eltern-/Lehrer-Entscheidungen,
-- Lehrer-Ansicht „Inhalte prüfen“, Lehrplan-Übersicht und Rückmeldungen direkt in die Werkstatt.

alter table schule.lernender add column if not exists schulart text not null default 'gym_by' check (schulart in ('gym_by','rs_by','ib_myp'));

-- Jahrgang eines Themas je Schulart (früheste Basis-Zuordnung im Lehrplan). IB: MYP-Jahr.
create or replace function schule.thema_jahrgang(p_thema bigint) returns jsonb
language sql stable set search_path to '' as $$
  select coalesce(jsonb_object_agg(x.schulart, x.jahr), '{}'::jsonb) from (
    select q.schulart, min(q.jahr_von) jahr from schule.zuordnung z join schule.eintrag e on e.id = z.eintrag_id join schule.quelle q on q.id = e.quelle_id
     where z.thema_id = p_thema and q.aktiv and q.rolle = 'basis' and not e.archiviert group by q.schulart) x;
$$;

-- Stand eines Themas für ein Kind: erledigt / laeuft / offen / keine_einheit
create or replace function schule.thema_stand(p_l bigint, p_thema bigint) returns text
language sql stable set search_path to '' as $$
  with e as (select id from schule.einheit where thema_id = p_thema and status in ('geprueft','freigegeben') order by version desc limit 1)
  select case when not exists (select 1 from e) then 'keine_einheit'
    when exists (select 1 from schule.lernziel_stand s join e on e.id = s.einheit_id where s.lernender_id = p_l)
      and not exists (select 1 from schule.lernziel_stand s join e on e.id = s.einheit_id where s.lernender_id = p_l and s.pflicht and s.status not in ('nachgewiesen','korrigiert','gesichert'))
      then 'erledigt'
    when exists (select 1 from schule.karte_stand k join e on e.id = k.einheit_id where k.lernender_id = p_l)
      or exists (select 1 from schule.lernziel_stand s join e on e.id = s.einheit_id where s.lernender_id = p_l and s.status <> 'offen') then 'laeuft'
    else 'offen' end;
$$;

-- Plan = nur Einträge, die Eltern oder Lehrer gesetzt haben. Die automatische Vorschlagsroute (Claude, 9.11.) zählt nicht.
create or replace function schule.ist_plan(r schule.route) returns boolean
language sql immutable as $$ select r.art = 'normal' and r.status <> 'entfernt' and coalesce(r.geaendert_von, '') not in ('claude', 'system') $$;

do $$
declare d text;
begin
  -- Übersicht: Route ohne Vorschlagsroute; Jahrgang je Einheit/Ort; Zielschulart je Kind
  select pg_get_functiondef('api.schule_uebersicht(text, jsonb)'::regprocedure) into d;
  d := replace(d, $x$from schule.route r where r.lernender_id = l.id),$x$,
    $x$from schule.route r where r.lernender_id = l.id and (r.art <> 'normal' or schule.ist_plan(r) or r.status = 'fertig' or r.kann_schon)),$x$);
  d := replace(d, $x$'pflicht_anzahl', jsonb_array_length$x$, $x$'jahrgang', schule.thema_jahrgang(e.thema_id), 'pflicht_anzahl', jsonb_array_length$x$);
  d := replace(d, $x$'id', l.id, 'name', l.anzeigename, 'klasse', l.klasse,$x$, $x$'id', l.id, 'name', l.anzeigename, 'klasse', l.klasse, 'schulart', l.schulart,$x$);
  if position('schule.ist_plan(r)' in d) = 0 or position('thema_jahrgang' in d) = 0 or position('''schulart''' in d) = 0 then raise exception 'uebersicht nicht angepasst'; end if;
  execute d;
end $$;

-- Themenplan lesen: Plan (nur Eltern/Lehrer), alle Orte mit Themen, Jahrgang je Schulart und Stand des Kindes
create or replace function api.schule_plan_lesen(p_schluessel text, p_daten jsonb) returns jsonb
language plpgsql stable security definer set search_path to '' as $$
declare v_l bigint := nullif(p_daten->>'lernender_id','')::bigint; v_k schule.lernender;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  select * into v_k from schule.lernender where id = v_l and aktiv;
  if v_k.id is null then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  return jsonb_build_object('ok', true,
    'kind', jsonb_build_object('id', v_k.id, 'name', v_k.anzeigename, 'klasse', v_k.klasse, 'schulart', v_k.schulart, 'ist_test', v_k.ist_test),
    'revision', (select coalesce(max(r.revision), 0) from schule.route r where r.lernender_id = v_l and r.art = 'normal'),
    'plan', (select coalesce(jsonb_agg(jsonb_build_object('block_id', r.block_id, 'position', r.position, 'art', r.art, 'status', r.status,
                 'kann_schon', r.kann_schon, 'geaendert_von', r.geaendert_von, 'geaendert_am', r.geaendert_am) order by r.art = 'normal', r.position), '[]'::jsonb)
             from schule.route r where r.lernender_id = v_l and (schule.ist_plan(r) or (r.art = 'rueckreise' and r.status not in ('fertig','entfernt')))),
    'kann_schon', (select coalesce(jsonb_agg(r.block_id), '[]'::jsonb) from schule.route r where r.lernender_id = v_l and r.kann_schon and r.status <> 'entfernt'),
    'orte', (select coalesce(jsonb_agg(jsonb_build_object('block_id', b.id, 'titel', b.titel, 'stadt', b.stadt, 'kontinent', k.titel, 'kontinent_id', k.id,
                 'reihenfolge', b.reihenfolge,
                 'themen', (select coalesce(jsonb_agg(jsonb_build_object('thema_id', t.id, 'titel', t.unterthema, 'jahrgang', schule.thema_jahrgang(t.id),
                                 'stand', schule.thema_stand(v_l, t.id),
                                 'einheit', (select jsonb_build_object('id', e.id, 'status', e.status,
                                                'karten', jsonb_array_length(coalesce(e.inhalt->'etappen','[]'::jsonb)),
                                                'aufgaben', (select count(*) from schule.aufgabe a where a.einheit_id = e.id),
                                                'neu', (select count(*) from schule.aufgabe a where a.einheit_id = e.id and not a.freigegeben))
                                             from schule.einheit e where e.thema_id = t.id order by (e.status in ('geprueft','freigegeben')) desc, e.version desc limit 1))
                               order by bt.reihenfolge, t.reihenfolge), '[]'::jsonb)
                            from schule.block_thema bt join schule.thema t on t.id = bt.thema_id where bt.block_id = b.id))
               order by k.reihenfolge, b.reihenfolge), '[]'::jsonb)
             from schule.block b left join schule.kontinent k on k.id = b.kontinent_id where b.fach = 'Mathematik'),
    'notizen', (select coalesce(jsonb_agg(jsonb_build_object('id', n.id, 'text', n.text, 'von', n.von, 'am', n.am) order by n.am desc), '[]'::jsonb)
                from (select * from schule.notiz where lernender_id = v_l order by am desc limit 30) n),
    'verlauf', (select coalesce(jsonb_agg(jsonb_build_object('akteur', a.akteur, 'anlass', a.anlass, 'ereignis', a.ereignis, 'am', a.am) order by a.am desc), '[]'::jsonb)
                from (select * from schule.route_aenderung where lernender_id = v_l order by am desc limit 20) a));
end $$;

-- Zielschulart je Kind setzen (Eltern/Lehrer)
create or replace function api.schule_kind_setzen(p_schluessel text, p_daten jsonb) returns jsonb
language plpgsql security definer set search_path to '' as $$
declare v_l bigint := nullif(p_daten->>'lernender_id','')::bigint;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  update schule.lernender set schulart = coalesce(nullif(p_daten->>'schulart',''), schulart),
    klasse = coalesce(nullif(p_daten->>'klasse','')::smallint, klasse) where id = v_l;
  if not found then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  return jsonb_build_object('ok', true);
end $$;

-- Inhalte prüfen: Einheit mit allen Lernkarten und allen Aufgaben samt Lösung (nur Eltern/Lehrer, nur lesen)
create or replace function api.schule_inhalt_lesen(p_schluessel text, p_daten jsonb) returns jsonb
language plpgsql stable security definer set search_path to '' as $$
declare v_e bigint := nullif(p_daten->>'einheit_id','')::bigint; e schule.einheit;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  select * into e from schule.einheit where id = v_e;
  if e.id is null then raise exception 'Einheit nicht gefunden' using errcode = 'P0001'; end if;
  return jsonb_build_object('ok', true, 'einheit_id', e.id, 'status', e.status, 'version', e.version,
    'ort', (select jsonb_build_object('stadt', b.stadt, 'titel', b.titel) from schule.block b where b.id = e.block_id),
    'thema', (select jsonb_build_object('titel', t.unterthema, 'jahrgang', schule.thema_jahrgang(t.id)) from schule.thema t where t.id = e.thema_id),
    'inhalt', e.inhalt - 'pruefhinweise',
    'aufgaben', (select coalesce(jsonb_agg(jsonb_build_object('id', a.id, 'lernziel', a.variante_gruppe, 'pool', a.pool, 'stufe', a.stufe, 'antworttyp', a.antworttyp,
                   'frage', a.frage, 'antworten', a.antworten, 'loesung', a.loesung, 'tipp', a.tipp, 'loesungsweg', a.loesungsweg, 'freigegeben', a.freigegeben)
                 order by a.variante_gruppe, a.pool = 'uebung' desc, a.pool, a.stufe nulls last, a.reihenfolge), '[]'::jsonb) from schule.aufgabe a where a.einheit_id = e.id),
    'rueckmeldungen', (select coalesce(jsonb_agg(jsonb_build_object('id', r.id, 'art', r.art, 'text', r.text, 'status', r.status, 'antwort', r.antwort,
                   'lernziel', r.lernziel, 'aufgabe_id', r.aufgabe_id, 'am', r.am) order by r.am desc), '[]'::jsonb) from schule.rueckmeldung r where r.einheit_id = e.id));
end $$;

-- Rückmeldungen landen sofort als Werkstatt-Nachricht bei Claude (Wunsch 150).
create or replace function schule.rueckmeldung_an_werkstatt() returns trigger
language plpgsql security definer set search_path to '' as $$
declare v_ort text; v_auf text;
begin
  select coalesce(b.stadt, '') || ' – ' || b.titel into v_ort from schule.block b where b.id = new.block_id;
  select a.frage->>'text' into v_auf from schule.aufgabe a where a.id = new.aufgabe_id;
  insert into werkstatt.nachrichten (wunsch_id, von_id, an_id, art, text)
  values (150, (select id from council.teilnehmer where name = 'Sebastian (App)' limit 1), (select id from council.teilnehmer where name = 'Claude (App)' limit 1), 'info',
    'RÜCKMELDUNG LERN-APP #' || new.id || ' von ' || new.von || ' – ' || new.art || E'\n' || new.text ||
    coalesce(E'\nOrt: ' || v_ort, '') || coalesce(' · Einheit ' || new.einheit_id, '') || coalesce(' · Lernkarte ' || new.lernziel, '') ||
    coalesce(E'\nAufgabe #' || new.aufgabe_id || ': ' || v_auf, '') ||
    E'\nBeantworten: update schule.rueckmeldung set status, antwort (sichtbar in der App unter Rückmeldungen).');
  return new;
end $$;
drop trigger if exists rueckmeldung_an_werkstatt on schule.rueckmeldung;
create trigger rueckmeldung_an_werkstatt after insert on schule.rueckmeldung for each row execute function schule.rueckmeldung_an_werkstatt();

grant execute on function api.schule_kind_setzen(text, jsonb), api.schule_inhalt_lesen(text, jsonb) to council_mcp;
revoke all on function api.schule_kind_setzen(text, jsonb), api.schule_inhalt_lesen(text, jsonb) from public, anon, authenticated;
