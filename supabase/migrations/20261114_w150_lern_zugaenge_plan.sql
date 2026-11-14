-- W150 (Claude): Eigene Lern-Zugänge (Eltern/Lehrer/Kind) und Themenplan je Kind.
-- Lern-Sitzungen gelten nur für die Lernen-Schnittstelle: Ihr Schlüssel hat die Form 'lern:<token_hash>'.
-- council.zugang() kennt diese Form nicht, daher lehnen alle übrigen api.*-Funktionen sie ab.

create table if not exists schule.lern_login (
  id bigint generated always as identity primary key,
  name text not null check (length(trim(name)) between 1 and 60),
  rolle text not null check (rolle in ('eltern','lehrer','kind')),
  lernender_id bigint references schule.lernender(id) on delete cascade,
  code_hash text not null unique,
  aktiv boolean not null default true,
  angelegt_am timestamptz not null default now(),
  angelegt_von text,
  zuletzt timestamptz,
  check (rolle <> 'kind' or lernender_id is not null)
);
create table if not exists schule.lern_sitzung (
  token_hash text primary key,
  login_id bigint not null references schule.lern_login(id) on delete cascade,
  erstellt_am timestamptz not null default now(),
  laeuft_ab timestamptz not null,
  zuletzt timestamptz not null default now()
);
create table if not exists schule.lern_fehlversuch (
  id bigint generated always as identity primary key,
  am timestamptz not null default now()
);
alter table schule.lern_login enable row level security;
alter table schule.lern_sitzung enable row level security;
alter table schule.lern_fehlversuch enable row level security;
revoke all on schule.lern_login, schule.lern_sitzung, schule.lern_fehlversuch from public, anon, authenticated;

-- Wer steckt hinter einem Schlüssel? Nur für Lern-Sitzungen; sonst leer.
create or replace function schule.lern_ich(p_schluessel text)
returns table(login_id bigint, rolle text, lernender_id bigint, name text)
language plpgsql stable security definer set search_path to '' as $$
begin
  if p_schluessel is null or left(p_schluessel, 5) <> 'lern:' then return; end if;
  return query select l.id, l.rolle, l.lernender_id, l.name
    from schule.lern_sitzung s join schule.lern_login l on l.id = s.login_id
   where s.token_hash = substr(p_schluessel, 6) and s.laeuft_ab > now() and l.aktiv;
  if not found then raise exception 'Nicht angemeldet' using errcode = 'P0001'; end if;
end $$;

create or replace function schule.ist_lern(p_schluessel text) returns boolean
language sql immutable as $$ select coalesce(left(p_schluessel, 5) = 'lern:', false) $$;

-- Teilnehmer-Nummer: Lern-Logins bekommen eine negative Nummer (kein Council-Teilnehmer).
create or replace function schule.wer_tn(p_schluessel text) returns bigint
language plpgsql stable security definer set search_path to '' as $$
declare v bigint;
begin
  if schule.ist_lern(p_schluessel) then select -i.login_id into v from schule.lern_ich(p_schluessel) i; return v; end if;
  return council.zugang(p_schluessel, 'teilnehmen');
end $$;

-- Leitung = Eltern oder Lehrer (Themen, Entwürfe fürs Testkind, Lernstand aller Kinder).
create or replace function schule.ist_leiter(p_schluessel text) returns boolean
language plpgsql stable security definer set search_path to '' as $$
begin
  if schule.ist_lern(p_schluessel) then
    return exists (select 1 from schule.lern_ich(p_schluessel) i where i.rolle in ('eltern','lehrer'));
  end if;
  return exists (select 1 from council.zugaenge z where z.schluessel_hash = p_schluessel and z.aktiv and 'leiten' = any(z.rechte));
end $$;

-- Eltern = Belohnungen und Zugänge. Der App-Zugang (Council-Leitung) zählt als Eltern.
create or replace function schule.ist_eltern(p_schluessel text) returns boolean
language plpgsql stable security definer set search_path to '' as $$
begin
  if schule.ist_lern(p_schluessel) then
    return exists (select 1 from schule.lern_ich(p_schluessel) i where i.rolle = 'eltern');
  end if;
  return exists (select 1 from council.zugaenge z where z.schluessel_hash = p_schluessel and z.aktiv and 'leiten' = any(z.rechte));
end $$;

