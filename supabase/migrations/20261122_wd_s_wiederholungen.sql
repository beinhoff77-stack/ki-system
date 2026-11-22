-- Bau-Auftrag WD (22.11.), Server-Teil WD-S: Wiederholungen dynamisch – Stau vermeiden, Belohnung fürs Ablegen.
-- Vorgabe: inhalte/AUFTRAEGE.md „Bau-Auftrag WD“ und „Nachtrag zum Bau-Auftrag WD – Reihenfolge und Schnittstelle“ (verbindlich).
--
-- Befund heute (Live-Text gelesen 22.11.):
--   Takt: Landung → Stufe 0 (1 Lerntag), jede richtige fällige Wiederholung +1 Stufe: 3, 7, 14, 30 Lerntage; ab Stufe 4 bleibt es bei 30 (karte_buchen).
--   Sterne: Trigger versuch_sterne gibt für JEDE richtige Antwort außerhalb von Tests (auch mit Tipp/2. Anlauf, auch Wiederholung und Mischkarte)
--   sterne_uebung_richtig = 10 Sterne – aber je Aufgabe nur einmal im Leben (Schlüssel lernender, grund 'uebung', bezug 'aufgabe:<id>').
--   Eine richtige Wiederholung gibt heute also 10 Sterne, wenn die Aufgabe noch nie richtig war (die Runde wählt bevorzugt ungesehene Aufgaben), sonst 0.
--   Mischkarte genauso (10 oder 0). → NICHT gekürzt: sterne_wdh_richtig steht auf 10 (Schnittstelle nennt 5) – Sebastian entscheidet (eine Zeile in schule.regel).
--
-- Was diese Datei baut (Schnittstelle laut Nachtrag):
--   WD-1 schule_wiederholung: runde (ein Fünftel der fälligen, aufgerundet, min 6, max 12, bis Klasse 6 max 10; bis 6 fällige: alle), faellig, aufgaben[] in der
--        Reihenfolge Wiederholungs-Fehler → am längsten fällig → niedrigste Stufe (die ersten `runde` sind Pflicht: aufgaben[].pflicht), runde_gemacht, gestaffelt.
--   WD-2 schule.wdh_runde + api.schule_wiederholung_runde_fertig {lernender_id}: Merker je Kind und Lerntag (heute_tag) auf dem Server.
--   WD-3 Mischkarten: Auswahl und Ausgabe bevorzugen fällige Etappen; Mischkarte aus fälliger Etappe, richtig im 1. Versuch ohne Tipp = bestandene Wiederholung
--        (rückt im Takt weiter wie karte_buchen), zusätzlich zum bisherigen Beleg (misch_ok_am). Falsch: wie heute (fällig, öffnet nie). Häufigkeit unverändert.
--   WD-4 flug_wdh_setzen: gesetzte Etappen kommen gestaffelt in den Takt – je Kind höchstens wdh_gesetzt_je_lerntag (6) neue erste Wiederholungen je Lerntag,
--        in Aufruf-Reihenfolge (Plan-Reihenfolge, Etappen-Reihenfolge). Den vorhandenen Stau streckt die eigene Datei 20261122_wd_4b_stau_strecken.sql.
--   WD-5 Sterne je bestandener Wiederholung (Runde, freiwillig, Mischkarte nach WD-3): einmal je Etappe und Fälligkeit (grund 'wdh', bezug 'wdh:<einheit>:<etappe>:<beginn>');
--        für denselben Versuch dann keine 'uebung'-Sterne (nichts doppelt).
--   WD-6 Ablegen: besteht eine Etappe die Wiederholung auf Stufe 4 (30 Lerntage), ist sie abgelegt: raus aus dem Takt (keine Fälligkeit mehr), 30 Sterne, Einblendung;
--        alle Pflicht-Etappen des Flugs abgelegt: 100 Sterne, Flug golden; alle Flüge eines Orts abgelegt: Orts-Stempel golden. Je Kind und Etappe/Flug/Ort einmal
--        (schule.abgelegt, wie flug_erstabschluss). Fällt eine abgelegte Etappe später wieder auf (falsch beim Üben, falsche Mischkarte), kommt sie wie heute
--        in den Takt zurück; das Gold bleibt.
--   Antworten: schule_uebung_pruefen + wiederholung {bestanden, sterne, stufe_neu, naechste_in} und abgelegt {etappe {titel, sterne}, flug? {titel, sterne}, ort_gold?};
--   schule_konto: konto.fluege[] {thema_id, einheit_id, titel, abgelegt, etappen_abgelegt, etappen}, konto.orte[].gold.
--
-- Technik: Ein Trigger vor jeder Änderung an schule.karte_stand erkennt die Antwort auf eine fällige Etappe (richtig/falsch zählt hoch) und ob sie bestanden ist
--   (Stufe +1, neuer Beginn, kein Fehler). So bleiben karte_buchen, uebung_pruefen_intern und die Versuch-Trigger unverändert; geändert (genau bezeichnete Stellen,
--   jede genau einmal geprüft): sterne_aus_versuch, misch_buchen, mischkarten_waehlen, mischkarten, flug_wdh_setzen, api.schule_uebung_pruefen, api.schule_konto;
--   neu geschrieben: api.schule_wiederholung (gleiche Felder wie bisher plus die neuen).
-- Bestand: neue Tabellen und Regeln; keine Änderung an Lernständen, Karten, Plan (am Ende geprüft: Prüfsummen vorher = nachher, sonst Abbruch).
-- Nicht ausgeführt – der Haupt-Chat spielt ein (dazu lernen-api: Aktion schule_wiederholung_runde_fertig). Kein DROP, kein DELETE. Wiederholt ausführbar.

