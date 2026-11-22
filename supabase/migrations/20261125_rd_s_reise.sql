-- RD-S (Bau-Auftrag RD, 23.11.): Reise-Aufbau in die Datenbank – Kontinent, Land je Flug, Stadt je Etappe, Reserve, Antarktis-Stationen,
-- Lesefunktion für die Reisekarte je Kind und Aktion api.schule_reise_karte (lernen-api 0.9.3).
-- Nur neue Tabellen und Funktionen. Bestehende Tabellen (block, kontinent, route, karte_stand, lernstand, sterne …) und Funktionen
-- (Abflugtafel, reiseoptionen, Visum, Stempel, Sterne) bleiben unverändert; die bisherigen Ortsnamen (block.stadt/land) bleiben, bis die Karte live ist.
-- Daten kommen getrennt mit inhalte/reise/rd_einspiel_2311.sql (erzeugt von inhalte/reise/rd_bauen.py aus aufbau-vorschlag.json).
-- Wiederholbar: create … if not exists / create or replace; kein DROP, kein DELETE.

-- 1) Kontinent der Reise (Themengebiet ↔ Reise). Der bisherige schule.kontinent (titel = Themengebiet, erdteil = bisherige Anzeige) bleibt.
create table if not exists schule.reise_kontinent (
  kontinent_id bigint primary key references schule.kontinent (id),
  reise        text not null unique,
  reihenfolge  integer not null
);

-- 2) Land je Flug (Thema bzw. Teil) und Reserve-Länder in einer Tabelle, damit „jedes Land genau einmal“ über beide gilt.
create table if not exists schule.reise_land (
  id                     bigint generated always as identity primary key,
  art                    text not null check (art in ('flug', 'reserve')),
  kontinent_id           bigint not null references schule.kontinent (id),
  thema_id               bigint unique references schule.thema (id),              -- je Flug (Thema bzw. Teil) genau ein Land
  flug_schluessel        text unique,                                              -- „29“ bzw. „29-2“ wie in aufbau-vorschlag.json
  name                   text not null unique,                                     -- deutscher Name, bei Landesteilen „Brasilien – Süden“
  iso                    text not null check (iso ~ '^[A-Z]{2}$'),                 -- ISO 3166-1 alpha-2 (Flagge, Kartenpfad)
  region                 text,                                                     -- Landesteil (z. B. AU-Bundesstaat), sonst leer
  region_schluessel      text generated always as (coalesce(region, '')) stored,
  mitte_breite           numeric(9,5) not null check (mitte_breite between -90 and 90),
  mitte_laenge           numeric(9,5) not null check (mitte_laenge between -180 and 180),
  mitte_quelle           text,
  hauptstadt_name        text not null,                                            -- deutscher Name
  hauptstadt_breite      numeric(9,5) not null check (hauptstadt_breite between -90 and 90),
  hauptstadt_laenge      numeric(9,5) not null check (hauptstadt_laenge between -180 and 180),
  hauptstadt_geonames_id bigint,
  hauptort               jsonb,                                                    -- nur Landesteile: {name, breite, laenge, geonames_id, art}
  kurzflug               boolean not null default false,
  insel_ausnahme         boolean not null default false,
  nachbarteil            boolean not null default false,                           -- Teil > 1 im Nachbarland des vorigen Teils
  nachbarschaft          text,
  reihenfolge            integer not null,
  constraint reise_land_art_thema check ((art = 'flug') = (thema_id is not null and flug_schluessel is not null)),
  constraint reise_land_einmal unique (iso, region_schluessel),                     -- jedes Land (bzw. jeder Landesteil) genau einmal
  constraint reise_land_id_thema unique (id, thema_id),
  constraint reise_land_teil check (not (nachbarteil and insel_ausnahme))
);

