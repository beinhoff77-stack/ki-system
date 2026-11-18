-- Bau-Auftrag G, Teil 4 (Werkstatt-Wunsch 176, P3): Expeditionen – Technik.
-- Nicht ausgeführt – der Haupt-Chat spielt ein. Setzt Teil 1 und Teil 3 voraus. Kein DROP von Tabellen, Spalten oder Funktionen, kein DELETE.
-- Ausnahme wie bei Migration F: aufgabe_pool_check und sterne_grund_check werden um je einen Wert erweitert (drop constraint + add constraint in einem Befehl; keine Daten betroffen).
--
-- Datenmodell (Entscheidung): Kopf in neuer Tabelle schule.expedition; jeder Teil ist eine Zeile in schule.aufgabe (pool 'expedition', expedition_id, teil).
-- Begründung: Teile sind Bordkarten mit denselben Antwortformen – Bewertung (schule.antwort_bewerten), zweiter Versuch, Lösung zeigen und schule.versuch (aufgabe_id ist Pflicht und
-- Fremdschlüssel) funktionieren unverändert; einheit_id/variante_gruppe des Teils zeigen auf die Etappe des Bezugs (Lernkarte), auf die Belege und Fälligkeit wirken.
-- Ein eigener Pool hält Teile aus allen Übungs-, Misch-, Wiederholungs- und Testauswahlen heraus (die filtern auf pool = 'uebung'/'test'/…).
-- aufgabe_schutz nimmt Expeditions-Teile aus (sonst könnte der Abgleich Teile nicht ändern, deren Bezugs-Etappe in einem freigegebenen Flug liegt).
--
-- Regeln:
--   angeboten, wenn ALLE Voraussetzungs-Lernkarten beim Kind gelandet sind (karte_stand.sitzt, jede Version der Einheit des Themas); Plan-Reihenfolge egal.
--   Entwürfe (status 'entwurf') nur für das Testkind.
--   Teil endgültig erledigt = richtig, oder 2. Versuch/Tipp gegeben (Lösung gezeigt). Der nächste Teil nennt seine Werte selbst (Format, Teil 2).
--   Teil richtig im 1. Versuch ohne Tipp → karte_stand.angewandt_am der Bezugs-Etappe („in neuer Aufgabe angewandt“, Anzeige kommt mit P5).
--   Teil endgültig falsch → Bezugs-Etappe am nächsten Lerntag fällig (wie eine falsche Mischkarte). Keine Minuspunkte.
--   Alle Teile erledigt → „geschafft“: Expeditions-Stempel und Sterne (Regel sterne_expedition_geschafft = 50; ein Ort bringt 100). Jeder richtige Teil bringt wie jede Bordkarte 10 Sterne.
--   Zählt nie für „gelandet“. Abbruch verliert nichts: der Stand steht in schule.versuch.
-- Neue Felder für die App (keine neue Aktion in lernen-api):
--   schule_konto: expeditionen = [{id, schluessel, titel, klasse, einleitung, grafik, zustand ('angeboten'|'begonnen'|'geschafft'), teile_gesamt, teile_erledigt,
--                 teile: [Bordkarte + k, erledigt, richtig_erst, loesung?, loesungsweg? (nur wenn erledigt)]}]; konto.expeditions_stempel
--   schule_uebung_pruefen nimmt Teile an (aufgabe_id eines Teils) und antwortet bei Expeditionen mit expedition: {id, teil, erledigt, geschafft, sterne}
--   schule_uebersicht: je Kind expeditionen = [{id, zustand}]; für Eltern/Lehrer oben expeditionen = alle mit Status, Voraussetzungen und Teilen (mit Lösung) für „Inhalte ansehen“
-- Import: schule.expedition_importieren(datei jsonb, status text default null) → neu anlegen oder abgleichen (nach schluessel bzw. Teil-Kennung k), nichts löschen;
--         Teile, die nicht mehr in der Datei stehen, werden gesperrt (freigegeben = false).

