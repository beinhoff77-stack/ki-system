-- TEMPO-S1: kleiner NACHBAU für den lokalen Test (tools/tests/tempo_test.py, leere lokale Postgres-Instanz). NICHT die echte Datenbank.
-- Nur die Teile, die schule.etappen_stand liest; Hilfsfunktionen mit den Texten aus den Migrationen im Repo (Stand nach FT-S/RB-S), vereinfacht nur
-- dort, wo etappen_stand sie nicht berührt (kind_gruppe, ist_plan). Die Daten sind erfunden (Testkinder 1–4), Größen ähnlich wie live
-- (95 Einheiten mit je 5–10 Etappen, rund 20 Übungen je Etappe, einige Tausend Versuche; live laut 1175: 32 417 Aufgaben, 958 Versuche).
-- etappen_stand selbst legt der Test an: alte Fassung = nachgerechneter Text aus den Migrationen (tempo_einspielen.py).
create role anon nologin;
create role authenticated nologin;
create schema schule;
create schema api;
create table schule.lernender (id bigint primary key, ist_test boolean not null default false, aktiv boolean not null default true, zeitzone text);
create table schule.thema (id bigint primary key, zusatz text[] not null default '{}');
create table schule.block_thema (block_id bigint, thema_id bigint);
create table schule.einheit (id bigint primary key, thema_id bigint, block_id bigint, status text not null default 'geprueft', version int default 1, inhalt jsonb default '{}');
create table schule.aufgabe (id bigserial primary key, einheit_id bigint, pool text not null default 'uebung', variante_gruppe text, freigegeben boolean not null default true,
  stufe smallint, typ text, zaehlt text, reihenfolge int, frage jsonb default '{}');
create table schule.testsitzung (id bigserial primary key, lernender_id bigint, einheit_id bigint, art text, ergebnis text, abgeschlossen_am timestamptz);
create table schule.versuch (id bigserial primary key, lernender_id bigint not null, aufgabe_id bigint not null, client_id text, richtig boolean not null, hilfe smallint,
  anlauf smallint, testsitzung_id bigint, misch boolean not null default false, am timestamptz not null default now(), unique (lernender_id, client_id));
create unique index versuch_sitzung_aufgabe on schule.versuch (testsitzung_id, aufgabe_id) where testsitzung_id is not null;
create table schule.lernziel_stand (lernender_id bigint, einheit_id bigint, lernziel text, status text, pflicht boolean default true, primary key (lernender_id, einheit_id, lernziel));
create table schule.karte_stand (lernender_id bigint not null, einheit_id bigint not null, lernziel text not null,
  serie smallint not null default 0, richtig int not null default 0, falsch int not null default 0, sitzt boolean not null default false, sitzt_am timestamptz,
  wdh_stufe smallint not null default 0, faellig_am timestamptz, zuletzt timestamptz, schwer_ok boolean not null default false, wdh_fehler smallint not null default 0,
  wdh_ab timestamptz, wdh_lerntage smallint, eigene_loesungen int not null default 0, typen text[] not null default '{}', folge int not null default 0,
  fehler_folge int not null default 0, stufe_senkung smallint not null default 0, gezaehlt jsonb not null default '{}', geoeffnet_am timestamptz,
  misch_ok_am timestamptz, gesetzt_am timestamptz, gesetzt_von text, wdh_gesetzt_am timestamptz, primary key (lernender_id, einheit_id, lernziel));
create table schule.misch_ausgabe (id bigserial primary key, lernender_id bigint, aufgabe_id bigint, einheit_id bigint, lernziel text, ausgegeben_am timestamptz default now(), eingeloest_am timestamptz, verfallen_am timestamptz);
create table schule.lerntag (lernender_id bigint, fach text, datum date, zeitzone text, primary key (lernender_id, fach, datum));
create table schule.regel (schluessel text primary key, wert jsonb);
create table schule.route (id bigserial primary key, lernender_id bigint, block_id bigint, art text default 'normal', status text default 'offen', ausgelassen bigint[] default '{}', kann_wdh_themen bigint[] default '{}');

