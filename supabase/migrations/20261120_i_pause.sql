-- Bau-Auftrag I, Teil 1, Punkt 10 (Sebastians Entscheidung 20.11.): Reisetage und Pausen eintragen.
-- Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE (Löschen = als gelöscht markieren; vergangene Einträge bleiben sichtbar).
--
-- Neu: Tabelle schule.pause (je Kind: von, bis, grund, wer, am; geaendert_am, geloescht_am).
--   Wirkung nur in der App-Anzeige „Lernt“ / „kein Lerntag seit …“ (Startseite, Zu tun, Überblick): eingetragene Tage zählen dort nicht.
--   Lernregeln, Wiederholungen und Nachtests bleiben unverändert (sie zählen ohnehin in Lerntagen).
-- Eintragen, ändern, löschen über die bestehende Aktion schule_notiz_setzen – keine neue Aktion in lernen-api:
--   {lernender_id, pause: {von, bis, grund?}}                 neuer Eintrag für dieses Kind
--   {alle: true, pause: {von, bis, grund?}}                    je ein Eintrag für jedes sichtbare Kind (ohne Testkinder)
--   {pause: {id, von, bis, grund?}}                            ändern;   {pause: {id, loeschen: true}}  löschen (markieren)
--   Nur Eltern/Lehrer (ist_leiter), Zugriff auf das Kind wird geprüft.
-- schule_lernstand liefert pausen[] (nicht gelöschte, neueste zuerst).

create table if not exists schule.pause (
  id bigint generated always as identity primary key,
  lernender_id bigint not null references schule.lernender(id),
  von date not null,
  bis date not null,
  grund text,
  wer text not null,
  am timestamptz not null default now(),
  geaendert_am timestamptz,
  geloescht_am timestamptz,
  constraint pause_zeitraum check (bis >= von and bis - von <= 366),
  constraint pause_grund check (grund is null or length(grund) between 1 and 40)
);
create index if not exists pause_kind on schule.pause (lernender_id, von);
alter table schule.pause enable row level security; -- nur über die api-Funktionen (security definer), wie die übrigen schule-Tabellen
comment on table schule.pause is 'I-10: Reisetage/Pausen je Kind – zählen nicht für „Lernt“/„kein Lerntag seit …“ in der App; Lernregeln unverändert';

create or replace function api.schule_notiz_setzen(p_schluessel text, p_daten jsonb)
 returns jsonb
 language plpgsql
 security definer
 set search_path to ''
