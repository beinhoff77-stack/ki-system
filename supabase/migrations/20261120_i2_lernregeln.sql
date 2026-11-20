-- Bau-Auftrag I, Teil 2 (20.11.): Lernregeln – H10 Mischkarte serverseitig binden, H2 „endgültig falsch“ als gemeinsame Regel,
-- H6 Tag für „heute selbst gelöst“ vom Server, H12 Voraussetzungen einer Expedition auch auf die Lernkarte prüfen.
-- Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE, keine Bestandsänderung. Wiederholt ausführbar.
--
-- H10: Der Server merkt sich, welche Mischkarten er ausgegeben hat (schule.misch_ausgabe; Eintrag in schule.mischkarten beim Ausliefern).
--      misch_gueltig verlangt zusätzlich eine ausgegebene, noch nicht eingelöste Karte der letzten 24 Stunden; misch_buchen löst sie ein.
--      Ohne passende Ausgabe: normale Buchung als Übung, kein Misch-Beleg. Die App 0.80.0 holt ihre Mischkarten über schule_einheit_lesen
--      → sie sind ausgegeben, der Ablauf bleibt gleich; gefälschte Angaben (misch/aktuell_*) bringen keinen Beleg mehr.
--      uebung_pruefen_intern prüft die Mischkarte einmal vor dem Speichern (v_misch) – nach dem Einlösen wäre sie sonst für die Antwort schon „verbraucht“.
-- H2: schule.versuch_wertung(v) = eigen | neutral | falsch | ersetzt | offen | test. „endgültig falsch“ = letzter Versuch dieser Bordkarte in dieser Runde falsch,
--      gleich welcher Anlauf: ein falscher 1. Anlauf ist „offen“, bis ein 2. Anlauf derselben Bordkarte kommt (→ „ersetzt“) oder das Kind weitergeht
--      bzw. 30 Minuten vergehen (→ „falsch“). Der Trigger versuch_karte bucht damit; offene erste Anläufe merkt er sich (versuch.wertung_offen)
--      und bucht sie beim nächsten Versuch des Kindes nach. Alte Zeilen haben wertung_offen = null und werden nie nachgebucht (keine Bestandsänderung).
--      schule.folge_nachrechnen(kind, einheit, lernziel, ab) rechnet „folge“ mit derselben Regel nach – nur lesen, schreibt nichts.
-- H6: schule.heute_tag(kind) = Kalendertag des Kindes (seine Zeitzone); schule_einheit_lesen und schule_uebung_pruefen.karte liefern 'heute_tag'.
-- H12: expedition_importieren prüft jede angegebene Voraussetzung auch auf eine vorhandene Lernkarte (Lernziel mit Übungen), nicht nur auf das Thema.

-- ---------- H10: ausgegebene Mischkarten ----------
create table if not exists schule.misch_ausgabe (
  id bigint generated always as identity primary key,
  lernender_id bigint not null references schule.lernender(id),
  aufgabe_id bigint not null references schule.aufgabe(id),
  ausgegeben_am timestamptz not null default now(),
  eingeloest_am timestamptz
);
create index if not exists misch_ausgabe_offen on schule.misch_ausgabe (lernender_id, aufgabe_id) where eingeloest_am is null;
alter table schule.misch_ausgabe enable row level security; -- nur über die schule-Funktionen
comment on table schule.misch_ausgabe is 'I-2/H10: vom Server ausgegebene Mischkarten; nur eine ausgegebene, nicht eingelöste Karte der letzten 24 h gibt einen Misch-Beleg';

do $mig$
declare d text;
begin
  -- bisherige Auswahl als schule.mischkarten_waehlen behalten (nur beim ersten Lauf, sonst wäre es schon der neue Text)
  if not exists (select 1 from pg_proc p join pg_namespace n on n.oid = p.pronamespace where n.nspname = 'schule' and p.proname = 'mischkarten_waehlen') then
    d := pg_get_functiondef('schule.mischkarten(bigint, bigint, integer)'::regprocedure);
    if position('LANGUAGE sql' in d) = 0 or position('kand as (' in d) = 0 then raise exception 'schule.mischkarten hat nicht den erwarteten Text'; end if;
    d := replace(d, 'FUNCTION schule.mischkarten(', 'FUNCTION schule.mischkarten_waehlen(');
    execute d;
  end if;
