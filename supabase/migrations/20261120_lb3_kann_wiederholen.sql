-- Bau-Auftrag LB, LB-3 Serverteil (20.11., von Sebastian bestätigt, ohne Vortest): „Kann er – aber wiederholen“, „Wieder in die Wiederholung“, Sammelaktionen, 4 Stufen.
-- Vorgabe: inhalte/pruefung/lehrer/umsetzung-lb.md (Abschnitte „Die 4 Stufen“ und LB-3). Nach 20261120_i3_lernregeln_nachpruefung.sql.
-- Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE (auch keine Versuche), keine Änderung am Bestand. Wiederholt ausführbar.
--
-- Neu
--   route.kann_wdh_themen bigint[]            Flüge „Kann er – aber wiederholen“ je Kind und Ort (wie kann_schon_themen)
--   karte_stand.gesetzt_am / gesetzt_von      Herkunft „gesetzt“ einer Landung (durch kann_wdh); null = selbst gelandet
--   schule.plan_setzen_intern(kind, daten, akteur)   der ganze Plan-Schritt (api.schule_plan_setzen ruft ihn nach der Zugriffsprüfung)
--     Eintrag zusätzlich: kann_wdh_themen [ids] (Zustand), wieder_wdh_themen [ids] (Aktion „Wieder in die Wiederholung“)
--     daten zusätzlich: rueckgaengig = schritt_id (stellt die Karten-Stände dieses Schritts wieder her; zusammen mit den Einträgen von davor)
--     Antwort zusätzlich: schritt_id
--   schule.thema_stufe(kind, thema) jsonb      die 4 Stufen nach der Tabelle des Gestalters (Server rechnet, App zeigt)
--   schule.thema_kann_wdh, schule.flug_ohne_test, schule.thema_einheit, schule.karte_lage,
--   schule.flug_wdh_setzen, schule.flug_wdh_zuruecknehmen, schule.flug_wieder_wdh, schule.karten_wiederherstellen
-- Geändert
--   thema_stand / ort_stand: kann_wdh zählt als erledigt (gelandet), außer eine Etappe ist wieder offen
--   karte_sicher: gesetzte Etappe sicher = gelandet + Wiederholung nach 14 Lerntagen + Mischkarte richtig, falls seit der Landung eine ausgegeben wurde (kein Nachtest)
--   flug_nachtest: null („entfällt“) für kann_wdh-Flüge; nachtest_stand: grund 'gesetzt'; test_starten_intern: kein Flug-Test/Nachtest (ok=false, grund nichts_zu_testen, gesetzt=true)
--   schule_plan_lesen: plan[].kann_wdh_themen, themen[].kann_wdh, themen[].stufe, kann_wdh: true (Merkmal für die App)
--   schule_lernstand: einheiten[].thema_id, einheiten[].stufe, karten[].gesetzt, karten[].gesetzt_am
--   schule_lehrplan_uebersicht: themen[].stufe {kind_id: stufe}
--   schule_uebersicht: route[].kann_wdh_themen, stand[].ohne_test; einheit_lesen_intern: ohne_test

-- ---------- Spalten ----------
alter table schule.route add column if not exists kann_wdh_themen bigint[] not null default '{}';
comment on column schule.route.kann_wdh_themen is 'LB-3: Flüge „Kann er – aber wiederholen“ (gesetzt gelandet, Wiederholung ab Stufe 1, kein Flug-Test/Nachtest)';
alter table schule.karte_stand add column if not exists gesetzt_am timestamptz;
alter table schule.karte_stand add column if not exists gesetzt_von text;
comment on column schule.karte_stand.gesetzt_am is 'LB-3: Landung vom Lehrer gesetzt („Kann er – aber wiederholen“); null = selbst gelandet';

-- ---------- Hilfen ----------
create or replace function schule.thema_einheit(p_thema bigint)
 returns bigint language sql stable set search_path to ''
as $function$
  select e.id from schule.einheit e where e.thema_id = p_thema and e.status in ('geprueft', 'freigegeben') order by e.version desc limit 1;
$function$;

create or replace function schule.thema_kann_wdh(p_l bigint, p_thema bigint)
 returns boolean language sql stable set search_path to ''
as $function$
  select exists (select 1 from schule.route r join schule.block_thema bt on bt.block_id = r.block_id and bt.thema_id = p_thema
                  where r.lernender_id = p_l and r.art = 'normal' and r.status <> 'entfernt' and not (p_thema = any(r.ausgelassen))
                    and p_thema = any(r.kann_wdh_themen));
$function$;

create or replace function schule.flug_ohne_test(p_l bigint, p_einheit bigint)
 returns boolean language sql stable set search_path to ''
as $function$
  select coalesce(schule.thema_kann_wdh(p_l, (select e.thema_id from schule.einheit e where e.id = p_einheit)), false);
$function$;

create or replace function schule.karte_lage(k schule.karte_stand)
 returns jsonb language sql immutable set search_path to ''
as $function$
  select jsonb_build_object('sitzt', k.sitzt, 'sitzt_am', k.sitzt_am, 'wdh_stufe', k.wdh_stufe, 'faellig_am', k.faellig_am, 'wdh_fehler', k.wdh_fehler,
    'wdh_ab', k.wdh_ab, 'wdh_lerntage', k.wdh_lerntage, 'gesetzt_am', k.gesetzt_am, 'gesetzt_von', k.gesetzt_von);
$function$;