-- Prüfsummen vorher (Karten, Lernstände, Plan) – Vergleich am Ende
create temp table wd_vorher on commit drop as
  select 'karte' t, md5(coalesce(string_agg(x::text, '|' order by x::text), '')) s from schule.karte_stand x
  union all select 'lernziel', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernziel_stand x
  union all select 'route', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.route x
  union all select 'sterne', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x;

-- Regeln (änderbar ohne Bau)
insert into schule.regel (schluessel, wert, hinweis) values
  ('wdh_runde_min', '6', 'WD-1: Wiederholungs-Runde mindestens (bis zu dieser Zahl fälliger: alle)'),
  ('wdh_runde_max', '12', 'WD-1: Wiederholungs-Runde höchstens'),
  ('wdh_runde_max_bis_kl6', '10', 'WD-1: Wiederholungs-Runde höchstens bis Klasse 6'),
  ('wdh_runde_teiler', '5', 'WD-1: Runde = fällige / Teiler, aufgerundet'),
  ('wdh_gesetzt_je_lerntag', '6', 'WD-4: gesetzte Etappen, die je Lerntag neu in den Takt kommen'),
  ('sterne_wdh_richtig', '10', 'WD-5: je bestandener Wiederholung. Schnittstelle nennt 5; heute gibt eine richtige Wiederholung 10 (sterne_uebung_richtig) – Sebastian entscheidet 5 oder 10'),
  ('sterne_etappe_abgelegt', '30', 'WD-6: Etappe abgelegt'),
  ('sterne_flug_abgelegt', '100', 'WD-6: alle Etappen eines Flugs abgelegt')
on conflict (schluessel) do nothing;

create or replace function schule.wd_regel(p text, p_std integer)
 returns integer language sql stable set search_path to ''