create or replace function schule.sieht(p_schluessel text, p_lernender bigint) returns boolean
language plpgsql stable security definer set search_path to '' as $$
declare v_tn bigint;
begin
  if schule.ist_lern(p_schluessel) then
    return exists (select 1 from schule.lern_ich(p_schluessel) i where i.rolle in ('eltern','lehrer') or i.lernender_id = p_lernender);
  end if;
  v_tn := council.zugang(p_schluessel, 'teilnehmen');
  return schule.ist_leiter(p_schluessel) or exists (select 1 from schule.zugang g where g.lernender_id = p_lernender and g.nutzer_ref = 'tn:' || v_tn);
end $$;

create or replace function schule.zugriff(p_schluessel text, p_lernender bigint) returns bigint
language plpgsql security definer set search_path to '' as $$
declare v_tn bigint;
begin
  v_tn := schule.wer_tn(p_schluessel);
  if schule.sieht(p_schluessel, p_lernender) then return v_tn; end if;
  raise exception 'Kein Zugriff auf diesen Lernenden' using errcode = 'P0001';
end $$;

-- Bestehende Funktionen auf die neuen Prüfungen umstellen (Text ersetzen, Rest bleibt gleich).
do $$
declare f text; d text; n int;
begin
  foreach f in array array['schule_uebersicht','schule_eltern','schule_belohnung_setzen','schule_einloesung_entscheiden','schule_lehrplan_lesen'] loop
    select pg_get_functiondef(p.oid) into d from pg_proc p join pg_namespace s on s.oid = p.pronamespace where s.nspname = 'api' and p.proname = f;
    n := length(d);
    d := replace(d, 'council.zugang(p_schluessel, ''teilnehmen'')', 'schule.wer_tn(p_schluessel)');
    if f in ('schule_eltern','schule_belohnung_setzen','schule_einloesung_entscheiden') then
      d := replace(d, 'if not schule.ist_leiter(p_schluessel) then raise exception ''Nur Eltern/Lehrer''', 'if not schule.ist_eltern(p_schluessel) then raise exception ''Nur Eltern''');
    end if;
    if f = 'schule_uebersicht' then
      d := replace(d, '(v_leiter or exists (select 1 from schule.zugang g where g.lernender_id = l.id and g.nutzer_ref = ''tn:'' || v_tn))', 'schule.sieht(p_schluessel, l.id)');
      if position('schule.sieht(p_schluessel, l.id)' in d) = 0 then raise exception 'uebersicht: Filter nicht ersetzt'; end if;
    end if;
    if position('council.zugang' in d) > 0 then raise exception '% enthält noch council.zugang', f; end if;
    execute d;
  end loop;
end $$;

-- Anmelden mit Code (nur über die Serverfunktion lernen-api, nicht für council_mcp freigegeben).
create or replace function schule.lern_code_norm(p text) returns text
language sql immutable as $$ select upper(regexp_replace(coalesce(p, ''), '[^A-Za-z0-9]', '', 'g')) $$;

create or replace function schule.lern_anmelden(p_code text) returns jsonb
language plpgsql security definer set search_path to '' as $$
declare v_l schule.lern_login; v_token text;
begin
  if (select count(*) from schule.lern_fehlversuch where am > now() - interval '10 minutes') >= 30 then
    raise exception 'Zu viele Versuche. Bitte in 10 Minuten erneut.' using errcode = 'P0001';
  end if;
  select * into v_l from schule.lern_login
   where code_hash = encode(extensions.digest(schule.lern_code_norm(p_code), 'sha256'), 'hex') and aktiv;
  if v_l.id is null then
    insert into schule.lern_fehlversuch default values;
    delete from schule.lern_fehlversuch where am < now() - interval '1 day';
    raise exception 'Code unbekannt' using errcode = 'P0001';
  end if;
  v_token := encode(extensions.gen_random_bytes(32), 'hex');
  insert into schule.lern_sitzung(token_hash, login_id, laeuft_ab)
  values (encode(extensions.digest(v_token, 'sha256'), 'hex'), v_l.id, now() + interval '180 days');
  update schule.lern_login set zuletzt = now() where id = v_l.id;
  return jsonb_build_object('token', v_token, 'rolle', v_l.rolle, 'name', v_l.name, 'lernender_id', v_l.lernender_id);
end $$;