end $mig$;

create or replace function schule.mischkarten(p_lernender bigint, p_einheit bigint, p_anzahl integer default 8)
 returns jsonb
 language plpgsql
 set search_path to ''
as $function$
declare v_j jsonb; v_ids bigint[];
begin
  v_j := schule.mischkarten_waehlen(p_lernender, p_einheit, p_anzahl);
  select coalesce(array_agg((x->>'id')::bigint), '{}') into v_ids from jsonb_array_elements(v_j) x;
  -- I-2/H10: ausgegeben merken; schon offene Ausgaben derselben Bordkarte nur auffrischen
  update schule.misch_ausgabe m set ausgegeben_am = now() where m.lernender_id = p_lernender and m.eingeloest_am is null and m.aufgabe_id = any(v_ids);
  insert into schule.misch_ausgabe(lernender_id, aufgabe_id)
  select p_lernender, u.id from unnest(v_ids) u(id)
   where not exists (select 1 from schule.misch_ausgabe o where o.lernender_id = p_lernender and o.aufgabe_id = u.id and o.eingeloest_am is null);
  return v_j;
end $function$;

create or replace function schule.misch_gueltig(p_lernender bigint, a schule.aufgabe, p jsonb)
 returns boolean
 language sql
 stable
 set search_path to ''
as $function$
  select coalesce(coalesce((p->>'misch')::boolean, false) and a.pool = 'uebung' and a.stufe in (2, 3) and a.freigegeben
     and nullif(p->>'aktuell_einheit', '') is not null and nullif(p->>'aktuell_lernziel', '') is not null
     and not ((p->>'aktuell_einheit')::bigint = a.einheit_id and p->>'aktuell_lernziel' = a.variante_gruppe)
     and exists (select 1 from schule.karte_stand k where k.lernender_id = p_lernender and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe and k.sitzt)
     -- I-2/H10: nur eine vom Server ausgegebene, noch nicht eingelöste Mischkarte der letzten 24 Stunden
     and exists (select 1 from schule.misch_ausgabe m where m.lernender_id = p_lernender and m.aufgabe_id = a.id and m.eingeloest_am is null
                   and m.ausgegeben_am >= now() - interval '24 hours'), false);
$function$;

create or replace function schule.misch_buchen(p_l bigint, p_aufgabe bigint, p_richtig boolean, p_hilfe smallint, p_zeit timestamp with time zone)
 returns void
 language plpgsql
 set search_path to ''
as $function$
declare a schule.aufgabe;
begin
  select * into a from schule.aufgabe where id = p_aufgabe;
  if a.id is null or a.pool <> 'uebung' then return; end if;
  -- I-2/H10: die ausgegebene Mischkarte ist damit eingelöst
  update schule.misch_ausgabe set eingeloest_am = p_zeit
   where id = (select m.id from schule.misch_ausgabe m where m.lernender_id = p_l and m.aufgabe_id = p_aufgabe and m.eingeloest_am is null order by m.ausgegeben_am limit 1);
  if not exists (select 1 from schule.karte_stand k where k.lernender_id = p_l and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe and k.sitzt) then
    perform schule.karte_buchen(p_l, p_aufgabe, p_richtig, p_hilfe, p_zeit); return;
  end if;
  if p_richtig then
    if coalesce(p_hilfe, 0) = 0 then
      update schule.karte_stand set misch_ok_am = p_zeit, richtig = richtig + 1, zuletzt = p_zeit
       where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe;
    end if; -- Tipp oder 2. Versuch: kein Beleg, nichts fällig
  else
    update schule.karte_stand set falsch = falsch + 1 where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe;
    perform schule.karte_faellig_machen(p_l, a.einheit_id, a.variante_gruppe, p_zeit); -- H8: nur fällig, nie wieder öffnen
  end if;
end $function$;

-- ---------- H2: eine Regel für „endgültig falsch“ ----------
alter table schule.versuch add column if not exists wertung_offen boolean;
comment on column schule.versuch.wertung_offen is 'I-2/H2: falscher 1. Anlauf, noch nicht entschieden (2. Anlauf oder weitergegangen); null = vor I-2 oder entschieden ohne Merker';

create or replace function schule.versuch_wertung(v schule.versuch)
 returns text
 language sql
 stable
 set search_path to ''
