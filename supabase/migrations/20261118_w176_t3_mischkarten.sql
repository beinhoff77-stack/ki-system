-- Bau-Auftrag G, Teil 3 (Werkstatt-Wunsch 176, P2): Gemischte Reihenfolge – Mischkarten.
-- Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE; Lernstände bleiben unverändert.
--
-- Idee: Beim normalen Üben ist jede 4. Bordkarte (Klasse ≤ 6: jede 6.) eine Bordkarte aus einer anderen Etappe, die bei diesem Kind schon gelandet ist.
-- Keine Zusatzkarten, kein Pflicht-Tor. Quelle dynamisch je Kind, unabhängig vom Flugplan (wie api.schule_wiederholung).
-- Keine neue Aktion in lernen-api:
--   schule_einheit_lesen liefert zusätzlich  mischkarten: [Bordkarte + einheit_id, lernziel, etappe, stadt, quelle ('flug' | 'kontinent' | 'aelter')]  und  misch_jede: 4 bzw. 6
--   schule_uebung_pruefen nimmt  misch: true  an (sonst wie bisher) und antwortet zusätzlich mit  misch: { etappe, stadt, ok }  (ohne karte der aktuellen Etappe)
-- Wirkung (Trigger schule.versuch_karte → schule.misch_buchen):
--   richtig im 1. Versuch ohne Tipp → karte_stand.misch_ok_am der Herkunftsetappe (Beleg „in Mischung erkannt“, Bedingung für „sicher“)
--   endgültig falsch → Herkunftsetappe wie ein Fehler in der Wiederholung (am nächsten Lerntag fällig); keine Abzüge
--   zählt nie für „gelandet“ der gerade geübten Etappe; Knobel-Bordkarten (bonus) und gesperrte Aufgaben kommen nie als Mischkarte
-- „sicher“ verlangt ab jetzt zusätzlich misch_ok_am.

alter table schule.karte_stand add column if not exists misch_ok_am timestamptz;
comment on column schule.karte_stand.misch_ok_am is 'W176 P2: zuletzt in einer Mischkarte richtig erkannt (1. Versuch ohne Tipp)';
alter table schule.versuch add column if not exists misch boolean not null default false;
comment on column schule.versuch.misch is 'W176 P2: Versuch als Mischkarte beim Üben einer anderen Etappe';

insert into schule.regel(schluessel, wert, hinweis) values
  ('misch_jede', '4'::jsonb, 'W176: beim Üben jede n-te Bordkarte als Mischkarte (Startwert, an Daten justieren)'),
  ('misch_jede_bis_kl6', '6'::jsonb, 'W176: dasselbe für Klasse ≤ 6'),
  ('misch_ab_gelandet', '3'::jsonb, 'W176: Mischkarten erst, wenn im aktuellen Flug so viele Etappen gelandet sind')
  on conflict (schluessel) do nothing;

-- Kandidaten: je gelandeter Etappe des Kindes eine Bordkarte (Pool uebung, Stufe 2–3, nur freigegebene Aufgaben – auch beim Testkind; Entwurfs-Flüge nur für das Testkind), am seltensten gesehen.
-- Reihenfolge: gleicher Flug, gleicher Kontinent, älterer Flug. Die gerade geübte Etappe schließt die App aus (sie kennt sie).
create or replace function schule.mischkarten(p_lernender bigint, p_einheit bigint, p_anzahl int default 8)
 returns jsonb
 language sql
 volatile -- random() für die Auswahl bei Gleichstand
 set search_path to ''
as $function$
  with ich as (select coalesce(ist_test, false) test from schule.lernender where id = p_lernender),
  hier as (select b.kontinent_id from schule.einheit e join schule.block b on b.id = e.block_id where e.id = p_einheit),
  kand as (
    select k.einheit_id, k.lernziel, e.inhalt, b.stadt,
           case when k.einheit_id = p_einheit then 'flug' when b.kontinent_id = (select kontinent_id from hier) then 'kontinent' else 'aelter' end quelle,
           (select a.id from schule.aufgabe a
             where a.einheit_id = k.einheit_id and a.variante_gruppe = k.lernziel and a.pool = 'uebung' and a.stufe in (2, 3)
               and a.freigegeben -- gesperrte Aufgaben nie, auch nicht für das Testkind (Korrektur 18.11.); Entwurfs-Flüge des Testkinds über e.status unten
             order by (select count(*) from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id), random() limit 1) aufgabe_id
      from schule.karte_stand k join schule.einheit e on e.id = k.einheit_id join schule.block b on b.id = e.block_id
     where k.lernender_id = p_lernender and k.sitzt
       and (e.status in ('geprueft', 'freigegeben') or (e.status = 'entwurf' and (select test from ich))))
  select coalesce(jsonb_agg(x.j order by x.rang, x.zufall), '[]'::jsonb) from (
    select schule.aufgabe_anzeige(a, true) || jsonb_build_object('einheit_id', kand.einheit_id, 'quelle', kand.quelle, 'stadt', kand.stadt,
             'etappe', (select et->>'titel' from jsonb_array_elements(kand.inhalt->'etappen') et where et->>'lernziel' = kand.lernziel limit 1)) j,
           case kand.quelle when 'flug' then 1 when 'kontinent' then 2 else 3 end rang, random() zufall
      from kand join schule.aufgabe a on a.id = kand.aufgabe_id
     order by rang, zufall limit p_anzahl) x;
