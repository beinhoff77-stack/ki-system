-- TL-S (22.11.): Teilung von 7 Themen in 15 Teile (8 neue Flüge; Stand LK-D 3, Entscheidungen 22.11., 17:05) (inhalte/AUFTRAEGE.md „Entscheidung Teilung (22.11., 16:20 Berlin)“, Abschnitt „An bau-lehrer – TL-S“).
-- Daten: inhalte/pruefung/lehrplan/lk_teilung_2211.json (Teile, Untertitel, Etappen, Klassen, „ohne eigenen Punkt“ = Zusatz, Kanten), Bericht lk_teilung_2211.md.
-- Einspielen NACH LK-S (20261123_lk_s_thema_je_klasse.sql: zuordnung.etappen, Sichten) und erst, wenn das Gym-Audit (LK-D 3) vorliegt – in EINER Transaktion.
-- Was passiert je geteiltem Thema (Funktion schule.tl_teilen):
--   * Teil 1 bleibt das bisherige Thema (gleiche Id, gleiche Einheit, gleicher Ort); Teil 2 … n werden neue Themen mit eigener Einheit und eigenem
--     vorläufigem Ort (Kopie des bisherigen Orts, direkt dahinter im selben Kontinent; die folgenden Orte rücken in der Reihenfolge nach) bis zum Reise-Aufbau.
--   * Titel „‹Titel› – Teil k von n“, neue Spalten thema.untertitel, teil_nr, teil_von, teil_stamm, zusatz (Schularten, in denen der Teil Zusatz ist).
--   * Etappen: Katalog der bisherigen Einheit wird auf Teil 1 verkleinert, die neuen Einheiten bekommen ihre Etappen (Inhalt kopiert, Etappen-Listen gefiltert).
--     Etappen aus der Liste, die es in der Datenbank noch nicht gibt (z. B. neue Etappen aus LK-D), werden übersprungen und gemeldet.
--     Freigegebene Einheiten/Aufgaben sind gegen Änderung geschützt (einheit_schutz/aufgabe_schutz): die Einheit wird dafür in dieser Transaktion kurz auf
--     'geprueft' gesetzt und danach wieder freigegeben – bewusst, nur für diesen Schritt.
--   * Aufgaben (alle Pools außer Expedition) ziehen mit ihrer Etappe um – gleiche Aufgaben-Ids, also bleiben Antworten, Sterne „aufgabe:…“ und
--     „gezählt“ gültig. Aufgaben ohne Etappe im Katalog und Expeditions-Aufgaben bleiben bei Teil 1 (gemeldet).
--   * Lernstand je Etappe (Karten, Lernziel-Stand, besprochen, Was wackelt, Wiederholungs-Runden, Staffel-Sicherung, abgelegt, Rückmeldungen, Lage offener
--     Misch-Ausgaben), Kann-Texte, Sterne-Bezüge landung:/wdh: ziehen mit. Abgeschlossene Tests und Flug-Abschlüsse bleiben bei Teil 1.
--   * B3b (ChatGPT 939/940): Alte Antworten (versuch → aufgabe → einheit) erscheinen beim richtigen Teil, weil die Aufgabe mit gleicher Id in die Einheit des
--     Teils zieht – ohne Lesepfad-Umbau gilt das für Was wackelt, Lernstand, Lehrer-Ansicht und Wertung. Regression: supabase/tests/tl_s_rauchtest.sql (3).
--   * Plan: Wer den bisherigen Ort im Plan hat, bekommt die neuen Orte direkt dahinter (Status wie bisher, „laeuft“ → „offen“; Zusatz-Teil der eigenen
--     Schulart als Art 'zusatz'). Stufen-Einträge und Themen-Listen des Plans werden auf die Teile übertragen („Kann er“ gilt für das ganze Thema).
--   * Ist ein neuer Teil nach dem Umhängen für ein Kind vollständig (alle Etappen gelandet, gesetzt oder nachgewiesen): Flug-Abschluss (Stempel) und Ort
--     „fertig“ → 100 Sterne über den bestehenden Trigger route_sterne (Entscheidung Punkt 4). Etappen- und Landungs-Sterne wandern mit, nichts wird gekürzt.
--     Ein abgeschlossener Flug-Test der alten Einheit wird für den Teil als abgeschlossene Test-Sitzung mitgeführt (sonst zeigt thema_stufe „Test offen“;
--     das Einfügen bucht keine Sterne – testsitzung_sterne läuft nur bei UPDATE).
--   * Lehrplan-Zuordnungen: Punkt → Teil nach zuordnung.etappen; ein Punkt über mehrere Teile wird je Teil mit seinen Etappen geführt (Hauptbezug je Teil).
-- Danach: Voraussetzungen nach `kanten` (bisherige Kanten auf den richtigen Teil, Teil k braucht Teil k−1), Zusatz-Regel je Schulart (neue Tabelle
-- schule.voraussetzung_schulart: eine Kante, deren Voraussetzung in der Schulart Zusatz ist, ist dort nur „empfohlen“; dafür braucht der Folgeteil dort hart
-- den Teil davor – 46 Teil 3 braucht im Gymnasium hart nur Teil 1), Visum (v_ort_visum) und Reiseoptionen je Schulart, Schnittstelle (teil, Untertitel, Zusatz).
-- Vorher/Nachher je Kind (B4) je Thema (Abbruch bei Unterschied) und über alles: Stufen aller nicht geteilten Themen, Lernstand und Sterne außerhalb der Teilung,
-- Plan-Reihenfolge der bisherigen Orte, ganze Karten- und Lernziel-Zeilen (alle wdh_*-Felder, misch_ok_am), offene Mischkarten, thema_stufe,
-- Reiseoptionen und Visum. Erlaubte Deltas (sonst Abbruch): im Plan/gesetzt/Rückreise je Teil wie vorher (Zusatz-Teil der eigenen Schulart: als „zusatz“
-- im Plan); Etappen/begonnen/gelandet/sicher/wieder offen summieren sich über die Teile zum alten Wert; Stufe je Teil ergibt sich neu; Reiseoptionen und
-- Visum gleich, wenn neue Orte auf den Ort von Teil 1 abgebildet werden.
-- TL-S 2 (Probelauf 17:25, ChatGPT 942/943): je Lehrplan-Punkt genau EIN Hauptbezug (zuordnung_eintrag_id_idx) – über mehrere Teile: Haupt beim Teil mit den
-- meisten Etappen des Punkts, die übrigen Teile Nebenbezug mit rolle/etappen; thema_lage_klasse zählt diese Nebenbezüge von Geschwister-Teilen mit.
-- B2: eine Regel Pflicht/Kür je Kind (schule.pflicht_lernziele: Gruppe → Schulart → lernziele_pflicht); B3: Schulartwechsel gleicht lernziel_stand.pflicht ab
-- (Trigger, nichts gelöscht). Daten: supabase/werkzeug/tl_s_daten.py (aus lk_teilung_2211.json, auch art_je_schulart der Kanten).
-- Kür je Etappe und Schulart (17:05): bewertung.pflicht_je_schulart, schule.pflicht_lernziele(kind, einheit), lernziele_anlegen je Kind, wdh_ablegen und
-- konto_wd auf die Liste des Kindes; die Daten (etappen[].kuer_in) liefert LK-D 4 – ohne sie gilt die bisherige Pflichtliste für alle.
-- Teile ohne Etappe in der Datenbank (101 Teil 2: cavalieri) werden als leere Hülle angelegt (Entwurf, nicht im Plan); Zuordnungen folgen der vollen Liste.
-- LW-Rest: schule.besprochen_aktiv (LA-3) mit der endgültigen Fehler-Semantik von LW-S 2 (schule.fehler_endgueltig_am) – Voraussetzung LW-S 2.
-- Kein DROP, kein DELETE. Wiederholt ausführbar (geteilte Themen werden übersprungen). Erweiterung (LK-D 3: 2, 57, 101): weitere Einträge in den Daten
-- (Block v_daten) ergänzen – das Verfahren ist allgemein.

do $$ begin   -- Schritt 0: Reihenfolge
  if not exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'zuordnung' and column_name = 'etappen') then
    raise exception 'TL-S: zuerst LK-S (20261123_lk_s_thema_je_klasse.sql) einspielen'; end if;
  if to_regprocedure('schule.fehler_endgueltig_am(schule.versuch)') is null then
    raise exception 'TL-S: zuerst LW-S/LW-S 2 (20261123_lw_s_wackelt_status.sql) einspielen'; end if;
end $$;

-- LW-Rest (ChatGPT 939/940): besprochen_aktiv (LA-3) mit derselben endgültigen Fehler-Semantik wie LW-S 2.
-- Eine Besprochen-Markierung gilt nicht mehr, sobald danach eine Antwort der Etappe endgültig falsch wurde
-- (falsche Testantwort sofort; Übung nach der Wertung: 2. Anlauf sofort, 1. Anlauf nach 30 Minuten oder beim Weitergehen; neutral/ersetzt/offen zählt nicht).
create or replace function schule.besprochen_aktiv(p_l bigint, p_e bigint, p_lz text)
 returns schule.besprochen language sql stable set search_path to ''
as $function$
  select b.* from schule.besprochen b
   where b.lernender_id = p_l and b.einheit_id = p_e and b.lernziel = p_lz
     and not exists (select 1 from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                      where v.lernender_id = p_l and a.einheit_id = p_e and a.variante_gruppe = p_lz and not v.richtig
                        and schule.fehler_endgueltig_am(v) > b.am);
$function$;

create temp table if not exists tl_vorher (t text, s text) on commit drop;
truncate tl_vorher; -- nur die Hilfstabelle dieser Sitzung
-- Stand außerhalb der Teilung (muss gleich bleiben): Stufen der nicht geteilten Themen, Karten/Lernziel-Stand anderer Einheiten, Sterne ohne neue Ort-Sterne
create or replace function pg_temp.tl_stand() returns table (t text, s text) language plpgsql as $f$
declare v_geteilt bigint[] := array[26, 29, 44, 46, 61, 91, 101];
  v_e bigint[] := array(select e.id from schule.einheit e where e.thema_id in (select x.id from schule.thema x where x.id = any(v_geteilt) or x.teil_stamm = any(v_geteilt)));