create table if not exists schule.expedition (
  id bigint generated always as identity primary key,
  schluessel text not null unique,
  klasse jsonb not null default '{}'::jsonb,
  titel text not null,
  einleitung text not null default '',
  grafik jsonb,
  voraussetzungen jsonb not null default '[]'::jsonb, -- [{thema_schluessel, thema_id, lernziel}]
  autor text,
  status text not null default 'entwurf' check (status in ('entwurf', 'geprueft', 'freigegeben')),
  version int not null default 1,
  angelegt_am timestamptz not null default now(),
  geaendert_am timestamptz not null default now()
);
comment on table schule.expedition is 'W176 P3: Expedition (größere Aufgabe aus 3–5 Teilen über mehrere Etappen); Teile in schule.aufgabe (pool expedition)';
alter table schule.expedition enable row level security; -- Zugriff nur über die api-Funktionen (security definer), wie die übrigen schule-Tabellen

alter table schule.aufgabe add column if not exists expedition_id bigint references schule.expedition(id);
alter table schule.aufgabe add column if not exists teil text;
create unique index if not exists aufgabe_expedition_teil on schule.aufgabe(expedition_id, teil) where expedition_id is not null;
alter table schule.aufgabe drop constraint if exists aufgabe_pool_check,
  add constraint aufgabe_pool_check check (pool = any (array['uebung', 'test', 'korrektur', 'sicherung', 'bonus', 'expedition']));
alter table schule.sterne drop constraint if exists sterne_grund_check,
  add constraint sterne_grund_check check (grund = any (array['uebung', 'test', 'ort', 'einloesung', 'korrektur_hand', 'bonus', 'expedition']));
alter table schule.karte_stand add column if not exists angewandt_am timestamptz;
comment on column schule.karte_stand.angewandt_am is 'W176 P3: zuletzt in einer Expedition richtig angewandt (1. Versuch ohne Tipp); Anzeige mit P5';
insert into schule.regel(schluessel, wert, hinweis) values ('sterne_expedition_geschafft', '50'::jsonb, 'W176: Expedition geschafft (alle Teile erledigt) – Vorschlag; ein Ort bringt 100')
  on conflict (schluessel) do nothing;

-- Expeditions-Teile dürfen abgeglichen werden, auch wenn ihre Bezugs-Etappe in einem freigegebenen Flug liegt
create or replace function schule.aufgabe_schutz()
 returns trigger
 language plpgsql
as $function$
begin
  if coalesce(new.pool, old.pool) = 'expedition' and coalesce(old.pool, new.pool) = 'expedition' then return coalesce(new, old); end if;
  if exists (select 1 from schule.einheit e where e.id = coalesce(old.einheit_id, new.einheit_id) and e.status = 'freigegeben') then
    raise exception 'Aufgaben einer freigegebenen Einheit sind unveränderlich';
  end if;
  return coalesce(new, old);
end $function$;

-- ---------- Import / Abgleich ----------
create or replace function schule.expedition_importieren(p jsonb, p_status text default null)
 returns jsonb
 language plpgsql
 security definer
 set search_path to ''
as $function$
declare v_id bigint; v_vor jsonb := '[]'::jsonb; v jsonb; t jsonb; v_t bigint; v_e bigint; v_a bigint; v_neu int := 0; v_geaendert int := 0; v_gesperrt int; v_ks text[] := '{}'; v_nr int := 0;
  v_alt schule.expedition;