-- setzt alle noch nicht gelandeten Etappen des Flugs auf gelandet (Herkunft „gesetzt“), Wiederholung ab Stufe 1; gibt die Lage davor zurück
create or replace function schule.flug_wdh_setzen(p_l bigint, p_thema bigint, p_wer text)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_e bigint := schule.thema_einheit(p_thema); v_lz text; v_vor schule.karte_stand; v_snap jsonb := '[]'::jsonb;
begin
  if v_e is null then return v_snap; end if;
  perform schule.lernziele_anlegen(p_l, v_e);
  for v_lz in select x->>'lernziel' from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) x where e.id = v_e loop
    v_vor := null;
    select * into v_vor from schule.karte_stand where lernender_id = p_l and einheit_id = v_e and lernziel = v_lz for update;
    if v_vor.lernender_id is not null and v_vor.sitzt then continue; end if; -- schon gelandet: bleibt unberührt
    v_snap := v_snap || jsonb_build_object('einheit_id', v_e, 'lernziel', v_lz, 'vorher', case when v_vor.lernender_id is null then null else schule.karte_lage(v_vor) end);
    insert into schule.karte_stand(lernender_id, einheit_id, lernziel) values (p_l, v_e, v_lz) on conflict do nothing;
    update schule.karte_stand set sitzt = true, sitzt_am = now(), wdh_stufe = 0, faellig_am = now() + interval '1 day', wdh_fehler = 0,
           wdh_ab = now(), wdh_lerntage = 1, gesetzt_am = now(), gesetzt_von = p_wer
     where lernender_id = p_l and einheit_id = v_e and lernziel = v_lz;
  end loop;
  return v_snap;
end $function$;

-- Rücknahme: gesetzte Landungen ohne eigene Versuche seither aufheben; mit eigenen Versuchen bleibt der Stand (nur die Herkunft „gesetzt“ fällt weg)
create or replace function schule.flug_wdh_zuruecknehmen(p_l bigint, p_thema bigint)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare k schule.karte_stand; v_snap jsonb := '[]'::jsonb;
begin
  for k in select ks.* from schule.karte_stand ks join schule.einheit e on e.id = ks.einheit_id
            where ks.lernender_id = p_l and e.thema_id = p_thema and ks.gesetzt_am is not null for update of ks loop
    v_snap := v_snap || jsonb_build_object('einheit_id', k.einheit_id, 'lernziel', k.lernziel, 'vorher', schule.karte_lage(k));
    if exists (select 1 from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                where v.lernender_id = p_l and v.testsitzung_id is null and a.einheit_id = k.einheit_id and a.variante_gruppe = k.lernziel and v.am >= k.gesetzt_am) then
      update schule.karte_stand set gesetzt_am = null, gesetzt_von = null where lernender_id = p_l and einheit_id = k.einheit_id and lernziel = k.lernziel;
    else
      update schule.karte_stand set sitzt = false, sitzt_am = null, wdh_stufe = 0, faellig_am = null, wdh_fehler = 0, wdh_ab = null, wdh_lerntage = null,
             gesetzt_am = null, gesetzt_von = null
       where lernender_id = p_l and einheit_id = k.einheit_id and lernziel = k.lernziel;
    end if;
  end loop;
  return v_snap;
end $function$;

-- „Wieder in die Wiederholung“: gelandete Etappen des Flugs starten erneut bei Stufe 1 (fällig am nächsten Lerntag); gelandet, Belege und Verlauf bleiben
create or replace function schule.flug_wieder_wdh(p_l bigint, p_thema bigint)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare k schule.karte_stand; v_snap jsonb := '[]'::jsonb; v_e bigint := schule.thema_einheit(p_thema);
begin
  for k in select ks.* from schule.karte_stand ks where ks.lernender_id = p_l and ks.einheit_id = v_e and ks.sitzt for update loop
    v_snap := v_snap || jsonb_build_object('einheit_id', k.einheit_id, 'lernziel', k.lernziel, 'vorher', schule.karte_lage(k));
    update schule.karte_stand set wdh_stufe = 0, faellig_am = now() + interval '1 day', wdh_fehler = 0, wdh_ab = now(), wdh_lerntage = 1
     where lernender_id = p_l and einheit_id = k.einheit_id and lernziel = k.lernziel;
  end loop;
  return v_snap;
end $function$;

-- Rückgängig eines Schritts: Lage davor wiederherstellen, aber nur für Etappen ohne eigene Versuche seit dem Schritt
create or replace function schule.karten_wiederherstellen(p_l bigint, p_karten jsonb, p_seit timestamptz)
 returns integer language plpgsql set search_path to ''
as $function$
declare v_w jsonb; v_vor jsonb; n_zurueck int := 0;
begin
  for v_w in select q.eintrag from jsonb_array_elements(coalesce(p_karten, '[]'::jsonb)) with ordinality q(eintrag, nr) order by q.nr desc loop -- rückwärts: die früheste Lage gilt
    if exists (select 1 from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                where v.lernender_id = p_l and v.testsitzung_id is null and a.einheit_id = (v_w->>'einheit_id')::bigint and a.variante_gruppe = v_w->>'lernziel' and v.am >= p_seit) then
      continue; -- das Kind hat seither etwas gezeigt: Stand bleibt
    end if;
    v_vor := v_w->'vorher';
    if v_vor is null or jsonb_typeof(v_vor) = 'null' then
      update schule.karte_stand set sitzt = false, sitzt_am = null, wdh_stufe = 0, faellig_am = null, wdh_fehler = 0, wdh_ab = null, wdh_lerntage = null, gesetzt_am = null, gesetzt_von = null
       where lernender_id = p_l and einheit_id = (v_w->>'einheit_id')::bigint and lernziel = v_w->>'lernziel';
    else
      update schule.karte_stand set sitzt = coalesce((v_vor->>'sitzt')::boolean, false), sitzt_am = (v_vor->>'sitzt_am')::timestamptz, wdh_stufe = coalesce((v_vor->>'wdh_stufe')::smallint, 0),
             faellig_am = (v_vor->>'faellig_am')::timestamptz, wdh_fehler = coalesce((v_vor->>'wdh_fehler')::smallint, 0), wdh_ab = (v_vor->>'wdh_ab')::timestamptz,
             wdh_lerntage = (v_vor->>'wdh_lerntage')::smallint, gesetzt_am = (v_vor->>'gesetzt_am')::timestamptz, gesetzt_von = v_vor->>'gesetzt_von'
       where lernender_id = p_l and einheit_id = (v_w->>'einheit_id')::bigint and lernziel = v_w->>'lernziel';
    end if;
    n_zurueck := n_zurueck + 1;
  end loop;
  return n_zurueck;