begin
  t := 'stufen_andere'; select md5(coalesce(string_agg(l.id || ':' || th.id || ':' || coalesce(schule.thema_stufe(l.id, th.id)::text, ''), '|' order by l.id, th.id), ''))
    into s from schule.lernender l cross join schule.thema th where th.id <> all(v_geteilt) and coalesce(th.teil_stamm, 0) <> all(v_geteilt); return next;
  t := 'karten_andere'; select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) into s from schule.karte_stand x where x.einheit_id <> all(v_e); return next;
  t := 'lernziel_andere'; select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) into s from schule.lernziel_stand x where x.einheit_id <> all(v_e); return next;
  t := 'sterne'; select md5(coalesce(string_agg(x.lernender_id || ':' || x.menge || ':' || x.grund || ':' || x.bezug, '|' order by x.lernender_id, x.grund, x.bezug), '')) into s
    from schule.sterne x where not (x.grund = 'ort' and x.bezug in (select 'block:' || b.id from schule.block b where b.schluessel ~ '-teil[0-9]+$'))
                           and not (x.bezug ~ ('^(landung|wdh):(' || coalesce(array_to_string(v_e, '|'), '0') || '):')); return next;
  -- erlaubtes Delta: Art „zusatz“, die TL-S für einen Teil 1 gesetzt hat (Teil 1 in der Schulart des Kindes Zusatz), zählt wie „normal“
  t := 'plan_reihenfolge'; select md5(coalesce(string_agg(r.lernender_id || ':' || r.block_id || ':' || r.status || ':'
         || case when r.art = 'zusatz' and r.geaendert_von = 'TL-S' then 'normal' else r.art end, '|' order by r.lernender_id, r.position), '')) into s
    from schule.route r join schule.block b on b.id = r.block_id where b.schluessel !~ '-teil[0-9]+$'; return next;
end $f$;

-- 1. Felder
alter table schule.thema add column if not exists untertitel text;
alter table schule.thema add column if not exists teil_nr smallint;
alter table schule.thema add column if not exists teil_von smallint;
alter table schule.thema add column if not exists teil_stamm bigint;
alter table schule.thema add column if not exists zusatz text[];
comment on column schule.thema.untertitel is 'TL-S: Untertitel eines Teils („Teil 2 von 2 · ‹Untertitel›“)';
comment on column schule.thema.teil_nr is 'TL-S: Nummer des Teils eines geteilten Themas (1 = bisheriges Thema)';
comment on column schule.thema.teil_von is 'TL-S: Anzahl der Teile';
comment on column schule.thema.teil_stamm is 'TL-S: Id des Ausgangsthemas (Teil 1)';
comment on column schule.thema.zusatz is 'TL-S: Schularten, in denen dieser Teil Zusatz ist (kein eigener Lehrplanpunkt; sperrt dort nichts)';
create table if not exists schule.voraussetzung_schulart (
  thema_id bigint not null references schule.thema(id),
  braucht_id bigint not null references schule.thema(id),
  schulart text not null,
  art text not null,
  begruendung text,
  primary key (thema_id, braucht_id, schulart),
  constraint voraussetzung_schulart_art_check check (art in ('hart', 'empfohlen')),
  constraint voraussetzung_schulart_schulart_check check (schulart in ('gym_by', 'rs_by', 'ib_myp'))
);
alter table schule.voraussetzung_schulart enable row level security;
comment on table schule.voraussetzung_schulart is 'TL-S: abweichende Art einer Voraussetzung je Schulart (Zusatz-Regel); ohne Eintrag gilt schule.voraussetzung.art';

create temp table if not exists tl_visum_vorher (ort_id bigint, braucht_ort_id bigint) on commit drop;
truncate tl_visum_vorher;
insert into tl_visum_vorher select distinct v.ort_id, v.braucht_ort_id from schule.v_ort_visum v;

-- Hilfen
-- ---------- Kür je Etappe und Schulart (Entscheidung 22.11., 17:05) ----------
-- Heute: Pflicht/Kür je Etappe für alle Kinder gleich (bewertung.lernziele_pflicht / lernziele_vertiefung), je Kind festgehalten in lernziel_stand.pflicht
-- (lernziele_anlegen). Neu (B2): bewertung.pflicht_je_schulart {"gym_by": [...], "rs_I": [...], "rs_II_III": [...], "rs_by": [...], "myp_standard": [...], "ib_myp": [...]}
-- – Liste der Gruppe des Kindes, sonst der Schulart, sonst lernziele_pflicht; alle übrigen Etappen der Einheit sind für dieses Kind Kür.
-- Alle Leser von lernziel_stand.pflicht (Flug-Test-Wertung, Korrektur, Flug-Abschluss/Stempel, 100 Ort-Sterne, Nachtests, Ort-/Thema-Stand) folgen damit der Regel.
-- Pflicht-Etappen einer Einheit für ein Kind (ohne Rückfall auf „alle Etappen“; den machen die Aufrufer wie bisher selbst)
create or replace function schule.pflicht_schluessel(p_l bigint)
 returns text[] language sql stable set search_path to ''
as $function$
  -- Reihenfolge: Gruppe (rs_I, rs_II_III, myp_standard …; kind_zweig aus LK-S), dann Schulart (gym_by, rs_by, ib_myp)
  select array[schule.kind_zweig(coalesce(l.schulart, 'gym_by'), l.zweig), coalesce(l.schulart, 'gym_by')] from schule.lernender l where l.id = p_l;
$function$;
create or replace function schule.pflicht_lernziele(p_l bigint, p_e bigint)
 returns text[] language sql stable set search_path to ''