as $function$
  select case
    when v.testsitzung_id is not null then 'test'
    when v.richtig and coalesce(v.hilfe, 0) = 0 and coalesce(v.anlauf, 1) = 1 then 'eigen'
    when v.richtig then 'neutral'                                   -- Tipp oder 2. Anlauf richtig: zählt nicht, bricht nichts
    when coalesce(v.anlauf, 0) <> 1 then 'falsch'                   -- ohne zweite Chance oder 2. Anlauf: endgültig
    when exists (select 1 from schule.versuch n where n.lernender_id = v.lernender_id and n.aufgabe_id = v.aufgabe_id and n.testsitzung_id is null
                   and n.anlauf = 2 and (n.am, n.id) > (v.am, v.id) and n.am <= v.am + interval '30 minutes') then 'ersetzt' -- der 2. Anlauf entscheidet
    when v.am < now() - interval '30 minutes'
      or exists (select 1 from schule.versuch n where n.lernender_id = v.lernender_id and n.testsitzung_id is null and n.id <> v.id
                   and (n.am, n.id) > (v.am, v.id) and not (n.aufgabe_id = v.aufgabe_id and n.anlauf = 2)) then 'falsch' -- weitergegangen: endgültig
    else 'offen' end;
$function$;
comment on function schule.versuch_wertung(schule.versuch) is 'I-2/H2: eigen | neutral | falsch | ersetzt | offen | test – gemeinsame Regel für Buchung (versuch_karte) und Nachrechnung (folge_nachrechnen)';

create or replace function schule.versuch_buchen(v schule.versuch)
 returns void
 language plpgsql
 set search_path to ''
as $function$
begin
  if coalesce(v.misch, false) then perform schule.misch_buchen(v.lernender_id, v.aufgabe_id, v.richtig, v.hilfe, now());
  else perform schule.karte_buchen(v.lernender_id, v.aufgabe_id, v.richtig, v.hilfe, now()); end if;
  perform schule.expedition_buchen(v.lernender_id, v.aufgabe_id, v.richtig, v.hilfe, v.anlauf, now()); -- prüft selbst den Pool
end $function$;

create or replace function schule.versuch_karte()
 returns trigger
 language plpgsql
 set search_path to ''
as $function$
declare o schule.versuch; w text;
begin
  if new.testsitzung_id is not null then return new; end if;
  -- I-2/H2: offene erste Anläufe dieses Kindes entscheiden – endgültig falsch nachbuchen, ersetzte schließen
  for o in select * from schule.versuch x where x.lernender_id = new.lernender_id and x.wertung_offen and x.id <> new.id order by x.am, x.id loop
    w := schule.versuch_wertung(o);
    if w = 'falsch' then perform schule.versuch_buchen(o); end if;
    if w <> 'offen' then update schule.versuch set wertung_offen = false where id = o.id; end if;
  end loop;
  if schule.versuch_wertung(new) = 'offen' then
    update schule.versuch set wertung_offen = true where id = new.id;
  else
    perform schule.versuch_buchen(new);
  end if;
  return new;
end $function$;

create or replace function schule.folge_nachrechnen(p_l bigint, p_e bigint, p_lz text, p_ab timestamptz default null)
 returns integer
 language plpgsql
 stable
 set search_path to ''
as $function$
declare w schule.versuch; f int := 0; z text;
begin
  for w in select v.* from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
            where v.lernender_id = p_l and a.einheit_id = p_e and a.variante_gruppe = p_lz and a.pool = 'uebung' and v.testsitzung_id is null
              and (p_ab is null or v.am > p_ab) order by v.am, v.id loop
    z := schule.versuch_wertung(w);
    if z = 'eigen' then f := f + 1; elsif z = 'falsch' then f := 0; end if;
  end loop;
  return f;
end $function$;
comment on function schule.folge_nachrechnen(bigint, bigint, text, timestamptz) is 'I-2/H2: „folge“ einer Etappe aus den Versuchen nach derselben Regel wie die Buchung (nur lesen); p_ab z. B. sitzt_am/geoeffnet_am';

-- ---------- H6: Tag des Kindes ----------
create or replace function schule.heute_tag(p_l bigint)
 returns date
 language sql
 stable
 set search_path to ''