-- vereinfacht (etappen_stand braucht sie nur über zusatz_eingeplant)
create function schule.kind_gruppe(p_l bigint) returns text language sql stable set search_path to '' as $$ select 'gym_by'::text $$;
create function schule.ist_plan(r schule.route) returns boolean language sql stable set search_path to '' as $$ select r.status in ('offen', 'laeuft') $$;

-- Texte wie im Repo
create function schule.aufgabe_zaehlt(a schule.aufgabe) returns boolean language sql immutable set search_path to '' as $function$
  select a.zaehlt is distinct from 'nein';
$function$;
create function schule.aufgabe_anwenden(a schule.aufgabe) returns boolean language sql immutable set search_path to '' as $function$
  select coalesce(a.typ in ('einkleidung', 'transfer', 'pruefung'), false);
$function$;
create function schule.wd_regel(p text, p_std integer) returns integer language sql stable set search_path to '' as $function$
  select coalesce((select (r.wert #>> '{}')::int from schule.regel r where r.schluessel = p), p_std);
$function$;
create function schule.karte_ziel(p_einheit bigint, p_lz text) returns integer language sql stable set search_path to '' as $function$
  select least(6, greatest(2, count(*)))::int from schule.aufgabe a
   where schule.aufgabe_zaehlt(a) and a.einheit_id = p_einheit and a.pool = 'uebung' and a.variante_gruppe = p_lz and a.freigegeben;
$function$;
create function schule.karte_schwer_noetig(p_einheit bigint, p_lz text) returns boolean language sql stable set search_path to '' as $function$
  select exists (select 1 from schule.aufgabe a
   where schule.aufgabe_zaehlt(a) and a.einheit_id = p_einheit and a.pool = 'uebung' and a.variante_gruppe = p_lz and a.freigegeben and a.stufe = 3);
$function$;
create function schule.karte_typen_noetig(p_einheit bigint, p_lz text) returns integer language sql stable set search_path to '' as $function$
  select least(2, count(distinct a.typ))::int from schule.aufgabe a
   where schule.aufgabe_zaehlt(a) and a.einheit_id = p_einheit and a.pool = 'uebung' and a.variante_gruppe = p_lz and a.freigegeben and a.typ is not null;
$function$;
create function schule.karte_faellig(k schule.karte_stand) returns boolean language sql stable set search_path to '' as $function$
  select coalesce(k.sitzt, false) and case
    when k.wdh_lerntage is null or k.wdh_ab is null then coalesce(k.faellig_am <= now(), false)
    else (select (select count(*) from schule.lerntag t where t.lernender_id = k.lernender_id and t.fach = 'Mathematik'
                    and (t.datum::timestamp at time zone t.zeitzone) > k.wdh_ab and t.datum < (now() at time zone z.tz)::date)
                 + case when (now() at time zone z.tz)::date > (k.wdh_ab at time zone z.tz)::date then 1 else 0 end >= k.wdh_lerntage
            from (select coalesce((select l.zeitzone from schule.lernender l where l.id = k.lernender_id), 'UTC') as tz) z)
  end;
$function$;
create function schule.thema_kann_wdh(p_l bigint, p_thema bigint) returns boolean language sql stable set search_path to '' as $function$
  select exists (select 1 from schule.route r join schule.block_thema bt on bt.block_id = r.block_id and bt.thema_id = p_thema
                  where r.lernender_id = p_l and r.art = 'normal' and r.status <> 'entfernt' and not (p_thema = any(r.ausgelassen))
                    and p_thema = any(r.kann_wdh_themen));
$function$;
create function schule.zusatz_eingeplant(p_l bigint, p_thema bigint) returns boolean language sql stable set search_path to '' as $$
  select coalesce((select schule.kind_gruppe(p_l) = any(t.zusatz) from schule.thema t where t.id = p_thema), false)
     and exists (select 1 from schule.route r join schule.block_thema bt on bt.block_id = r.block_id and bt.thema_id = p_thema
                  where r.lernender_id = p_l and r.art = 'normal' and r.status <> 'entfernt'
                    and (schule.ist_plan(r) or r.status = 'fertig')
                    and not (p_thema = any(coalesce(r.ausgelassen, '{}'))));
$$;
create function schule.flug_ohne_test(p_l bigint, p_einheit bigint) returns boolean language sql stable set search_path to '' as $$
  select coalesce(schule.thema_kann_wdh(p_l, (select e.thema_id from schule.einheit e where e.id = p_einheit)), false)
      or coalesce(schule.zusatz_eingeplant(p_l, (select e.thema_id from schule.einheit e where e.id = p_einheit)), false);   -- ZP-S
$$;
create function schule.flug_nachtest(p_lernender bigint, p_einheit bigint) returns boolean language sql stable set search_path to '' as $function$
  select case when schule.flug_ohne_test(p_lernender, p_einheit) then null -- LB-3: entfällt
    else exists (select 1 from schule.testsitzung t where t.lernender_id = p_lernender and t.einheit_id = p_einheit and t.art = 'nachtest' and t.ergebnis = 'bestanden') end;
$function$;
create function schule.etappe_fertig(k schule.karte_stand, p_status text) returns boolean language sql stable set search_path to '' as $function$
  select coalesce(k.sitzt, false) or (k.sitzt_am is null and coalesce(p_status in ('nachgewiesen', 'korrigiert', 'gesichert'), false));
$function$;
create function schule.karte_sicher(k schule.karte_stand) returns boolean language sql stable set search_path to '' as $function$
  select coalesce(k.sitzt, false) and coalesce(k.wdh_stufe, 0) >= 4
     and case when k.gesetzt_am is not null or schule.flug_ohne_test(k.lernender_id, k.einheit_id) then
       (select (k.misch_ok_am is not null and k.misch_ok_am >= s.seit)
            or (not exists (select 1 from schule.misch_ausgabe m join schule.aufgabe a on a.id = m.aufgabe_id
                             where m.lernender_id = k.lernender_id and a.einheit_id = k.einheit_id and a.variante_gruppe = k.lernziel and m.eingeloest_am >= s.seit)
                and not exists (select 1 from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                             where v.lernender_id = k.lernender_id and coalesce(v.misch, false) and a.einheit_id = k.einheit_id and a.variante_gruppe = k.lernziel and v.am >= s.seit))
          from (select coalesce(k.wdh_gesetzt_am, k.gesetzt_am, k.sitzt_am) as seit) s)
     else
       k.misch_ok_am is not null and k.misch_ok_am >= k.sitzt_am
       and exists (select 1 from schule.testsitzung t join schule.versuch v on v.testsitzung_id = t.id join schule.aufgabe a on a.id = v.aufgabe_id
                    where t.lernender_id = k.lernender_id and t.einheit_id = k.einheit_id and t.art = 'nachtest' and t.ergebnis = 'bestanden'
                      and t.abgeschlossen_am >= k.sitzt_am and a.variante_gruppe = k.lernziel and v.richtig)
     end;
$function$;
create function schule.karte_anwenden_noetig(p_einheit bigint, p_lz text) returns boolean language sql stable set search_path to '' as $function$
  select exists (select 1 from schule.aufgabe a
   where a.einheit_id = p_einheit and a.pool = 'uebung' and a.variante_gruppe = p_lz and a.freigegeben and schule.aufgabe_zaehlt(a) and schule.aufgabe_anwenden(a));
$function$;
create function schule.karte_anwenden_pflicht(k schule.karte_stand, p_einheit bigint, p_lz text) returns boolean language sql stable set search_path to '' as $function$
  select schule.wd_regel('anwenden_pflicht', 0) = 1
     and k.sitzt_am is null and not coalesce(k.sitzt, false) and schule.karte_anwenden_noetig(p_einheit, p_lz);
$function$;
create function schule.karte_anwenden_ok(k schule.karte_stand) returns boolean language sql stable set search_path to '' as $function$
  select exists (select 1 from jsonb_object_keys(coalesce(k.gezaehlt, '{}'::jsonb)) x join schule.aufgabe a on a.id = x::bigint
                  where schule.aufgabe_anwenden(a) and schule.aufgabe_zaehlt(a));
$function$;
create function schule.karte_bearbeitungen(p_l bigint, p_e bigint, p_lz text) returns integer language sql stable set search_path to '' as $function$
  select count(*)::int from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
   where v.lernender_id = p_l and a.einheit_id = p_e and a.variante_gruppe = p_lz and a.pool = 'uebung'
     and v.testsitzung_id is null and not coalesce(v.misch, false) and coalesce(v.anlauf, 1) <> 2;
$function$;

-- Zugriff und Merkheft: NACHBAU (die echte api.schule_merkheft steht nicht im Repo). Gleiche Bauart: Zugriff prüfen, je Einheit etappen_stand.
create function schule.zugriff(p_schluessel text, p_lernender bigint) returns bigint language plpgsql security definer set search_path to '' as $$
begin
  if p_schluessel is distinct from 'nachbau-schluessel' then raise exception 'Kein Zugriff auf diesen Lernenden' using errcode = 'P0001'; end if;
  return 1;
end $$;
create function api.schule_merkheft(p_schluessel text, p_daten jsonb) returns jsonb language plpgsql stable security definer set search_path to '' as $$
declare v_l bigint := (p_daten->>'lernender_id')::bigint;
begin
  perform schule.zugriff(p_schluessel, v_l);
  return jsonb_build_object('ok', true, 'einheiten', (select coalesce(jsonb_agg(jsonb_build_object('einheit_id', e.id, 'block_id', e.block_id,
      'etappen', e.inhalt->'etappen', 'abschnitte', e.inhalt->'abschnitte', 'stand', schule.etappen_stand(v_l, e.id)) order by e.id), '[]'::jsonb)
    from schule.einheit e where e.status in ('geprueft', 'freigegeben')));
end $$;

-- ---------- erfundene Daten ----------
select setseed(0.20261207);
insert into schule.regel values ('anwenden_pflicht', '1');
insert into schule.lernender (id, ist_test, zeitzone) values (1, false, 'Europe/Berlin'), (2, false, 'Pacific/Auckland'), (3, true, null), (4, false, 'UTC');
insert into schule.thema (id, zusatz) select g, case when g % 17 = 0 then '{gym_by}'::text[] else '{}' end from generate_series(1, 100) g;
insert into schule.block_thema select g, g from generate_series(1, 100) g;
-- 95 Einheiten; Einheit 5: keine Etappen, Einheit 6: doppelte Etappe, Einheit 8: Entwurf, Einheit 9: Etappe 1 ohne Übungen
-- (eine Etappe ohne lernziel bricht alte und neue Fassung gleich ab: jsonb_object_agg mit leerem Schlüssel – live offenbar nicht vorhanden)
insert into schule.einheit (id, thema_id, block_id, status, inhalt)
select g, g, g, case when g = 8 then 'entwurf' else 'geprueft' end,
  case when g = 5 then '{"ziel": "leer"}'::jsonb
       else jsonb_build_object('etappen', (select jsonb_agg(x order by n) from (
              select n, case when g = 6 and n = 3 then jsonb_build_object('lernziel', 'e6_lz1', 'titel', 'doppelt')
                             else jsonb_build_object('lernziel', 'e' || g || '_lz' || n, 'titel', 'Etappe ' || n) end x
                from generate_series(1, 5 + g % 6) n) q), 'abschnitte', jsonb_build_array(jsonb_build_object('titel', 'A')))
  end
  from generate_series(1, 95) g;
-- Übungen und Testaufgaben je Etappe (einige gesperrt, einige zählen nicht, Stufen und Typen gemischt; eine Etappe ohne Übungen)
insert into schule.aufgabe (einheit_id, pool, variante_gruppe, freigegeben, stufe, typ, zaehlt, reihenfolge)
select e.id, case when i % 7 = 0 then 'test' else 'uebung' end, et->>'lernziel', random() > 0.1, 1 + (i % 3),
       (array['direkt', 'einkleidung', 'transfer', 'umkehr', null])[1 + (i % 5)], case when i % 11 = 0 then 'nein' when i % 13 = 0 then 'ja' end, i
  from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]')) with ordinality o(et, nr), generate_series(1, 22) i
 where et ? 'lernziel' and not (e.id = 9 and o.nr = 1);
-- Versuche: Kind 1 viel, Kind 2 mittel, Testkind wenig, Kind 4 keine
insert into schule.testsitzung (lernender_id, einheit_id, art, ergebnis, abgeschlossen_am)
select l, e, case when e % 2 = 0 then 'nachtest' else 'blocktest' end, case when e % 3 = 0 then 'bestanden' else 'offen' end, now() - interval '3 days'
  from (values (1), (2), (3)) k(l), generate_series(1, 95, 4) e;
insert into schule.versuch (lernender_id, aufgabe_id, client_id, richtig, hilfe, anlauf, testsitzung_id, misch, am)
select k.l, a.id, 'c' || k.l || '-' || a.id || '-' || r, random() > 0.35, (random() * 2)::int, 1 + (random() > 0.8)::int,
       case when a.pool = 'test' then (select t.id from schule.testsitzung t where t.lernender_id = k.l and t.einheit_id = a.einheit_id limit 1) end,
       random() > 0.9, now() - (random() * interval '30 days')
  from (values (1, 0.2), (2, 0.1), (3, 0.03)) k(l, anteil), schule.aufgabe a, generate_series(1, 2) r
 where random() + 0 * a.id + 0 * r < k.anteil   -- je Zeile neu würfeln (sonst rechnet Postgres random() einmal je Kind)
   and (a.pool <> 'test' or (r = 1 and exists (select 1 from schule.testsitzung t where t.lernender_id = k.l and t.einheit_id = a.einheit_id)));
-- Lernstand je Etappe (verschiedene Status), Karten in allen Lagen
insert into schule.lernziel_stand (lernender_id, einheit_id, lernziel, status)
select distinct on (k.l, e.id, et->>'lernziel') k.l, e.id, et->>'lernziel', (array['offen', 'nachgewiesen', 'korrigiert', 'gesichert', 'fehler'])[1 + (random() * 4)::int]
  from (values (1), (2), (3)) k(l), schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]')) et
 where et ? 'lernziel' and random() < 0.6;
insert into schule.karte_stand (lernender_id, einheit_id, lernziel, serie, sitzt, sitzt_am, wdh_stufe, faellig_am, schwer_ok, wdh_ab, wdh_lerntage,
  eigene_loesungen, typen, folge, fehler_folge, stufe_senkung, gezaehlt, misch_ok_am, gesetzt_am, wdh_gesetzt_am)
select distinct on (k.l, e.id, et->>'lernziel') k.l, e.id, et->>'lernziel', (random() * 3)::int, s.sitzt,
       case when s.sitzt or random() < 0.2 then now() - interval '20 days' end, case when s.sitzt then (random() * 5)::int else 0 end,
       now() + (random() - 0.5) * interval '10 days', random() < 0.3, case when random() < 0.5 then now() - interval '9 days' end, case when random() < 0.5 then 3 end,
       (random() * 6)::int, case when random() < 0.5 then '{direkt,umkehr}'::text[] else '{}' end, (random() * 3)::int, (random() * 2)::int, (random() * 2)::int,
       coalesce((select jsonb_object_agg(a.id::text, true) from schule.aufgabe a where a.einheit_id = e.id and a.variante_gruppe = et->>'lernziel' and random() < 0.3), '{}'),
       case when random() < 0.4 then now() - interval '2 days' end, case when random() < 0.1 then now() - interval '25 days' end, null
  from (values (1), (2), (3)) k(l), schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]')) et, lateral (select random() + 0 * e.id + 0 * length(et::text) < 0.5 sitzt) s
 where et ? 'lernziel' and random() + 0 * e.id < 0.7;
insert into schule.misch_ausgabe (lernender_id, aufgabe_id, einheit_id, lernziel, ausgegeben_am, eingeloest_am)
select v.lernender_id, v.aufgabe_id, a.einheit_id, a.variante_gruppe, v.am, case when random() < 0.5 then v.am end
  from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id where v.misch;
insert into schule.lerntag select l, 'Mathematik', current_date - d, 'Europe/Berlin' from (values (1), (2)) k(l), generate_series(1, 20) d;
insert into schule.route (lernender_id, block_id, status, kann_wdh_themen, ausgelassen)
select l, b, (array['offen', 'fertig', 'laeuft'])[1 + b % 3], case when b % 5 = 0 then array[b::bigint] else '{}' end, case when b % 19 = 0 then array[b::bigint] else '{}' end
  from (values (1), (2), (3)) k(l), generate_series(1, 95, 2) b;
-- wie live: Bestand mit Änderungen (HOT-Ketten) – Aufgaben werden nachträglich freigegeben/gesperrt
update schule.aufgabe set freigegeben = not freigegeben where id % 97 = 0;
analyze;