as $function$
  select coalesce((select (r.wert #>> '{}')::int from schule.regel r where r.schluessel = p), p_std);
$function$;

-- WD-2: Pflicht-Runde je Kind und Lerntag erledigt
create table if not exists schule.wdh_runde (
  lernender_id bigint not null references schule.lernender(id),
  tag date not null,
  fertig_am timestamptz not null default now(),
  primary key (lernender_id, tag)
);
comment on table schule.wdh_runde is 'WD-2: Wiederholungs-Runde dieses Lerntags (schule.heute_tag) erledigt – gilt für alle Geräte';
alter table schule.wdh_runde enable row level security;
revoke all on table schule.wdh_runde from public, anon, authenticated;

-- WD-6: endgültig abgelegt – je Kind und Etappe/Flug/Ort höchstens einmal (bezug 'etappe:<einheit>:<etappe>', 'flug:<thema>', 'ort:<block>')
create table if not exists schule.abgelegt (
  lernender_id bigint not null references schule.lernender(id),
  bezug text not null,
  art text not null check (art in ('etappe', 'flug', 'ort')),
  einheit_id bigint, lernziel text, thema_id bigint, block_id bigint,
  sterne integer not null default 0,
  am timestamptz not null default now(),
  primary key (lernender_id, bezug)
);
comment on table schule.abgelegt is 'WD-6: Etappe/Flug/Ort endgültig abgelegt (einmalig, bleibt auch wenn die Etappe später wieder in den Takt kommt)';
alter table schule.abgelegt enable row level security;
revoke all on table schule.abgelegt from public, anon, authenticated;

-- WD-1: Größe der Runde
create or replace function schule.wdh_runde_groesse(p_l bigint, p_faellig integer)
 returns integer language sql stable set search_path to ''
as $function$
  select case when p_faellig <= schule.wd_regel('wdh_runde_min', 6) then p_faellig
    else least(case when coalesce((select l.klasse from schule.lernender l where l.id = p_l), 99) <= 6
                    then schule.wd_regel('wdh_runde_max_bis_kl6', 10) else schule.wd_regel('wdh_runde_max', 12) end,
               greatest(schule.wd_regel('wdh_runde_min', 6), ceil(p_faellig::numeric / greatest(schule.wd_regel('wdh_runde_teiler', 5), 1))::int)) end;
$function$;

-- WD-4: erster Lerntag mit freiem Platz für eine gesetzte Etappe (zählt gesetzte Etappen auf Stufe 0, die an diesem Lerntag zum ersten Mal fällig werden)
create or replace function schule.wdh_staffel_tag(p_l bigint)
 returns integer language plpgsql stable set search_path to ''
as $function$
declare v_max int := greatest(schule.wd_regel('wdh_gesetzt_je_lerntag', 6), 1); v_tage int[]; d int := 1;
begin
  select coalesce(array_agg(schule.karte_wdh_in(k)), '{}') into v_tage from schule.karte_stand k
   where k.lernender_id = p_l and k.sitzt and k.wdh_gesetzt_am is not null and k.wdh_stufe = 0 and k.wdh_fehler = 0
     and not exists (select 1 from schule.abgelegt g where g.lernender_id = k.lernender_id and g.bezug = 'etappe:' || k.einheit_id || ':' || k.lernziel);
  while d < 400 and (select count(*) from unnest(v_tage) x where x = d) >= v_max loop d := d + 1; end loop;
  return d;
end $function$;

-- WD-6: Etappe ablegen (einmalig), dann Flug und Orte prüfen. Liefert die Einblendung oder null (schon früher abgelegt).
create or replace function schule.wdh_ablegen(p_l bigint, p_e bigint, p_lz text)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_ein schule.einheit; v_st int := schule.wd_regel('sterne_etappe_abgelegt', 30); v_sf int := schule.wd_regel('sterne_flug_abgelegt', 100);
  v_erg jsonb; v_pflicht text[]; v_b bigint; v_gold boolean := false;
begin
  select * into v_ein from schule.einheit where id = p_e;
  insert into schule.abgelegt (lernender_id, bezug, art, einheit_id, lernziel, thema_id, block_id, sterne)
  values (p_l, 'etappe:' || p_e || ':' || p_lz, 'etappe', p_e, p_lz, v_ein.thema_id, v_ein.block_id, v_st) on conflict do nothing;
  if not found then return null; end if;
  insert into schule.sterne (lernender_id, menge, grund, bezug) values (p_l, v_st, 'etappe_abgelegt', 'etappe:' || p_e || ':' || p_lz) on conflict do nothing;
  v_erg := jsonb_build_object('etappe', jsonb_build_object('titel',
             (select et->>'titel' from jsonb_array_elements(coalesce(v_ein.inhalt->'etappen', '[]'::jsonb)) et where et->>'lernziel' = p_lz limit 1), 'sterne', v_st));
  -- Flug: alle Pflicht-Etappen abgelegt (ohne Pflichtliste: alle Etappen)
  select coalesce(nullif(array(select jsonb_array_elements_text(coalesce(v_ein.inhalt->'bewertung'->'lernziele_pflicht', '[]'::jsonb))), '{}'),
                  array(select et->>'lernziel' from jsonb_array_elements(coalesce(v_ein.inhalt->'etappen', '[]'::jsonb)) et)) into v_pflicht;
  if cardinality(v_pflicht) > 0 and not exists (select 1 from unnest(v_pflicht) p
       where not exists (select 1 from schule.abgelegt g where g.lernender_id = p_l and g.bezug = 'etappe:' || p_e || ':' || p)) then
    insert into schule.abgelegt (lernender_id, bezug, art, einheit_id, thema_id, block_id, sterne)
    values (p_l, 'flug:' || v_ein.thema_id, 'flug', p_e, v_ein.thema_id, v_ein.block_id, v_sf) on conflict do nothing;
    if found then
      insert into schule.sterne (lernender_id, menge, grund, bezug) values (p_l, v_sf, 'flug_abgelegt', 'flug:' || v_ein.thema_id) on conflict do nothing;
      v_erg := v_erg || jsonb_build_object('flug', jsonb_build_object('titel', (select t.unterthema from schule.thema t where t.id = v_ein.thema_id), 'sterne', v_sf));
      -- Orte, in denen dieser Flug liegt: alle Flüge mit Inhalt abgelegt → Stempel golden
      for v_b in select bt.block_id from schule.block_thema bt where bt.thema_id = v_ein.thema_id loop
        if not exists (select 1 from schule.block_thema bt2 where bt2.block_id = v_b and schule.thema_einheit(bt2.thema_id) is not null
                         and not exists (select 1 from schule.abgelegt g where g.lernender_id = p_l and g.bezug = 'flug:' || bt2.thema_id)) then
          insert into schule.abgelegt (lernender_id, bezug, art, block_id) values (p_l, 'ort:' || v_b, 'ort', v_b) on conflict do nothing;
          if found then v_gold := true; end if;
        end if;
      end loop;
      if v_gold then v_erg := v_erg || jsonb_build_object('ort_gold', true); end if;
    end if;
  end if;
  return v_erg;
end $function$;
revoke all on function schule.wdh_ablegen(bigint, bigint, text) from public, anon, authenticated;

-- WD-3/5/6: Antwort auf eine fällige Etappe erkennen (vor jeder Änderung an schule.karte_stand)
create or replace function schule.karte_wdh_ereignis()
 returns trigger language plpgsql set search_path to ''
as $function$
declare v_bestanden boolean; v_sterne int := 0; v_beginn text; v_abgelegt jsonb; v_erg jsonb;
begin
  if not old.sitzt or (new.richtig <= old.richtig and new.falsch <= old.falsch) then return new; end if; -- keine Antwort
  if not schule.karte_faellig(old) then return new; end if;                                           -- keine Wiederholung
  v_bestanden := new.richtig > old.richtig and new.sitzt and new.wdh_fehler = 0 and new.wdh_ab is distinct from old.wdh_ab
                 and new.wdh_stufe = least(old.wdh_stufe + 1, 4);
  if v_bestanden then
    v_beginn := coalesce(extract(epoch from coalesce(old.wdh_ab, old.faellig_am))::bigint::text, 'x');
    insert into schule.sterne (lernender_id, menge, grund, bezug)
    values (new.lernender_id, schule.wd_regel('sterne_wdh_richtig', 10), 'wdh', 'wdh:' || new.einheit_id || ':' || new.lernziel || ':' || v_beginn)
    on conflict do nothing returning menge into v_sterne;
    perform set_config('schule.wdh_karte', new.einheit_id || '/' || new.lernziel, true);  -- sterne_aus_versuch: für diesen Versuch keine 'uebung'-Sterne
    if old.wdh_stufe >= 4 then                                                             -- letzte Wiederholung (30 Lerntage) bestanden: abgelegt
      new.faellig_am := null; new.wdh_ab := null; new.wdh_lerntage := null;
      v_abgelegt := schule.wdh_ablegen(new.lernender_id, new.einheit_id, new.lernziel);
    end if;
  end if;
  v_erg := jsonb_strip_nulls(jsonb_build_object('bestanden', v_bestanden, 'sterne', coalesce(v_sterne, 0), 'stufe_neu', new.wdh_stufe,
             'naechste_in', case when new.sitzt then new.wdh_lerntage end, 'einheit_id', new.einheit_id, 'lernziel', new.lernziel, 'abgelegt', v_abgelegt));
  perform set_config('schule.wdh_ergebnis', v_erg::text, true);
  return new;
end $function$;
create or replace trigger karte_wdh_ereignis before update on schule.karte_stand for each row execute function schule.karte_wdh_ereignis();

-- Stellen in vorhandenen Funktionen ersetzen: jede Stelle genau einmal, sonst Abbruch; schon eingespielt (Merkmal im Text) → nichts tun
create or replace function pg_temp.wd_ersetzen(p_fn text, p_merkmal text, p_alt text[], p_neu text[])
 returns void language plpgsql as $f$
declare d text := pg_get_functiondef(p_fn::regprocedure); i int;
begin
  if position(p_merkmal in d) > 0 then raise notice '% schon umgebaut', p_fn; return; end if;
  for i in 1 .. cardinality(p_alt) loop
    if (length(d) - length(replace(d, p_alt[i], ''))) / length(p_alt[i]) <> 1 then
      raise exception '%: Stelle % nicht genau einmal gefunden: %', p_fn, i, left(p_alt[i], 80); end if;
    d := replace(d, p_alt[i], p_neu[i]);
  end loop;
  execute d;
end $f$;

-- WD-5: keine 'uebung'-Sterne für den Versuch, der eine Wiederholung bestanden hat (die gibt 'wdh'-Sterne)
select pg_temp.wd_ersetzen('schule.sterne_aus_versuch()', 'WD-5',
  array[$a$begin
  if new.richtig and new.testsitzung_id is null then$a$,
        $a$    else
      insert into schule.sterne(lernender_id, menge, grund, bezug)
      values (new.lernender_id, schule.sterne_regel('sterne_uebung_richtig'), 'uebung', 'aufgabe:' || new.aufgabe_id)$a$],
  array[$a$declare v_wdh text := coalesce(current_setting('schule.wdh_karte', true), ''); -- WD-5: von karte_wdh_ereignis für diesen Versuch gesetzt
begin
  if v_wdh <> '' then perform set_config('schule.wdh_karte', '', true); end if;
  if new.richtig and new.testsitzung_id is null then$a$,
        $a$    elsif v_wdh <> '' and v_wdh = (select a.einheit_id || '/' || a.variante_gruppe from schule.aufgabe a where a.id = new.aufgabe_id) then
      null; -- WD-5: bestandene Wiederholung – Sterne bucht die Wiederholung (grund 'wdh'), nicht doppelt
    else
      insert into schule.sterne(lernender_id, menge, grund, bezug)
      values (new.lernender_id, schule.sterne_regel('sterne_uebung_richtig'), 'uebung', 'aufgabe:' || new.aufgabe_id)$a$]);

-- WD-3: Mischkarte aus fälliger Etappe, richtig im 1. Versuch ohne Tipp = bestandene Wiederholung (Takt wie karte_buchen: 1, 3, 7, 14, 30)
select pg_temp.wd_ersetzen('schule.misch_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)', 'WD-3',
  array[$a$      update schule.karte_stand set misch_ok_am = p_zeit, richtig = richtig + 1, zuletzt = p_zeit
       where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe;$a$],
  array[$a$      update schule.karte_stand k set misch_ok_am = p_zeit, richtig = k.richtig + 1, zuletzt = p_zeit,
             -- WD-3: aus einer fälligen Etappe zählt sie als bestandene Wiederholung (rückt im Takt weiter)
             wdh_fehler = case when schule.karte_faellig(k) then 0 else k.wdh_fehler end,
             wdh_stufe = case when schule.karte_faellig(k) then least(k.wdh_stufe + 1, 4) else k.wdh_stufe end,
             faellig_am = case when schule.karte_faellig(k) then p_zeit + (array[1, 3, 7, 14, 30])[least(k.wdh_stufe + 1, 4) + 1] * interval '1 day' else k.faellig_am end,
             wdh_ab = case when schule.karte_faellig(k) then p_zeit else k.wdh_ab end,
             wdh_lerntage = case when schule.karte_faellig(k) then (array[1, 3, 7, 14, 30])[least(k.wdh_stufe + 1, 4) + 1] else k.wdh_lerntage end
       where k.lernender_id = p_l and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe;$a$]);

-- WD-3: Auswahl neuer Mischkarten bevorzugt fällige Etappen (sonst wie bisher)
select pg_temp.wd_ersetzen('schule.mischkarten_waehlen(bigint, bigint, integer)', 'WD-3',
  array[$a$    select k.einheit_id, k.lernziel, e.inhalt, b.stadt,$a$,
        $a$'quelle', kand.quelle, 'stadt', kand.stadt,$a$,
        $a$           case kand.quelle when 'flug' then 1 when 'kontinent' then 2 else 3 end rang, random() zufall$a$,
        $a$     order by rang, zufall limit p_anzahl) x;$a$,
        $a$jsonb_agg(x.j order by x.rang, x.zufall)$a$],
  array[$a$    select k.einheit_id, k.lernziel, e.inhalt, b.stadt, schule.karte_faellig(k) faellig, -- WD-3$a$,
        $a$'quelle', kand.quelle, 'faellig', kand.faellig, 'stadt', kand.stadt,$a$,
        $a$           case when kand.faellig then 0 else 1 end vorrang, case kand.quelle when 'flug' then 1 when 'kontinent' then 2 else 3 end rang, random() zufall$a$,
        $a$     order by vorrang, rang, zufall limit p_anzahl) x;$a$,
        $a$jsonb_agg(x.j order by x.vorrang, x.rang, x.zufall)$a$]);

-- WD-3: ausgegebene Mischkarten aus fälligen Etappen zuerst
select pg_temp.wd_ersetzen('schule.mischkarten(bigint, bigint, integer)', 'WD-3',
  array[$a$jsonb_agg(z.j order by z.rang, z.nr)$a$,
        $a$           u.nr
      from unnest(v_ids)$a$],
  array[$a$jsonb_agg(z.j order by z.vorrang, z.rang, z.nr)$a$,
        $a$           u.nr, case when coalesce((select schule.karte_faellig(k) from schule.karte_stand k
                                       where k.lernender_id = p_lernender and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe), false) then 0 else 1 end vorrang -- WD-3
      from unnest(v_ids)$a$]);

-- WD-4: gesetzte Etappen gestaffelt in den Takt (statt alle am nächsten Lerntag)
select pg_temp.wd_ersetzen('schule.flug_wdh_setzen(bigint, bigint, text)', 'WD-4',
  array[$a$v_snap jsonb := '[]'::jsonb;$a$,
        $a$    v_vor := null;
$a$,
        $a$      update schule.karte_stand set wdh_stufe = 0, faellig_am = now() + interval '1 day', wdh_fehler = 0, wdh_ab = now(), wdh_lerntage = 1, wdh_gesetzt_am = now()$a$,
        $a$      update schule.karte_stand set sitzt = true, sitzt_am = now(), wdh_stufe = 0, faellig_am = now() + interval '1 day', wdh_fehler = 0,
             wdh_ab = now(), wdh_lerntage = 1, gesetzt_am = now(), gesetzt_von = p_wer, wdh_gesetzt_am = now()$a$],
  array[$a$v_snap jsonb := '[]'::jsonb; v_tag int;$a$,
        $a$    v_vor := null;
    v_tag := schule.wdh_staffel_tag(p_l); -- WD-4: höchstens wdh_gesetzt_je_lerntag neue Etappen je Lerntag
$a$,
        $a$      update schule.karte_stand set wdh_stufe = 0, faellig_am = now() + v_tag * interval '1 day', wdh_fehler = 0, wdh_ab = now(), wdh_lerntage = v_tag, wdh_gesetzt_am = now()$a$,
        $a$      update schule.karte_stand set sitzt = true, sitzt_am = now(), wdh_stufe = 0, faellig_am = now() + v_tag * interval '1 day', wdh_fehler = 0,
             wdh_ab = now(), wdh_lerntage = v_tag, gesetzt_am = now(), gesetzt_von = p_wer, wdh_gesetzt_am = now()$a$]);

-- Antwort: wiederholung / abgelegt aus karte_wdh_ereignis anhängen (schule.uebung_pruefen_wd; die api-Funktion ruft sie nach der Zugriffsprüfung)
create or replace function schule.uebung_pruefen_wd(p_l bigint, p_daten jsonb)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_r jsonb; v_w jsonb;
begin
  perform set_config('schule.wdh_ergebnis', '', true);
  v_r := schule.uebung_pruefen_intern(p_l, p_daten);
  v_w := nullif(current_setting('schule.wdh_ergebnis', true), '')::jsonb;
  perform set_config('schule.wdh_ergebnis', '', true);
  if v_w is not null then
    v_r := v_r || jsonb_build_object('wiederholung', jsonb_build_object('bestanden', v_w->'bestanden', 'sterne', v_w->'sterne', 'stufe_neu', v_w->'stufe_neu', 'naechste_in', v_w->'naechste_in'))
               || case when v_w ? 'abgelegt' then jsonb_build_object('abgelegt', v_w->'abgelegt') else '{}'::jsonb end;
  end if;
  return v_r;
end $function$;
revoke all on function schule.uebung_pruefen_wd(bigint, jsonb) from public, anon, authenticated;

select pg_temp.wd_ersetzen('api.schule_uebung_pruefen(text, jsonb)', 'uebung_pruefen_wd',
  array[$a$  return schule.uebung_pruefen_intern(v_l, p_daten); end $a$],
  array[$a$  return schule.uebung_pruefen_wd(v_l, p_daten); end $a$]); -- WD-S

-- Konto/Reisepass: je Flug abgelegt, je Ort gold
create or replace function schule.konto_wd(p_l bigint)
 returns jsonb language sql stable set search_path to ''
as $function$
  with k as (select schule.konto(p_l) j),
  fl as (
    select e.id einheit_id, e.thema_id, t.unterthema titel,
           coalesce(nullif(array(select jsonb_array_elements_text(coalesce(e.inhalt->'bewertung'->'lernziele_pflicht', '[]'::jsonb))), '{}'),
                    array(select et->>'lernziel' from jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) et)) etappen
      from schule.einheit e join schule.thema t on t.id = e.thema_id
     where exists (select 1 from schule.karte_stand ks where ks.lernender_id = p_l and ks.einheit_id = e.id))
  select (select j from k)
    || jsonb_build_object('orte', (select coalesce(jsonb_agg(o || jsonb_build_object('gold', exists (select 1 from schule.abgelegt g
                                     where g.lernender_id = p_l and g.bezug = 'ort:' || (o->>'block_id')))), '[]'::jsonb)
                                   from jsonb_array_elements(coalesce((select j->'orte' from k), '[]'::jsonb)) o))
    || jsonb_build_object('fluege', (select coalesce(jsonb_agg(jsonb_build_object('thema_id', fl.thema_id, 'einheit_id', fl.einheit_id, 'titel', fl.titel,
           'abgelegt', exists (select 1 from schule.abgelegt g where g.lernender_id = p_l and g.bezug = 'flug:' || fl.thema_id),
           'etappen', cardinality(fl.etappen),
           'etappen_abgelegt', (select count(*) from unnest(fl.etappen) x where exists (select 1 from schule.abgelegt g
                                  where g.lernender_id = p_l and g.bezug = 'etappe:' || fl.einheit_id || ':' || x))) order by fl.thema_id), '[]'::jsonb) from fl));