as $function$
  select (now() at time zone coalesce((select l.zeitzone from schule.lernender l where l.id = p_l), 'Europe/Berlin'))::date;
$function$;

do $mig$
declare d text;
begin
  -- uebung_pruefen_intern: Mischkarte einmal vor dem Speichern prüfen; heute_tag in der Karte
  d := pg_get_functiondef('schule.uebung_pruefen_intern(bigint, jsonb)'::regprocedure);
  if position('v_misch' in d) = 0 then
    if position('v_hilfe smallint := least(greatest(coalesce((p_daten->>''hilfe'')::smallint, 0), 0), 2);' in d) = 0
       or position('v_anlauf, schule.misch_gueltig(p_lernender, a, p_daten));' in d) = 0
       or position('  if schule.misch_gueltig(p_lernender, a, p_daten) then' in d) = 0
       or position('  insert into schule.versuch(lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf, misch)' in d) = 0
    then raise exception 'uebung_pruefen_intern: Stellen nicht gefunden'; end if;
    d := replace(d, 'v_hilfe smallint := least(greatest(coalesce((p_daten->>''hilfe'')::smallint, 0), 0), 2);',
                    'v_hilfe smallint := least(greatest(coalesce((p_daten->>''hilfe'')::smallint, 0), 0), 2); v_misch boolean;');
    d := replace(d, '  insert into schule.versuch(lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf, misch)',
                    '  v_misch := schule.misch_gueltig(p_lernender, a, p_daten); -- I-2/H10: einmal vor dem Speichern (danach ist die Ausgabe eingelöst)
  insert into schule.versuch(lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf, misch)');
    d := replace(d, 'v_anlauf, schule.misch_gueltig(p_lernender, a, p_daten));', 'v_anlauf, v_misch);');
    d := replace(d, '  if schule.misch_gueltig(p_lernender, a, p_daten) then', '  if v_misch then');
  end if;
  if position('''heute_tag''' in d) = 0 then
    if position('''heute_selbst'', schule.heute_selbst(p_lernender),' in d) = 0 then raise exception 'uebung_pruefen_intern: heute_selbst nicht gefunden'; end if;
    d := replace(d, '''heute_selbst'', schule.heute_selbst(p_lernender),', '''heute_selbst'', schule.heute_selbst(p_lernender), ''heute_tag'', schule.heute_tag(p_lernender),');
  end if;
  execute d;

  -- einheit_lesen_intern: heute_tag
  d := pg_get_functiondef('schule.einheit_lesen_intern(bigint, bigint)'::regprocedure);
  if position('''heute_tag''' in d) = 0 then
    if position('''heute_selbst'', schule.heute_selbst(p_lernender),' in d) = 0 then raise exception 'einheit_lesen_intern: heute_selbst nicht gefunden'; end if;
    d := replace(d, '''heute_selbst'', schule.heute_selbst(p_lernender),', '''heute_selbst'', schule.heute_selbst(p_lernender), ''heute_tag'', schule.heute_tag(p_lernender),');
    execute d;
  end if;

  -- H12: Voraussetzung auch auf die Lernkarte prüfen (vor jedem Schreiben)
  d := pg_get_functiondef('schule.expedition_importieren(jsonb, text)'::regprocedure);
  if position('Voraussetzung: Lernkarte' in d) = 0 then
    if position('    if v_t is null then raise exception ''Voraussetzung: Thema % gibt es nicht'', v->>''thema_schluessel''; end if;' in d) = 0 then
      raise exception 'expedition_importieren: Stelle nicht gefunden'; end if;
    d := replace(d, '    if v_t is null then raise exception ''Voraussetzung: Thema % gibt es nicht'', v->>''thema_schluessel''; end if;',
      '    if v_t is null then raise exception ''Voraussetzung: Thema % gibt es nicht'', v->>''thema_schluessel''; end if;
    if not exists (select 1 from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
                    where e.thema_id = v_t and a.variante_gruppe = v->>''lernziel'' and a.pool = ''uebung'' and e.status <> ''ersetzt'') then
      raise exception ''Voraussetzung: Lernkarte %/% gibt es nicht'', v->>''thema_schluessel'', v->>''lernziel''; end if; -- I-2/H12');
    execute d;
  end if;
end $mig$;