begin
  if p_status is not null and p_status not in ('entwurf', 'geprueft', 'freigegeben') then raise exception 'p_status: entwurf, geprueft oder freigegeben'; end if;
  if coalesce(p->>'schluessel', '') = '' or jsonb_typeof(p->'teile') is distinct from 'array' then raise exception 'Datei unvollständig (schluessel, teile)'; end if;
  for v in select * from jsonb_array_elements(coalesce(p->'voraussetzungen', '[]'::jsonb)) loop
    select id into v_t from schule.thema where schluessel = v->>'thema_schluessel';
    if v_t is null then raise exception 'Voraussetzung: Thema % gibt es nicht', v->>'thema_schluessel'; end if;
    v_vor := v_vor || jsonb_build_object('thema_schluessel', v->>'thema_schluessel', 'thema_id', v_t, 'lernziel', v->>'lernziel');
  end loop;
  select * into v_alt from schule.expedition where schluessel = p->>'schluessel';
  if v_alt.id is null then
    insert into schule.expedition(schluessel, klasse, titel, einleitung, grafik, voraussetzungen, autor, status)
    values (p->>'schluessel', coalesce(p->'klasse', '{}'), p->>'titel', coalesce(p->>'einleitung', ''), p->'grafik', v_vor, p->>'autor', coalesce(p_status, 'entwurf'))
    returning id into v_id;
  else
    v_id := v_alt.id;
    update schule.expedition set klasse = coalesce(p->'klasse', '{}'), titel = p->>'titel', einleitung = coalesce(p->>'einleitung', ''), grafik = p->'grafik', voraussetzungen = v_vor,
           autor = p->>'autor', status = coalesce(p_status, status), version = version + 1, geaendert_am = now()
     where id = v_id and (klasse, titel, einleitung, grafik, voraussetzungen, autor, status) is distinct from
           (coalesce(p->'klasse', '{}'), p->>'titel', coalesce(p->>'einleitung', ''), p->'grafik', v_vor, p->>'autor', coalesce(p_status, status));
  end if;
  for t in select * from jsonb_array_elements(p->'teile') loop
    v_nr := v_nr + 1; v_ks := v_ks || (t->>'k');
    select id into v_t from schule.thema where schluessel = t->'bezug'->>'thema_schluessel';
    if v_t is null then raise exception 'Teil %: Bezug-Thema % gibt es nicht', t->>'k', t->'bezug'->>'thema_schluessel'; end if;
    select e.id into v_e from schule.einheit e where e.thema_id = v_t and e.status <> 'ersetzt'
     order by (e.status in ('freigegeben', 'geprueft')) desc, e.version desc limit 1;
    if v_e is null then raise exception 'Teil %: zum Thema % gibt es keinen Flug', t->>'k', t->'bezug'->>'thema_schluessel'; end if;
    select id into v_a from schule.aufgabe where expedition_id = v_id and teil = t->>'k';
    if v_a is null then
      insert into schule.aufgabe(einheit_id, thema_id, teilfaehigkeit, art, stufe, variante_gruppe, antworttyp, frage, antworten, loesung, tipp, loesungsweg, punkte_max, reihenfolge, pool,
                                 expedition_id, teil, freigegeben)
      values (v_e, v_t, null, 'uebung', null, t->'bezug'->>'lernziel', t->>'y', t->'f', case when t ? 'a' then t->'a' end, t->'o', t->>'h', t->>'w', 1, v_nr, 'expedition', v_id, t->>'k', true);
      v_neu := v_neu + 1;
    else
      update schule.aufgabe set einheit_id = v_e, thema_id = v_t, variante_gruppe = t->'bezug'->>'lernziel', antworttyp = t->>'y', frage = t->'f',
             antworten = case when t ? 'a' then t->'a' end, loesung = t->'o', tipp = t->>'h', loesungsweg = t->>'w', reihenfolge = v_nr, freigegeben = true
       where id = v_a and (einheit_id, thema_id, variante_gruppe, antworttyp, frage, antworten, loesung, tipp, loesungsweg, reihenfolge, freigegeben) is distinct from
             (v_e, v_t, t->'bezug'->>'lernziel', t->>'y', t->'f', case when t ? 'a' then t->'a' end, t->'o', t->>'h', t->>'w', v_nr, true);
      if found then v_geaendert := v_geaendert + 1; end if;
    end if;
  end loop;
  update schule.aufgabe set freigegeben = false where expedition_id = v_id and freigegeben and not (teil = any(v_ks));
  get diagnostics v_gesperrt = row_count;
  return jsonb_build_object('expedition_id', v_id, 'schluessel', p->>'schluessel', 'teile_neu', v_neu, 'teile_geaendert', v_geaendert, 'teile_gesperrt', v_gesperrt,
    'status', (select status from schule.expedition where id = v_id));
end $function$;