create or replace function schule.lern_sitzung_pruefen(p_token text) returns text
language plpgsql security definer set search_path to '' as $$
declare v_hash text;
begin
  if p_token is null or length(p_token) < 32 then return null; end if;
  v_hash := encode(extensions.digest(p_token, 'sha256'), 'hex');
  update schule.lern_sitzung s set zuletzt = now(), laeuft_ab = greatest(s.laeuft_ab, now() + interval '90 days')
   where s.token_hash = v_hash and s.laeuft_ab > now()
     and exists (select 1 from schule.lern_login l where l.id = s.login_id and l.aktiv);
  if not found then return null; end if;
  return 'lern:' || v_hash;
end $$;

create or replace function schule.lern_abmelden(p_token text) returns void
language sql security definer set search_path to '' as $$
  delete from schule.lern_sitzung where token_hash = encode(extensions.digest(coalesce(p_token, ''), 'sha256'), 'hex');
$$;

revoke all on function schule.lern_anmelden(text), schule.lern_sitzung_pruefen(text), schule.lern_abmelden(text) from public, anon, authenticated, council_mcp;

-- Wer bin ich?
create or replace function api.schule_ich(p_schluessel text, p_daten jsonb default null) returns jsonb
language plpgsql stable security definer set search_path to '' as $$
declare v record;
begin
  if schule.ist_lern(p_schluessel) then
    select * into v from schule.lern_ich(p_schluessel);
    return jsonb_build_object('ok', true, 'rolle', v.rolle, 'name', v.name, 'lernender_id', v.lernender_id, 'app', false);
  end if;
  perform council.zugang(p_schluessel, 'teilnehmen');
  return jsonb_build_object('ok', true, 'rolle', case when schule.ist_eltern(p_schluessel) then 'eltern' else 'gast' end, 'name', 'Eltern', 'app', true);
end $$;

-- Themenplan lesen (Eltern/Lehrer).
create or replace function api.schule_plan_lesen(p_schluessel text, p_daten jsonb) returns jsonb
language plpgsql stable security definer set search_path to '' as $$
declare v_l bigint := nullif(p_daten->>'lernender_id','')::bigint; v_k schule.lernender;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  select * into v_k from schule.lernender where id = v_l and aktiv;
  if v_k.id is null then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  return jsonb_build_object('ok', true,
    'kind', jsonb_build_object('id', v_k.id, 'name', v_k.anzeigename, 'klasse', v_k.klasse, 'ist_test', v_k.ist_test),
    'revision', (select coalesce(max(r.revision), 0) from schule.route r where r.lernender_id = v_l and r.art = 'normal'),
    'plan', (select coalesce(jsonb_agg(jsonb_build_object('route_id', r.id, 'block_id', r.block_id, 'position', r.position, 'art', r.art,
                 'status', r.status, 'kann_schon', r.kann_schon, 'geaendert_von', r.geaendert_von, 'geaendert_am', r.geaendert_am)
               order by r.art = 'normal', r.position), '[]'::jsonb)
             from schule.route r where r.lernender_id = v_l and r.status <> 'entfernt'),
    'orte', (select coalesce(jsonb_agg(jsonb_build_object('block_id', b.id, 'titel', b.titel, 'stadt', b.stadt, 'land', b.land, 'ziel_klasse', b.ziel_klasse,
                 'kontinent', k.titel, 'reihenfolge', b.reihenfolge,
                 'einheiten', (select coalesce(jsonb_agg(jsonb_build_object('id', e.id, 'status', e.status, 'titel', t.unterthema,
                                  'pflicht', jsonb_array_length(coalesce(e.inhalt->'bewertung'->'lernziele_pflicht','[]'::jsonb)),
                                  'fertig', (select count(*) from schule.lernziel_stand s where s.lernender_id = v_l and s.einheit_id = e.id and s.pflicht
                                               and s.status in ('nachgewiesen','korrigiert','gesichert')),
                                  'fehler', (select count(*) from schule.lernziel_stand s where s.lernender_id = v_l and s.einheit_id = e.id and s.status = 'fehler'))
                                order by e.id), '[]'::jsonb)
                               from schule.einheit e join schule.thema t on t.id = e.thema_id
                               where e.block_id = b.id and (e.status in ('geprueft','freigegeben') or v_k.ist_test)))
               order by k.reihenfolge, b.reihenfolge), '[]'::jsonb)
             from schule.block b left join schule.kontinent k on k.id = b.kontinent_id where b.fach = 'Mathematik'),
    'notizen', (select coalesce(jsonb_agg(jsonb_build_object('id', n.id, 'text', n.text, 'von', n.von, 'am', n.am) order by n.am desc), '[]'::jsonb)
                from (select * from schule.notiz where lernender_id = v_l order by am desc limit 30) n),
    'verlauf', (select coalesce(jsonb_agg(jsonb_build_object('akteur', a.akteur, 'anlass', a.anlass, 'ereignis', a.ereignis, 'am', a.am) order by a.am desc), '[]'::jsonb)
                from (select * from schule.route_aenderung where lernender_id = v_l order by am desc limit 20) a));
