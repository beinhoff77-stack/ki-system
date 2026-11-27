-- Bau-Auftrag WD (22.11.), Server-Teil WD-S (Stand WD-S 2, 22.11. abends): Wiederholungen dynamisch – Stau vermeiden, Belohnung fürs Ablegen.
-- Vorgabe: inhalte/AUFTRAEGE.md „Bau-Auftrag WD“, „Nachtrag zum Bau-Auftrag WD – Reihenfolge und Schnittstelle“ (verbindlich) und „Rückläufer 22.11. abends“ Teil A
-- (ChatGPT 911/912).
--
-- Ziel und Grenzen (ehrlich):
--   Ziel ist, einen Stau schrittweise abzubauen – bei ausreichender Kapazität in etwa fünf Lerntagen. Das ist keine Garantie: Wer täglich mehr landet
--   als die Runde trägt, baut weiter auf. Bekannte Grenze: Ohne Bündeln (Entscheidung des Nutzers: jede Etappe für sich) trägt die Kapazität dauerhaft
--   etwa 3 Landungen je Lerntag (jede Landung erzeugt 5 Wiederholungen; die Runde hat höchstens 12 Pflicht-Plätze, dazu freiwillige und Mischkarten).
--
-- Befund heute (Live-Text gelesen 22.11.):
--   Takt: Landung → Stufe 0 (1 Lerntag), jede richtige fällige Wiederholung +1 Stufe: 3, 7, 14, 30 Lerntage; ab Stufe 4 bleibt es bei 30 (karte_buchen).
--   Sterne: Trigger versuch_sterne gibt für JEDE richtige Antwort außerhalb von Tests (auch mit Tipp/2. Anlauf, auch Wiederholung und Mischkarte)
--   sterne_uebung_richtig = 10 Sterne – aber je Aufgabe nur einmal im Leben (Schlüssel lernender, grund 'uebung', bezug 'aufgabe:<id>').
--   → NICHT gekürzt: sterne_wdh_richtig steht auf 10 (Schnittstelle nennt 5), bis der Nutzer entscheidet (eine Zeile in schule.regel).
--
-- Was diese Datei baut:
--   WD-1 Runde: Größe ein Fünftel der fälligen, aufgerundet, min 6, max 12 (bis Klasse 6 max 10; bis 6 fällige: alle). Auswahl: mindestens ein Drittel der
--        Pflicht-Plätze für die am längsten fälligen Etappen, die übrigen nach Wiederholungs-Fehler (auch falsche Mischkarte seit Beginn der Fälligkeit) →
--        am längsten fällig → niedrigste Stufe.
--   WD-2 Runde serverseitig: beim ersten Abruf des Lerntags festgehalten (schule.wdh_runde: Tagesziel, schule.wdh_runde_etappe: zugeordnete Etappen).
--        Jede Antwort auf eine dieser Etappen (richtig oder falsch – falsch = bearbeitet, nicht bestanden) hakt sie ab; sind alle abgehakt, setzt der Server
--        „gemacht“ selbst. Eine Etappe ohne verfügbare Aufgabe (inzwischen gesperrt) zählt als bearbeitet; 0 fällige = sofort gemacht. Zweites Gerät setzt
--        dieselbe Runde fort; neue Fälligkeiten am selben Tag sind nur freiwillig. api.schule_wiederholung_runde_fertig bestätigt nur und lehnt ab, wenn
--        Aufgaben fehlen.
--   WD-3 Mischkarten: Auswahl und Ausgabe bevorzugen fällige Etappen. Mischkarte aus fälliger Etappe, richtig im 1. Versuch ohne Tipp = bestandene
--        Wiederholung (Takt wie karte_buchen); aus nicht fälliger Etappe nur der Misch-Beleg (misch_ok_am), kein Fortschritt. Falsch: wie heute (fällig,
--        öffnet nie) und zählt für die Reihenfolge der nächsten Runde als Wiederholungs-Fehler.
--   WD-4 flug_wdh_setzen: gesetzte Etappen gestaffelt – je Kind höchstens wdh_gesetzt_je_lerntag (6) neue erste Wiederholungen je Lerntag.
--        Den vorhandenen Stau streckt die eigene Datei 20261122_wd_4b_stau_strecken.sql.
--   WD-5 Sterne je bestandener Wiederholung: genau einmal je Etappe und Fälligkeit (grund 'wdh', bezug 'wdh:<einheit>:<etappe>:<beginn>') – auch bei zwei
--        Geräten oder doppelt gesendeter Antwort: Nach dem ersten Bestehen ist die Etappe nicht mehr fällig (Zeile gesperrt: karte_buchen „for update“,
--        misch_buchen über update), der Schlüssel verhindert eine zweite Buchung. Für denselben Versuch keine 'uebung'-Sterne.
--   WD-6 Ablegen: bestandene fünfte Wiederholung (die auf Stufe 4, 30 Lerntage nach der vierten) – frühestens 55 Lerntage nach der Landung (1+3+7+14+30).
--        Nicht zusätzlich an „sicher“ gebunden (Wunsch der Kinder). „abgelegt“ ist ein eigenes Ereignis in schule.abgelegt, nie aus wdh_stufe abgeleitet.
--        Etappe: raus aus dem Takt, 30 Sterne; alle Pflicht-Etappen des Flugs: 100 Sterne, Flug golden; alle Flüge eines Orts: Stempel golden; je einmal.
--        Letzte Wiederholung: Wiederholungs-Sterne + 30 + ggf. 100 kommen zusammen, je einmal.
--        Rückfall: Fällt eine abgelegte Etappe beim Üben, mit einer Mischkarte oder im Nachtest/Test durch, kommt sie am nächsten Lerntag zurück in den
--        Takt (Stufe 2); Gold, Sterne und Einblendung bleiben, ein zweites Ablegen gibt nichts.
--   Antworten: schule_uebung_pruefen + wiederholung {bestanden, sterne, stufe_neu, naechste_in} und abgelegt {etappe {titel, sterne}, flug? {titel, sterne}, ort_gold?};
--   schule_konto: konto.fluege[] {thema_id, einheit_id, titel, abgelegt, etappen_abgelegt, etappen}, konto.orte[].gold.
--
-- Technik: Ein Trigger vor jeder Änderung an schule.karte_stand erkennt die Antwort auf eine Etappe (richtig/falsch zählt hoch), hakt die Runde ab,
--   erkennt bestandene Wiederholungen und den Rückfall nach dem Ablegen; ein Trigger nach „fehler“ in schule.lernziel_stand holt abgelegte Etappen zurück.
--   karte_buchen, uebung_pruefen_intern, test_abschliessen_intern und die Versuch-Trigger bleiben unverändert; geändert (genau bezeichnete Stellen, jede genau
--   einmal geprüft): sterne_aus_versuch, misch_buchen, mischkarten_waehlen, mischkarten, flug_wdh_setzen, api.schule_uebung_pruefen, api.schule_konto;
--   neu geschrieben: api.schule_wiederholung (bisherige Felder bleiben). Prüfregel sterne_grund_check um 'wdh', 'etappe_abgelegt', 'flug_abgelegt' erweitert.
-- Bestand: neue Tabellen, Regeln, erweiterte Prüfregel; keine Änderung an Lernständen, Karten, Plan, Sternen (am Ende geprüft, sonst Abbruch).
-- In einer Transaktion einspielen. Nicht ausgeführt – der Haupt-Chat spielt ein (dazu lernen-api 0.9.0). Kein DROP einer Tabelle/Spalte, kein DELETE.
-- Wiederholt ausführbar.

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

