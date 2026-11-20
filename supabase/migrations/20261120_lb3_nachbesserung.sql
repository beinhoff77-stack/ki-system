-- Bau-Auftrag LB-3, Nachbesserung (20.11.): drei Muss aus der Prüfung von ChatGPT (Werkstatt 881, 882), dazu Sollte 4–6.
-- Vorgabe: inhalte/AUFTRAEGE.md, Abschnitt „Bau-Auftrag LB-3, Nachbesserung“. Nach 20261120_lb3_kann_wiederholen.sql, 20261120_i5_stufe_nachtragstest.sql
-- und 20261120_ab_s_abschluss.sql (karte_buchen mit landung_speichern).
-- Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE, keine Änderung am Bestand (Stand 20.11. lesend geprüft: keine Route mit
-- kann_wdh_themen, keine Karte mit gesetzt_am). Wiederholt ausführbar.
--
-- Muss 1  flug_wdh_setzen: auch schon gelandete Etappen starten die Wiederholung bei Stufe 1 (fällig am nächsten Lerntag); Landung (sitzt_am),
--         eigene Lösungen und Belege bleiben, Herkunft bleibt „selbst gelandet“ (kein gesetzt_am). Die Lage davor steht im Schritt (Rückgängig).
--         Neu: karte_stand.wdh_gesetzt_am – wann die Wiederholung durch „Kann er – aber wiederholen“ neu begann (für Muss 3).
-- Muss 2  Eine gesetzte Etappe bleibt bei Rücknahme oder Rückgängig nur gelandet, wenn das Kind sie seit dem Setzen nach der normalen Regel selbst
--         gelandet hätte: schule.karte_landet(k) – dieselbe Prüfung, die karte_buchen jetzt aufruft (eigene Lösungen ≥ Ziel, Typen, schwere, Folge).
--         Dafür zählt karte_buchen eigene Lösungen, Typen, schwere und Folge auch in gesetzten Etappen weiter (die Wiederholung läuft daneben wie bisher).
--         Sonst wird sie wieder offen (sitzt_am null). Versuche, eigene Lösungen und Sterne bleiben.
-- Muss 3  karte_sicher: in einem Flug auf „Kann er – aber wiederholen“ gilt für ALLE Etappen: sicher = gelandet + Wiederholung nach 14 Lerntagen
--         (wdh_stufe ≥ 4) + Mischkarte richtig, falls seit dem Setzen eine eingelöst oder beantwortet wurde (eine nur vorgeladene zählt nicht).
-- Sollte 4  rueckgaengig nimmt nur den jüngsten Plan-Schritt des Kindes an.
-- Sollte 5  thema_stufe: „komplett“ gesetzt, aber eine Etappe wieder offen → Stufe bleibt ◉, zusätzlich hinweis 'rueckfall' (wieder_offen > 0).
-- Sollte 6  schule.heute_bis(kind): nächster Tagesbeginn in der Zeitzone des Kindes; einheit_lesen_intern und uebung_pruefen_intern liefern 'heute_bis'.

alter table schule.karte_stand add column if not exists wdh_gesetzt_am timestamptz;
comment on column schule.karte_stand.wdh_gesetzt_am is 'LB-3 Nachbesserung: Beginn der Wiederholung durch „Kann er – aber wiederholen“ (für alle Etappen des Flugs, auch selbst gelandete)';

-- ---------- gemeinsame Landeregel ----------
create or replace function schule.karte_landet(k schule.karte_stand)
 returns boolean language sql stable set search_path to ''
as $function$
  select coalesce(k.eigene_loesungen, 0) >= schule.karte_ziel(k.einheit_id, k.lernziel)
     and coalesce(array_length(k.typen, 1), 0) >= schule.karte_typen_noetig(k.einheit_id, k.lernziel)
     and (coalesce(k.schwer_ok, false) or not schule.karte_schwer_noetig(k.einheit_id, k.lernziel))
     and coalesce(k.folge, 0) >= least(3, schule.karte_ziel(k.einheit_id, k.lernziel));
$function$;
comment on function schule.karte_landet(schule.karte_stand) is 'Landeregel einer Etappe (eigene Lösungen ≥ Ziel, Typen, schwere, Folge) – karte_buchen und die Rücknahme gesetzter Landungen';

-- ---------- Lage einer Karte (für Rückgängig) ----------
create or replace function schule.karte_lage(k schule.karte_stand)
 returns jsonb language sql immutable set search_path to ''