end $function$;

-- ---------- Regeln: Stand, sicher, kein Test ----------
create or replace function schule.thema_stand(p_l bigint, p_thema bigint)
 returns text language sql stable set search_path to ''
as $function$
  with e as (select id from schule.einheit where thema_id = p_thema and status in ('geprueft','freigegeben') order by version desc limit 1)
  select case when exists (select 1 from schule.route r where r.lernender_id = p_l and r.art = 'normal' and r.status <> 'entfernt' and p_thema = any(r.kann_schon_themen)) then 'erledigt' -- LA-4
    when schule.thema_kann_wdh(p_l, p_thema) then -- LB-3: gesetzt gelandet; eine wieder offene Etappe macht ihn wieder „läuft“
      case when exists (select 1 from schule.karte_stand k join e on e.id = k.einheit_id where k.lernender_id = p_l and not k.sitzt and k.sitzt_am is not null) then 'laeuft' else 'erledigt' end
    when not exists (select 1 from e) then 'keine_einheit'
    when exists (select 1 from schule.lernziel_stand s join e on e.id = s.einheit_id where s.lernender_id = p_l)
      and not exists (select 1 from schule.lernziel_stand s join e on e.id = s.einheit_id where s.lernender_id = p_l and s.pflicht and s.status not in ('nachgewiesen','korrigiert','gesichert'))
      then 'erledigt'
    when exists (select 1 from schule.karte_stand k join e on e.id = k.einheit_id where k.lernender_id = p_l)
      or exists (select 1 from schule.lernziel_stand s join e on e.id = s.einheit_id where s.lernender_id = p_l and s.status <> 'offen') then 'laeuft'
    else 'offen' end;
$function$;

create or replace function schule.ort_stand(p_lernender bigint, p_block bigint)
 returns jsonb language sql stable set search_path to ''
as $function$
  with aus as (
    select coalesce((select r.ausgelassen from schule.route r where r.lernender_id = p_lernender and r.block_id = p_block and r.art = 'normal' and r.status <> 'entfernt'
                     order by r.id limit 1), '{}'::bigint[]) as liste,
           coalesce((select r.kann_schon_themen from schule.route r where r.lernender_id = p_lernender and r.block_id = p_block and r.art = 'normal' and r.status <> 'entfernt'
                     order by r.id limit 1), '{}'::bigint[]) as kann,
           coalesce((select r.kann_wdh_themen from schule.route r where r.lernender_id = p_lernender and r.block_id = p_block and r.art = 'normal' and r.status <> 'entfernt'
                     order by r.id limit 1), '{}'::bigint[]) as kw
  ), th as (
    select bt.thema_id, t.schluessel, aus.kann, aus.kw,
      (select e.id from schule.einheit e where e.thema_id = bt.thema_id and e.status in ('geprueft','freigegeben') order by e.version desc limit 1) as einheit_id
    from schule.block_thema bt join schule.thema t on t.id = bt.thema_id, aus
    where bt.block_id = p_block and not (bt.thema_id = any(aus.liste))
  ), st as (
    select th.*, case when th.thema_id = any(th.kann) then 'erledigt' -- LA-4
      when th.thema_id = any(th.kw) then -- LB-3: zählt als gelandet, außer eine Etappe ist wieder offen
        case when exists (select 1 from schule.karte_stand k where k.lernender_id = p_lernender and k.einheit_id = th.einheit_id and not k.sitzt and k.sitzt_am is not null) then 'offen' else 'erledigt' end
      when th.einheit_id is null then 'keine_einheit'
      when not exists (select 1 from schule.lernziel_stand s where s.lernender_id = p_lernender and s.einheit_id = th.einheit_id) then 'offen'
      when exists (select 1 from schule.lernziel_stand s where s.lernender_id = p_lernender and s.einheit_id = th.einheit_id and s.pflicht and s.status not in ('nachgewiesen','korrigiert','gesichert')) then 'offen'
      else 'erledigt' end as zustand
    from th
  )
  select jsonb_build_object('block_id', p_block, 'abgeschlossen', coalesce(bool_and(zustand = 'erledigt'), false) and count(*) > 0,
    'themen', coalesce(jsonb_agg(jsonb_build_object('thema', schluessel, 'einheit_id', einheit_id, 'zustand', zustand)), '[]'))
  from st;
$function$;

create or replace function schule.karte_sicher(k schule.karte_stand)
 returns boolean language sql stable set search_path to ''
as $function$
  select coalesce(k.sitzt, false) and coalesce(k.wdh_stufe, 0) >= 4
     and case when k.gesetzt_am is not null then -- LB-3: gesetzt – kein Nachtest; Mischkarte nur, falls seit der Landung eine ausgegeben wurde
       (k.misch_ok_am is not null and k.misch_ok_am >= k.sitzt_am)
       or not exists (select 1 from schule.misch_ausgabe m join schule.aufgabe a on a.id = m.aufgabe_id
                       where m.lernender_id = k.lernender_id and a.einheit_id = k.einheit_id and a.variante_gruppe = k.lernziel and m.ausgegeben_am >= k.sitzt_am)
     else
       k.misch_ok_am is not null and k.misch_ok_am >= k.sitzt_am
       and exists (select 1 from schule.testsitzung t join schule.versuch v on v.testsitzung_id = t.id join schule.aufgabe a on a.id = v.aufgabe_id
                    where t.lernender_id = k.lernender_id and t.einheit_id = k.einheit_id and t.art = 'nachtest' and t.ergebnis = 'bestanden'
                      and t.abgeschlossen_am >= k.sitzt_am and a.variante_gruppe = k.lernziel and v.richtig)
     end;