-- ---------- Zustand je Kind ----------
create or replace function schule.expedition_sichtbar(p_lernender bigint, x schule.expedition)
 returns boolean language sql stable set search_path to ''
as $function$
  select x.status in ('geprueft', 'freigegeben') or (x.status = 'entwurf' and coalesce((select ist_test from schule.lernender where id = p_lernender), false));
$function$;

create or replace function schule.expedition_voraussetzungen_ok(p_lernender bigint, x schule.expedition)
 returns boolean language sql stable set search_path to ''
as $function$
  select jsonb_array_length(x.voraussetzungen) > 0 and not exists (
    select 1 from jsonb_array_elements(x.voraussetzungen) v
     where not exists (select 1 from schule.karte_stand k join schule.einheit e on e.id = k.einheit_id
                        where k.lernender_id = p_lernender and k.sitzt and e.thema_id = (v->>'thema_id')::bigint and k.lernziel = v->>'lernziel'));
$function$;

-- erledigt = richtig, oder endgültig (2. Versuch bzw. ohne zweite Chance, Lösung gezeigt)
create or replace function schule.expedition_teil_erledigt(p_lernender bigint, p_aufgabe bigint)
 returns boolean language sql stable set search_path to ''
as $function$
  select exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = p_aufgabe and v.testsitzung_id is null
                  and (v.richtig or coalesce(v.anlauf, 0) <> 1));
$function$;

create or replace function schule.expedition_zustand(p_lernender bigint, x schule.expedition)
 returns text language sql stable set search_path to ''
as $function$
  with t as (select a.id, schule.expedition_teil_erledigt(p_lernender, a.id) erl,
                    exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id) ber
               from schule.aufgabe a where a.expedition_id = x.id and a.freigegeben)
  select case when (select count(*) from t) > 0 and (select bool_and(erl) from t) then 'geschafft'
              when (select bool_or(ber) from t) then 'begonnen'
              when schule.expedition_voraussetzungen_ok(p_lernender, x) then 'angeboten'
              else null end;
$function$;

-- Expeditionen für die Kinderansicht: angebotene, begonnene und geschaffte (sichtbar je Status)
create or replace function schule.expeditionen_kind(p_lernender bigint)
 returns jsonb language sql stable set search_path to ''
as $function$
  select coalesce(jsonb_agg(jsonb_build_object('id', x.id, 'schluessel', x.schluessel, 'titel', x.titel, 'klasse', x.klasse, 'einleitung', x.einleitung, 'grafik', x.grafik,
      'zustand', z.zustand, 'status', x.status,
      'teile', (select coalesce(jsonb_agg(schule.aufgabe_anzeige(a, true) || jsonb_build_object('k', a.teil, 'erledigt', te.erl,
                   'richtig_erst', exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id and v.richtig and coalesce(v.hilfe, 0) = 0 and coalesce(v.anlauf, 1) = 1))
                   || case when te.erl then jsonb_build_object('loesung', a.loesung, 'loesungsweg', a.loesungsweg) else '{}'::jsonb end order by a.reihenfolge, a.id), '[]'::jsonb)
                from schule.aufgabe a cross join lateral (select schule.expedition_teil_erledigt(p_lernender, a.id) erl) te
               where a.expedition_id = x.id and a.freigegeben),
      'teile_gesamt', (select count(*) from schule.aufgabe a where a.expedition_id = x.id and a.freigegeben),
      'teile_erledigt', (select count(*) from schule.aufgabe a where a.expedition_id = x.id and a.freigegeben and schule.expedition_teil_erledigt(p_lernender, a.id)))
      order by case z.zustand when 'begonnen' then 1 when 'angeboten' then 2 else 3 end, x.id), '[]'::jsonb)
    from schule.expedition x cross join lateral (select schule.expedition_zustand(p_lernender, x) zustand) z
   where schule.expedition_sichtbar(p_lernender, x) and z.zustand is not null;
$function$;

-- Für Eltern/Lehrer: alle Expeditionen lesbar (mit Lösungen)
create or replace function schule.expeditionen_alle()
 returns jsonb language sql stable set search_path to ''