as $function$
  select jsonb_build_object('sitzt', k.sitzt, 'sitzt_am', k.sitzt_am, 'wdh_stufe', k.wdh_stufe, 'faellig_am', k.faellig_am, 'wdh_fehler', k.wdh_fehler,
    'wdh_ab', k.wdh_ab, 'wdh_lerntage', k.wdh_lerntage, 'gesetzt_am', k.gesetzt_am, 'gesetzt_von', k.gesetzt_von, 'wdh_gesetzt_am', k.wdh_gesetzt_am);
$function$;

-- ---------- Muss 1: Setzen startet die Wiederholung für alle Etappen neu ----------
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
    v_snap := v_snap || jsonb_build_object('einheit_id', v_e, 'lernziel', v_lz, 'vorher', case when v_vor.lernender_id is null then null else schule.karte_lage(v_vor) end);
    if v_vor.lernender_id is not null and v_vor.sitzt then
      -- schon gelandet: Landung, Herkunft und Belege bleiben; nur die Wiederholung beginnt neu bei Stufe 1
      update schule.karte_stand set wdh_stufe = 0, faellig_am = now() + interval '1 day', wdh_fehler = 0, wdh_ab = now(), wdh_lerntage = 1, wdh_gesetzt_am = now()
       where lernender_id = p_l and einheit_id = v_e and lernziel = v_lz;
    else
      insert into schule.karte_stand(lernender_id, einheit_id, lernziel) values (p_l, v_e, v_lz) on conflict do nothing;
      update schule.karte_stand set sitzt = true, sitzt_am = now(), wdh_stufe = 0, faellig_am = now() + interval '1 day', wdh_fehler = 0,
             wdh_ab = now(), wdh_lerntage = 1, gesetzt_am = now(), gesetzt_von = p_wer, wdh_gesetzt_am = now()
       where lernender_id = p_l and einheit_id = v_e and lernziel = v_lz;
    end if;
  end loop;
  return v_snap;
end $function$;

-- ---------- Muss 2: Rücknahme lässt keine unbelegte Landung stehen ----------
create or replace function schule.flug_wdh_zuruecknehmen(p_l bigint, p_thema bigint)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare k schule.karte_stand; v_snap jsonb := '[]'::jsonb;
begin
  for k in select ks.* from schule.karte_stand ks join schule.einheit e on e.id = ks.einheit_id
            where ks.lernender_id = p_l and e.thema_id = p_thema and (ks.gesetzt_am is not null or ks.wdh_gesetzt_am is not null) for update of ks loop
    v_snap := v_snap || jsonb_build_object('einheit_id', k.einheit_id, 'lernziel', k.lernziel, 'vorher', schule.karte_lage(k));
    if k.gesetzt_am is null or (k.sitzt and schule.karte_landet(k)) then
      -- selbst gelandet oder seit dem Setzen nach der normalen Regel gelandet: bleibt gelandet, nur die Herkunft „gesetzt“ fällt weg
      update schule.karte_stand set gesetzt_am = null, gesetzt_von = null, wdh_gesetzt_am = null
       where lernender_id = p_l and einheit_id = k.einheit_id and lernziel = k.lernziel;
    else
      -- unbelegt: wieder offen; Versuche, eigene Lösungen, Typen und Folge zählen für die offene Etappe weiter
      update schule.karte_stand set sitzt = false, sitzt_am = null, wdh_stufe = 0, faellig_am = null, wdh_fehler = 0, wdh_ab = null, wdh_lerntage = null,
             gesetzt_am = null, gesetzt_von = null, wdh_gesetzt_am = null
       where lernender_id = p_l and einheit_id = k.einheit_id and lernziel = k.lernziel;
    end if;
  end loop;
  return v_snap;
end $function$;

-- Rückgängig eines Schritts: gesetzte Landungen dieses Schritts nach Muss 2; sonst Lage davor, außer das Kind hat seither an der Etappe geübt
create or replace function schule.karten_wiederherstellen(p_l bigint, p_karten jsonb, p_seit timestamptz)
 returns integer language plpgsql set search_path to ''