-- Prüfregel der Sterne-Gründe um die neuen Gründe erweitern (Constraint ersetzen; bestehende Gründe bleiben)
do $mig$
declare d text := (select pg_get_constraintdef(c.oid) from pg_constraint c where c.conrelid = 'schule.sterne'::regclass and c.conname = 'sterne_grund_check');
begin
  if d is not null and position('etappe_abgelegt' in d) > 0 then return; end if;
  if d is not null and d <> $a$CHECK ((grund = ANY (ARRAY['uebung'::text, 'test'::text, 'ort'::text, 'einloesung'::text, 'korrektur_hand'::text, 'bonus'::text, 'expedition'::text])))$a$ then
    raise exception 'sterne_grund_check hat sich geändert (%), bitte prüfen', d; end if;
  alter table schule.sterne drop constraint if exists sterne_grund_check;
  alter table schule.sterne add constraint sterne_grund_check check (grund = any (array['uebung', 'test', 'ort', 'einloesung', 'korrektur_hand', 'bonus', 'expedition',
                                                                                       'wdh', 'etappe_abgelegt', 'flug_abgelegt']));
end $mig$;

-- WD-2: die Runde je Kind und Lerntag (heute_tag), beim ersten Abruf festgehalten
create table if not exists schule.wdh_runde (
  lernender_id bigint not null references schule.lernender(id),
  tag date not null,
  ziel integer not null default 0,            -- Pflicht-Aufgaben dieser Runde
  faellig integer not null default 0,         -- fällige beim Festhalten
  angelegt_am timestamptz not null default now(),
  fertig_am timestamptz,                       -- vom Server gesetzt, sobald alle Etappen bearbeitet sind
  primary key (lernender_id, tag)
);
comment on table schule.wdh_runde is 'WD-2: Wiederholungs-Runde eines Lerntags (festgehalten beim ersten Abruf); fertig_am setzt der Server';
alter table schule.wdh_runde enable row level security;
revoke all on table schule.wdh_runde from public, anon, authenticated;