end $$;

-- Themenplan setzen: Reihenfolge = Reihenfolge im Array. Nicht genannte Orte werden aus dem Plan genommen.
create or replace function api.schule_plan_setzen(p_schluessel text, p_daten jsonb) returns jsonb
language plpgsql security definer set search_path to '' as $$
declare v_l bigint := nullif(p_daten->>'lernender_id','')::bigint; v_rev int; v_akt text; v_e jsonb; v_pos int := 0;
  v_b bigint; v_r schule.route; v_ids bigint[] := '{}'; v_n int;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  if not exists (select 1 from schule.lernender where id = v_l and aktiv) then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  if jsonb_typeof(p_daten->'eintraege') <> 'array' then raise exception 'eintraege fehlt' using errcode = 'P0001'; end if;
  perform 1 from schule.lernender where id = v_l for update;
  select coalesce(max(revision), 0) into v_rev from schule.route where lernender_id = v_l and art = 'normal';
  if p_daten ? 'revision' and (p_daten->>'revision')::int <> v_rev then
    raise exception 'Der Plan wurde inzwischen geändert. Bitte neu laden.' using errcode = 'P0001';
  end if;
  v_akt := coalesce((select i.rolle || ':' || i.name from schule.lern_ich(p_schluessel) i where schule.ist_lern(p_schluessel)), 'eltern:App');
  -- erst alle normalen Einträge aus dem Weg schieben (Positionen sind eindeutig)
  update schule.route set position = position + 100000 where lernender_id = v_l and art = 'normal';
  for v_e in select * from jsonb_array_elements(p_daten->'eintraege') loop
    v_b := (v_e->>'block_id')::bigint;
    if not exists (select 1 from schule.block where id = v_b and fach = 'Mathematik') then raise exception 'Unbekannter Ort %', v_b using errcode = 'P0001'; end if;
    if v_b = any(v_ids) then raise exception 'Ort doppelt im Plan' using errcode = 'P0001'; end if;
    v_ids := v_ids || v_b; v_pos := v_pos + 1;
    select * into v_r from schule.route where lernender_id = v_l and block_id = v_b and art = 'normal' order by id limit 1;
    if v_r.id is null then
      insert into schule.route(lernender_id, block_id, position, art, status, kann_schon, revision, geaendert_von, geaendert_am)
      values (v_l, v_b, v_pos, 'normal', 'offen', coalesce((v_e->>'kann_schon')::boolean, false), v_rev + 1, v_akt, now());
    else
      update schule.route set position = v_pos,
        status = case when status = 'entfernt' then 'offen' else status end,
        kann_schon = coalesce((v_e->>'kann_schon')::boolean, kann_schon),
        revision = v_rev + 1, geaendert_von = v_akt, geaendert_am = now()
       where id = v_r.id;
    end if;
  end loop;
  update schule.route set status = 'entfernt', position = 200000 + (position - 100000), revision = v_rev + 1, geaendert_von = v_akt, geaendert_am = now()
   where lernender_id = v_l and art = 'normal' and not (block_id = any(v_ids)) and position >= 100000;
  get diagnostics v_n = row_count;
  insert into schule.route_aenderung(lernender_id, route_id, akteur, anlass, ereignis)
  values (v_l, null, v_akt, 'plan', jsonb_build_object('reihenfolge', to_jsonb(v_ids), 'entfernt', v_n, 'revision', v_rev + 1));
  return jsonb_build_object('ok', true, 'revision', v_rev + 1, 'anzahl', cardinality(v_ids));
end $$;