as $function$
declare v_w jsonb; v_vor jsonb; n_zurueck int := 0; k schule.karte_stand; v_e bigint; v_lz text; v_gesetzt_hier boolean;
begin
  for v_w in select q.eintrag from jsonb_array_elements(coalesce(p_karten, '[]'::jsonb)) with ordinality q(eintrag, nr) order by q.nr desc loop -- rückwärts: die früheste Lage gilt
    v_e := (v_w->>'einheit_id')::bigint; v_lz := v_w->>'lernziel'; v_vor := v_w->'vorher';
    if v_vor is not null and jsonb_typeof(v_vor) = 'null' then v_vor := null; end if;
    k := null;
    select * into k from schule.karte_stand where lernender_id = p_l and einheit_id = v_e and lernziel = v_lz for update;
    if k.lernender_id is null then continue; end if;
    -- in diesem Schritt gesetzte Landung (vorher nicht gelandet und nicht gesetzt)?
    v_gesetzt_hier := k.gesetzt_am is not null and k.gesetzt_am >= p_seit
                      and not coalesce((v_vor->>'sitzt')::boolean, false) and (v_vor is null or v_vor->>'gesetzt_am' is null);
    if v_gesetzt_hier and k.sitzt and schule.karte_landet(k) then
      update schule.karte_stand set gesetzt_am = null, gesetzt_von = null, wdh_gesetzt_am = null
       where lernender_id = p_l and einheit_id = v_e and lernziel = v_lz;
      n_zurueck := n_zurueck + 1; continue;
    end if;
    if not v_gesetzt_hier and exists (select 1 from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                where v.lernender_id = p_l and v.testsitzung_id is null and a.einheit_id = v_e and a.variante_gruppe = v_lz and v.am >= p_seit) then
      continue; -- das Kind hat seither an einer nicht gesetzten Etappe geübt: Stand bleibt
    end if;
    if v_vor is null then
      update schule.karte_stand set sitzt = false, sitzt_am = null, wdh_stufe = 0, faellig_am = null, wdh_fehler = 0, wdh_ab = null, wdh_lerntage = null,
             gesetzt_am = null, gesetzt_von = null, wdh_gesetzt_am = null
       where lernender_id = p_l and einheit_id = v_e and lernziel = v_lz;
    else
      update schule.karte_stand set sitzt = coalesce((v_vor->>'sitzt')::boolean, false), sitzt_am = (v_vor->>'sitzt_am')::timestamptz, wdh_stufe = coalesce((v_vor->>'wdh_stufe')::smallint, 0),
             faellig_am = (v_vor->>'faellig_am')::timestamptz, wdh_fehler = coalesce((v_vor->>'wdh_fehler')::smallint, 0), wdh_ab = (v_vor->>'wdh_ab')::timestamptz,
             wdh_lerntage = (v_vor->>'wdh_lerntage')::smallint, gesetzt_am = (v_vor->>'gesetzt_am')::timestamptz, gesetzt_von = v_vor->>'gesetzt_von',
             wdh_gesetzt_am = (v_vor->>'wdh_gesetzt_am')::timestamptz
       where lernender_id = p_l and einheit_id = v_e and lernziel = v_lz;
    end if;
    n_zurueck := n_zurueck + 1;
  end loop;
  return n_zurueck;
end $function$;

-- ---------- Muss 3: „sicher“ richtet sich nach dem Flug ----------
create or replace function schule.karte_sicher(k schule.karte_stand)
 returns boolean language sql stable set search_path to ''
as $function$
  select coalesce(k.sitzt, false) and coalesce(k.wdh_stufe, 0) >= 4
     and case when k.gesetzt_am is not null or schule.flug_ohne_test(k.lernender_id, k.einheit_id) then
       -- „Kann er – aber wiederholen“ (für alle Etappen des Flugs): kein Nachtest; Mischkarte nur, falls seit dem Setzen eine eingelöst oder beantwortet wurde
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

-- ---------- Sollte 6: Tagesende in der Zeitzone des Kindes ----------
create or replace function schule.heute_bis(p_l bigint)
 returns timestamptz language sql stable set search_path to ''
as $function$
  select ((schule.heute_tag(p_l) + 1)::timestamp at time zone coalesce((select l.zeitzone from schule.lernender l where l.id = p_l), 'Europe/Berlin'));
$function$;
comment on function schule.heute_bis(bigint) is 'LB-3 Nachbesserung (H6): Beginn des nächsten Tages in der Zeitzone des Kindes – bis dahin gilt heute_tag';