as $function$
  select coalesce(jsonb_agg(jsonb_build_object('id', x.id, 'schluessel', x.schluessel, 'titel', x.titel, 'klasse', x.klasse, 'einleitung', x.einleitung, 'grafik', x.grafik,
      'status', x.status, 'version', x.version, 'autor', x.autor, 'voraussetzungen', x.voraussetzungen,
      'teile', (select coalesce(jsonb_agg(jsonb_build_object('id', a.id, 'k', a.teil, 'antworttyp', a.antworttyp, 'frage', a.frage, 'antworten', a.antworten, 'loesung', a.loesung,
                   'tipp', a.tipp, 'loesungsweg', a.loesungsweg, 'lernziel', a.variante_gruppe, 'thema_id', a.thema_id) order by a.reihenfolge, a.id), '[]'::jsonb)
                from schule.aufgabe a where a.expedition_id = x.id and a.freigegeben)) order by x.schluessel), '[]'::jsonb)
    from schule.expedition x;
$function$;

-- ---------- Buchung eines Teils (über den Trigger versuch_karte) ----------
create or replace function schule.expedition_buchen(p_l bigint, p_aufgabe bigint, p_richtig boolean, p_hilfe smallint, p_anlauf smallint, p_zeit timestamp with time zone)
 returns void
 language plpgsql
 set search_path to ''
as $function$
declare a schule.aufgabe; v_proxy bigint;
begin
  select * into a from schule.aufgabe where id = p_aufgabe;
  if a.id is null or a.pool <> 'expedition' then return; end if;
  if p_richtig then
    if coalesce(p_hilfe, 0) = 0 and coalesce(p_anlauf, 1) = 1 then
      update schule.karte_stand set angewandt_am = p_zeit where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe;
    end if;
  else
    -- Bezugs-Etappe am nächsten Lerntag fällig: wie ein Fehler in der Wiederholung, gebucht über eine Übung dieser Etappe
    select id into v_proxy from schule.aufgabe where einheit_id = a.einheit_id and variante_gruppe = a.variante_gruppe and pool = 'uebung' order by freigegeben desc, id limit 1;
    if v_proxy is not null and exists (select 1 from schule.karte_stand k where k.lernender_id = p_l and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe and k.sitzt) then
      perform schule.karte_buchen(p_l, v_proxy, false, 0::smallint, p_zeit);
    end if;
  end if;
  -- alle Teile erledigt → geschafft: Stempel und Sterne (je Expedition einmal)
  if not exists (select 1 from schule.aufgabe t where t.expedition_id = a.expedition_id and t.freigegeben and not schule.expedition_teil_erledigt(p_l, t.id)) then
    insert into schule.sterne(lernender_id, menge, grund, bezug)
    values (p_l, schule.sterne_regel('sterne_expedition_geschafft'), 'expedition', 'expedition:' || a.expedition_id)
    on conflict do nothing;
  end if;
end $function$;

create or replace function schule.versuch_karte()
 returns trigger
 language plpgsql
 set search_path to ''
as $function$
begin
  if new.testsitzung_id is null and not (coalesce(new.anlauf, 0) = 1 and not new.richtig) then
    if new.misch then perform schule.misch_buchen(new.lernender_id, new.aufgabe_id, new.richtig, new.hilfe, now());
    else perform schule.karte_buchen(new.lernender_id, new.aufgabe_id, new.richtig, new.hilfe, now()); end if;
    perform schule.expedition_buchen(new.lernender_id, new.aufgabe_id, new.richtig, new.hilfe, new.anlauf, now()); -- prüft selbst den Pool
  end if;
  return new;
end $function$;