$function$;

select pg_temp.wd_ersetzen('api.schule_konto(text, jsonb)', 'konto_wd',
  array[$a$'konto', schule.konto(v_l),$a$],
  array[$a$'konto', schule.konto_wd(v_l), -- WD-S: + fluege[], orte[].gold$a$]);

-- WD-1/WD-2/WD-4: schule_wiederholung (bisherige Felder ok, aufgaben, faellig bleiben; neu: runde, runde_gemacht, gestaffelt, aufgaben[].pflicht)
--   anzahl: höchstens so viele Aufgaben (bisher höchstens 6, jetzt höchstens 60); ohne anzahl alle fälligen (≤ 60). Die App 0.84 schickt anzahl 6 → wie bisher 6 Stück.
create or replace function schule.wiederholung_intern(p_l bigint, p_daten jsonb, p_leiter boolean)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_l bigint := p_l; v_n int := least(coalesce(nullif(p_daten->>'anzahl', '')::int, 60), 60);
  v_test boolean; v_leiter boolean; v_erg jsonb; v_faellig int; v_runde int;
begin
  select ist_test into v_test from schule.lernender where id = v_l;
  v_leiter := p_leiter;
  select count(*) into v_faellig from schule.karte_stand k where k.lernender_id = v_l and schule.karte_faellig(k);
  v_runde := schule.wdh_runde_groesse(v_l, v_faellig);
  -- Reihenfolge WD-1: Wiederholungs-Fehler, am längsten fällig, niedrigste Stufe
  select coalesce(jsonb_agg(x.j || jsonb_build_object('pflicht', x.nr <= v_runde) order by x.nr), '[]'::jsonb) into v_erg from (
    select row_number() over (order by (k.wdh_fehler > 0) desc, k.faellig_am nulls first, k.wdh_stufe, k.einheit_id, k.lernziel) nr,
           schule.aufgabe_anzeige(a, true) || jsonb_build_object('einheit_id', k.einheit_id, 'stadt', b.stadt, 'lernziel', k.lernziel, 'wdh_stufe', k.wdh_stufe,
             'etappe', (select et->>'titel' from jsonb_array_elements(e.inhalt->'etappen') et where et->>'lernziel' = k.lernziel limit 1)) j
      from schule.karte_stand k join schule.einheit e on e.id = k.einheit_id join schule.block b on b.id = e.block_id
      cross join lateral (select a.* from schule.aufgabe a where a.einheit_id = k.einheit_id and a.pool = 'uebung' and a.variante_gruppe = k.lernziel
                            and (a.freigegeben)
                          order by (coalesce(a.stufe, 2) = 1), (select count(*) from schule.versuch vs where vs.lernender_id = v_l and vs.aufgabe_id = a.id), random() limit 1) a
     where k.lernender_id = v_l and schule.karte_faellig(k)
       and (e.status in ('geprueft','freigegeben') or (e.status = 'entwurf' and coalesce(v_test, false) and v_leiter))
     order by nr limit v_n) x;
  return jsonb_build_object('ok', true, 'aufgaben', v_erg, 'faellig', v_faellig, 'runde', v_runde,
    'runde_gemacht', exists (select 1 from schule.wdh_runde r where r.lernender_id = v_l and r.tag = schule.heute_tag(v_l)),
    'gestaffelt', (select count(*) from schule.karte_stand k where k.lernender_id = v_l and k.sitzt and k.wdh_gesetzt_am is not null and k.wdh_stufe = 0
                     and k.wdh_fehler = 0 and k.wdh_lerntage > 1 and not schule.karte_faellig(k)));