-- ---------- Einfügungen an geprüften Stellen ----------
do $mig$
declare d text; v_alt text; v_neu text;
begin
  -- Muss 2: karte_buchen zählt in gesetzten Etappen weiter und nutzt die gemeinsame Landeregel
  d := pg_get_functiondef('schule.karte_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)'::regprocedure);
  if position('karte_landet' in d) = 0 then
    if position('v_landet boolean := false;' in d) = 0
       or position(E'  if not k.sitzt then\n    if v_eigen then' in d) = 0
       or position(E'    if k.eigene_loesungen >= v_ziel\n       and coalesce(array_length(k.typen, 1), 0) >= schule.karte_typen_noetig(a.einheit_id, a.variante_gruppe)\n       and (k.schwer_ok or not schule.karte_schwer_noetig(a.einheit_id, a.variante_gruppe))\n       and k.folge >= least(3, v_ziel) then' in d) = 0
       or position(E'  else\n    if not p_richtig then\n      if k.wdh_fehler >= 1 then' in d) = 0
    then raise exception 'karte_buchen: Stellen nicht gefunden'; end if;
    d := replace(d, 'v_landet boolean := false;', 'v_landet boolean := false; v_war_gelandet boolean;');
    d := replace(d, E'  if not k.sitzt then\n    if v_eigen then',
      E'  v_war_gelandet := k.sitzt;\n  if not k.sitzt or k.gesetzt_am is not null then -- LB-3 Nachbesserung: in gesetzten Etappen zählen eigene Lösungen, Typen, schwere und Folge weiter (für die Rücknahme)\n    if v_eigen then');
    d := replace(d, E'    if k.eigene_loesungen >= v_ziel\n       and coalesce(array_length(k.typen, 1), 0) >= schule.karte_typen_noetig(a.einheit_id, a.variante_gruppe)\n       and (k.schwer_ok or not schule.karte_schwer_noetig(a.einheit_id, a.variante_gruppe))\n       and k.folge >= least(3, v_ziel) then',
      E'    if not v_war_gelandet and schule.karte_landet(k) then -- gemeinsame Landeregel');
    d := replace(d, E'  else\n    if not p_richtig then\n      if k.wdh_fehler >= 1 then',
      E'  end if;\n  if v_war_gelandet then -- Wiederholung (gelandete und gesetzte Etappen)\n    if not p_richtig then\n      if k.wdh_fehler >= 1 then');
    execute d;
  end if;

  -- Sollte 4: Rückgängig nur für den jüngsten Plan-Schritt des Kindes
  d := pg_get_functiondef('schule.plan_setzen_intern(bigint, jsonb, text)'::regprocedure);
  if position('Inzwischen wurde etwas anderes geändert.' in d) = 0 then
    v_alt := $a$if v_zr.id is null then raise exception 'Schritt zum Rückgängigmachen nicht gefunden' using errcode = 'P0001'; end if;$a$;
    if position(v_alt in d) = 0 then raise exception 'plan_setzen_intern: Stelle nicht gefunden'; end if;
    d := replace(d, v_alt, v_alt || $a$
    if v_zr.id <> (select max(ra.id) from schule.route_aenderung ra where ra.lernender_id = p_l and ra.anlass = 'plan') then -- LB-3 Nachbesserung: nur der jüngste Schritt
      raise exception 'Inzwischen wurde etwas anderes geändert.' using errcode = 'P0001'; end if;$a$);
    execute d;
  end if;

  -- Sollte 5: Rückfall bei „Kann er komplett“
  d := pg_get_functiondef('schule.thema_stufe(bigint, bigint)'::regprocedure);
  if position('''hinweis''' in d) = 0 then
    v_alt := $a$'rueckreise', v_rr, 'test_offen', v_test,$a$;
    if position(v_alt in d) = 0 then raise exception 'thema_stufe: Stelle nicht gefunden'; end if;
    d := replace(d, v_alt, $a$'hinweis', case when v_ges = 'komplett' and v_wo > 0 then 'rueckfall' end, 'rueckreise', v_rr, 'test_offen', v_test,$a$);
    execute d;
  end if;

  -- Sollte 6: heute_bis neben heute_tag
  v_alt := $a$'heute_tag', schule.heute_tag(p_lernender),$a$;
  v_neu := $a$'heute_tag', schule.heute_tag(p_lernender), 'heute_bis', schule.heute_bis(p_lernender),$a$;
  d := pg_get_functiondef('schule.einheit_lesen_intern(bigint, bigint)'::regprocedure);
  if position('heute_bis' in d) = 0 then
    if position(v_alt in d) = 0 then raise exception 'einheit_lesen_intern: Stelle nicht gefunden'; end if;
    execute replace(d, v_alt, v_neu);
  end if;
  d := pg_get_functiondef('schule.uebung_pruefen_intern(bigint, jsonb)'::regprocedure);
  if position('heute_bis' in d) = 0 then
    if position(v_alt in d) = 0 then raise exception 'uebung_pruefen_intern: Stelle nicht gefunden'; end if;
    execute replace(d, v_alt, v_neu);
  end if;
end $mig$;