as $function$
  select coalesce(array(select jsonb_array_elements_text(coalesce(
           (select e.inhalt#>array['bewertung', 'pflicht_je_schulart', k] from unnest(schule.pflicht_schluessel(p_l)) with ordinality u(k, o)
             where jsonb_typeof(e.inhalt#>array['bewertung', 'pflicht_je_schulart', k]) = 'array' order by o limit 1),
           e.inhalt#>'{bewertung,lernziele_pflicht}', '[]'::jsonb))), '{}')
    from schule.einheit e where e.id = p_e;
$function$;
comment on function schule.pflicht_lernziele(bigint, bigint) is 'TL-S (B2): die eine Regel Pflicht/Kür je Kind – pflicht_je_schulart der Gruppe, sonst der Schulart des Kindes, sonst lernziele_pflicht; alle übrigen Etappen sind Kür';
revoke all on function schule.pflicht_lernziele(bigint, bigint), schule.pflicht_schluessel(bigint) from public, anon, authenticated;

-- lernziele_anlegen: Pflicht je Kind. Bestehende Zeilen werden nur angepasst, wenn die Einheit eine Liste für die Schulart des Kindes hat
-- (ohne Liste: Verhalten wie bisher, „on conflict do nothing“). Eine Kür-Etappe zählt damit nicht für Flug-Test-Wertung, Flug-Abschluss, Nachtest, Ort/Stempel.
create or replace function schule.lernziele_anlegen(p_lernender bigint, p_einheit bigint)
 returns void language plpgsql set search_path to ''
as $function$
declare v_in jsonb; v_pf text[]; v_je_sa boolean;
begin
  select e.inhalt into v_in from schule.einheit e where e.id = p_einheit;
  if v_in is null then return; end if;
  v_pf := schule.pflicht_lernziele(p_lernender, p_einheit);
  -- Abgleich bestehender Zeilen nur bei Einheiten mit Listen je Schulart/Gruppe (ohne: Verhalten wie bisher); so auch beim Rückwechsel der Schulart
  v_je_sa := jsonb_typeof(v_in#>'{bewertung,pflicht_je_schulart}') = 'object' and v_in#>'{bewertung,pflicht_je_schulart}' <> '{}'::jsonb;
  insert into schule.lernziel_stand (lernender_id, einheit_id, lernziel, pflicht)
  select p_lernender, p_einheit, q.lz, q.lz = any(v_pf)
    from (select distinct lz from (select unnest(v_pf) lz
                                   union all select jsonb_array_elements_text(coalesce(v_in#>'{bewertung,lernziele_pflicht}', '[]'::jsonb))
                                   union all select jsonb_array_elements_text(coalesce(v_in#>'{bewertung,lernziele_vertiefung}', '[]'::jsonb))) x) q
  on conflict (lernender_id, einheit_id, lernziel) do update set pflicht = excluded.pflicht
   where v_je_sa and schule.lernziel_stand.pflicht is distinct from excluded.pflicht;
end $function$;

-- alle Kinder einer Einheit nachziehen (nach Änderung von pflicht_je_schulart; nur Kinder mit Lernstand in der Einheit)
create or replace function schule.pflicht_abgleichen(p_e bigint)
 returns int language plpgsql set search_path to ''
as $function$
declare r record; n int := 0;
begin
  for r in select distinct s.lernender_id from schule.lernziel_stand s where s.einheit_id = p_e loop
    perform schule.lernziele_anlegen(r.lernender_id, p_e); n := n + 1;
  end loop;
  return n;
end $function$;
revoke all on function schule.lernziele_anlegen(bigint, bigint), schule.pflicht_abgleichen(bigint) from public, anon, authenticated;

-- B3 Schulartwechsel: Pflicht/Kür der Einheiten mit Listen je Schulart neu setzen. Nichts wird gelöscht (Karten, Sterne, Erstabschlüsse, Stempel bleiben);
-- eine neue Pflicht-Etappe steht als „offen“ da und öffnet den Flug wieder (Nachtragstest W177/I-5), ein Rückwechsel macht sie wieder zur Kür.
create or replace function schule.lernender_pflicht_abgleich()
 returns trigger language plpgsql set search_path to ''
as $function$
declare r record;
begin
  if new.schulart is distinct from old.schulart or new.zweig is distinct from old.zweig then
    for r in select distinct s.einheit_id from schule.lernziel_stand s join schule.einheit e on e.id = s.einheit_id
              where s.lernender_id = new.id and jsonb_typeof(e.inhalt#>'{bewertung,pflicht_je_schulart}') = 'object' loop
      perform schule.lernziele_anlegen(new.id, r.einheit_id);
    end loop;
  end if;
  return new;
end $function$;
revoke all on function schule.lernender_pflicht_abgleich() from public, anon, authenticated;
do $$ begin
  if not exists (select 1 from pg_trigger where tgname = 'lernender_pflicht_abgleich' and tgrelid = 'schule.lernender'::regclass) then
    create trigger lernender_pflicht_abgleich after update of schulart, zweig on schule.lernender for each row execute function schule.lernender_pflicht_abgleich();
  end if;
end $$;

-- thema_stufe (B2): ein Teil ohne Pflicht-Etappe für das Kind hat keinen Zwangstest; Fehler in Kür-Etappen machen den Flug nicht „dran“
do $$
declare d text; a1 text := $a$or exists (select 1 from schule.lernziel_stand s where s.lernender_id = p_l and s.einheit_id = v_e and s.status = 'fehler')$a$;
  n1 text := $a$or exists (select 1 from schule.lernziel_stand s where s.lernender_id = p_l and s.einheit_id = v_e and s.pflicht /* TL-S: nur Pflicht */ and s.status = 'fehler')$a$;
  a2 text := $a$or (v_n > 0 and v_gel = v_n and (not exists$a$;
  n2 text := $a$or (v_n > 0 and v_gel = v_n and cardinality(schule.pflicht_lernziele(p_l, v_e)) > 0 /* TL-S: ohne Pflicht kein Zwangstest */ and (not exists$a$;
begin
  d := pg_get_functiondef('schule.thema_stufe(bigint, bigint)'::regprocedure);
  if position('TL-S: nur Pflicht' in d) > 0 then raise notice 'thema_stufe schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a1, ''))) / length(a1) <> 1 or (length(d) - length(replace(d, a2, ''))) / length(a2) <> 1 then
    raise exception 'TL-S: Anker in thema_stufe nicht eindeutig'; end if;
  execute replace(replace(d, a1, n1), a2, n2);
end $$;

-- Leser der Pflichtliste ohne lernziel_stand: wdh_ablegen („Flug abgelegt“) und konto_wd (Etappen je Flug) – auf die Liste des Kindes umstellen
do $$
declare d text; a text; n text;
begin
  d := pg_get_functiondef('schule.wdh_ablegen(bigint, bigint, text)'::regprocedure);
  a := $a$coalesce(nullif(array(select jsonb_array_elements_text(coalesce(v_ein.inhalt->'bewertung'->'lernziele_pflicht', '[]'::jsonb))), '{}'),$a$;
  n := $a$coalesce(nullif(schule.pflicht_lernziele(p_l, p_e), '{}') /* TL-S: Pflicht je Schulart */,$a$;
  if position(n in d) > 0 then raise notice 'wdh_ablegen schon umgestellt';
  elsif (length(d) - length(replace(d, a, ''))) / length(a) = 1 then execute replace(d, a, n);
  else raise exception 'TL-S: Anker in wdh_ablegen nicht eindeutig'; end if;
  d := pg_get_functiondef('schule.konto_wd(bigint)'::regprocedure);
  a := $a$coalesce(nullif(array(select jsonb_array_elements_text(coalesce(e.inhalt->'bewertung'->'lernziele_pflicht', '[]'::jsonb))), '{}'),$a$;
  n := $a$coalesce(nullif(schule.pflicht_lernziele(p_l, e.id), '{}') /* TL-S: Pflicht je Schulart */,$a$;
  if position(n in d) > 0 then raise notice 'konto_wd schon umgestellt';
  elsif (length(d) - length(replace(d, a, ''))) / length(a) = 1 then execute replace(d, a, n);
  else raise exception 'TL-S: Anker in konto_wd nicht eindeutig'; end if;
end $$;

-- Stand vorher – nach den gewollten Regel-Änderungen (Kür zählt nicht, B2), vor der Teilung
insert into tl_vorher select * from pg_temp.tl_stand();

create or replace function schule.tl_inhalt(p_inhalt jsonb, p_behalten text[])
 returns jsonb language sql immutable set search_path to ''
as $function$
  select p_inhalt
    || jsonb_build_object('etappen', coalesce((select jsonb_agg(q order by o) from jsonb_array_elements(coalesce(p_inhalt->'etappen', '[]'::jsonb)) with ordinality x(q, o)
                                               where (q->>'lernziel') = any(p_behalten)), '[]'::jsonb))
    || case when jsonb_typeof(p_inhalt->'bewertung') = 'object' then jsonb_build_object('bewertung', (p_inhalt->'bewertung')
         || case when jsonb_typeof(p_inhalt#>'{bewertung,lernziele_pflicht}') = 'array' then jsonb_build_object('lernziele_pflicht',
              coalesce((select jsonb_agg(q) from jsonb_array_elements_text(p_inhalt#>'{bewertung,lernziele_pflicht}') q where q = any(p_behalten)), '[]'::jsonb)) else '{}'::jsonb end
         || case when jsonb_typeof(p_inhalt#>'{bewertung,lernziele_vertiefung}') = 'array' then jsonb_build_object('lernziele_vertiefung',
              coalesce((select jsonb_agg(q) from jsonb_array_elements_text(p_inhalt#>'{bewertung,lernziele_vertiefung}') q where q = any(p_behalten)), '[]'::jsonb)) else '{}'::jsonb end
         || case when jsonb_typeof(p_inhalt#>'{bewertung,pflicht_je_schulart}') = 'object' then jsonb_build_object('pflicht_je_schulart',
              (select coalesce(jsonb_object_agg(k, coalesce((select jsonb_agg(q) from jsonb_array_elements_text(v) q where q = any(p_behalten)), '[]'::jsonb)), '{}'::jsonb)
                 from jsonb_each(p_inhalt#>'{bewertung,pflicht_je_schulart}') x(k, v))) else '{}'::jsonb end
         || case when jsonb_typeof(p_inhalt#>'{bewertung,testaufgaben_je_lernziel}') = 'object' then jsonb_build_object('testaufgaben_je_lernziel',
              coalesce((select jsonb_object_agg(k, v) from jsonb_each(p_inhalt#>'{bewertung,testaufgaben_je_lernziel}') x(k, v) where k = any(p_behalten)), '{}'::jsonb)) else '{}'::jsonb end)
       else '{}'::jsonb end;
$function$;

-- erledigt: gelandet, gesetzt oder nachgewiesen
create or replace function schule.tl_erledigt(p_l bigint, p_e bigint, p_lz text)
 returns boolean language sql stable set search_path to ''
as $function$
  select exists (select 1 from schule.karte_stand k where k.lernender_id = p_l and k.einheit_id = p_e and k.lernziel = p_lz and (k.sitzt or k.gesetzt_am is not null))
      or exists (select 1 from schule.lernziel_stand s where s.lernender_id = p_l and s.einheit_id = p_e and s.lernziel = p_lz and s.status in ('nachgewiesen', 'korrigiert', 'gesichert'));
$function$;

-- Ort eines Teils auf den Ort von Teil 1 abbilden (für die erlaubten Delta-Regeln bei Reiseoptionen und Visum)
create or replace function schule.tl_ort_stamm(p_block bigint)
 returns bigint language sql stable set search_path to ''
as $function$
  select coalesce((select coalesce(e.block_id, (select bt2.block_id from schule.block_thema bt2 where bt2.thema_id = t.teil_stamm order by bt2.reihenfolge limit 1))
                     from schule.block_thema bt join schule.thema t on t.id = bt.thema_id and t.teil_nr > 1
                     left join schule.einheit e on e.id = schule.thema_einheit(t.teil_stamm)
                    where bt.block_id = p_block limit 1), p_block);
$function$;
create or replace function schule.tl_reise_ohne(p jsonb, p_kontinent text)
 returns jsonb language sql immutable set search_path to ''
as $function$
  select coalesce(p, '{}'::jsonb) - 'optionen' || jsonb_build_object('optionen', coalesce((select jsonb_agg(o order by ord)
           from jsonb_array_elements(coalesce(p->'optionen', '[]'::jsonb)) with ordinality x(o, ord) where o->>'kontinent' is distinct from p_kontinent), '[]'::jsonb));
$function$;
-- Reiseoptionen: Optionen für neue Orte weglassen, fehlende Visa auf den Ort von Teil 1 abbilden (Titel), doppelte zusammenfassen
create or replace function schule.tl_reise_abgebildet(p jsonb)
 returns jsonb language sql stable set search_path to ''
as $function$
  select coalesce(p, '{}'::jsonb) - 'optionen' || jsonb_build_object('optionen', coalesce((
    select jsonb_agg(o - 'visum_fehlt' || jsonb_build_object('visum_fehlt', coalesce((
             select jsonb_agg(distinct jsonb_build_object('ort', coalesce((select b1.titel from schule.block b0 join schule.block b1 on b1.id = schule.tl_ort_stamm(b0.id)
                                                                             where b0.titel = f->>'ort' limit 1), f->>'ort'), 'kontinent', f->'kontinent'))
               from jsonb_array_elements(coalesce(o->'visum_fehlt', '[]'::jsonb)) f), '[]'::jsonb)) order by ord)
      from jsonb_array_elements(coalesce(p->'optionen', '[]'::jsonb)) with ordinality x(o, ord)
     where schule.tl_ort_stamm((o->>'ort_id')::bigint) = (o->>'ort_id')::bigint), '[]'::jsonb));
$function$;

-- Stand je Kind für eine Teilung (B4): fest = muss gleich bleiben; neu = was die Teilung hinzufügt (Bericht)
create or replace function schule.tl_kind_stand(p_einheiten bigint[], p_bloecke_neu bigint[], p_themen bigint[])
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare v jsonb; v_ids text := array_to_string(p_einheiten, '|'); v_re text := '^(landung|wdh):(' || array_to_string(p_einheiten, '|') || '):';
begin
  select coalesce(jsonb_object_agg(l.id, jsonb_build_object(
    'fest', jsonb_build_object(
      -- B4: ganze Zeilen (alle Wiederholungs- und Misch-Felder: wdh_stufe, wdh_fehler, wdh_ab, wdh_lerntage, wdh_gesetzt_am, faellig_am, misch_ok_am, gezaehlt …)
      'etappen', (select coalesce(jsonb_object_agg(k.lernziel, to_jsonb(k) - 'einheit_id' - 'lernender_id'), '{}'::jsonb)
                    from schule.karte_stand k where k.lernender_id = l.id and k.einheit_id = any(p_einheiten)),
      'lernziel_stand', (select coalesce(jsonb_object_agg(s.lernziel, to_jsonb(s) - 'einheit_id' - 'lernender_id'), '{}'::jsonb)
                           from schule.lernziel_stand s where s.lernender_id = l.id and s.einheit_id = any(p_einheiten)),
      'misch_offen', (select coalesce(jsonb_agg(m.aufgabe_id order by m.aufgabe_id), '[]'::jsonb) from schule.misch_ausgabe m
                        where m.lernender_id = l.id and m.eingeloest_am is null and m.verfallen_am is null),
      'sterne', (select coalesce(jsonb_agg(jsonb_build_array(s.grund, s.menge, regexp_replace(s.bezug, v_re, '\1:E:')) order by s.grund, regexp_replace(s.bezug, v_re, '\1:E:'), s.menge), '[]'::jsonb)
                   from schule.sterne s where s.lernender_id = l.id and not (s.grund = 'ort' and s.bezug = any(array(select 'block:' || b from unnest(p_bloecke_neu) b)))),
      'flug_abschluesse', (select coalesce(jsonb_agg(jsonb_build_array(f.einheit_id, f.sitzung_id, f.am) order by f.einheit_id), '[]'::jsonb)
                             from schule.flug_erstabschluss f where f.lernender_id = l.id and f.einheit_id = p_einheiten[1]),
      'abgelegt', (select coalesce(jsonb_agg(jsonb_build_array(a.art, regexp_replace(a.bezug, '^etappe:(' || v_ids || '):', 'etappe:E:'), a.sterne) order by a.art, a.bezug), '[]'::jsonb)
                     from schule.abgelegt a where a.lernender_id = l.id),
      'tests', (select coalesce(jsonb_agg(t.id order by t.id), '[]'::jsonb) from schule.testsitzung t where t.lernender_id = l.id and t.einheit_id = p_einheiten[1])),
    'neu', jsonb_build_object(
      'ort_sterne', (select coalesce(sum(s.menge), 0) from schule.sterne s where s.lernender_id = l.id and s.grund = 'ort' and s.bezug = any(array(select 'block:' || b from unnest(p_bloecke_neu) b))),
      'flug_abschluesse', (select count(*) from schule.flug_erstabschluss f where f.lernender_id = l.id and f.einheit_id = any(p_einheiten[2:])),
      'plan', (select coalesce(jsonb_agg(jsonb_build_array(r.block_id, r.status, r.art) order by r.position), '[]'::jsonb) from schule.route r where r.lernender_id = l.id and r.block_id = any(p_bloecke_neu)),
      'stufen', (select coalesce(jsonb_object_agg(t, schule.thema_stufe(l.id, t) - array['hinweis']), '{}'::jsonb) from unnest(p_themen) t),
      'reise', schule.tl_reise_abgebildet(schule.reiseoptionen(l.id))))), '{}'::jsonb)
    into v from schule.lernender l;
  return v;
end $function$;

-- 2. Teilen eines Themas aus seiner bisherigen Einheit (Teil-Verfahren für freigegebene Flüge)
-- p: {thema, titel, teile: [{teil, untertitel, etappen[], klasse: {gym_by, rs_by, ib_myp}, zusatz[]}]}
create or replace function schule.tl_teilen(p jsonb)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_alt bigint := (p->>'thema')::bigint; t schule.thema; v_e schule.einheit; b schule.block; v_n int := jsonb_array_length(p->'teile');
  v_kat text[]; v_alle text[] := '{}'; v_et text[]; v_fehlt text[] := '{}'; v_tp jsonb; v_k int; v_th bigint; v_ne bigint; v_nb bigint;
  v_ids bigint[]; v_einh bigint[]; v_bl bigint[] := '{}'; v_teil_et jsonb := '{}'; v_tab text; v_cnt int; v_um jsonb := '{}'::jsonb; r record; z record;
  v_vor jsonb; v_nach jsonb; v_diff jsonb; v_pos int; v_status text; v_kf jsonb; v_part int; v_sub text[]; v_erste boolean; v_verbl int := 0; v_exp int := 0;
  v_titel text := p->>'titel'; v_teil_voll jsonb := '{}'; v_pj jsonb;
begin
  select * into t from schule.thema where id = v_alt;
  if t.id is null then raise exception 'TL-S: Thema % fehlt', v_alt; end if;
  if t.teil_von is not null then return jsonb_build_object('thema', v_alt, 'uebersprungen', 'schon geteilt'); end if;
  select * into v_e from schule.einheit where id = schule.thema_einheit(v_alt);
  if v_e.id is null then raise exception 'TL-S: Thema % hat keine Einheit', v_alt; end if;
  select * into b from schule.block where id = coalesce(v_e.block_id, (select bt.block_id from schule.block_thema bt where bt.thema_id = v_alt order by bt.reihenfolge limit 1));
  if b.id is null then raise exception 'TL-S: Thema % hat keinen Ort', v_alt; end if;
  if exists (select 1 from schule.testsitzung s where s.einheit_id = v_e.id and s.status <> 'abgeschlossen' and s.abgeschlossen_am is null) then
    raise exception 'TL-S: offene Test-Sitzung bei Thema % – erst abschließen', v_alt; end if;
  select array_agg(q->>'lernziel') into v_kat from jsonb_array_elements(coalesce(v_e.inhalt->'etappen', '[]'::jsonb)) q;
  -- Teile gegen den Katalog: Etappen, die es noch nicht gibt, überspringen; jeder Teil nicht leer, disjunkt, zusammen der ganze Katalog
  for v_k in 1 .. v_n loop
    v_et := array(select x from jsonb_array_elements_text(p->'teile'->(v_k - 1)->'etappen') x where x = any(v_kat));
    v_fehlt := v_fehlt || array(select x from jsonb_array_elements_text(p->'teile'->(v_k - 1)->'etappen') x where not x = any(v_kat));
    if cardinality(v_et) = 0 and v_k = 1 then raise exception 'TL-S: Thema % Teil 1 hat keine Etappe in der Datenbank', v_alt; end if;
    -- Teil k > 1 ohne Etappe in der Datenbank (z. B. 101 Teil 2: cavalieri aus LK-D 3 noch nicht eingespielt): leere Hülle als Entwurf, nicht im Plan
    v_teil_voll := v_teil_voll || jsonb_build_object(v_k::text, p->'teile'->(v_k - 1)->'etappen');
    if v_alle && v_et then raise exception 'TL-S: Thema % – Etappe in zwei Teilen', v_alt; end if;
    v_alle := v_alle || v_et; v_teil_et := v_teil_et || jsonb_build_object(v_k::text, to_jsonb(v_et));
  end loop;
  if not v_kat <@ v_alle then raise exception 'TL-S: Thema % – Etappen ohne Teil: %', v_alt, array(select x from unnest(v_kat) x where not x = any(v_alle)); end if;

  v_ids := array[v_alt]; v_einh := array[v_e.id];
  v_vor := schule.tl_kind_stand(v_einh, '{}', array[v_alt]);

  -- Teil 1: Titel, Klasse (je Schulart eine Klasse laut Liste; Gym nur, wenn Zusatz), Zusatz
  v_tp := p->'teile'->0;
  v_kf := coalesce(t.klasse_fest, '{}'::jsonb) || jsonb_build_object('rs_by', v_tp->'klasse'->'rs_by', 'ib_myp', v_tp->'klasse'->'ib_myp')
          || case when v_tp->'zusatz' ? 'gym_by' then jsonb_build_object('gym_by', v_tp->'klasse'->'gym_by') else '{}'::jsonb end;
  update schule.thema set unterthema = v_titel || ' – Teil 1 von ' || v_n, untertitel = v_tp->>'untertitel', teil_nr = 1, teil_von = v_n, teil_stamm = v_alt,
         zusatz = nullif(array(select jsonb_array_elements_text(v_tp->'zusatz')), '{}'), klasse_fest = v_kf where id = v_alt;
  -- Platz für die neuen Orte direkt hinter dem bisherigen Ort
  update schule.block set reihenfolge = reihenfolge + (v_n - 1) where kontinent_id is not distinct from b.kontinent_id and reihenfolge > b.reihenfolge;
  -- Schutz der freigegebenen Einheit für diesen Schritt aufheben (Status kurz 'geprueft', am Ende wieder wie vorher)
  if v_e.status = 'freigegeben' then update schule.einheit set status = 'geprueft' where id = v_e.id; end if;

  for v_k in 2 .. v_n loop
    v_tp := p->'teile'->(v_k - 1);
    v_et := array(select jsonb_array_elements_text(v_teil_et->v_k::text));
    v_kf := jsonb_build_object('rs_by', v_tp->'klasse'->'rs_by', 'ib_myp', v_tp->'klasse'->'ib_myp')
            || case when v_tp->'zusatz' ? 'gym_by' then jsonb_build_object('gym_by', v_tp->'klasse'->'gym_by') else '{}'::jsonb end;
    insert into schule.thema (fach, schluessel, block, unterthema, beschreibung, reihenfolge, pruefstatus, klasse_fest, lehrplan_reihenfolge, lernbereich, lehrplan, kurz,
                              untertitel, teil_nr, teil_von, teil_stamm, zusatz)
    values (t.fach, t.schluessel || '_teil' || v_k, t.block, v_titel || ' – Teil ' || v_k || ' von ' || v_n, t.beschreibung, t.reihenfolge, t.pruefstatus, v_kf,
            t.lehrplan_reihenfolge, t.lernbereich, t.lehrplan, t.kurz, v_tp->>'untertitel', v_k, v_n, v_alt, nullif(array(select jsonb_array_elements_text(v_tp->'zusatz')), '{}'))
    returning id into v_th;
    insert into schule.block (fach, schluessel, titel, etappe, ziel_klasse, ziel_begruendung, module, reihenfolge, kontinent_id, stadt, land, lat, lon)
    values (b.fach, b.schluessel || '-teil' || v_k, b.titel || ' · Teil ' || v_k, b.etappe, b.ziel_klasse, b.ziel_begruendung, b.module, b.reihenfolge + v_k - 1,
            b.kontinent_id, b.stadt, b.land, b.lat, b.lon)
    returning id into v_nb;
    insert into schule.block_thema (block_id, thema_id, reihenfolge) values (v_nb, v_th, 0);
    v_pj := coalesce(v_tp->'pflicht_je_schulart', '{}'::jsonb);
    insert into schule.einheit (thema_id, block_id, version, status, schema_version, inhalt, erstellt_von, geprueft_von, geprueft_am)
    values (v_th, v_nb, 1, 'entwurf', v_e.schema_version,
            schule.tl_inhalt(case when v_pj = '{}'::jsonb then v_e.inhalt
                                  else jsonb_set(v_e.inhalt, '{bewertung}', coalesce(v_e.inhalt->'bewertung', '{}'::jsonb) || jsonb_build_object('pflicht_je_schulart', v_pj)) end, v_et),
            'TL-S (aus Einheit ' || v_e.id || ')', v_e.geprueft_von, v_e.geprueft_am)
    returning id into v_ne;
    update schule.aufgabe set einheit_id = v_ne, thema_id = v_th where einheit_id = v_e.id and variante_gruppe = any(v_et) and pool <> 'expedition';
    get diagnostics v_cnt = row_count; v_um := v_um || jsonb_build_object('aufgaben_teil_' || v_k, v_cnt);
    update schule.etappe_text set thema_id = v_th where thema_id = v_alt and lernziel = any(v_et);
    foreach v_tab in array array['karte_stand', 'lernziel_stand', 'besprochen', 'wdh_runde_etappe', 'wdh_staffel_sicherung', 'rueckmeldung'] loop
      if to_regclass('schule.' || v_tab) is not null then
        execute format('update schule.%I set einheit_id = $1 where einheit_id = $2 and lernziel = any($3)', v_tab) using v_ne, v_e.id, v_et;
        get diagnostics v_cnt = row_count; v_um := v_um || jsonb_build_object(v_tab || '_teil_' || v_k, v_cnt);
      end if;
    end loop;
    update schule.misch_ausgabe set einheit_id = v_ne where einheit_id = v_e.id and lernziel = any(v_et);
    if to_regclass('schule.wackelt_status') is not null then
      execute 'update schule.wackelt_status set einheit_id = $1, thema_id = $2 where einheit_id = $3 and lernziel = any($4)' using v_ne, v_th, v_e.id, v_et;
    end if;
    update schule.abgelegt set einheit_id = v_ne, thema_id = v_th, bezug = 'etappe:' || v_ne || ':' || lernziel
     where einheit_id = v_e.id and lernziel = any(v_et) and bezug = 'etappe:' || v_e.id || ':' || lernziel;
    update schule.sterne s set bezug = regexp_replace(s.bezug, '^(landung|wdh):' || v_e.id || ':', '\1:' || v_ne || ':')
     where s.bezug ~ ('^(landung|wdh):' || v_e.id || ':') and split_part(s.bezug, ':', 3) = any(v_et);
    -- Stufen-Einträge der Kinder („Kann er …“ gilt für das ganze Thema)
    update schule.lernender set stufen = stufen || jsonb_build_object(v_th::text, stufen->v_alt::text) where stufen ? v_alt::text;
    v_ids := v_ids || v_th; v_einh := v_einh || v_ne; v_bl := v_bl || v_nb;
  end loop;

  -- Einheit von Teil 1 verkleinern, alle Einheiten (wieder) freigeben
  v_pj := coalesce(p->'teile'->0->'pflicht_je_schulart', '{}'::jsonb);
  update schule.einheit set inhalt = schule.tl_inhalt(case when v_pj = '{}'::jsonb then inhalt
                                                           else jsonb_set(inhalt, '{bewertung}', coalesce(inhalt->'bewertung', '{}'::jsonb) || jsonb_build_object('pflicht_je_schulart', v_pj)) end,
                                                      array(select jsonb_array_elements_text(v_teil_et->'1'))) where id = v_e.id;
  update schule.einheit set status = v_e.status where id = v_e.id;
  update schule.einheit set status = v_e.status, freigegeben_von = case when v_e.status = 'freigegeben' then 'TL-S' end,
         freigegeben_am = case when v_e.status = 'freigegeben' then now() end
   where id = any(v_einh[2:]) and jsonb_array_length(coalesce(inhalt->'etappen', '[]'::jsonb)) > 0;   -- leere Hülle bleibt Entwurf
  select count(*) into v_verbl from schule.aufgabe a where a.einheit_id = v_e.id and a.pool <> 'expedition' and not coalesce(a.variante_gruppe, '') = any(array(select jsonb_array_elements_text(v_teil_et->'1')));
  select count(*) into v_exp from schule.aufgabe a where a.einheit_id = v_e.id and a.pool = 'expedition';

  -- Plan: neue Orte direkt hinter dem bisherigen Ort (Kinder, die ihn im Plan haben)
  -- Teil 1 ist in der Schulart des Kindes Zusatz (z. B. 101 Teil 1 in der Realschule): offener Pflicht-Eintrag wird „zusatz“
  update schule.route ro set art = 'zusatz', geaendert_von = 'TL-S', geaendert_am = now()
   where ro.block_id = b.id and ro.art = 'normal' and ro.status not in ('fertig', 'entfernt')
     and (select coalesce(ll.schulart, 'gym_by') from schule.lernender ll where ll.id = ro.lernender_id) = any(array(select jsonb_array_elements_text(p->'teile'->0->'zusatz')));
  for r in select * from schule.route where block_id = b.id order by lernender_id, id loop
    for v_k in 2 .. v_n loop
      continue when jsonb_array_length(v_teil_et->v_k::text) = 0;
      v_pos := (select x.position from schule.route x where x.id = r.id) + v_k - 1;   -- aktuelle Position (kann sich durch frühere Einfügungen verschoben haben)
      update schule.route set position = position + 1 where lernender_id = r.lernender_id and position >= v_pos;   -- route_pos ist deferrable
      v_tp := p->'teile'->(v_k - 1);
      insert into schule.route (lernender_id, block_id, position, art, status, kann_schon, ziel_themen, geaendert_von, geaendert_am, ausgelassen, status_vor_entfernen,
                                kann_schon_themen, kann_wdh_themen)
      values (r.lernender_id, v_bl[v_k - 1], v_pos,
              case when (select coalesce(l.schulart, 'gym_by') from schule.lernender l where l.id = r.lernender_id) = any(array(select jsonb_array_elements_text(v_tp->'zusatz')))
                   then 'zusatz' else r.art end,
              case r.status when 'fertig' then 'offen' when 'laeuft' then 'offen' else r.status end, r.kann_schon,
              case when v_alt = any(r.ziel_themen) then array[v_ids[v_k]] end, 'TL-S', now(),
              case when v_alt = any(r.ausgelassen) then array[v_ids[v_k]] else '{}'::bigint[] end, r.status_vor_entfernen,
              case when v_alt = any(r.kann_schon_themen) then array[v_ids[v_k]] else '{}'::bigint[] end,
              case when v_alt = any(r.kann_wdh_themen) then array[v_ids[v_k]] else '{}'::bigint[] end);
    end loop;
  end loop;

  -- Vollständig übernommene neue Teile: Flug-Abschluss (Stempel) und Ort „fertig“ (100 Sterne über route_sterne)
  for v_k in 2 .. v_n loop
    v_et := array(select jsonb_array_elements_text(v_teil_et->v_k::text));
    continue when cardinality(v_et) = 0;
    -- Kür zählt nicht (Entscheidung 17:05): nur die Pflicht-Etappen des Kindes; ohne Pflicht-Etappe im Teil alle Etappen (wie wdh_ablegen)
    for r in select l.id from schule.lernender l
              where (select bool_and(schule.tl_erledigt(l.id, v_einh[v_k], x))
                       from unnest(coalesce(nullif(array(select y from unnest(schule.pflicht_lernziele(l.id, v_einh[v_k])) y where y = any(v_et)), '{}'), v_et)) x) loop
      insert into schule.flug_erstabschluss (lernender_id, einheit_id, sitzung_id, am)
      values (r.id, v_einh[v_k], null, coalesce((select f.am from schule.flug_erstabschluss f where f.lernender_id = r.id and f.einheit_id = v_e.id), now()))
      on conflict do nothing;
      -- abgeschlossener Flug-Test der alten Einheit gilt auch für den neuen Teil (sonst zeigt thema_stufe „Test offen“); Einfügen bucht keine Sterne
      insert into schule.testsitzung (lernender_id, art, block_id, thema_id, einheit_id, aufgaben, status, regel_version, gestartet_am, abgeschlossen_am, ort_geschafft, flug_geschafft)
      select ts.lernender_id, 'blocktest', v_bl[v_k - 1], v_ids[v_k], v_einh[v_k],
             array(select aa from unnest(ts.aufgaben) aa where aa in (select x.id from schule.aufgabe x where x.einheit_id = v_einh[v_k])),
             'abgeschlossen', ts.regel_version, ts.gestartet_am, ts.abgeschlossen_am, true, true
        from schule.testsitzung ts
       where ts.lernender_id = r.id and ts.einheit_id = v_e.id and ts.art = 'blocktest' and ts.status = 'abgeschlossen'
         and not exists (select 1 from schule.testsitzung y where y.lernender_id = r.id and y.einheit_id = v_einh[v_k] and y.art = 'blocktest' and y.status = 'abgeschlossen')
       order by ts.abgeschlossen_am limit 1;
      if not exists (select 1 from schule.route x where x.lernender_id = r.id and x.block_id = v_bl[v_k - 1]) then   -- nicht im Plan: Ort trotzdem als geschafft führen
        insert into schule.route (lernender_id, block_id, position, art, status, geaendert_von, geaendert_am)
        values (r.id, v_bl[v_k - 1], coalesce((select max(x.position) from schule.route x where x.lernender_id = r.id), 0) + 1, 'normal', 'offen', 'TL-S', now());
      end if;
      update schule.route set status = 'fertig', art = case when art = 'zusatz' then 'normal' else art end, geaendert_von = 'TL-S', geaendert_am = now()
       where lernender_id = r.id and block_id = v_bl[v_k - 1] and status <> 'fertig';
      v_um := v_um || jsonb_build_object('vollstaendig_teil_' || v_k, coalesce((v_um->>('vollstaendig_teil_' || v_k))::int, 0) + 1);
    end loop;
  end loop;

  -- Lehrplan-Zuordnungen (B3a; echte Datenbank: je Punkt genau EIN Hauptbezug, zuordnung_eintrag_id_idx, und (eintrag_id, thema_id) eindeutig):
  -- Punkt → Teil nach seinen Etappen. Reicht ein Punkt über mehrere Teile, behält der Teil mit den meisten seiner Etappen (bei Gleichstand der frühere)
  -- die bisherige Zeile samt Bezug; die übrigen Teile bekommen einen Nebenbezug mit rolle und ihren Etappen. thema_lage_klasse (unten) zählt solche
  -- Nebenbezüge von Geschwister-Teilen wie den Hauptbezug, damit jeder Teil seine Klassen behält. Punkte „ganzes Thema“ ('*') gelten für alle Teile.
  for z in select * from schule.zuordnung where thema_id = v_alt and etappen is not null and not ('*' = any(etappen)) order by id loop
    select k into v_part from generate_series(1, v_n) k
     order by cardinality(array(select x from unnest(z.etappen) x where x = any(array(select jsonb_array_elements_text(v_teil_voll->k::text))))) desc, k limit 1;
    if not exists (select 1 from unnest(z.etappen) x where x = any(array(select jsonb_array_elements_text(v_teil_voll->v_part::text)))) then continue; end if;
    v_sub := array(select x from unnest(z.etappen) x where x = any(array(select jsonb_array_elements_text(v_teil_voll->v_part::text))));
    update schule.zuordnung set thema_id = v_ids[v_part], etappen = v_sub where id = z.id;
    for v_k in select k from generate_series(1, v_n) k where k <> v_part
                  and (select array(select jsonb_array_elements_text(v_teil_voll->k::text))) && z.etappen order by 1 loop
      v_sub := array(select x from unnest(z.etappen) x where x = any(array(select jsonb_array_elements_text(v_teil_voll->v_k::text))));
      insert into schule.zuordnung (eintrag_id, thema_id, bezug, begruendung, pruefstatus, rolle, etappen)
      values (z.eintrag_id, v_ids[v_k], 'neben', 'TL-S 22.11.2026: Punkt über mehrere Teile von Thema ' || v_alt || ' – Hauptbezug bei Teil ' || v_part
              || ', hier die Etappen von Teil ' || v_k, z.pruefstatus, z.rolle, v_sub)
      on conflict (eintrag_id, thema_id) do update set etappen = excluded.etappen, rolle = coalesce(schule.zuordnung.rolle, excluded.rolle)
       where schule.zuordnung.bezug = 'neben';
    end loop;
  end loop;
  for z in select * from schule.zuordnung where thema_id = v_alt and '*' = any(coalesce(etappen, '{}')) order by id loop
    for v_k in 2 .. v_n loop
      insert into schule.zuordnung (eintrag_id, thema_id, bezug, begruendung, pruefstatus, rolle, etappen)
      values (z.eintrag_id, v_ids[v_k], 'neben', 'TL-S 22.11.2026: Punkt gilt für das ganze Thema ' || v_alt || ' – auch für Teil ' || v_k, z.pruefstatus, z.rolle, z.etappen)
      on conflict (eintrag_id, thema_id) do nothing;
    end loop;
  end loop;

  -- Vorher/Nachher je Kind (B4)
  v_nach := schule.tl_kind_stand(v_einh, v_bl, v_ids);
  select jsonb_object_agg(k, jsonb_build_object('vorher', v_vor->k->'fest', 'nachher', v_nach->k->'fest')) into v_diff
    from (select jsonb_object_keys(v_vor) k) x where (v_vor->k->'fest') is distinct from (v_nach->k->'fest');
  if v_diff is not null then raise exception 'TL-S: Thema % – Vorher/Nachher je Kind verschieden: %', v_alt, v_diff; end if;
  -- B4 erlaubte Deltas (jede andere Abweichung bricht ab):
  --   • im Plan, gesetzt (kann schon / kann wiederholen) und Rückreise: jeder Teil wie das Thema vorher;
  --   • Etappen, begonnen, gelandet, sicher, wieder offen: verteilen sich ohne Verlust auf die Teile (Summe wie vorher);
  --   • die Stufe je Teil ergibt sich neu aus seinen Etappen (z. B. Teil 1 schon gelandet → „wiederholung“) – sie wird nicht verglichen;
  --   • Reiseoptionen: gleich, wenn neue Orte auf den Ort von Teil 1 abgebildet werden.
  select jsonb_object_agg(k, jsonb_build_object('vorher', v_vor->k->'neu'->'stufen'->v_alt::text, 'nachher', v_nach->k->'neu'->'stufen',
                                                'reise_vorher', v_vor->k->'neu'->'reise', 'reise_nachher', v_nach->k->'neu'->'reise')) into v_diff
    from (select jsonb_object_keys(v_vor) k) x
   where exists (select 1 from unnest(v_ids) i, unnest(array['im_plan', 'gesetzt', 'rueckreise']) f
                  where (v_nach->k->'neu'->'stufen'->i::text->f) is distinct from (v_vor->k->'neu'->'stufen'->v_alt::text->f)
                    -- Zusatz-Teil in der Schulart des Kindes: steht als „zusatz“ im Plan (thema_stufe zählt nur „normal“) – erlaubt
                    -- leerer Teil (Etappen noch nicht in der Datenbank): nicht im Plan – erlaubt
                    and not (f = 'im_plan' and (v_nach->k->'neu'->'stufen'->i::text->>'etappen')::int = 0)
                    and not (f = 'im_plan' and (v_nach->k->'neu'->'stufen'->i::text->>'im_plan')::boolean is false
                             and (select coalesce(ll.schulart, 'gym_by') from schule.lernender ll where ll.id = k::bigint) = any(coalesce((select th.zusatz from schule.thema th where th.id = i), '{}'::text[]))
                             and ((v_vor->k->'neu'->'stufen'->v_alt::text->>'im_plan')::boolean is not true
                                  or exists (select 1 from schule.route rr join schule.block_thema bt2 on bt2.block_id = rr.block_id and bt2.thema_id = i
                                              where rr.lernender_id = k::bigint and rr.art = 'zusatz' and rr.status <> 'entfernt'))))
      or exists (select 1 from unnest(array['etappen', 'begonnen', 'gelandet', 'sicher', 'wieder_offen']) f
                  where (select sum(coalesce((v_nach->k->'neu'->'stufen'->i::text->>f)::int, 0)) from unnest(v_ids) i)
                        is distinct from coalesce((v_vor->k->'neu'->'stufen'->v_alt::text->>f)::int, 0))
      or (case when (select coalesce(ll.schulart, 'gym_by') from schule.lernender ll where ll.id = k::bigint) = any(array(select jsonb_array_elements_text(p->'teile'->0->'zusatz')))
               -- Teil 1 ist in der Schulart des Kindes Zusatz: die Option dieses Kontinents darf wegfallen oder wechseln (erlaubtes Delta)
               then schule.tl_reise_ohne(v_nach->k->'neu'->'reise', (select ko.titel from schule.kontinent ko where ko.id = b.kontinent_id))
                    is distinct from schule.tl_reise_ohne(v_vor->k->'neu'->'reise', (select ko.titel from schule.kontinent ko where ko.id = b.kontinent_id))
               else (v_nach->k->'neu'->'reise') is distinct from (v_vor->k->'neu'->'reise') end);
  if v_diff is not null then raise exception 'TL-S: Thema % – Stufen/Reiseoptionen außerhalb der erlaubten Deltas: %', v_alt, v_diff; end if;
  return jsonb_build_object('thema', v_alt, 'teile', to_jsonb(v_ids), 'einheiten', to_jsonb(v_einh), 'orte_neu', to_jsonb(v_bl),
    'etappen_je_teil', v_teil_et, 'etappen_noch_nicht_in_db', to_jsonb(v_fehlt), 'aufgaben_ohne_etappe_bei_teil_1', v_verbl, 'expeditions_aufgaben_bei_teil_1', v_exp,
    'umgehaengt', v_um, 'je_kind', (select jsonb_object_agg(k, v_nach->k->'neu') from jsonb_object_keys(v_nach) k));
end $function$;

-- Id eines Knotens „Thema Teil k“ (k null = Thema selbst bzw. Teil 1)
create or replace function schule.tl_knoten(p_thema bigint, p_teil int)
 returns bigint language sql stable set search_path to ''
as $function$
  select coalesce((select t.id from schule.thema t where t.teil_stamm = p_thema and t.teil_nr = coalesce(p_teil, 1)), p_thema);
$function$;

-- 3. Teilen, Kanten, Zusatz-Regel
do $mig$
declare v_daten jsonb := $json${"plan": [{"thema": 26, "titel": "Direkte Proportionalität und Dreisatz", "teile": [{"teil": 1, "untertitel": "Dreisatz", "etappen": ["einheit", "dreisatz", "geschickt", "sach", "aenderung"], "klasse": {"gym_by": 5, "rs_by": 5, "ib_myp": 2}, "zusatz": [], "pflicht_je_schulart": {}}, {"teil": 2, "untertitel": "proportionale Zuordnungen erkennen", "etappen": ["erkennen", "vervielfachen", "pruefen"], "klasse": {"gym_by": 5, "rs_by": 6, "ib_myp": 2}, "zusatz": [], "pflicht_je_schulart": {}}]}, {"thema": 29, "titel": "Terme umformen", "teile": [{"teil": 1, "untertitel": "zusammenfassen und ausmultiplizieren", "etappen": ["zusammenfassen", "produkte", "minusklammer", "ausmultiplizieren", "aequivalenz"], "klasse": {"gym_by": 7, "rs_by": 7, "ib_myp": 1}, "zusatz": [], "pflicht_je_schulart": {}}, {"teil": 2, "untertitel": "Summe mal Summe, binomische Formeln, Gleichungen mit Klammern", "etappen": ["summe_mal_summe", "ausklammern", "binomisch", "gleichungen_binomisch"], "klasse": {"gym_by": 7, "rs_by": 8, "ib_myp": 4}, "zusatz": [], "pflicht_je_schulart": {}}]}, {"thema": 44, "titel": "Konstruktionen, Kongruenz und Beweise", "teile": [{"teil": 1, "untertitel": "Dreiecke konstruieren, Kongruenz", "etappen": ["gleichschenklig", "kongruenzsatz", "konstruierbar", "planfigur", "satz_kehrsatz"], "klasse": {"gym_by": 7, "rs_by": 7, "ib_myp": 2}, "zusatz": [], "pflicht_je_schulart": {}}, {"teil": 2, "untertitel": "Vierecke", "etappen": ["vierecke", "vierecke_konstruieren"], "klasse": {"gym_by": 7, "rs_by": 8, "ib_myp": null}, "zusatz": ["gym_by", "ib_myp"], "pflicht_je_schulart": {}}]}, {"thema": 46, "titel": "Kongruenzabbildungen", "teile": [{"teil": 1, "untertitel": "Spiegeln und Symmetrie", "etappen": ["achsenspiegelung", "mittelsenkrechte", "winkelhalbierende", "symmetrie", "vierecke_ordnen", "eigenschaften"], "klasse": {"gym_by": 7, "rs_by": 6, "ib_myp": 3}, "zusatz": [], "pflicht_je_schulart": {}}, {"teil": 2, "untertitel": "Verschieben und Vektoren", "etappen": ["verschiebung", "gegenvektor", "vektor_koordinaten"], "klasse": {"gym_by": 7, "rs_by": 7, "ib_myp": 3}, "zusatz": ["gym_by"], "pflicht_je_schulart": {}}, {"teil": 3, "untertitel": "Drehen und Punktspiegelung", "etappen": ["punktspiegelung", "drehung", "vektor_drehen"], "klasse": {"gym_by": 7, "rs_by": 8, "ib_myp": 3}, "zusatz": [], "pflicht_je_schulart": {}}]}, {"thema": 61, "titel": "Zufall und Laplace", "teile": [{"teil": 1, "untertitel": "Ergebnis, Ereignis, relative Häufigkeit", "etappen": ["begriffe", "rel_haeufigkeit", "darstellen"], "klasse": {"gym_by": 8, "rs_by": 8, "ib_myp": 2}, "zusatz": [], "pflicht_je_schulart": {}}, {"teil": 2, "untertitel": "Laplace-Wahrscheinlichkeit", "etappen": ["laplace", "laplace_pruefen", "gegenereignis", "grosse_zahlen"], "klasse": {"gym_by": 8, "rs_by": 9, "ib_myp": 2}, "zusatz": [], "pflicht_je_schulart": {}}]}, {"thema": 91, "titel": "Schrägbilder und Raumdarstellung", "teile": [{"teil": 1, "untertitel": "Schrägbilder und Lage im Raum", "etappen": ["pyramide", "lage", "wahre_groesse", "raumwinkel"], "klasse": {"gym_by": 10, "rs_by": 7, "ib_myp": null}, "zusatz": ["ib_myp"], "pflicht_je_schulart": {}}, {"teil": 2, "untertitel": "Raumkoordinaten, Körpersymmetrie, Rotationskörper", "etappen": ["koordinaten", "rotation", "axialschnitt", "koerper_symmetrie"], "klasse": {"gym_by": 10, "rs_by": 8, "ib_myp": null}, "zusatz": ["ib_myp"], "pflicht_je_schulart": {}}]}, {"thema": 101, "titel": "Prismen und Zylinder", "teile": [{"teil": 1, "untertitel": "gerade Prismen und Zylinder", "etappen": ["prisma_volumen", "prisma_oberflaeche", "prisma_umstellen", "zylinder_volumen", "zylinder_oberflaeche", "sach", "verstehen"], "klasse": {"gym_by": 8, "rs_by": 9, "ib_myp": null}, "zusatz": ["ib_myp", "rs_by"], "pflicht_je_schulart": {}}, {"teil": 2, "untertitel": "schiefe Körper und Cavalieri", "etappen": ["cavalieri"], "klasse": {"gym_by": 10, "rs_by": 9, "ib_myp": null}, "zusatz": ["ib_myp"], "pflicht_je_schulart": {}}]}], "kanten": [{"thema": 26, "thema_teil": 1, "braucht": 25, "braucht_teil": null, "art": "hart", "herkunft": "bisher", "art_je_schulart": {"gym_by": "hart", "rs_by": "hart", "ib_myp": "hart"}}, {"thema": 29, "thema_teil": 1, "braucht": 28, "braucht_teil": null, "art": "hart", "herkunft": "bisher", "art_je_schulart": {"gym_by": "hart", "rs_by": "hart", "ib_myp": "hart"}}, {"thema": 8, "thema_teil": null, "braucht": 29, "braucht_teil": 2, "art": "hart", "herkunft": "bisher", "art_je_schulart": {"gym_by": "hart", "rs_by": "hart", "ib_myp": "hart"}}, {"thema": 49, "thema_teil": null, "braucht": 46, "braucht_teil": 3, "art": "empfohlen", "herkunft": "bisher", "art_je_schulart": {"gym_by": "empfohlen", "rs_by": "empfohlen", "ib_myp": "empfohlen"}}, {"thema": 63, "thema_teil": null, "braucht": 61, "braucht_teil": 1, "art": "hart", "herkunft": "bisher", "art_je_schulart": {"gym_by": "hart", "rs_by": "hart", "ib_myp": "hart"}}, {"thema": 62, "thema_teil": null, "braucht": 61, "braucht_teil": 2, "art": "hart", "herkunft": "bisher", "art_je_schulart": {"gym_by": "hart", "rs_by": "hart", "ib_myp": "hart"}}, {"thema": 47, "thema_teil": null, "braucht": 46, "braucht_teil": 1, "art": "empfohlen", "herkunft": "bisher (inhaltlich zugeordnet)", "art_je_schulart": {"gym_by": "empfohlen", "rs_by": "empfohlen", "ib_myp": "empfohlen"}}, {"thema": 74, "thema_teil": null, "braucht": 46, "braucht_teil": 2, "art": "empfohlen", "herkunft": "bisher", "art_je_schulart": {"gym_by": "empfohlen", "rs_by": "empfohlen", "ib_myp": "empfohlen"}}, {"thema": 4, "thema_teil": null, "braucht": 29, "braucht_teil": 1, "art": "empfohlen", "herkunft": "bisher (inhaltlich zugeordnet)", "art_je_schulart": {"gym_by": "empfohlen", "rs_by": "empfohlen", "ib_myp": "empfohlen"}}, {"thema": 93, "thema_teil": null, "braucht": 26, "braucht_teil": 2, "art": "hart", "herkunft": "bisher", "art_je_schulart": {"gym_by": "hart", "rs_by": "hart", "ib_myp": "hart"}}, {"thema": 91, "thema_teil": 1, "braucht": 52, "braucht_teil": null, "art": "hart", "herkunft": "bisher", "art_je_schulart": {"gym_by": "hart", "rs_by": "hart", "ib_myp": "Zusatz"}}, {"thema": 61, "thema_teil": 1, "braucht": 21, "braucht_teil": null, "art": "hart", "herkunft": "bisher", "art_je_schulart": {"gym_by": "hart", "rs_by": "hart", "ib_myp": "hart"}}, {"thema": 97, "thema_teil": null, "braucht": 29, "braucht_teil": 2, "art": "hart", "herkunft": "bisher", "art_je_schulart": {"gym_by": "hart", "rs_by": "hart", "ib_myp": "hart"}}, {"thema": 35, "thema_teil": null, "braucht": 29, "braucht_teil": 2, "art": "empfohlen", "herkunft": "bisher", "art_je_schulart": {"gym_by": "empfohlen", "rs_by": "empfohlen", "ib_myp": "empfohlen"}}, {"thema": 29, "thema_teil": 1, "braucht": 102, "braucht_teil": null, "art": "hart", "herkunft": "bisher", "art_je_schulart": {"gym_by": "hart", "rs_by": "hart", "ib_myp": "hart"}}, {"thema": 31, "thema_teil": null, "braucht": 29, "braucht_teil": 2, "art": "hart", "herkunft": "bisher", "art_je_schulart": {"gym_by": "hart", "rs_by": "hart", "ib_myp": "hart"}}, {"thema": 44, "thema_teil": 1, "braucht": 43, "braucht_teil": null, "art": "empfohlen", "herkunft": "bisher", "art_je_schulart": {"gym_by": "empfohlen", "rs_by": "empfohlen", "ib_myp": "empfohlen"}}, {"thema": 44, "thema_teil": 1, "braucht": 98, "braucht_teil": null, "art": "empfohlen", "herkunft": "bisher", "art_je_schulart": {"gym_by": "empfohlen", "rs_by": "empfohlen", "ib_myp": "empfohlen"}}, {"thema": 44, "thema_teil": 1, "braucht": 46, "braucht_teil": 1, "art": "empfohlen", "herkunft": "bisher (inhaltlich zugeordnet)", "art_je_schulart": {"gym_by": "empfohlen", "rs_by": "empfohlen", "ib_myp": "empfohlen"}}, {"thema": 46, "thema_teil": 1, "braucht": 42, "braucht_teil": null, "art": "empfohlen", "herkunft": "bisher", "art_je_schulart": {"gym_by": "empfohlen", "rs_by": "empfohlen", "ib_myp": "empfohlen"}}, {"thema": 64, "thema_teil": null, "braucht": 61, "braucht_teil": 2, "art": "hart", "herkunft": "bisher", "art_je_schulart": {"gym_by": "hart", "rs_by": "hart", "ib_myp": "hart"}}, {"thema": 92, "thema_teil": null, "braucht": 101, "braucht_teil": 2, "art": "empfohlen", "herkunft": "bisher", "art_je_schulart": {"gym_by": "empfohlen", "rs_by": "empfohlen", "ib_myp": "empfohlen"}}, {"thema": 101, "thema_teil": 1, "braucht": 99, "braucht_teil": null, "art": "empfohlen", "herkunft": "bisher", "art_je_schulart": {"gym_by": "empfohlen", "rs_by": "Zusatz", "ib_myp": "Zusatz"}}, {"thema": 101, "thema_teil": 1, "braucht": 100, "braucht_teil": null, "art": "empfohlen", "herkunft": "bisher", "art_je_schulart": {"gym_by": "empfohlen", "rs_by": "Zusatz", "ib_myp": "Zusatz"}}, {"thema": 101, "thema_teil": 1, "braucht": 51, "braucht_teil": null, "art": "empfohlen", "herkunft": "bisher", "art_je_schulart": {"gym_by": "empfohlen", "rs_by": "Zusatz", "ib_myp": "Zusatz"}}, {"thema": 26, "thema_teil": 2, "braucht": 26, "braucht_teil": 1, "art": "hart", "herkunft": "Teilung", "art_je_schulart": {"gym_by": "hart", "rs_by": "hart", "ib_myp": "hart"}}, {"thema": 29, "thema_teil": 2, "braucht": 29, "braucht_teil": 1, "art": "hart", "herkunft": "Teilung", "art_je_schulart": {"gym_by": "hart", "rs_by": "hart", "ib_myp": "hart"}}, {"thema": 44, "thema_teil": 2, "braucht": 44, "braucht_teil": 1, "art": "hart", "herkunft": "Teilung", "art_je_schulart": {"gym_by": "Zusatz", "rs_by": "hart", "ib_myp": "Zusatz"}}, {"thema": 46, "thema_teil": 2, "braucht": 46, "braucht_teil": 1, "art": "hart", "herkunft": "Teilung", "art_je_schulart": {"gym_by": "Zusatz", "rs_by": "hart", "ib_myp": "hart"}}, {"thema": 46, "thema_teil": 3, "braucht": 46, "braucht_teil": 2, "art": "hart", "herkunft": "Teilung", "art_je_schulart": {"gym_by": "empfohlen", "rs_by": "hart", "ib_myp": "hart"}}, {"thema": 61, "thema_teil": 2, "braucht": 61, "braucht_teil": 1, "art": "hart", "herkunft": "Teilung", "art_je_schulart": {"gym_by": "hart", "rs_by": "hart", "ib_myp": "hart"}}, {"thema": 91, "thema_teil": 2, "braucht": 91, "braucht_teil": 1, "art": "hart", "herkunft": "Teilung", "art_je_schulart": {"gym_by": "hart", "rs_by": "hart", "ib_myp": "Zusatz"}}, {"thema": 101, "thema_teil": 2, "braucht": 101, "braucht_teil": 1, "art": "hart", "herkunft": "Teilung", "art_je_schulart": {"gym_by": "hart", "rs_by": "empfohlen", "ib_myp": "Zusatz"}}, {"thema": 46, "thema_teil": 3, "braucht": 46, "braucht_teil": 1, "art": "empfohlen", "herkunft": "Teilung über Zusatz-Teil hinweg", "art_je_schulart": {"gym_by": "hart"}}]}$json$::jsonb; x jsonb; r jsonb; k jsonb; v_a bigint; v_b bigint; v_a0 bigint; v_b0 bigint; z record; v_n int := 0;
begin
  for x in select * from jsonb_array_elements(v_daten->'plan') loop
    r := schule.tl_teilen(x);
    raise notice 'TL-S Thema %: %', x->>'thema', r - 'je_kind';
    raise notice 'TL-S Thema % je Kind (Nummern; neu: Plan, Ort-Sterne, Flug-Abschlüsse): %', x->>'thema',
      (select jsonb_object_agg(kk, (r->'je_kind'->kk) - 'stufen') from jsonb_object_keys(coalesce(r->'je_kind', '{}'::jsonb)) kk);
  end loop;
  -- Kanten: bisherige Kanten auf den richtigen Teil (Art laut Liste), Teilungs-Kanten neu
  for k in select * from jsonb_array_elements(v_daten->'kanten') loop
    v_a := schule.tl_knoten((k->>'thema')::bigint, (k->>'thema_teil')::int); v_b := schule.tl_knoten((k->>'braucht')::bigint, (k->>'braucht_teil')::int);
    v_a0 := (k->>'thema')::bigint; v_b0 := (k->>'braucht')::bigint;
    if k->>'herkunft' <> 'Teilung' and (v_a <> v_a0 or v_b <> v_b0)
       and exists (select 1 from schule.voraussetzung v where v.thema_id = v_a0 and v.braucht_id = v_b0)
       and not exists (select 1 from schule.voraussetzung v where v.thema_id = v_a and v.braucht_id = v_b) then
      update schule.voraussetzung set thema_id = v_a, braucht_id = v_b, art = k->>'art' where thema_id = v_a0 and braucht_id = v_b0;
    else
      insert into schule.voraussetzung (thema_id, braucht_id, begruendung, art)
      values (v_a, v_b, case when k->>'herkunft' = 'Teilung' then 'TL-S: Teil braucht den Teil davor' else 'TL-S: Kante nach lk_teilung_2211' end, k->>'art')
      on conflict (thema_id, braucht_id) do update set art = excluded.art;
    end if;
    -- Art je Schulart laut Liste (nur wo sie von der Gesamt-Art abweicht; „Zusatz“ = nur empfohlen)
    insert into schule.voraussetzung_schulart (thema_id, braucht_id, schulart, art, begruendung)
    select v_a, v_b, x.key, case when x.value #>> '{}' = 'hart' then 'hart' else 'empfohlen' end, 'TL-S: Kante je Schulart nach lk_teilung_2211'
      from jsonb_each(coalesce(k->'art_je_schulart', '{}'::jsonb)) x
     where (case when x.value #>> '{}' = 'hart' then 'hart' else 'empfohlen' end) <> k->>'art'
    on conflict (thema_id, braucht_id, schulart) do update set art = excluded.art;
    v_n := v_n + 1;
  end loop;
  -- Zusatz-Regel je Schulart: Voraussetzung, die in der Schulart Zusatz ist, ist dort nur empfohlen; der Folgeteil braucht dort hart den Teil davor
  for z in select v.thema_id x, v.braucht_id p, s.schulart from schule.voraussetzung v join schule.thema t on t.id = v.braucht_id
                                                             cross join lateral unnest(t.zusatz) s(schulart) where v.art = 'hart' loop
    insert into schule.voraussetzung_schulart (thema_id, braucht_id, schulart, art, begruendung) values (z.x, z.p, z.schulart, 'empfohlen', 'TL-S: Voraussetzung ist in dieser Schulart Zusatz')
    on conflict (thema_id, braucht_id, schulart) do update set art = excluded.art;
    -- Überbrückung nur, wenn der Folgeteil in dieser Schulart selbst Pflicht ist (ein Zusatz-Teil braucht keine harte Brücke)
    continue when z.schulart = any(coalesce((select t2.zusatz from schule.thema t2 where t2.id = z.x), '{}'));
    insert into schule.voraussetzung (thema_id, braucht_id, begruendung, art)
    select z.x, v.braucht_id, 'TL-S: über einen Zusatz-Teil hinweg (je Schulart hart)', 'empfohlen' from schule.voraussetzung v where v.thema_id = z.p and v.art = 'hart' and v.braucht_id <> z.x
    on conflict (thema_id, braucht_id) do nothing;
    insert into schule.voraussetzung_schulart (thema_id, braucht_id, schulart, art, begruendung)
    select z.x, v.braucht_id, z.schulart, 'hart', 'TL-S: Teil davor ist in dieser Schulart Zusatz – hart braucht es den Teil davor'
      from schule.voraussetzung v where v.thema_id = z.p and v.art = 'hart' and v.braucht_id <> z.x
    on conflict (thema_id, braucht_id, schulart) do update set art = excluded.art;
  end loop;
  raise notice 'TL-S: % Kanten verarbeitet; Zusatz-Abweichungen: %', v_n, (select count(*) from schule.voraussetzung_schulart);
end $mig$;

-- 3b. Lehrplan-Lage: Nebenbezüge von Geschwister-Teilen (Hauptbezug desselben Punkts bei einem anderen Teil desselben Themas) zählen in
--     thema_lage_klasse wie Hauptbezüge – so behält jeder Teil seine Klassen, obwohl je Punkt nur ein Hauptbezug erlaubt ist.
do $$
declare d text; a text := $a$(zu.bezug = 'haupt'::text)$a$; n text;
begin
  if to_regclass('schule.thema_lage_klasse') is null then raise notice 'thema_lage_klasse fehlt (LK-S?) – übersprungen'; return; end if;
  d := pg_get_viewdef('schule.thema_lage_klasse'::regclass);
  if position('TL-S Geschwister-Teil' in d) > 0 or position('teil_stamm' in d) > 0 then raise notice 'thema_lage_klasse schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'TL-S: Anker in thema_lage_klasse nicht eindeutig'; end if;
  n := $n$((zu.bezug = 'haupt'::text) OR ((zu.bezug = 'neben'::text) AND (zu.etappen IS NOT NULL) AND (EXISTS ( SELECT 1
           FROM schule.thema t1 JOIN schule.zuordnung zh ON zh.eintrag_id = zu.eintrag_id AND zh.bezug = 'haupt'::text
           JOIN schule.thema t2 ON t2.id = zh.thema_id
          WHERE t1.id = zu.thema_id AND t1.teil_stamm IS NOT NULL AND t2.teil_stamm = t1.teil_stamm AND t2.id <> t1.id))))$n$;
  execute 'create or replace view schule.thema_lage_klasse as ' || replace(d, a, n);
  comment on view schule.thema_lage_klasse is 'LK-S 2 / TL-S: je Schulart, Zweig, Thema und belegter Klasse (Hauptbezüge; bei geteilten Themen auch Nebenbezüge von Geschwister-Teilen): Rolle, klasse_route, Etappen, Lernbereiche';
end $$;

-- 4. Visum und Reiseoptionen je Schulart (Zusatz-Regel)
create or replace view schule.v_ort_visum as
 SELECT DISTINCT bt.block_id AS ort_id,
    bt2.block_id AS braucht_ort_id,
    s.schulart
   FROM schule.voraussetzung v
     CROSS JOIN (VALUES ('gym_by'::text), ('rs_by'::text), ('ib_myp'::text)) s(schulart)
     JOIN schule.block_thema bt ON bt.thema_id = v.thema_id
     JOIN schule.block_thema bt2 ON bt2.thema_id = v.braucht_id
     LEFT JOIN schule.voraussetzung_schulart o ON o.thema_id = v.thema_id AND o.braucht_id = v.braucht_id AND o.schulart = s.schulart
  WHERE coalesce(o.art, v.art) = 'hart'::text AND bt.block_id <> bt2.block_id;

do $$
declare d text := pg_get_functiondef('schule.reiseoptionen(bigint)'::regprocedure);
  a text := 'where v.ort_id = n.id and v.braucht_ort_id not in (select block_id from ok)';
begin
  if position('v.schulart' in d) > 0 then raise notice 'reiseoptionen schon umgebaut'; return; end if;
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'TL-S: Stelle in reiseoptionen nicht genau einmal gefunden'; end if;
  execute replace(d, a, a || ' and v.schulart = coalesce((select schulart from l), ''gym_by'') /* TL-S: Visum je Schulart */');
end $$;

-- 5. Schnittstelle: Teil, Untertitel, Zusatz je Thema; Voraussetzungen je Schulart
create or replace function schule.thema_teil_json(p_thema bigint)
 returns jsonb language sql stable set search_path to ''
as $function$
  select case when t.teil_von is null then '{}'::jsonb
              else jsonb_build_object('teil', jsonb_strip_nulls(jsonb_build_object('nr', t.teil_nr, 'von', t.teil_von, 'stamm', t.teil_stamm,
                     'untertitel', t.untertitel, 'zusatz', to_jsonb(t.zusatz)))) end
    from schule.thema t where t.id = p_thema;
$function$;
revoke all on function schule.thema_teil_json(bigint), schule.tl_inhalt(jsonb, text[]), schule.tl_erledigt(bigint, bigint, text), schule.tl_kind_stand(bigint[], bigint[], bigint[]),
  schule.tl_teilen(jsonb), schule.tl_knoten(bigint, int), schule.tl_ort_stamm(bigint), schule.tl_reise_abgebildet(jsonb), schule.tl_reise_ohne(jsonb, text) from public, anon, authenticated;
revoke all on schule.voraussetzung_schulart, schule.v_ort_visum from public, anon, authenticated;

do $$
declare d text; n int;
begin
  d := pg_get_functiondef('schule.lehrplan_matrix_lk(jsonb, bigint)'::regprocedure);
  if position('thema_teil_json' in d) = 0 then
    n := (length(d) - length(replace(d, 't.j || jsonb_build_object(', ''))) / length('t.j || jsonb_build_object(');
    if n <> 2 then raise exception 'TL-S: lehrplan_matrix_lk – Stellen % statt 2', n; end if;
    d := replace(d, 't.j || jsonb_build_object(', 't.j || schule.thema_teil_json((t.j->>''thema_id'')::bigint) || jsonb_build_object(');
    if position('|| jsonb_build_object(''lehrplan_zuordnung'', schule.lehrplan_zuordnung_json());' in d) = 0 or position('|| jsonb_build_object(''zweig'', v_zw);' in d) = 0 then
      raise exception 'TL-S: lehrplan_matrix_lk – Ende nicht gefunden'; end if;
    d := replace(d, '|| jsonb_build_object(''lehrplan_zuordnung'', schule.lehrplan_zuordnung_json());',
      '|| jsonb_build_object(''lehrplan_zuordnung'', schule.lehrplan_zuordnung_json())
         || jsonb_build_object(''verbindungen_schulart'', (select coalesce(jsonb_agg(jsonb_build_array(o.thema_id, o.braucht_id, o.schulart, case o.art when ''hart'' then ''h'' else ''e'' end)
                                                         order by o.thema_id, o.braucht_id, o.schulart), ''[]''::jsonb) from schule.voraussetzung_schulart o));   -- TL-S');
    d := replace(d, '|| jsonb_build_object(''zweig'', v_zw);',
      '|| jsonb_build_object(''zweig'', v_zw)
           || jsonb_build_object(''verbindungen_kind'', (select coalesce(jsonb_agg(jsonb_build_array(o.thema_id, o.braucht_id, case o.art when ''hart'' then ''h'' else ''e'' end)
                                                     order by o.thema_id, o.braucht_id), ''[]''::jsonb) from schule.voraussetzung_schulart o where o.schulart = v_sa));   -- TL-S');
    execute d;
  end if;
  d := pg_get_functiondef('schule.lehrplan_thema_lk(jsonb, bigint, bigint, boolean)'::regprocedure);
  if position('thema_teil_json' in d) = 0 then
    n := (length(d) - length(replace(d, 'return p_r || v_kk ||', ''))) / length('return p_r || v_kk ||');
    if n <> 2 then raise exception 'TL-S: lehrplan_thema_lk – Stellen % statt 2', n; end if;
    execute replace(d, 'return p_r || v_kk ||', 'return p_r || v_kk || schule.thema_teil_json(p_thema) ||');
  end if;
end $$;

-- 6. Prüfung über alles: außerhalb der Teilung unverändert
do $mig$
declare v_t text;
begin
  select string_agg(v.t, ', ') into v_t from tl_vorher v join pg_temp.tl_stand() n on n.t = v.t where n.s <> v.s;
  if v_t is not null then raise exception 'TL-S: Stand außerhalb der Teilung verändert (%)', v_t; end if;
  -- B4 Visum je Schulart: nach Abbildung der neuen Orte auf den Ort von Teil 1 (ohne Schleifen) wie vorher
  select string_agg(distinct s.schulart || ':' || coalesce(d.ort_id::text, '') || '→' || coalesce(d.braucht_ort_id::text, ''), ', ') into v_t
    from (values ('gym_by'), ('rs_by'), ('ib_myp')) s(schulart),
         lateral ((select schule.tl_ort_stamm(a.ort_id) ort_id, schule.tl_ort_stamm(a.braucht_ort_id) braucht_ort_id from tl_visum_vorher a
                    where schule.tl_ort_stamm(a.ort_id) <> schule.tl_ort_stamm(a.braucht_ort_id)
                   except select schule.tl_ort_stamm(v.ort_id), schule.tl_ort_stamm(v.braucht_ort_id) from schule.v_ort_visum v where v.schulart = s.schulart)
                  union all
                  (select schule.tl_ort_stamm(v.ort_id), schule.tl_ort_stamm(v.braucht_ort_id) from schule.v_ort_visum v
                    where v.schulart = s.schulart and schule.tl_ort_stamm(v.ort_id) <> schule.tl_ort_stamm(v.braucht_ort_id)
                   except select schule.tl_ort_stamm(a.ort_id), schule.tl_ort_stamm(a.braucht_ort_id) from tl_visum_vorher a)) d;
  if v_t is not null then raise exception 'TL-S: Visum außerhalb der erlaubten Deltas: %', v_t; end if;
  raise notice 'TL-S: Stufen der übrigen Themen, Karten und Lernziel-Stand anderer Flüge, Sterne (außer neuen Ort-Sternen), Plan-Reihenfolge der bisherigen Orte, Visum (abgebildet) unverändert';
end $mig$;