end $function$;

revoke all on function schule.wiederholung_intern(bigint, jsonb, boolean) from public, anon, authenticated;

create or replace function api.schule_wiederholung(p_schluessel text, p_daten jsonb)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_l bigint := (p_daten->>'lernender_id')::bigint;
begin
  perform schule.zugriff(p_schluessel, v_l);
  return schule.wiederholung_intern(v_l, p_daten, schule.ist_leiter(p_schluessel)); -- WD-S
end $function$;

-- WD-2: Merker setzen
create or replace function schule.wdh_runde_fertig(p_l bigint)
 returns jsonb language plpgsql set search_path to ''
as $function$
begin
  insert into schule.wdh_runde (lernender_id, tag) values (p_l, schule.heute_tag(p_l)) on conflict do nothing;
  return jsonb_build_object('ok', true, 'runde_gemacht', true, 'tag', schule.heute_tag(p_l));
end $function$;
revoke all on function schule.wdh_runde_fertig(bigint) from public, anon, authenticated;

create or replace function api.schule_wiederholung_runde_fertig(p_schluessel text, p_daten jsonb default null)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_l bigint := (p_daten->>'lernender_id')::bigint;
begin
  perform schule.zugriff(p_schluessel, v_l);
  return schule.wdh_runde_fertig(v_l);
end $function$;
grant execute on function api.schule_wiederholung_runde_fertig(text, jsonb) to council_mcp;
revoke all on function api.schule_wiederholung_runde_fertig(text, jsonb) from public, anon, authenticated;

-- Bestand unverändert?
do $mig$
declare v_t text;
begin
  select string_agg(v.t, ', ') into v_t from wd_vorher v
   where v.s <> (select case v.t
       when 'karte' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.karte_stand x)
       when 'lernziel' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernziel_stand x)
       when 'route' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.route x)
       when 'sterne' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x) end);
  if v_t is not null then raise exception 'WD-S: Bestand verändert (%)', v_t; end if;
  raise notice 'WD-S: Karten, Lernstände, Plan, Sterne unverändert';
end $mig$;