create table if not exists schule.wdh_runde_etappe (
  lernender_id bigint not null, tag date not null, nr integer not null,
  einheit_id bigint not null, lernziel text not null,
  bearbeitet_am timestamptz,                   -- Antwort (richtig oder falsch) auf diese Etappe an diesem Lerntag
  primary key (lernender_id, tag, einheit_id, lernziel),
  foreign key (lernender_id, tag) references schule.wdh_runde (lernender_id, tag)
);
comment on table schule.wdh_runde_etappe is 'WD-2: Etappen der Wiederholungs-Runde eines Lerntags';
alter table schule.wdh_runde_etappe enable row level security;
revoke all on table schule.wdh_runde_etappe from public, anon, authenticated;

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

-- Hat diese Etappe eine Aufgabe, die gerade gezeigt werden kann? (sonst zählt sie in der Runde als bearbeitet)
create or replace function schule.wdh_aufgabe_da(p_e bigint, p_lz text)
 returns boolean language sql stable set search_path to ''
as $function$
  select exists (select 1 from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
                  where a.einheit_id = p_e and a.variante_gruppe = p_lz and a.pool = 'uebung' and a.freigegeben and e.status in ('geprueft', 'freigegeben'));
$function$;

-- WD-2: Runde prüfen – sind alle Etappen bearbeitet (oder ohne Aufgabe), setzt der Server fertig_am. Liefert die Zahl offener Etappen.
create or replace function schule.wdh_runde_pruefen(p_l bigint, p_tag date)
 returns integer language plpgsql set search_path to ''
as $function$
declare v_offen int;
begin
  select count(*) into v_offen from schule.wdh_runde_etappe r
   where r.lernender_id = p_l and r.tag = p_tag and r.bearbeitet_am is null and schule.wdh_aufgabe_da(r.einheit_id, r.lernziel);
  if v_offen = 0 then
    update schule.wdh_runde set fertig_am = now() where lernender_id = p_l and tag = p_tag and fertig_am is null;
  end if;
  return v_offen;
end $function$;

-- WD-3/5/6/2: Antwort auf eine Etappe (vor jeder Änderung an schule.karte_stand)
create or replace function schule.karte_wdh_ereignis()
 returns trigger language plpgsql set search_path to ''