-- 3) Stadt je Etappe (Thema + Lernziel; Einheit beim Einspielen) und Reserve-Städte.
create table if not exists schule.reise_stadt (
  id             bigint generated always as identity primary key,
  art            text not null check (art in ('etappe', 'reserve')),
  land_id        bigint not null references schule.reise_land (id),
  thema_id       bigint,
  einheit_id     bigint references schule.einheit (id),                            -- Einheit beim Einspielen (Lesefunktion nimmt die aktuelle des Themas)
  lernziel       text,
  name           text not null,
  breite         numeric(9,5) not null check (breite between -90 and 90),
  laenge         numeric(9,5) not null check (laenge between -180 and 180),
  geonames_id    bigint not null,
  geonames_name  text,
  reihenfolge    integer not null check (reihenfolge > 0),
  kuer_vorschlag text[],                                                           -- nur zum Abgleich: Kür-Gruppen laut Reise-Aufbau; maßgeblich ist die Pflichtliste der Einheit
  constraint reise_stadt_art check ((art = 'etappe') = (thema_id is not null and lernziel is not null)),
  constraint reise_stadt_land_thema foreign key (land_id, thema_id) references schule.reise_land (id, thema_id),  -- Stadt gehört zum Land ihres Flugs
  constraint reise_stadt_einmal unique (geonames_id),                               -- jede Stadt genau einmal
  constraint reise_stadt_etappe unique (thema_id, lernziel),                        -- je Etappe höchstens eine Stadt (mindestens eine: reise_abweichung)
  constraint reise_stadt_folge unique (land_id, art, reihenfolge)
);

-- 4) Antarktis-Stationen der Expeditionen.
create table if not exists schule.reise_station (
  id        bigint generated always as identity primary key,
  name      text not null unique,
  betreiber text,
  breite    numeric(9,5) not null check (breite between -90 and -60),
  laenge    numeric(9,5) not null check (laenge between -180 and 180)
);
create table if not exists schule.reise_station_expedition (
  expedition_id bigint primary key references schule.expedition (id),              -- je Expedition genau eine Station
  station_id    bigint not null references schule.reise_station (id)
);

-- 5) Quellen (Angabe auf der Info-Seite und in jeder Karten-Antwort).
create table if not exists schule.reise_quelle (
  schluessel text primary key,
  was        text not null,
  quelle     text not null,
  lizenz     text not null,
  link       text
);

alter table schule.reise_kontinent enable row level security;   -- nur über die api-Funktionen (security definer), wie die übrigen schule-Tabellen
alter table schule.reise_land enable row level security;
alter table schule.reise_stadt enable row level security;
alter table schule.reise_station enable row level security;
alter table schule.reise_station_expedition enable row level security;
alter table schule.reise_quelle enable row level security;
revoke all on schule.reise_kontinent, schule.reise_land, schule.reise_stadt, schule.reise_station, schule.reise_station_expedition, schule.reise_quelle
  from public, anon, authenticated;

-- 6) Abgleich Reise ↔ Datenbank: jede Etappe jedes freigegebenen Flugs braucht genau eine Stadt; jede Etappen-Stadt braucht ihre Etappe.
create or replace view schule.reise_abweichung as
  with fl as (select l.id land_id, l.thema_id, schule.thema_einheit(l.thema_id) einheit_id from schule.reise_land l where l.art = 'flug'),
       et as (select fl.thema_id, fl.einheit_id, x->>'lernziel' lernziel, o::int nr
                from fl join schule.einheit e on e.id = fl.einheit_id, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]')) with ordinality q(x, o))
  select 'etappe_ohne_stadt'::text art, et.thema_id, et.lernziel, null::text stadt
    from et where not exists (select 1 from schule.reise_stadt s where s.thema_id = et.thema_id and s.lernziel = et.lernziel)
  union all
  select 'stadt_ohne_etappe', s.thema_id, s.lernziel, s.name
    from schule.reise_stadt s where s.art = 'etappe'
     and not exists (select 1 from et where et.thema_id = s.thema_id and et.lernziel = s.lernziel)
  union all
  select 'reihenfolge_anders', s.thema_id, s.lernziel, s.name
    from schule.reise_stadt s join et on et.thema_id = s.thema_id and et.lernziel = s.lernziel where s.reihenfolge <> et.nr
  union all
  select 'thema_ohne_land', t.id, null, null                                      -- freigegebener Flug ohne Land (z. B. nach neuer Teilung)
    from schule.thema t where schule.thema_einheit(t.id) is not null and not exists (select 1 from schule.reise_land l where l.thema_id = t.id)
  union all
  select 'land_ohne_freigabe', l.thema_id, null, l.name
    from fl join schule.reise_land l on l.id = fl.land_id where fl.einheit_id is null;