$function$;

create or replace function schule.flug_nachtest(p_lernender bigint, p_einheit bigint)
 returns boolean language sql stable set search_path to ''
as $function$
  select case when schule.flug_ohne_test(p_lernender, p_einheit) then null -- LB-3: entfällt
    else exists (select 1 from schule.testsitzung t where t.lernender_id = p_lernender and t.einheit_id = p_einheit and t.art = 'nachtest' and t.ergebnis = 'bestanden') end;
$function$;

-- ---------- die 4 Stufen ----------
create or replace function schule.thema_stufe(p_l bigint, p_thema bigint)
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare v_e bigint := schule.thema_einheit(p_thema); v_r schule.route; v_n int := 0; v_gel int := 0; v_sich int := 0; v_beg int := 0; v_wo int := 0;
  v_wmin int; v_bis int; v_rr boolean; v_test boolean := false; v_ges text; v_implan boolean; v_stufe text;
begin
  select r.* into v_r from schule.route r join schule.block_thema bt on bt.block_id = r.block_id and bt.thema_id = p_thema
   where r.lernender_id = p_l and r.art = 'normal' and r.status <> 'entfernt' order by r.id limit 1;
  v_implan := v_r.id is not null and not (p_thema = any(v_r.ausgelassen));
  v_ges := case when schule.thema_kann_schon(p_l, p_thema) then 'komplett' when schule.thema_kann_wdh(p_l, p_thema) then 'wiederholen' end;
  if v_e is not null then
    select count(*) into v_n from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) x where e.id = v_e;
    select count(*) filter (where k.sitzt), count(*) filter (where schule.karte_sicher(k)),
           count(*) filter (where k.sitzt or k.sitzt_am is not null or coalesce(k.richtig, 0) + coalesce(k.falsch, 0) > 0),
           count(*) filter (where not k.sitzt and k.sitzt_am is not null), min(k.wdh_stufe) filter (where k.sitzt), min(schule.karte_wdh_in(k)) filter (where k.sitzt)
      into v_gel, v_sich, v_beg, v_wo, v_wmin, v_bis
      from schule.karte_stand k
     where k.lernender_id = p_l and k.einheit_id = v_e
       and k.lernziel in (select x->>'lernziel' from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) x where e.id = v_e);
    if v_ges is null then
      v_test := exists (select 1 from schule.testsitzung t where t.lernender_id = p_l and t.einheit_id = v_e and t.status = 'laeuft')
             or exists (select 1 from schule.lernziel_stand s where s.lernender_id = p_l and s.einheit_id = v_e and s.status = 'fehler')
             or (v_n > 0 and v_gel = v_n and not exists (select 1 from schule.testsitzung t where t.lernender_id = p_l and t.einheit_id = v_e and t.art = 'blocktest' and t.status = 'abgeschlossen'));
    end if;
  end if;
  v_rr := exists (select 1 from schule.route r join schule.block_thema bt on bt.block_id = r.block_id and bt.thema_id = p_thema
                   where r.lernender_id = p_l and r.art = 'rueckreise' and r.status not in ('fertig', 'entfernt'));
  v_stufe := case
    when v_ges = 'komplett' then 'komplett'
    when v_wo > 0 or v_rr then 'dran'
    when v_n > 0 and v_sich = v_n then 'komplett'
    when v_test then 'dran'
    when v_ges = 'wiederholen' or (v_n > 0 and v_gel = v_n) then 'wiederholung'
    when v_beg > 0 then 'dran'
    when v_implan then 'kommt'
    else 'nicht_im_plan' end;
  return jsonb_build_object('stufe', v_stufe,
    'zeichen', case v_stufe when 'komplett' then '◉' when 'wiederholung' then '↻' when 'dran' then '▶' when 'kommt' then '○' else '+' end,
    'gesetzt', v_ges, 'im_plan', v_implan, 'etappen', v_n, 'begonnen', v_beg, 'gelandet', v_gel, 'sicher', v_sich, 'wieder_offen', v_wo,
    'wdh_stufe_min', v_wmin, 'wdh_nr', case when v_wmin is null then null else least(v_wmin + 1, 5) end, 'naechste_in', v_bis,
    'rueckreise', v_rr, 'test_offen', v_test, 'ohne_test', v_ges = 'wiederholen');
end $function$;
comment on function schule.thema_stufe(bigint, bigint) is 'LB-3: Stufe eines Flugs für ein Kind – komplett ◉ · wiederholung ↻ · dran ▶ · kommt ○ · nicht_im_plan + (Regeln: umsetzung-lb.md, „Die 4 Stufen“)';

-- ---------- Plan-Schritt (innen) ----------
create or replace function schule.plan_setzen_intern(p_l bigint, p_daten jsonb, p_akt text)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_rev int; v_e jsonb; v_pos int := 0; v_b bigint; v_r schule.route; v_ids bigint[] := '{}'; v_n int; v_aus bigint[]; v_ks bigint[]; v_wieder bigint[] := '{}';
  v_fertig int; v_offen int; v_kw bigint[]; v_ww bigint[]; v_ks_neu bigint[]; v_aus_neu bigint[]; v_kw_neu bigint[]; v_kw_alt bigint[]; v_kann_neu boolean;
  v_alle bigint[]; v_t bigint; v_snap jsonb := '[]'::jsonb; v_rid bigint; v_zr schule.route_aenderung; v_zurueck int := 0; v_ort schule.route;