$function$;

-- Buchung einer Mischkarte (nur wenn die Herkunftsetappe beim Kind gelandet ist; sonst wie eine normale Bordkarte)
create or replace function schule.misch_buchen(p_l bigint, p_aufgabe bigint, p_richtig boolean, p_hilfe smallint, p_zeit timestamp with time zone)
 returns void
 language plpgsql
 set search_path to ''
as $function$
declare a schule.aufgabe;
begin
  select * into a from schule.aufgabe where id = p_aufgabe;
  if a.id is null or a.pool <> 'uebung' then return; end if;
  if not exists (select 1 from schule.karte_stand k where k.lernender_id = p_l and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe and k.sitzt) then
    perform schule.karte_buchen(p_l, p_aufgabe, p_richtig, p_hilfe, p_zeit); return;
  end if;
  if p_richtig then
    if coalesce(p_hilfe, 0) = 0 then
      update schule.karte_stand set misch_ok_am = p_zeit, richtig = richtig + 1, zuletzt = p_zeit
       where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe;
    end if; -- Tipp oder 2. Versuch: kein Beleg, nichts fällig
  else
    perform schule.karte_buchen(p_l, p_aufgabe, false, p_hilfe, p_zeit); -- wie ein Fehler in der Wiederholung: am nächsten Lerntag fällig
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
  end if;
  return new;
end $function$;

-- „sicher“: zusätzlich eine richtige Mischkarte
create or replace function schule.karte_sicher(k schule.karte_stand)
 returns boolean
 language sql
 stable
 set search_path to ''
as $function$
  select coalesce(k.sitzt, false) and coalesce(k.wdh_stufe, 0) >= 4 and k.misch_ok_am is not null
     and exists (select 1 from schule.testsitzung t where t.lernender_id = k.lernender_id and t.einheit_id = k.einheit_id and t.art = 'nachtest' and t.ergebnis = 'bestanden');
$function$;