create or replace function api.schule_notiz_setzen(p_schluessel text, p_daten jsonb) returns jsonb
language plpgsql security definer set search_path to '' as $$
declare v_l bigint := nullif(p_daten->>'lernender_id','')::bigint; v_t text := trim(coalesce(p_daten->>'text','')); v_id bigint;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  if length(v_t) not between 1 and 2000 then raise exception 'Notiz leer oder zu lang' using errcode = 'P0001'; end if;
  insert into schule.notiz(lernender_id, text, von, am)
  values (v_l, v_t, coalesce((select i.rolle || ':' || i.name from schule.lern_ich(p_schluessel) i where schule.ist_lern(p_schluessel)), 'eltern:App'), now())
  returning id into v_id;
  return jsonb_build_object('ok', true, 'id', v_id);
end $$;

-- Zugänge verwalten (nur Eltern). Der Code wird nur einmal zurückgegeben und nur als Hash gespeichert.
create or replace function api.schule_zugaenge(p_schluessel text, p_daten jsonb default null) returns jsonb
language plpgsql stable security definer set search_path to '' as $$
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_eltern(p_schluessel) then raise exception 'Nur Eltern' using errcode = 'P0001'; end if;
  return jsonb_build_object('ok', true, 'zugaenge', (select coalesce(jsonb_agg(jsonb_build_object('id', l.id, 'name', l.name, 'rolle', l.rolle,
      'kind', (select anzeigename from schule.lernender where id = l.lernender_id), 'lernender_id', l.lernender_id, 'aktiv', l.aktiv,
      'angelegt_am', l.angelegt_am, 'zuletzt', l.zuletzt) order by l.aktiv desc, l.rolle, l.name), '[]'::jsonb) from schule.lern_login l));
end $$;

create or replace function api.schule_zugang_anlegen(p_schluessel text, p_daten jsonb) returns jsonb
language plpgsql security definer set search_path to '' as $$
declare v_rolle text := p_daten->>'rolle'; v_name text := trim(coalesce(p_daten->>'name',''));
  v_l bigint := nullif(p_daten->>'lernender_id','')::bigint; v_code text := ''; v_alpha text := 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  v_bytes bytea; i int; v_id bigint;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_eltern(p_schluessel) then raise exception 'Nur Eltern' using errcode = 'P0001'; end if;
  if v_rolle not in ('eltern','lehrer','kind') then raise exception 'Rolle eltern, lehrer oder kind' using errcode = 'P0001'; end if;
  if length(v_name) not between 1 and 60 then raise exception 'Name fehlt' using errcode = 'P0001'; end if;
  if v_rolle = 'kind' and not exists (select 1 from schule.lernender where id = v_l and aktiv) then raise exception 'Kind wählen' using errcode = 'P0001'; end if;
  if v_rolle <> 'kind' then v_l := null; end if;
  v_bytes := extensions.gen_random_bytes(12);
  for i in 0..11 loop v_code := v_code || substr(v_alpha, (get_byte(v_bytes, i) % 32) + 1, 1); end loop;
  insert into schule.lern_login(name, rolle, lernender_id, code_hash, angelegt_von)
  values (v_name, v_rolle, v_l, encode(extensions.digest(v_code, 'sha256'), 'hex'),
          coalesce((select i2.name from schule.lern_ich(p_schluessel) i2 where schule.ist_lern(p_schluessel)), 'App'))
  returning id into v_id;
  return jsonb_build_object('ok', true, 'id', v_id, 'code', substr(v_code,1,4) || '-' || substr(v_code,5,4) || '-' || substr(v_code,9,4));
end $$;

create or replace function api.schule_zugang_sperren(p_schluessel text, p_daten jsonb) returns jsonb
language plpgsql security definer set search_path to '' as $$
declare v_id bigint := nullif(p_daten->>'id','')::bigint;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_eltern(p_schluessel) then raise exception 'Nur Eltern' using errcode = 'P0001'; end if;
  if schule.ist_lern(p_schluessel) and exists (select 1 from schule.lern_ich(p_schluessel) i where i.login_id = v_id) then
    raise exception 'Den eigenen Zugang kannst du hier nicht sperren' using errcode = 'P0001';
  end if;
  update schule.lern_login set aktiv = false where id = v_id;
  if not found then raise exception 'Zugang nicht gefunden' using errcode = 'P0001'; end if;
  delete from schule.lern_sitzung where login_id = v_id;
  return jsonb_build_object('ok', true);