begin
  if not exists (select 1 from schule.lernender where id = p_l and aktiv) then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  if jsonb_typeof(p_daten->'eintraege') is distinct from 'array' then raise exception 'eintraege fehlt' using errcode = 'P0001'; end if;
  perform 1 from schule.lernender where id = p_l for update;
  select coalesce(max(revision), 0) into v_rev from schule.route where lernender_id = p_l and art = 'normal';
  if p_daten ? 'revision' and (p_daten->>'revision')::int <> v_rev then
    raise exception 'Der Plan wurde inzwischen geändert. Bitte neu laden.' using errcode = 'P0001';
  end if;
  -- LB-3: Rückgängig eines Schritts – Karten-Stände von davor (nur ohne eigene Versuche seither); die Einträge von davor schickt die App mit
  if nullif(p_daten->>'rueckgaengig', '') is not null then
    select * into v_zr from schule.route_aenderung where id = (p_daten->>'rueckgaengig')::bigint and lernender_id = p_l;
    if v_zr.id is null then raise exception 'Schritt zum Rückgängigmachen nicht gefunden' using errcode = 'P0001'; end if;
    if not coalesce((v_zr.ereignis->>'zurueckgenommen')::boolean, false) then
      v_zurueck := schule.karten_wiederherstellen(p_l, v_zr.ereignis->'karten', v_zr.am);
      update schule.route_aenderung set ereignis = ereignis || jsonb_build_object('zurueckgenommen', true) where id = v_zr.id;
    end if;
  end if;
  -- Positionen: route_pos (lernender_id, position) ist DEFERRABLE INITIALLY DEFERRED – Zwischenstände dürfen kollidieren, am Ende ist alles eindeutig.
  for v_e in select * from jsonb_array_elements(p_daten->'eintraege') loop
    v_b := (v_e->>'block_id')::bigint;
    if not exists (select 1 from schule.block where id = v_b and fach = 'Mathematik') then raise exception 'Unbekannter Ort %', v_b using errcode = 'P0001'; end if;
    if v_b = any(v_ids) then raise exception 'Ort doppelt im Plan' using errcode = 'P0001'; end if;
    v_ids := v_ids || v_b; v_pos := v_pos + 1;
    select coalesce(array_agg(bt.thema_id), '{}') into v_alle from schule.block_thema bt where bt.block_id = v_b;
    v_aus := null; v_ks := null; v_kw := null; v_ww := '{}'; -- fehlt eine Liste, bleibt die bisherige
    if v_e ? 'kann_schon_themen' then
      if jsonb_typeof(v_e->'kann_schon_themen') is distinct from 'array' then raise exception 'kann_schon_themen muss eine Liste sein' using errcode = 'P0001'; end if;
      select coalesce(array_agg(distinct x::bigint), '{}') into v_ks from jsonb_array_elements_text(v_e->'kann_schon_themen') x;
      if not (v_ks <@ v_alle) then raise exception 'Ein Flug mit „kann schon“ gehört nicht zu diesem Ort' using errcode = 'P0001'; end if;
    end if;
    if v_e ? 'ausgelassen' then
      if jsonb_typeof(v_e->'ausgelassen') is distinct from 'array' then raise exception 'ausgelassen muss eine Liste sein' using errcode = 'P0001'; end if;
      select coalesce(array_agg(distinct x::bigint), '{}') into v_aus from jsonb_array_elements_text(v_e->'ausgelassen') x;
      if not (v_aus <@ v_alle) then raise exception 'Ein abgewählter Flug gehört nicht zu diesem Ort' using errcode = 'P0001'; end if;
    end if;
    if v_e ? 'kann_wdh_themen' then -- LB-3
      if jsonb_typeof(v_e->'kann_wdh_themen') is distinct from 'array' then raise exception 'kann_wdh_themen muss eine Liste sein' using errcode = 'P0001'; end if;
      select coalesce(array_agg(distinct x::bigint), '{}') into v_kw from jsonb_array_elements_text(v_e->'kann_wdh_themen') x;
      if not (v_kw <@ v_alle) then raise exception 'Ein Flug mit „kann er – aber wiederholen“ gehört nicht zu diesem Ort' using errcode = 'P0001'; end if;
      if v_kw && coalesce(v_ks, '{}') or v_kw && coalesce(v_aus, '{}') or (v_kw <> '{}' and coalesce((v_e->>'kann_schon')::boolean, false)) then
        raise exception 'Ein Flug kann nur eine Einstellung haben (Lernen, Kann er – aber wiederholen, Kann er komplett, Aus dem Plan)' using errcode = 'P0001'; end if;
    end if;
    if v_e ? 'wieder_wdh_themen' then -- LB-3: Aktion „Wieder in die Wiederholung“
      if jsonb_typeof(v_e->'wieder_wdh_themen') is distinct from 'array' then raise exception 'wieder_wdh_themen muss eine Liste sein' using errcode = 'P0001'; end if;
      select coalesce(array_agg(distinct x::bigint), '{}') into v_ww from jsonb_array_elements_text(v_e->'wieder_wdh_themen') x;
      if not (v_ww <@ v_alle) then raise exception 'Ein Flug für „Wieder in die Wiederholung“ gehört nicht zu diesem Ort' using errcode = 'P0001'; end if;
    end if;
    v_r := null;
    select * into v_r from schule.route where lernender_id = p_l and block_id = v_b and art = 'normal' order by id limit 1;
    v_kw_alt := case when v_r.id is null or v_r.status = 'entfernt' then '{}' else coalesce(v_r.kann_wdh_themen, '{}') end;
    v_kann_neu := coalesce((v_e->>'kann_schon')::boolean, v_r.kann_schon, false);
    v_ks_neu := coalesce(v_ks, v_r.kann_schon_themen, '{}');
    v_aus_neu := coalesce(v_aus, v_r.ausgelassen, '{}');
    v_kw_neu := coalesce(v_kw, v_kw_alt);
    -- „Wieder in die Wiederholung“ eines „Kann er komplett“-Flugs = „Kann er – aber wiederholen“
    if v_ww <> '{}' then
      if v_ww && v_aus_neu then raise exception 'Ein abgewählter Flug kann nicht in die Wiederholung' using errcode = 'P0001'; end if;
      if v_kann_neu then v_kann_neu := false; v_ks_neu := array(select a from unnest(v_alle) a where not (a = any(v_aus_neu))); end if;
      v_kw_neu := array(select distinct a from unnest(v_kw_neu || array(select a2 from unnest(v_ww) a2 where a2 = any(v_ks_neu))) a);
      v_ks_neu := array(select a from unnest(v_ks_neu) a where not (a = any(v_ww)));
    end if;
    -- Einstellungen schließen einander aus: komplett/abgewählt gehen vor (alte App kennt kann_wdh nicht)
    if v_kann_neu then v_kw_neu := '{}'; end if;
    v_kw_neu := array(select a from unnest(v_kw_neu) a where not (a = any(v_ks_neu)) and not (a = any(v_aus_neu)));
    if v_r.id is null then
      insert into schule.route(lernender_id, block_id, position, art, status, kann_schon, ausgelassen, kann_schon_themen, kann_wdh_themen, revision, geaendert_von, geaendert_am)
      values (p_l, v_b, v_pos, 'normal', 'offen', v_kann_neu, v_aus_neu, v_ks_neu, v_kw_neu, v_rev + 1, p_akt, now());
    else
      -- P3: kommt in einen „fertigen“ Ort ein nicht erledigter Flug zurück, prüfen wir den Ort nach dem Speichern
      if v_r.status = 'fertig' and (exists (select 1 from unnest(v_r.kann_schon_themen) a where not (a = any(v_ks_neu) or a = any(v_kw_neu)))
                                    or exists (select 1 from unnest(v_r.ausgelassen) a where not (a = any(v_aus_neu)))
                                    or exists (select 1 from unnest(v_kw_alt) a where not (a = any(v_kw_neu) or a = any(v_ks_neu)))
                                    or (v_r.kann_schon and not v_kann_neu)) then
        v_wieder := v_wieder || v_b;
      end if;
      update schule.route set position = v_pos,
        status = case when status = 'entfernt' then coalesce(status_vor_entfernen, 'offen') else status end,
        status_vor_entfernen = null,
        kann_schon = v_kann_neu, ausgelassen = v_aus_neu, kann_schon_themen = v_ks_neu, kann_wdh_themen = v_kw_neu,
        revision = v_rev + 1, geaendert_von = p_akt, geaendert_am = now()
       where id = v_r.id;
    end if;
    -- LB-3: Karten-Stände (Reihenfolge: wieder in die Wiederholung, neu gesetzt, zurückgenommen)
    foreach v_t in array v_ww loop v_snap := v_snap || schule.flug_wieder_wdh(p_l, v_t); end loop;
    foreach v_t in array array(select a from unnest(v_kw_neu) a where not (a = any(v_kw_alt))) loop v_snap := v_snap || schule.flug_wdh_setzen(p_l, v_t, p_akt); end loop;
    foreach v_t in array array(select a from unnest(v_kw_alt) a where not (a = any(v_kw_neu))) loop v_snap := v_snap || schule.flug_wdh_zuruecknehmen(p_l, v_t); end loop;
  end loop;
  -- nicht mehr genannte Orte: gesetzte Landungen zurücknehmen, aus dem Plan nehmen und den alten Status merken
  for v_ort in select * from schule.route where lernender_id = p_l and art = 'normal' and status <> 'entfernt' and not (block_id = any(v_ids)) and kann_wdh_themen <> '{}' loop
    foreach v_t in array v_ort.kann_wdh_themen loop v_snap := v_snap || schule.flug_wdh_zuruecknehmen(p_l, v_t); end loop;
  end loop;
  update schule.route set status_vor_entfernen = status, status = 'entfernt', kann_wdh_themen = '{}', revision = v_rev + 1, geaendert_von = p_akt, geaendert_am = now()
   where lernender_id = p_l and art = 'normal' and status <> 'entfernt' and not (block_id = any(v_ids));
  get diagnostics v_n = row_count;
  -- entfernte Einträge fortlaufend hinter dem Plan (ab 1 000 001) – die Zahl wächst nicht mit jedem Speichern
  update schule.route r set position = 1000000 + x.nr
    from (select id, row_number() over (order by position, id) as nr from schule.route
           where lernender_id = p_l and art = 'normal' and status = 'entfernt') x
   where r.id = x.id and r.position <> 1000000 + x.nr;
  -- P3: Orte, deren geplante Flüge alle erledigt sind, werden „fertig“ – route_sterne bucht die Ort-Sterne einmal (wie bei „kann schon“)
  update schule.route r set status = 'fertig', revision = v_rev + 1, geaendert_von = p_akt, geaendert_am = now()
   where r.lernender_id = p_l and r.art = 'normal' and r.status not in ('fertig', 'entfernt') and r.block_id = any(v_ids)
     and (schule.ort_stand(p_l, r.block_id)->>'abgeschlossen')::boolean;
  get diagnostics v_fertig = row_count;
  -- P3 umgekehrt: ein nicht erledigter Flug ist zurück im Plan → Ort wieder offen (gebuchte Sterne bleiben, werden später nicht doppelt gebucht)
  update schule.route r set status = 'offen', revision = v_rev + 1, geaendert_von = p_akt, geaendert_am = now()
   where r.lernender_id = p_l and r.art = 'normal' and r.status = 'fertig' and r.block_id = any(v_wieder)
     and not coalesce((schule.ort_stand(p_l, r.block_id)->>'abgeschlossen')::boolean, false);
  get diagnostics v_offen = row_count;
  insert into schule.route_aenderung(lernender_id, route_id, akteur, anlass, ereignis)
  values (p_l, null, p_akt, 'plan', jsonb_build_object('reihenfolge', to_jsonb(v_ids), 'entfernt', v_n, 'revision', v_rev + 1, 'fertig_durch_abwahl', v_fertig, 'wieder_offen', v_offen,
          'karten', v_snap, 'rueckgaengig_von', nullif(p_daten->>'rueckgaengig', ''), 'karten_zurueck', v_zurueck))
  returning id into v_rid;
  return jsonb_build_object('ok', true, 'revision', v_rev + 1, 'anzahl', cardinality(v_ids), 'schritt_id', v_rid, 'karten_geaendert', jsonb_array_length(v_snap), 'karten_zurueck', v_zurueck);