as $function$
declare v_l bigint := nullif(p_daten->>'lernender_id','')::bigint; v_t text := trim(coalesce(p_daten->>'text','')); v_id bigint;
  v_p jsonb := p_daten->'pause'; v_von date; v_bis date; v_grund text; v_wer text; v_kinder bigint[]; v_kind bigint; v_alt schule.pause; v_neu bigint[] := '{}';
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  v_wer := coalesce((select i.rolle || ':' || i.name from schule.lern_ich(p_schluessel) i where schule.ist_lern(p_schluessel)), 'eltern:App');
  if p_daten ? 'pause' then -- I-10: Reisetage und Pausen
    if jsonb_typeof(v_p) is distinct from 'object' then raise exception 'pause muss ein Objekt sein' using errcode = 'P0001'; end if;
    if nullif(v_p->>'id', '') is not null then
      select * into v_alt from schule.pause where id = (v_p->>'id')::bigint and geloescht_am is null;
      if v_alt.id is null then raise exception 'Eintrag nicht gefunden' using errcode = 'P0001'; end if;
      perform schule.zugriff(p_schluessel, v_alt.lernender_id);
      if coalesce((v_p->>'loeschen')::boolean, false) then
        update schule.pause set geloescht_am = now(), geaendert_am = now() where id = v_alt.id;
        return jsonb_build_object('ok', true, 'geloescht', v_alt.id);
      end if;
    end if;
    begin
      v_von := (v_p->>'von')::date; v_bis := coalesce(nullif(v_p->>'bis', '')::date, v_von);
    exception when others then raise exception 'von/bis müssen Daten sein (JJJJ-MM-TT)' using errcode = 'P0001';
    end;
    if v_von is null or v_bis < v_von then raise exception 'Zeitraum: „bis“ darf nicht vor „von“ liegen' using errcode = 'P0001'; end if;
    if v_bis - v_von > 366 then raise exception 'Zeitraum höchstens ein Jahr' using errcode = 'P0001'; end if;
    v_grund := nullif(trim(coalesce(v_p->>'grund', '')), '');
    if length(v_grund) > 40 then raise exception 'Grund höchstens 40 Zeichen' using errcode = 'P0001'; end if;
    if v_alt.id is not null then
      update schule.pause set von = v_von, bis = v_bis, grund = v_grund, geaendert_am = now() where id = v_alt.id;
      return jsonb_build_object('ok', true, 'id', v_alt.id);
    end if;
    if coalesce((p_daten->>'alle')::boolean, false) then
      select coalesce(array_agg(l.id order by l.id), '{}') into v_kinder from schule.lernender l where l.aktiv and not l.ist_test and schule.sieht(p_schluessel, l.id);
    else
      perform schule.zugriff(p_schluessel, v_l);
      v_kinder := array[v_l];
    end if;
    if cardinality(v_kinder) = 0 then raise exception 'Kein Kind' using errcode = 'P0001'; end if;
    foreach v_kind in array v_kinder loop
      insert into schule.pause(lernender_id, von, bis, grund, wer) values (v_kind, v_von, v_bis, v_grund, v_wer) returning id into v_id;
      v_neu := v_neu || v_id;
    end loop;
    return jsonb_build_object('ok', true, 'ids', to_jsonb(v_neu));
  end if;
  if p_daten ? 'besprochen' then -- LA-3: Etappe besprochen
    perform schule.zugriff(p_schluessel, v_l);
    if nullif(p_daten->'besprochen'->>'einheit_id', '') is null or coalesce(p_daten->'besprochen'->>'lernziel', '') = '' then
      raise exception 'besprochen braucht einheit_id und lernziel' using errcode = 'P0001'; end if;
    insert into schule.besprochen(lernender_id, einheit_id, lernziel, von, am)
    values (v_l, (p_daten->'besprochen'->>'einheit_id')::bigint, p_daten->'besprochen'->>'lernziel', v_wer, now())
    on conflict (lernender_id, einheit_id, lernziel) do update set von = excluded.von, am = excluded.am;
    return jsonb_build_object('ok', true, 'besprochen_am', now());
  end if;
  if length(v_t) not between 1 and 2000 then raise exception 'Notiz leer oder zu lang' using errcode = 'P0001'; end if;
  insert into schule.notiz(lernender_id, text, von, am)
  values (v_l, v_t, v_wer, now())
  returning id into v_id;
  return jsonb_build_object('ok', true, 'id', v_id);
end $function$;

do $$
declare d text;
begin
  -- schule_lernstand: pausen[] des Kindes
  d := pg_get_functiondef('api.schule_lernstand(text, jsonb)'::regprocedure);
  if position('''lerntage'', (select coalesce(jsonb_agg(d.datum order by d.datum desc), ''[]''::jsonb)' in d) = 0 then raise exception 'Stelle in schule_lernstand nicht gefunden'; end if;
  if position('''pausen''' in d) > 0 then raise exception 'schule_lernstand liefert schon pausen'; end if;
  d := replace(d, '''lerntage'', (select coalesce(jsonb_agg(d.datum order by d.datum desc), ''[]''::jsonb)',
    $r$'pausen', (select coalesce(jsonb_agg(jsonb_build_object('id', pz.id, 'von', pz.von, 'bis', pz.bis, 'grund', pz.grund, 'wer', pz.wer, 'am', pz.am) order by pz.von desc, pz.id desc), '[]'::jsonb)
                  from schule.pause pz where pz.lernender_id = v_l and pz.geloescht_am is null),
    'lerntage', (select coalesce(jsonb_agg(d.datum order by d.datum desc), '[]'::jsonb)$r$);
  execute d;
end $$;