end $$;

grant execute on function api.schule_ich(text, jsonb), api.schule_plan_lesen(text, jsonb), api.schule_plan_setzen(text, jsonb),
  api.schule_notiz_setzen(text, jsonb), api.schule_zugaenge(text, jsonb), api.schule_zugang_anlegen(text, jsonb), api.schule_zugang_sperren(text, jsonb) to council_mcp;
revoke all on function api.schule_ich(text, jsonb), api.schule_plan_lesen(text, jsonb), api.schule_plan_setzen(text, jsonb),
  api.schule_notiz_setzen(text, jsonb), api.schule_zugaenge(text, jsonb), api.schule_zugang_anlegen(text, jsonb), api.schule_zugang_sperren(text, jsonb) from public, anon, authenticated;

-- Rückmeldungen von Eltern/Lehrer an die Entwicklung (Claude liest und beantwortet sie).
create table if not exists schule.rueckmeldung (
  id bigint generated always as identity primary key,
  von text not null,
  art text not null check (art in ('thema_fehlt','zu_ungenau','mehr_aufgaben','schwieriger','leichter','fehler','erklaerung','sonstiges')),
  text text not null check (length(text) between 1 and 4000),
  block_id bigint references schule.block(id),
  einheit_id bigint references schule.einheit(id),
  lernziel text,
  aufgabe_id bigint references schule.aufgabe(id),
  lernender_id bigint references schule.lernender(id),
  status text not null default 'offen' check (status in ('offen','in_arbeit','erledigt','abgelehnt')),
  antwort text,
  am timestamptz not null default now(),
  bearbeitet_am timestamptz
);
alter table schule.rueckmeldung enable row level security;
revoke all on schule.rueckmeldung from public, anon, authenticated;

create or replace function api.schule_rueckmeldung_geben(p_schluessel text, p_daten jsonb) returns jsonb
language plpgsql security definer set search_path to '' as $$
declare v_id bigint; v_e bigint := nullif(p_daten->>'einheit_id','')::bigint; v_a bigint := nullif(p_daten->>'aufgabe_id','')::bigint;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  if v_a is not null and v_e is null then select einheit_id into v_e from schule.aufgabe where id = v_a; end if;
  insert into schule.rueckmeldung(von, art, text, block_id, einheit_id, lernziel, aufgabe_id, lernender_id)
  values (coalesce((select i.rolle || ':' || i.name from schule.lern_ich(p_schluessel) i where schule.ist_lern(p_schluessel)), 'eltern:App'),
          coalesce(nullif(p_daten->>'art',''), 'sonstiges'), trim(coalesce(p_daten->>'text','')),
          coalesce(nullif(p_daten->>'block_id','')::bigint, (select block_id from schule.einheit where id = v_e)),
          v_e, nullif(p_daten->>'lernziel',''), v_a, nullif(p_daten->>'lernender_id','')::bigint)
  returning id into v_id;
  return jsonb_build_object('ok', true, 'id', v_id);
end $$;

create or replace function api.schule_rueckmeldungen(p_schluessel text, p_daten jsonb default null) returns jsonb
language plpgsql stable security definer set search_path to '' as $$
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  return jsonb_build_object('ok', true, 'rueckmeldungen', (select coalesce(jsonb_agg(jsonb_build_object(
      'id', r.id, 'von', r.von, 'art', r.art, 'text', r.text, 'status', r.status, 'antwort', r.antwort, 'am', r.am, 'bearbeitet_am', r.bearbeitet_am,
      'einheit_id', r.einheit_id, 'lernziel', r.lernziel, 'aufgabe_id', r.aufgabe_id,
      'ort', (select coalesce(b.stadt, b.titel) || ' – ' || b.titel from schule.block b where b.id = r.block_id),
      'aufgabe', (select a.frage->>'text' from schule.aufgabe a where a.id = r.aufgabe_id))
    order by (r.status in ('offen','in_arbeit')) desc, r.am desc), '[]'::jsonb)
    from (select * from schule.rueckmeldung order by am desc limit 200) r));
end $$;

grant execute on function api.schule_rueckmeldung_geben(text, jsonb), api.schule_rueckmeldungen(text, jsonb) to council_mcp;
revoke all on function api.schule_rueckmeldung_geben(text, jsonb), api.schule_rueckmeldungen(text, jsonb) from public, anon, authenticated;