as $function$
declare v_bestanden boolean; v_sterne int := 0; v_beginn text; v_abgelegt jsonb; v_erg jsonb; v_tag date;
begin
  -- Rückfall nach dem Ablegen: kommt eine abgelegte Etappe wieder in den Takt (Fehler beim Üben, falsche Mischkarte, Nachtest), dann mit Stufe 2 am nächsten Lerntag
  if old.sitzt and new.sitzt and old.wdh_ab is null and old.faellig_am is null and old.wdh_lerntage is null and new.wdh_ab is not null
     and exists (select 1 from schule.abgelegt g where g.lernender_id = new.lernender_id and g.bezug = 'etappe:' || new.einheit_id || ':' || new.lernziel) then
    new.wdh_stufe := 2; new.wdh_lerntage := 1; new.faellig_am := new.wdh_ab + interval '1 day';
  end if;
  if new.richtig <= old.richtig and new.falsch <= old.falsch then return new; end if;   -- keine Antwort
  -- WD-2: Antwort auf eine Etappe der heutigen Runde → bearbeitet (richtig oder falsch)
  v_tag := schule.heute_tag(new.lernender_id);
  update schule.wdh_runde_etappe set bearbeitet_am = now()
   where lernender_id = new.lernender_id and tag = v_tag and einheit_id = new.einheit_id and lernziel = new.lernziel and bearbeitet_am is null;
  if found then perform schule.wdh_runde_pruefen(new.lernender_id, v_tag); end if;
  if not old.sitzt or not schule.karte_faellig(old) then return new; end if;               -- keine Wiederholung
  v_bestanden := new.richtig > old.richtig and new.sitzt and new.wdh_fehler = 0 and new.wdh_ab is distinct from old.wdh_ab
                 and new.wdh_stufe = least(old.wdh_stufe + 1, 4);
  if v_bestanden then
    v_beginn := coalesce(extract(epoch from coalesce(old.wdh_ab, old.faellig_am))::bigint::text, 'x');
    insert into schule.sterne (lernender_id, menge, grund, bezug)
    values (new.lernender_id, schule.wd_regel('sterne_wdh_richtig', 10), 'wdh', 'wdh:' || new.einheit_id || ':' || new.lernziel || ':' || v_beginn)
    on conflict do nothing returning menge into v_sterne;
    perform set_config('schule.wdh_karte', new.einheit_id || '/' || new.lernziel, true);  -- sterne_aus_versuch: für diesen Versuch keine 'uebung'-Sterne
    if old.wdh_stufe >= 4 then                                                             -- fünfte Wiederholung (30 Lerntage) bestanden: abgelegt
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

-- WD-6 Rückfall im Nachtest/Test: Etappe einer Testsitzung auf „fehler“ → eine abgelegte Etappe kommt am nächsten Lerntag zurück (Stufe 2 setzt der Trigger oben)
create or replace function schule.lernziel_rueckfall()
 returns trigger language plpgsql set search_path to ''
as $function$
begin
  if new.status = 'fehler' and old.status is distinct from 'fehler'
     and exists (select 1 from schule.abgelegt g where g.lernender_id = new.lernender_id and g.bezug = 'etappe:' || new.einheit_id || ':' || new.lernziel) then
    update schule.karte_stand set wdh_ab = now(), wdh_lerntage = 1, faellig_am = now() + interval '1 day'
     where lernender_id = new.lernender_id and einheit_id = new.einheit_id and lernziel = new.lernziel
       and sitzt and wdh_ab is null and faellig_am is null and wdh_lerntage is null;
  end if;
  return new;
end $function$;
create or replace trigger lernziel_rueckfall after update of status on schule.lernziel_stand for each row execute function schule.lernziel_rueckfall();

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

-- Reihenfolge-Merkmal „Wiederholungs-Fehler“: Fehler in der Wiederholung oder falsche Mischkarte seit Beginn der Fälligkeit
create or replace function schule.wdh_fehler(k schule.karte_stand)
 returns boolean language sql stable set search_path to ''
as $function$
  select coalesce(k.wdh_fehler, 0) > 0
      or exists (select 1 from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                  where v.lernender_id = k.lernender_id and coalesce(v.misch, false) and not v.richtig and v.testsitzung_id is null
                    and a.einheit_id = k.einheit_id and a.variante_gruppe = k.lernziel and v.am >= coalesce(k.wdh_ab, k.sitzt_am, '-infinity'::timestamptz));
$function$;

-- WD-1/WD-2: Runde des Lerntags festhalten (einmal je Kind und Tag; ein zweites Gerät bekommt dieselbe)
create or replace function schule.wdh_runde_holen(p_l bigint, p_tag date)
 returns void language plpgsql set search_path to ''