-- ---------- Antworten an die App (gezieltes Ersetzen; Stellen im Live-Text vorab geprüft) ----------
do $$
declare d text;
begin
  d := pg_get_functiondef('schule.uebung_pruefen_intern(bigint, jsonb)'::regprocedure);
  if position('if a.id is null or a.pool not in (''uebung'', ''bonus'') then raise exception ''Keine Übungsaufgabe'' using errcode = ''P0001''; end if;' in d) = 0
     or position('  if coalesce((p_daten->>''misch'')::boolean, false) and a.pool = ''uebung'' then' in d) = 0 then
    raise exception 'Stellen in uebung_pruefen_intern nicht gefunden (Teil 3 eingespielt?)';
  end if;
  d := replace(d, 'if a.id is null or a.pool not in (''uebung'', ''bonus'') then raise exception ''Keine Übungsaufgabe'' using errcode = ''P0001''; end if;',
    $r$if a.id is null or a.pool not in ('uebung', 'bonus', 'expedition') then raise exception 'Keine Übungsaufgabe' using errcode = 'P0001'; end if;
  if a.pool = 'expedition' and not exists (select 1 from schule.expedition x where x.id = a.expedition_id and schule.expedition_sichtbar(p_lernender, x)) then
    raise exception 'Diese Expedition ist noch nicht freigegeben' using errcode = 'P0001';
  end if;$r$);
  d := replace(d, '  if coalesce((p_daten->>''misch'')::boolean, false) and a.pool = ''uebung'' then',
    $r$  if a.pool = 'expedition' then
    return jsonb_strip_nulls(jsonb_build_object('ok', true, 'format_ok', true, 'richtig', v_ri, 'grund', b->>'grund', 'loesung', a.loesung, 'loesungsweg', a.loesungsweg,
      'expedition', jsonb_build_object('id', a.expedition_id, 'teil', a.teil, 'erledigt', true,
        'geschafft', not exists (select 1 from schule.aufgabe t where t.expedition_id = a.expedition_id and t.freigegeben and not schule.expedition_teil_erledigt(p_lernender, t.id)),
        'sterne', coalesce((select s.menge from schule.sterne s where s.lernender_id = p_lernender and s.grund = 'expedition' and s.bezug = 'expedition:' || a.expedition_id), 0))));
  end if;
  if coalesce((p_daten->>'misch')::boolean, false) and a.pool = 'uebung' then$r$);
  execute d;

  d := pg_get_functiondef('api.schule_konto(text, jsonb)'::regprocedure);
  if position('''knobel_tag'', case when' in d) = 0 then raise exception 'Stelle in api.schule_konto nicht gefunden'; end if;
  d := replace(d, '''knobel_tag'', case when', '''expeditionen'', schule.expeditionen_kind(v_l),
    ''knobel_tag'', case when');
  execute d;

  d := pg_get_functiondef('schule.konto(bigint)'::regprocedure);
  if position('''knobel_sterne'', (select count(*) from schule.sterne where lernender_id = p_lernender and grund = ''bonus''),' in d) = 0 then raise exception 'Stelle in schule.konto nicht gefunden'; end if;
  d := replace(d, '''knobel_sterne'', (select count(*) from schule.sterne where lernender_id = p_lernender and grund = ''bonus''),',
    '''knobel_sterne'', (select count(*) from schule.sterne where lernender_id = p_lernender and grund = ''bonus''),
    ''expeditions_stempel'', (select count(*) from schule.sterne where lernender_id = p_lernender and grund = ''expedition''),');
  execute d;

  d := pg_get_functiondef('api.schule_uebersicht(text, jsonb)'::regprocedure);
  if position('''stufen'', l.stufen,' in d) = 0 or position('''themen'', v_th);' in d) = 0 then raise exception 'Stellen in schule_uebersicht nicht gefunden'; end if;
  d := replace(d, '''stufen'', l.stufen,', $r$'stufen', l.stufen,
      'expeditionen', (select coalesce(jsonb_agg(jsonb_build_object('id', x.id, 'zustand', z.zustand) order by x.id), '[]'::jsonb)
                         from schule.expedition x cross join lateral (select schule.expedition_zustand(l.id, x) zustand) z
                        where schule.expedition_sichtbar(l.id, x) and z.zustand is not null),$r$);
  d := replace(d, '''themen'', v_th);', '''themen'', v_th, ''expeditionen'', case when v_leiter then schule.expeditionen_alle() end);');
  execute d;
end $$;