end $function$;

create or replace function api.schule_plan_setzen(p_schluessel text, p_daten jsonb)
 returns jsonb
 language plpgsql
 security definer
 set search_path to ''
as $function$
declare v_l bigint := nullif(p_daten->>'lernender_id','')::bigint; v_akt text;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  v_akt := coalesce((select i.rolle || ':' || i.name from schule.lern_ich(p_schluessel) i where schule.ist_lern(p_schluessel)), 'eltern:App');
  return schule.plan_setzen_intern(v_l, p_daten, v_akt); -- LB-3: ganzer Schritt innen (Rauchtest ohne Schlüssel)
end $function$;

-- ---------- Plan lesen ----------
create or replace function api.schule_plan_lesen(p_schluessel text, p_daten jsonb)
 returns jsonb
 language plpgsql
 stable security definer
 set search_path to ''
as $function$
declare v_l bigint := nullif(p_daten->>'lernender_id','')::bigint; v_k schule.lernender;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  select * into v_k from schule.lernender where id = v_l and aktiv;
  if v_k.id is null then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  return jsonb_build_object('ok', true, 'kann_abwaehlen', true, -- die App zeigt die Häkchen „im Plan“ erst, wenn die Datenbank „ausgelassen“ speichert
    'kann_wdh', true, -- LB-3: die App zeigt „Kann er – aber wiederholen“ und „Wieder in die Wiederholung“ erst, wenn der Server sie kennt
    'kind', jsonb_build_object('id', v_k.id, 'name', v_k.anzeigename, 'klasse', v_k.klasse, 'schulart', v_k.schulart, 'ist_test', v_k.ist_test, 'stufen', v_k.stufen),
    'revision', (select coalesce(max(r.revision), 0) from schule.route r where r.lernender_id = v_l and r.art = 'normal'),
    'plan', (select coalesce(jsonb_agg(jsonb_build_object('block_id', r.block_id, 'position', r.position, 'art', r.art, 'status', r.status,
                 'kann_schon', r.kann_schon, 'ausgelassen', to_jsonb(r.ausgelassen), 'kann_schon_themen', to_jsonb(r.kann_schon_themen), 'kann_wdh_themen', to_jsonb(r.kann_wdh_themen),
                 'geaendert_von', r.geaendert_von, 'geaendert_am', r.geaendert_am)
                 order by r.art = 'normal', r.position), '[]'::jsonb)
             from schule.route r where r.lernender_id = v_l
               and (schule.ist_plan(r) or (r.art = 'normal' and r.status = 'fertig') or (r.art = 'rueckreise' and r.status not in ('fertig','entfernt')))),
    'kann_schon', (select coalesce(jsonb_agg(r.block_id), '[]'::jsonb) from schule.route r where r.lernender_id = v_l and r.kann_schon and r.status <> 'entfernt'),
    'orte', (select coalesce(jsonb_agg(jsonb_build_object('block_id', b.id, 'titel', b.titel, 'stadt', b.stadt, 'kontinent', k.titel, 'kontinent_id', k.id,
                 'reihenfolge', b.reihenfolge,
                 'themen', (select coalesce(jsonb_agg(jsonb_build_object('thema_id', t.id, 'titel', t.unterthema, 'jahrgang', schule.thema_jahrgang(t.id),
                                 'stand', schule.thema_stand(v_l, t.id), 'kann_schon', schule.thema_kann_schon(v_l, t.id), 'lehrplan_reihenfolge', t.lehrplan_reihenfolge,
                                 'kann_wdh', schule.thema_kann_wdh(v_l, t.id), 'stufe', schule.thema_stufe(v_l, t.id),
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
    'verlauf', (select coalesce(jsonb_agg(jsonb_build_object('akteur', a.akteur, 'anlass', a.anlass, 'ereignis', a.ereignis - 'karten', 'am', a.am, 'schritt_id', a.id) order by a.am desc), '[]'::jsonb)
                from (select * from schule.route_aenderung where lernender_id = v_l order by am desc limit 20) a));
end $function$;

-- ---------- übrige Stellen: einfügen an geprüften Stellen ----------
do $mig$
declare d text;
begin
  -- nachtest_stand: gesetzte Flüge haben keinen Nachtest
  d := pg_get_functiondef('schule.nachtest_stand(bigint, bigint)'::regprocedure);
  if position('flug_ohne_test' in d) = 0 then
    if position(E'begin\n  select count(*) filter (where s.status = ''offen'')' in d) = 0 then raise exception 'nachtest_stand: Stelle nicht gefunden'; end if;
    d := replace(d, E'begin\n  select count(*) filter (where s.status = ''offen'')',
      E'begin\n  if schule.flug_ohne_test(p_lernender, p_einheit) then return jsonb_build_object(''faellig'', false, ''grund'', ''gesetzt''); end if; -- LB-3\n  select count(*) filter (where s.status = ''offen'')');
    execute d;
  end if;

  -- test_starten_intern: kein Flug-Test und kein Nachtest für gesetzte Flüge (ein laufender Test bleibt fortsetzbar)
  d := pg_get_functiondef('schule.test_starten_intern(bigint, jsonb)'::regprocedure);
  if position('flug_ohne_test' in d) = 0 then
    if position(E'  if t.id is null then\n    if v_art = ''blocktest'' then' in d) = 0 then raise exception 'test_starten_intern: Stelle nicht gefunden'; end if;
    d := replace(d, E'  if t.id is null then\n    if v_art = ''blocktest'' then',
      E'  if t.id is null and v_art in (''blocktest'', ''nachtest'') and schule.flug_ohne_test(p_lernender, v_einheit) then -- LB-3\n    return jsonb_build_object(''ok'', false, ''grund'', ''nichts_zu_testen'', ''gesetzt'', true, ''vorrat_erschoepft'', ''[]''::jsonb, ''noch_nicht_faellig'', ''[]''::jsonb);\n  end if;\n  if t.id is null then\n    if v_art = ''blocktest'' then');
    execute d;
  end if;

  -- einheit_lesen_intern: ohne_test
  d := pg_get_functiondef('schule.einheit_lesen_intern(bigint, bigint)'::regprocedure);
  if position('''ohne_test''' in d) = 0 then
    if position('''nachtest'', schule.nachtest_stand(p_lernender, p_einheit),' in d) = 0 then raise exception 'einheit_lesen_intern: Stelle nicht gefunden'; end if;
    d := replace(d, '''nachtest'', schule.nachtest_stand(p_lernender, p_einheit),',
                    '''ohne_test'', schule.flug_ohne_test(p_lernender, p_einheit), ''nachtest'', schule.nachtest_stand(p_lernender, p_einheit),');
    execute d;
  end if;

  -- schule_uebersicht: route[].kann_wdh_themen, stand[].ohne_test
  d := pg_get_functiondef('api.schule_uebersicht(text, jsonb)'::regprocedure);
  if position('kann_wdh_themen' in d) = 0 then
    if position('''kann_schon_themen'', to_jsonb(r.kann_schon_themen)) order by r.position)' in d) = 0
       or position('x.einheit_id = g.einheit_id and x.status = ''laeuft''))), ''[]''::jsonb)' in d) = 0 then raise exception 'schule_uebersicht: Stellen nicht gefunden'; end if;
    d := replace(d, '''kann_schon_themen'', to_jsonb(r.kann_schon_themen)) order by r.position)',
                    '''kann_schon_themen'', to_jsonb(r.kann_schon_themen), ''kann_wdh_themen'', to_jsonb(r.kann_wdh_themen)) order by r.position)');
    d := replace(d, 'x.einheit_id = g.einheit_id and x.status = ''laeuft''))), ''[]''::jsonb)',
                    'x.einheit_id = g.einheit_id and x.status = ''laeuft''), ''ohne_test'', schule.flug_ohne_test(l.id, g.einheit_id))), ''[]''::jsonb)');
    execute d;
  end if;

  -- schule_lernstand: einheiten[].thema_id/stufe, karten[].gesetzt/gesetzt_am
  d := pg_get_functiondef('api.schule_lernstand(text, jsonb)'::regprocedure);
  if position('thema_stufe' in d) = 0 then
    if position('''einheit_id'', e.id, ''titel'', t.unterthema, ''ort'', b.stadt, ''status'', e.status,' in d) = 0
       or position('group by e.id, t.unterthema, b.stadt' in d) = 0
       or position('''wieder_offen'', not coalesce(k.sitzt, false) and k.sitzt_am is not null, ''flug_nachtest'', schule.flug_nachtest(v_l, e.id),' in d) = 0
    then raise exception 'schule_lernstand: Stellen nicht gefunden'; end if;
    d := replace(d, '''einheit_id'', e.id, ''titel'', t.unterthema, ''ort'', b.stadt, ''status'', e.status,',
                    '''einheit_id'', e.id, ''titel'', t.unterthema, ''ort'', b.stadt, ''status'', e.status, ''thema_id'', t.id, ''stufe'', schule.thema_stufe(v_l, t.id),');
    d := replace(d, 'group by e.id, t.unterthema, b.stadt', 'group by e.id, t.id, t.unterthema, b.stadt');
    d := replace(d, '''wieder_offen'', not coalesce(k.sitzt, false) and k.sitzt_am is not null, ''flug_nachtest'', schule.flug_nachtest(v_l, e.id),',
                    '''wieder_offen'', not coalesce(k.sitzt, false) and k.sitzt_am is not null, ''flug_nachtest'', schule.flug_nachtest(v_l, e.id), ''gesetzt'', k.gesetzt_am is not null, ''gesetzt_am'', k.gesetzt_am,');
    execute d;
  end if;

  -- schule_lehrplan_uebersicht: themen[].stufe je Kind
  d := pg_get_functiondef('api.schule_lehrplan_uebersicht(text, jsonb)'::regprocedure);
  if position('thema_stufe' in d) = 0 then
    if position('''stand'', (select coalesce(jsonb_object_agg(l.id, schule.thema_stand(l.id, t.id)), ''{}''::jsonb) from schule.lernender l where l.aktiv and not l.ist_test),' in d) = 0 then
      raise exception 'schule_lehrplan_uebersicht: Stelle nicht gefunden'; end if;
    d := replace(d, '''stand'', (select coalesce(jsonb_object_agg(l.id, schule.thema_stand(l.id, t.id)), ''{}''::jsonb) from schule.lernender l where l.aktiv and not l.ist_test),',
                    '''stand'', (select coalesce(jsonb_object_agg(l.id, schule.thema_stand(l.id, t.id)), ''{}''::jsonb) from schule.lernender l where l.aktiv and not l.ist_test),
          ''stufe'', (select coalesce(jsonb_object_agg(l.id, schule.thema_stufe(l.id, t.id)), ''{}''::jsonb) from schule.lernender l where l.aktiv and not l.ist_test),');
    execute d;
  end if;
end $mig$;