as $function$
declare v_faellig int; v_da int; v_ziel int; v_alt int;
begin
  if exists (select 1 from schule.wdh_runde where lernender_id = p_l and tag = p_tag) then return; end if;
  if to_regclass('pg_temp.wd_kand') is null then
    create temp table wd_kand (einheit_id bigint, lernziel text, fehler boolean, faellig_am timestamptz, wdh_stufe int) on commit drop;
  end if;
  truncate wd_kand;  -- nur die Hilfstabelle dieser Sitzung
  insert into wd_kand select k.einheit_id, k.lernziel, schule.wdh_fehler(k), k.faellig_am, k.wdh_stufe
    from schule.karte_stand k where k.lernender_id = p_l and schule.karte_faellig(k);
  select count(*), count(*) filter (where schule.wdh_aufgabe_da(c.einheit_id, c.lernziel)) into v_faellig, v_da from wd_kand c;
  v_ziel := least(schule.wdh_runde_groesse(p_l, v_faellig), v_da);
  v_alt := ceil(v_ziel / 3.0)::int;                         -- mindestens ein Drittel für die am längsten fälligen
  insert into schule.wdh_runde (lernender_id, tag, ziel, faellig) values (p_l, p_tag, v_ziel, v_faellig) on conflict do nothing;
  if not found then return; end if;                         -- gleichzeitig von einem anderen Gerät angelegt
  insert into schule.wdh_runde_etappe (lernender_id, tag, nr, einheit_id, lernziel)
  with da as (select * from wd_kand c where schule.wdh_aufgabe_da(c.einheit_id, c.lernziel)),
  alt as (select d.* from da d order by d.faellig_am nulls first, d.wdh_stufe, d.einheit_id, d.lernziel limit v_alt),
  rest as (select d.* from da d where not exists (select 1 from alt x where x.einheit_id = d.einheit_id and x.lernziel = d.lernziel)
            order by d.fehler desc, d.faellig_am nulls first, d.wdh_stufe, d.einheit_id, d.lernziel limit greatest(v_ziel - v_alt, 0)),
  wahl as (select * from alt union all select * from rest)
  select p_l, p_tag, row_number() over (order by w.fehler desc, w.faellig_am nulls first, w.wdh_stufe, w.einheit_id, w.lernziel), w.einheit_id, w.lernziel from wahl w;
  perform schule.wdh_runde_pruefen(p_l, p_tag);             -- 0 fällige: sofort gemacht
end $function$;
revoke all on function schule.wdh_runde_holen(bigint, date) from public, anon, authenticated;

-- schule_wiederholung (bisherige Felder aufgaben, faellig bleiben; neu: runde, runde_bearbeitet, runde_offen, runde_gemacht, gestaffelt, aufgaben[].pflicht)
--   aufgaben: zuerst die noch offenen Etappen der Runde (pflicht = true, Reihenfolge der Runde), dann weitere fällige freiwillig (Fehler → am längsten fällig → Stufe).
--   anzahl: höchstens so viele Aufgaben (bisher höchstens 6, jetzt höchstens 60); ohne anzahl alle (≤ 60). p_tag nur für Rauchtests (sonst heute_tag).
create or replace function schule.wiederholung_intern(p_l bigint, p_daten jsonb, p_leiter boolean, p_tag date default null)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_l bigint := p_l; v_n int := least(coalesce(nullif(p_daten->>'anzahl', '')::int, 60), 60); v_tag date := coalesce(p_tag, schule.heute_tag(p_l));
  v_test boolean; v_erg jsonb; v_faellig int; v_r schule.wdh_runde; v_offen int;