do $$
declare d text;
begin
  -- uebung_pruefen_intern: misch annehmen, speichern und zurückmelden
  d := pg_get_functiondef('schule.uebung_pruefen_intern(bigint, jsonb)'::regprocedure);
  if position('insert into schule.versuch(lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf)' in d) = 0
     or position('(select count(*) + 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id), v_anlauf);' in d) = 0
     or position('  return jsonb_strip_nulls(jsonb_build_object(''ok'', true, ''format_ok'', true, ''richtig'', v_ri, ''grund'', b->>''grund'', ''loesung'', a.loesung, ''loesungsweg'', a.loesungsweg,' in d) = 0 then
    raise exception 'Stellen in uebung_pruefen_intern nicht gefunden';
  end if;
  d := replace(d, 'insert into schule.versuch(lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf)',
                  'insert into schule.versuch(lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf, misch)');
  d := replace(d, '(select count(*) + 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id), v_anlauf);',
                  '(select count(*) + 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id), v_anlauf, coalesce((p_daten->>''misch'')::boolean, false) and a.pool = ''uebung'');');
  d := replace(d, '  return jsonb_strip_nulls(jsonb_build_object(''ok'', true, ''format_ok'', true, ''richtig'', v_ri, ''grund'', b->>''grund'', ''loesung'', a.loesung, ''loesungsweg'', a.loesungsweg,',
    $r$  if coalesce((p_daten->>'misch')::boolean, false) and a.pool = 'uebung' then
    return jsonb_strip_nulls(jsonb_build_object('ok', true, 'format_ok', true, 'richtig', v_ri, 'grund', b->>'grund', 'loesung', a.loesung, 'loesungsweg', a.loesungsweg,
      'misch', jsonb_build_object('lernziel', a.variante_gruppe, 'einheit_id', a.einheit_id,
        'etappe', (select et->>'titel' from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') et where e.id = a.einheit_id and et->>'lernziel' = a.variante_gruppe limit 1),
        'stadt', (select b2.stadt from schule.einheit e join schule.block b2 on b2.id = e.block_id where e.id = a.einheit_id),
        'ok', v_ri and v_hilfe = 0 and coalesce(v_anlauf, 1) = 1)));
  end if;
  return jsonb_strip_nulls(jsonb_build_object('ok', true, 'format_ok', true, 'richtig', v_ri, 'grund', b->>'grund', 'loesung', a.loesung, 'loesungsweg', a.loesungsweg,$r$);
  execute d;

  -- einheit_lesen_intern: Mischkarten-Kandidaten und Dosis
  d := pg_get_functiondef('schule.einheit_lesen_intern(bigint, bigint)'::regprocedure);
  if position('''etappen_stand'', schule.etappen_stand(p_lernender, p_einheit),' in d) = 0 then raise exception 'Stelle in einheit_lesen_intern nicht gefunden'; end if;
  d := replace(d, '''etappen_stand'', schule.etappen_stand(p_lernender, p_einheit),',
    $r$'etappen_stand', schule.etappen_stand(p_lernender, p_einheit),
    'mischkarten', schule.mischkarten(p_lernender, p_einheit),
    'misch_jede', (select case when coalesce(l.klasse, 99) <= 6 then coalesce((select (wert #>> '{}')::int from schule.regel where schluessel = 'misch_jede_bis_kl6'), 6)
                               else coalesce((select (wert #>> '{}')::int from schule.regel where schluessel = 'misch_jede'), 4) end from schule.lernender l where l.id = p_lernender),
    'misch_ab', coalesce((select (wert #>> '{}')::int from schule.regel where schluessel = 'misch_ab_gelandet'), 3),$r$);
  execute d;

  -- etappen_stand und lernstand: Beleg der Mischkarte
  d := pg_get_functiondef('schule.etappen_stand(bigint, bigint)'::regprocedure);
  if position('''sicher'', coalesce(schule.karte_sicher(k), false),' in d) = 0 then raise exception 'Stelle in etappen_stand nicht gefunden (Teil 1 eingespielt?)'; end if;
  d := replace(d, '''sicher'', coalesce(schule.karte_sicher(k), false),', '''sicher'', coalesce(schule.karte_sicher(k), false), ''misch_ok'', k.misch_ok_am is not null,');
  execute d;
  d := pg_get_functiondef('api.schule_lernstand(text, jsonb)'::regprocedure);
  if position('''sicher'', coalesce(schule.karte_sicher(k), false),' in d) = 0 then raise exception 'Stelle in schule_lernstand nicht gefunden (Teil 1 eingespielt?)'; end if;
  d := replace(d, '''sicher'', coalesce(schule.karte_sicher(k), false),', '''sicher'', coalesce(schule.karte_sicher(k), false), ''misch_ok'', k.misch_ok_am is not null,');
  execute d;
end $$;

-- Korrektur 18.11. (Probelauf: Rauchtest „FEHLER 2“): Gesperrte Aufgaben (freigegeben = false, z. B. die seit 17.11. gesperrten überzähligen Übungen) bekommt auch das Testkind nicht mehr.
-- Dieselbe Stelle gab es an zwei weiteren Auswahl-Orten; dort gilt jetzt dieselbe Regel (Prüfen siehe 20261118_w176_a_gesperrt_pruefen.sql). Entwurfs-Flüge sieht das Testkind weiter – das regelt der Status der Einheit
-- (einheit_pruefen_sichtbar bzw. e.status), nicht das Feld freigegeben der Aufgabe.
do $$
declare d text;
begin
  d := pg_get_functiondef('schule.einheit_lesen_intern(bigint, bigint)'::regprocedure); -- Übungen und Knobel-Bordkarten der Einheit
  if position('(a.freigegeben or exists (select 1 from schule.lernender l where l.id = p_lernender and l.ist_test))' in d) = 0 then raise exception 'Stelle in einheit_lesen_intern nicht gefunden'; end if;
  d := replace(d, '(a.freigegeben or exists (select 1 from schule.lernender l where l.id = p_lernender and l.ist_test))', '(a.freigegeben)');
  execute d;
  d := pg_get_functiondef('api.schule_wiederholung(text, jsonb)'::regprocedure);
  if position('(a.freigegeben or coalesce(v_test, false))' in d) = 0 then raise exception 'Stelle in schule_wiederholung nicht gefunden'; end if;
  d := replace(d, '(a.freigegeben or coalesce(v_test, false))', '(a.freigegeben)');
  execute d;
  -- schule.uebung_pruefen_intern: bewusst NICHT mehr hier (Betrieb 18.11.) – beim Prüfen gilt die Regel aus 20261118_w176_a_gesperrt_pruefen.sql
  -- (gesperrte Bordkarte in geprüften/freigegebenen Flügen wird noch gewertet; die Sperre greift nur bei der Auswahl).
end $$;