revoke all on schule.reise_abweichung from public, anon, authenticated;

-- Kür-Abgleich (nur Meldung): wo der Reise-Aufbau eine andere Kür je Gruppe annimmt als die Pflichtliste der Einheit.
create or replace view schule.reise_kuer_abweichung as
  with g(gruppe, schulart) as (values ('gym_by', 'gym_by'), ('rs_I', 'rs_by'), ('rs_II_III', 'rs_by'), ('myp_standard', 'ib_myp'), ('myp_extended', 'ib_myp')),
       s as (select s.thema_id, s.lernziel, s.name, s.kuer_vorschlag, e.inhalt b, g.gruppe, g.schulart
               from schule.reise_stadt s join schule.einheit e on e.id = schule.thema_einheit(s.thema_id) cross join g where s.art = 'etappe'),
       l as (select s.*, coalesce(case when jsonb_typeof(s.b#>array['bewertung', 'pflicht_je_schulart', s.gruppe]) = 'array' then s.b#>array['bewertung', 'pflicht_je_schulart', s.gruppe] end,
                                  case when jsonb_typeof(s.b#>array['bewertung', 'pflicht_je_schulart', s.schulart]) = 'array' then s.b#>array['bewertung', 'pflicht_je_schulart', s.schulart] end,
                                  case when jsonb_typeof(s.b#>'{bewertung,lernziele_pflicht}') = 'array' then s.b#>'{bewertung,lernziele_pflicht}' end) liste from s)
  select thema_id, lernziel, name stadt, gruppe,
         liste is not null and not (liste ? lernziel) kuer_db, coalesce(gruppe = any(kuer_vorschlag), false) kuer_vorschlag
    from l
   where (liste is not null and not (liste ? lernziel)) <> coalesce(gruppe = any(kuer_vorschlag), false);
revoke all on schule.reise_kuer_abweichung from public, anon, authenticated;

-- 7) Stand einer Etappe für die Karte (gleiche Zählung wie schule.thema_stufe).
create or replace function schule.reise_etappe_stand(k schule.karte_stand)
 returns text language sql stable set search_path to ''
as $$
  select case when k.lernender_id is null then 'offen'
              when schule.karte_sicher(k) then 'sicher'
              when k.sitzt then 'gelandet'
              when k.sitzt_am is not null then 'wieder_offen'
              when coalesce(k.richtig, 0) + coalesce(k.falsch, 0) > 0 then 'begonnen'
              else 'offen' end;
$$;
revoke all on function schule.reise_etappe_stand(schule.karte_stand) from public, anon, authenticated;

-- 8) Lesefunktion für die Karte je Kind: Kontinente → Flüge → Städte, nächster Start, Antarktis, Quellen.
--    Nur lesend. Stufe/Plan/Gesetzt aus schule.thema_stufe, Stempel = Erstabschluss (flug_erstabschluss), golden = alle Etappen der Regel sicher,
--    Pflicht/Kür nach der Gruppe des Kindes (schule.pflicht_lernziele), Zusatz = Gruppe in thema.zusatz.
create or replace function schule.reise_karte(p_l bigint)
 returns jsonb language plpgsql stable security definer set search_path to ''
as $$
declare v_gr text := schule.kind_gruppe(p_l); v_kont jsonb := '[]'; v_fl jsonb; v_st jsonb; v_k record; v_f record; v_s record;
  v_e bigint; v_pf text[]; v_stufe jsonb; v_stand text; v_pfl boolean; v_zus boolean; v_platz int; v_golden boolean; v_stempel timestamptz;
  v_n int; v_gesch int; v_nzus int; v_start jsonb; v_rang int; v_best int := 2147483647; v_offen jsonb;
begin
  for v_k in select k.id, k.schluessel, k.titel, k.zusatz, k.reihenfolge, rk.reise
               from schule.kontinent k join schule.reise_kontinent rk on rk.kontinent_id = k.id order by rk.reihenfolge, k.id loop
    v_fl := '[]'; v_n := 0; v_gesch := 0; v_nzus := 0;
    for v_f in select l.*, t.unterthema titel, t.untertitel, t.teil_nr, t.teil_von, t.teil_stamm, coalesce(v_gr = any(t.zusatz), false) zus,
                      (select bt.reihenfolge from schule.block_thema bt where bt.thema_id = l.thema_id order by bt.block_id limit 1) bt_folge
                 from schule.reise_land l join schule.thema t on t.id = l.thema_id
                where l.art = 'flug' and l.kontinent_id = v_k.id and schule.thema_einheit(l.thema_id) is not null
                order by l.reihenfolge, l.id loop
      v_e := schule.thema_einheit(v_f.thema_id);
      v_pf := schule.pflicht_lernziele(p_l, v_e);
      v_stufe := schule.thema_stufe(p_l, v_f.thema_id);
      select min(r.position) into v_platz from schule.route r join schule.block_thema bt on bt.block_id = r.block_id and bt.thema_id = v_f.thema_id
       where r.lernender_id = p_l and r.art = 'normal' and r.status <> 'entfernt' and not (v_f.thema_id = any(coalesce(r.ausgelassen, '{}')));
      select fe.am into v_stempel from schule.flug_erstabschluss fe where fe.lernender_id = p_l and fe.einheit_id = v_e;
      v_golden := (v_stufe->>'etappen')::int > 0 and (v_stufe->>'sicher')::int = (v_stufe->>'etappen')::int;
      v_st := '[]'; v_offen := null;
      for v_s in select s.name, s.breite, s.laenge, s.geonames_id, s.lernziel, et.nr, et.titel, ks
                   from schule.reise_stadt s
                   join (select x->>'lernziel' lz, x->>'titel' titel, o::int nr from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]')) with ordinality q(x, o)
                          where e.id = v_e) et on et.lz = s.lernziel
                   left join schule.karte_stand ks on ks.lernender_id = p_l and ks.einheit_id = v_e and ks.lernziel = s.lernziel
                  where s.art = 'etappe' and s.thema_id = v_f.thema_id order by et.nr loop
        v_stand := schule.reise_etappe_stand(v_s.ks);
        v_pfl := v_pf is null or v_s.lernziel = any(v_pf);
        v_st := v_st || jsonb_build_object('nr', v_s.nr, 'name', v_s.name, 'breite', v_s.breite, 'laenge', v_s.laenge,
                                           'lernziel', v_s.lernziel, 'titel', v_s.titel, 'pflicht', v_pfl, 'stand', v_stand);
        if v_stand not in ('gelandet', 'sicher') and (v_offen is null or (v_pfl and not (v_offen->>'pflicht')::boolean)) then
          v_offen := jsonb_build_object('nr', v_s.nr, 'name', v_s.name, 'lernziel', v_s.lernziel, 'pflicht', v_pfl);
        end if;
      end loop;
      -- nächster Start: zuerst ein Flug „dran“, sonst der nächste „kommt“ im Plan; je nach Platz im Plan, dann Reihenfolge im Ort
      v_rang := case v_stufe->>'stufe' when 'dran' then 0 when 'kommt' then 1000000 end;
      if v_rang is not null and not v_f.zus then
        v_rang := v_rang + coalesce(v_platz, 99999) * 10 + coalesce(v_f.bt_folge, 9);
        if v_rang < v_best then
          v_best := v_rang;
          v_start := jsonb_build_object('thema_id', v_f.thema_id, 'kontinent_id', v_k.id, 'land', v_f.name, 'iso', v_f.iso, 'titel', v_f.titel,
                       'grund', v_stufe->>'stufe', 'stadt', coalesce(v_offen, (v_st->0) - array['breite', 'laenge', 'titel', 'stand']),
                       'staedte', jsonb_array_length(v_st));
        end if;
      end if;
      if v_f.zus then v_nzus := v_nzus + 1; else
        v_n := v_n + 1;
        if v_stufe->>'stufe' in ('komplett', 'wiederholung') then v_gesch := v_gesch + 1; end if;
      end if;
      v_fl := v_fl || jsonb_build_object(
        'thema_id', v_f.thema_id, 'flug', v_f.flug_schluessel, 'titel', v_f.titel, 'untertitel', v_f.untertitel,
        'teil', v_f.teil_nr, 'teil_von', v_f.teil_von, 'teil_stamm', v_f.teil_stamm,
        'land', v_f.name, 'iso', v_f.iso, 'region', v_f.region,
        'mitte', jsonb_build_object('breite', v_f.mitte_breite, 'laenge', v_f.mitte_laenge),
        'hauptstadt', jsonb_build_object('name', v_f.hauptstadt_name, 'breite', v_f.hauptstadt_breite, 'laenge', v_f.hauptstadt_laenge),
        'hauptort', v_f.hauptort,
        'kurzflug', v_f.kurzflug, 'insel_ausnahme', v_f.insel_ausnahme, 'nachbarteil', v_f.nachbarteil,
        'stufe', v_stufe->>'stufe', 'zeichen', v_stufe->>'zeichen', 'gesetzt', v_stufe->>'gesetzt',
        'stempel', v_stempel is not null, 'stempel_am', v_stempel, 'golden', v_golden,
        'im_plan', (v_stufe->>'im_plan')::boolean, 'plan_platz', v_platz, 'zusatz', v_f.zus,
        'etappen', (v_stufe->>'etappen')::int, 'gelandet', (v_stufe->>'gelandet')::int, 'sicher', (v_stufe->>'sicher')::int,
        'staedte', v_st);
    end loop;
    v_kont := v_kont || jsonb_build_object('id', v_k.id, 'schluessel', v_k.schluessel, 'themengebiet', v_k.titel, 'reise', v_k.reise, 'zusatz', v_k.zusatz,
                          'laender', v_n, 'geschafft', v_gesch, 'zusatz_laender', v_nzus, 'fluege', v_fl);
  end loop;
  return jsonb_build_object('gruppe', v_gr, 'kontinente', v_kont, 'naechster_start', v_start,
    'antarktis', jsonb_build_object('stationen', (select coalesce(jsonb_agg(jsonb_build_object('name', st.name, 'betreiber', st.betreiber, 'breite', st.breite, 'laenge', st.laenge,
                                     'expeditionen', (select jsonb_agg(x.schluessel order by x.schluessel) from schule.reise_station_expedition se join schule.expedition x on x.id = se.expedition_id
                                                       where se.station_id = st.id)) order by st.name), '[]') from schule.reise_station st)),
    'quellen', (select coalesce(jsonb_agg(jsonb_build_object('was', q.was, 'quelle', q.quelle, 'lizenz', q.lizenz, 'link', q.link) order by q.schluessel), '[]') from schule.reise_quelle q));
end $$;
revoke all on function schule.reise_karte(bigint) from public, anon, authenticated;

-- 9) Aktion für die App (Kind und Eltern/Lehrer mit Zugriff auf das Kind).
create or replace function api.schule_reise_karte(p_schluessel text, p_daten jsonb)
 returns jsonb language plpgsql stable security definer set search_path to ''
as $$
declare v_l bigint := nullif(p_daten->>'lernender_id', '')::bigint;
begin
  perform schule.zugriff(p_schluessel, v_l);
  if not exists (select 1 from schule.lernender where id = v_l and aktiv) then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  return jsonb_build_object('ok', true, 'lernender_id', v_l) || schule.reise_karte(v_l);
end $$;
grant execute on function api.schule_reise_karte(text, jsonb) to council_mcp;
revoke all on function api.schule_reise_karte(text, jsonb) from public, anon, authenticated;