begin
  select ist_test into v_test from schule.lernender where id = v_l;
  perform schule.wdh_runde_holen(v_l, v_tag);
  v_offen := schule.wdh_runde_pruefen(v_l, v_tag);
  select * into v_r from schule.wdh_runde where lernender_id = v_l and tag = v_tag;
  select count(*) into v_faellig from schule.karte_stand k where k.lernender_id = v_l and schule.karte_faellig(k);
  select coalesce(jsonb_agg(x.j || jsonb_build_object('pflicht', x.pflicht) order by x.rang, x.nr), '[]'::jsonb) into v_erg from (
    select q.* from (
      select case when r.nr is not null then 0 else 1 end rang,
             coalesce(r.nr, 1000 + row_number() over (order by schule.wdh_fehler(k) desc, k.faellig_am nulls first, k.wdh_stufe, k.einheit_id, k.lernziel)) nr,
             r.nr is not null pflicht,
             schule.aufgabe_anzeige(a, true) || jsonb_build_object('einheit_id', k.einheit_id, 'stadt', b.stadt, 'lernziel', k.lernziel, 'wdh_stufe', k.wdh_stufe,
               'etappe', (select et->>'titel' from jsonb_array_elements(e.inhalt->'etappen') et where et->>'lernziel' = k.lernziel limit 1)) j
        from schule.karte_stand k join schule.einheit e on e.id = k.einheit_id join schule.block b on b.id = e.block_id
        left join schule.wdh_runde_etappe r on r.lernender_id = k.lernender_id and r.tag = v_tag and r.einheit_id = k.einheit_id and r.lernziel = k.lernziel
        cross join lateral (select a.* from schule.aufgabe a where a.einheit_id = k.einheit_id and a.pool = 'uebung' and a.variante_gruppe = k.lernziel
                              and (a.freigegeben)
                            order by (coalesce(a.stufe, 2) = 1), (select count(*) from schule.versuch vs where vs.lernender_id = v_l and vs.aufgabe_id = a.id), random() limit 1) a
       where k.lernender_id = v_l
         and ((r.nr is not null and r.bearbeitet_am is null) or (r.nr is null and schule.karte_faellig(k)))
         and (e.status in ('geprueft','freigegeben') or (e.status = 'entwurf' and coalesce(v_test, false) and p_leiter))) q
     order by q.rang, q.nr limit v_n) x;
  return jsonb_build_object('ok', true, 'aufgaben', v_erg, 'faellig', v_faellig, 'runde', coalesce(v_r.ziel, 0),
    'runde_offen', v_offen, 'runde_bearbeitet', greatest(coalesce(v_r.ziel, 0) - v_offen, 0), 'runde_gemacht', v_r.fertig_am is not null,
    'gestaffelt', (select count(*) from schule.karte_stand k where k.lernender_id = v_l and k.sitzt and k.wdh_gesetzt_am is not null and k.wdh_stufe = 0
                     and k.wdh_fehler = 0 and k.wdh_lerntage > 1 and not schule.karte_faellig(k)));
end $function$;
revoke all on function schule.wiederholung_intern(bigint, jsonb, boolean, date) from public, anon, authenticated;

create or replace function api.schule_wiederholung(p_schluessel text, p_daten jsonb)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_l bigint := (p_daten->>'lernender_id')::bigint;
begin
  perform schule.zugriff(p_schluessel, v_l);
  return schule.wiederholung_intern(v_l, p_daten, schule.ist_leiter(p_schluessel)); -- WD-S
end $function$;

-- WD-2: bestätigen (setzt nichts selbst – „gemacht“ setzt der Server, sobald alle Etappen der Runde bearbeitet sind); fehlen Aufgaben: Ablehnung
create or replace function schule.wdh_runde_fertig(p_l bigint, p_tag date default null)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_tag date := coalesce(p_tag, schule.heute_tag(p_l)); v_offen int; v_r schule.wdh_runde;
begin
  perform schule.wdh_runde_holen(p_l, v_tag);
  v_offen := schule.wdh_runde_pruefen(p_l, v_tag);
  select * into v_r from schule.wdh_runde where lernender_id = p_l and tag = v_tag;
  if v_r.fertig_am is null then
    raise exception 'Die Wiederholungs-Runde ist noch nicht fertig: % von % bearbeitet', greatest(v_r.ziel - v_offen, 0), v_r.ziel using errcode = 'P0001';
  end if;
  return jsonb_build_object('ok', true, 'runde_gemacht', true, 'tag', v_tag, 'runde', v_r.ziel);
end $function$;
revoke all on function schule.wdh_runde_fertig(bigint, date) from public, anon, authenticated;

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
