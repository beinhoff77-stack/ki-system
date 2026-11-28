-- RB-S Einspiel-Paket (erzeugt von tools/tests/regelbezug_einspielen.py). Ein Aufruf, eine Transaktion. Fehler = alles zurück.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '180s', true);
create temp table rb_mig on commit drop as select $rbmig$-- RB-S (Regelbezug, Teil Datenbank): Regel-Kennung und Fehlbilder je Aufgabe; Rückmeldung bei falscher Antwort; erkanntes Fehlbild im Versuch.
-- Plan und Begründung: inhalte/plan/regelbezug.md. Einspielen NUR über das selbstprüfende Paket tools/tests/regelbezug_einspielen.py (eine Transaktion);
-- die Daten (Regeln/Fehlbilder der schon eingespielten Aufgaben) danach getrennt mit tools/regelbezug_sql.py (je Runde ein Paket).
--
-- WAS
-- 1. Zwei EIGENE Tabellen (der Aufgaben-Datensatz bleibt unberührt; aufgabe_schutz bleibt, wie er ist):
--      schule.aufgabe_regel     (aufgabe_id PK) regel = Kennung aus inhalte/mathe-profi/regeln-uebersicht/kennungen.json (rr.… / id.…)
--      schule.aufgabe_fehlbild  (aufgabe_id, nr) nr = Platz in der Liste „fehlbilder“ der Aufgaben-Datei (1, 2, …; Lücken in nr = nicht
--                               übernommene Einträge); art zahl | index | luecke | text, luecke (1-basiert, nur bei art luecke), wert (normiert:
--                               Zahl mit Punkt, Index als Zahl, Text wie in der Datei), beschreibung (Rückmeldung fürs Kind), fehlbild (fb.…), regel.
--    Je Aufgabe ist jeder Schlüssel (art, luecke, wert) höchstens einmal da (eindeutiger Index): ein Fehlbild ist an der Antwort eindeutig erkennbar.
--    Beide Tabellen: Row-Level-Security an, keine Policy, keine Rechte für anon/authenticated (wie die übrigen schule-Tabellen; Lesen nur über
--    die security-definer-Funktionen). Schutz wie bei den Aufgaben: kein UPDATE/DELETE, solange die Einheit der Aufgabe freigegeben ist
--    (schule.regelbezug_schutz; Expeditions-Aufgaben ausgenommen wie in aufgabe_schutz). Einfügen ist erlaubt (Nachtrag).
-- 2. schule.fehlbild_finden(aufgabe, antwort) -> nr oder null. Normiert die Antwort wie schule.antwort_bewerten. zahl: Wert innerhalb der
--    Toleranz der Aufgabe; auswahl/markierung: Index; luecken: NUR die erste falsche Lücke zählt (spätere sind oft Folgefehler); text: ohne
--    Leerzeichen, Groß/Klein egal. Richtige Antwort, Formatfehler, kein oder mehr als ein Treffer -> null. Fehler in der Funktion -> null
--    (die Bewertung darf daran nie scheitern).
-- 3. schule.regelbezug_antwort(aufgabe, antwort, richtig, endgueltig) -> jsonb oder null (null bei richtig oder ohne Daten):
--      {regel, fehlbild, fehlbild_nr, fehlbild_regel, text}   – fehlende Felder fehlen (jsonb_strip_nulls).
--    endgueltig = false (erster Fehlversuch mit zweiter Chance, „nochmal“): NUR regel – die Beschreibung kann ein Zwischenergebnis verraten.
-- 4. schule.uebung_pruefen_intern liefert das Objekt als Feld „regelbezug“ (Text-Patch auf die Live-Definition, Stellen aus BD-S2):
--      endgültige Antwort (4 Stellen „…'hinweis', b->>'hinweis', 'loesung', schule.loesung_sicht(a)“) und wiederholte endgültige Übertragung
--      (aus dem gespeicherten Versuch): volles Objekt; erster Fehlversuch und dessen Wiederholung: nur regel.
--    Ohne Daten in den neuen Tabellen ist das Feld null und fällt weg: Bestand antwortet Zeichen für Zeichen wie bisher.
-- 5. schule.versuch bekommt fehlbild_nr (smallint) und fehlbild (text, Kennung), beide nullable, ohne Vorgabe (kein Umschreiben, kein UPDATE).
--    Ein BEFORE-INSERT-Trigger (schule.versuch_fehlbild) setzt sie bei jeder falschen Antwort (Übung, Mischkarte, Expedition, Test), wenn ein
--    gespeichertes Fehlbild passt. Fehler im Trigger -> Versuch wird ohne Fehlbild gespeichert (nie abgewiesen).
-- 6. schule.versuch_regelbezug(versuch) -> jsonb für „Was wackelt“ (Stufe 2): wie 3, aus dem gespeicherten fehlbild_nr; für Versuche von vor RB-S
--    (fehlbild_nr leer, falsch) nachträglich berechnet, dann mit nachtraeglich = true.
-- 7. schule.fehlbild_probeantwort(aufgabe, art, luecke, wert) -> eine Antwort, die genau dieses Fehlbild zeigt (für die Prüfungen der Pakete).
--
-- WIE: neue Funktionen mit create or replace, Rechte revoke von public, anon, authenticated. uebung_pruefen_intern per Text-Patch
-- (je Stelle alter Text, neuer Text, erwartete Anzahl; alt -> ersetzen, fertig -> nichts, sonst Abbruch; halb umgestellt = Abbruch).
--
-- WAS NICHT: keine Spalte an schule.aufgabe, keine Änderung an aufgabe_schutz, kein UPDATE/DELETE von Daten, kein DROP. Keine Daten (die kommen
-- mit tools/regelbezug_sql.py). Keine Lese-Aktion für Eltern („Was wackelt“ Stufe 2 baut auf 5/6 auf). Die Zuordnung Lernkarte -> Regel
-- (Erklärkarte, Rückfall für Aufgaben ohne Regel) liegt NICHT in der Datenbank, sondern als Datei (inhalte/plan/regelbezug-lernkarten.json,
-- für den Client als statische Daten). Tests und Expeditionen bekommen kein „regelbezug“ in der Antwort (nur der Versuch speichert das Fehlbild).
-- Wiederholbar: ein zweiter Lauf ändert nichts.
-- Sperre: ALTER TABLE hält schule.versuch bis zum Ende der Transaktion (auch für Lesen) – nur in einer Nutzungspause einspielen.

select set_config('lock_timeout', '3s', true);

do $$ begin
  if to_regprocedure('schule.loesung_sicht(schule.aufgabe)') is null or to_regprocedure('schule.aufgabe_zaehlt(schule.aufgabe)') is null
     or to_regprocedure('schule.antwort_bewerten(schule.aufgabe, jsonb)') is null or to_regprocedure('schule.uebung_pruefen_intern(bigint, jsonb)') is null
  then raise exception 'RB-S: Voraussetzung fehlt (BD-S2, FT-S)'; end if;
end $$;

-- 1. Tabellen
create table if not exists schule.aufgabe_regel (
  aufgabe_id bigint primary key references schule.aufgabe(id) on delete cascade,
  regel text not null,
  am timestamptz not null default now(),
  constraint aufgabe_regel_kennung_check check (regel ~ '^(rr|id)\.[a-z0-9_.]+$')
);
create table if not exists schule.aufgabe_fehlbild (
  aufgabe_id bigint not null references schule.aufgabe(id) on delete cascade,
  nr smallint not null,
  art text not null,
  luecke smallint,
  wert text not null,
  beschreibung text not null,
  fehlbild text,
  regel text,
  am timestamptz not null default now(),
  primary key (aufgabe_id, nr),
  constraint aufgabe_fehlbild_nr_check check (nr >= 1),
  constraint aufgabe_fehlbild_art_check check (art in ('zahl', 'index', 'luecke', 'text')),
  constraint aufgabe_fehlbild_luecke_check check ((art = 'luecke') = (luecke is not null) and (luecke is null or luecke >= 1)),
  constraint aufgabe_fehlbild_wert_check check (case art when 'index' then wert ~ '^\d{1,4}$' when 'text' then length(wert) between 1 and 200
                                                     else wert ~ '^-?\d{1,15}(\.\d{1,15})?$' end),
  constraint aufgabe_fehlbild_beschreibung_check check (length(beschreibung) between 1 and 600),
  constraint aufgabe_fehlbild_kennung_check check (fehlbild is null or fehlbild ~ '^fb\.[a-z0-9_.]+$'),
  constraint aufgabe_fehlbild_regel_check check (regel is null or regel ~ '^(rr|id)\.[a-z0-9_.]+$')
);
create unique index if not exists aufgabe_fehlbild_schluessel on schule.aufgabe_fehlbild (aufgabe_id, art, coalesce(luecke, 0), wert);
alter table schule.aufgabe_regel enable row level security;     -- nur über die security-definer-Funktionen, wie die übrigen schule-Tabellen
alter table schule.aufgabe_fehlbild enable row level security;
revoke all on table schule.aufgabe_regel, schule.aufgabe_fehlbild from public, anon, authenticated;
comment on table schule.aufgabe_regel is 'RB-S: Regel-Kennung (kennungen.json) je Aufgabe; Quelle: Feld regel der Aufgaben-Datei (inhalte/mathe-profi/rollend-*)';
comment on table schule.aufgabe_fehlbild is 'RB-S: Fehlbilder je Aufgabe (nr = Platz in der Liste fehlbilder der Datei); erkannt von schule.fehlbild_finden, Rückmeldung in uebung_pruefen_intern.regelbezug';

-- Schutz wie aufgabe_schutz: freigegebene Einheit = unveränderlich (Einfügen bleibt erlaubt)
create or replace function schule.regelbezug_schutz()
 returns trigger language plpgsql set search_path to ''
as $function$
begin
  if exists (select 1 from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
              where a.id = old.aufgabe_id and e.status = 'freigegeben' and a.pool is distinct from 'expedition') then
    raise exception 'RB-S: Regel und Fehlbilder einer Aufgabe in einer freigegebenen Einheit sind unveränderlich (Berichtigung = neue Aufgabe)';
  end if;
  return coalesce(new, old);
end $function$;
do $$ begin
  if not exists (select 1 from pg_trigger where tgrelid = 'schule.aufgabe_regel'::regclass and tgname = 'aufgabe_regel_schutz') then
    create trigger aufgabe_regel_schutz before update or delete on schule.aufgabe_regel for each row execute function schule.regelbezug_schutz();
  end if;
  if not exists (select 1 from pg_trigger where tgrelid = 'schule.aufgabe_fehlbild'::regclass and tgname = 'aufgabe_fehlbild_schutz') then
    create trigger aufgabe_fehlbild_schutz before update or delete on schule.aufgabe_fehlbild for each row execute function schule.regelbezug_schutz();
  end if;
end $$;

-- 2. Erkennen
create or replace function schule.fehlbild_finden(a schule.aufgabe, p_antwort jsonb)
 returns smallint language plpgsql stable set search_path to ''
as $function$
declare s text; e text; v numeric; tol numeric; i int; n int := 0; v_nr smallint; v_soll jsonb;
begin
  if a.id is null or jsonb_typeof(p_antwort) is distinct from 'object' then return null; end if;
  if not exists (select 1 from schule.aufgabe_fehlbild f where f.aufgabe_id = a.id) then return null; end if;
  if a.antworttyp in ('auswahl', 'markierung') then
    if coalesce(p_antwort->>'index', '') !~ '^\d{1,4}$' or (p_antwort->>'index')::int = (a.loesung->>'index')::int then return null; end if;
    select min(f.nr), count(*) into v_nr, n from schule.aufgabe_fehlbild f
     where f.aufgabe_id = a.id and f.art = 'index' and f.wert::int = (p_antwort->>'index')::int;
  elsif a.antworttyp = 'luecken' then
    v_soll := a.loesung->'werte';
    if jsonb_typeof(p_antwort->'werte') is distinct from 'array' or jsonb_typeof(v_soll) is distinct from 'array'
       or jsonb_array_length(p_antwort->'werte') <> jsonb_array_length(v_soll) then return null; end if;
    for i in 0 .. jsonb_array_length(v_soll) - 1 loop
      s := replace(replace(regexp_replace(coalesce(p_antwort->'werte'->>i, ''), '[\s  ]', '', 'g'), '−', '-'), '–', '-');
      if left(s, 1) = '+' then s := substr(s, 2); end if;
      if s !~ '^-?\d{1,15}$' then return null; end if;
      if s::numeric <> (v_soll->>i)::numeric then   -- erste falsche Lücke: nur sie zählt
        select min(f.nr), count(*) into v_nr, n from schule.aufgabe_fehlbild f
         where f.aufgabe_id = a.id and f.art = 'luecke' and f.luecke = i + 1 and f.wert::numeric = s::numeric;
        exit;
      end if;
    end loop;
  elsif a.antworttyp = 'text' then
    s := upper(regexp_replace(coalesce(p_antwort->>'wert', ''), '[\s  ]', '', 'g'));
    if s = '' or s = upper(a.loesung->>'text') then return null; end if;
    select min(f.nr), count(*) into v_nr, n from schule.aufgabe_fehlbild f
     where f.aufgabe_id = a.id and f.art = 'text' and upper(regexp_replace(f.wert, '[\s  ]', '', 'g')) = s;
  elsif a.antworttyp = 'zahl' then
    s := regexp_replace(coalesce(p_antwort->>'wert', ''), '[\s  ]', '', 'g');
    if s = '' or position('.' in s) > 0 then return null; end if;
    e := a.loesung->>'einheit';
    if e is not null then s := replace(s, e, ''); end if;
    s := replace(replace(s, '−', '-'), ',', '.');
    if s !~ '^-?\d{1,15}(\.\d{1,15})?$' then return null; end if;
    v := s::numeric;
    tol := greatest(1e-9, coalesce((a.loesung->>'toleranz')::numeric, 0));
    if abs(v - (a.loesung->>'wert')::numeric) <= tol then return null; end if;
    select min(f.nr), count(*) into v_nr, n from schule.aufgabe_fehlbild f
     where f.aufgabe_id = a.id and f.art = 'zahl' and abs(f.wert::numeric - v) <= tol;
  end if;
  return case when n = 1 then v_nr end;
exception when others then
  return null;   -- die Bewertung darf an der Fehlbild-Suche nie scheitern
end $function$;
comment on function schule.fehlbild_finden(schule.aufgabe, jsonb) is 'RB-S: nr des Fehlbilds, das die (falsche) Antwort zeigt; null bei richtig, Formatfehler, keinem oder mehr als einem Treffer. Lücken: nur die erste falsche Lücke';

-- 3. Rückmeldung
create or replace function schule.regelbezug_antwort(a schule.aufgabe, p_antwort jsonb, p_richtig boolean, p_endgueltig boolean)
 returns jsonb language sql stable set search_path to ''
as $function$
  select case when p_richtig is distinct from false or a.id is null then null else
    nullif(jsonb_strip_nulls(jsonb_build_object(
      'regel', (select r.regel from schule.aufgabe_regel r where r.aufgabe_id = a.id),
      'fehlbild', f.fehlbild, 'fehlbild_nr', f.nr, 'fehlbild_regel', f.regel, 'text', f.beschreibung)), '{}'::jsonb) end
    from (select case when p_endgueltig then schule.fehlbild_finden(a, p_antwort) end nr) k
    left join schule.aufgabe_fehlbild f on f.aufgabe_id = a.id and f.nr = k.nr;
$function$;
comment on function schule.regelbezug_antwort(schule.aufgabe, jsonb, boolean, boolean) is 'RB-S: Feld regelbezug der Bewertungsantwort {regel, fehlbild, fehlbild_nr, fehlbild_regel, text}; null bei richtig/ohne Daten; nicht endgültig: nur regel';

-- 5. Versuch: erkanntes Fehlbild
alter table schule.versuch add column if not exists fehlbild_nr smallint;
alter table schule.versuch add column if not exists fehlbild text;
comment on column schule.versuch.fehlbild_nr is 'RB-S: nr des erkannten Fehlbilds (schule.aufgabe_fehlbild), gesetzt beim Speichern einer falschen Antwort; leer = keins erkannt oder Versuch von vor RB-S';
comment on column schule.versuch.fehlbild is 'RB-S: Kennung (fb.…) des erkannten Fehlbilds, falls das Fehlbild eine hat';

create or replace function schule.versuch_fehlbild()
 returns trigger language plpgsql set search_path to ''
as $function$
declare a schule.aufgabe; f schule.aufgabe_fehlbild;
begin
  if new.richtig is distinct from false or new.fehlbild_nr is not null then return new; end if;
  begin
    select * into a from schule.aufgabe where id = new.aufgabe_id;
    select * into f from schule.aufgabe_fehlbild x where x.aufgabe_id = a.id and x.nr = schule.fehlbild_finden(a, new.antwort);
    if f.nr is not null then new.fehlbild_nr := f.nr; new.fehlbild := f.fehlbild; end if;
  exception when others then null;   -- nie den Versuch abweisen
  end;
  return new;
end $function$;
do $$ begin
  if not exists (select 1 from pg_trigger where tgrelid = 'schule.versuch'::regclass and tgname = 'versuch_fehlbild') then
    create trigger versuch_fehlbild before insert on schule.versuch for each row execute function schule.versuch_fehlbild();
  end if;
end $$;

-- 6. Lesen für „Was wackelt“
create or replace function schule.versuch_regelbezug(v schule.versuch)
 returns jsonb language sql stable set search_path to ''
as $function$
  with n as (select coalesce(v.fehlbild_nr, case when not v.richtig then (select schule.fehlbild_finden(x, v.antwort) from schule.aufgabe x where x.id = v.aufgabe_id) end) nr)
  select case when v.richtig then null else nullif(jsonb_strip_nulls(jsonb_build_object(
    'regel', (select r.regel from schule.aufgabe_regel r where r.aufgabe_id = v.aufgabe_id),
    'fehlbild', f.fehlbild, 'fehlbild_nr', f.nr, 'fehlbild_regel', f.regel, 'text', f.beschreibung,
    'nachtraeglich', case when v.fehlbild_nr is null and f.nr is not null then true end)), '{}'::jsonb) end
    from n left join schule.aufgabe_fehlbild f on f.aufgabe_id = v.aufgabe_id and f.nr = n.nr;
$function$;

-- 7. Probe-Antwort zu einem Fehlbild (für die Prüfungen der Pakete)
create or replace function schule.fehlbild_probeantwort(a schule.aufgabe, p_art text, p_luecke int, p_wert text)
 returns jsonb language sql immutable set search_path to ''
as $function$
  select case p_art
    when 'index' then jsonb_build_object('index', p_wert::int)
    when 'text' then jsonb_build_object('wert', p_wert)
    when 'zahl' then jsonb_build_object('wert', replace(p_wert, '.', ','))
    when 'luecke' then jsonb_build_object('werte', (select jsonb_agg(case when o = p_luecke then to_jsonb(p_wert::numeric) else x end order by o)
                                                     from jsonb_array_elements(a.loesung->'werte') with ordinality t(x, o)))
  end;
$function$;

revoke all on function schule.regelbezug_schutz(), schule.fehlbild_finden(schule.aufgabe, jsonb), schule.regelbezug_antwort(schule.aufgabe, jsonb, boolean, boolean),
  schule.versuch_fehlbild(), schule.versuch_regelbezug(schule.versuch), schule.fehlbild_probeantwort(schule.aufgabe, text, integer, text)
  from public, anon, authenticated;

-- 4. Text-Patch uebung_pruefen_intern. Zustände je Eintrag:
--   alt    = alt steht genau so oft da wie erwartet, neu gar nicht  -> ersetzen
--   fertig = alt steht nicht mehr da, neu genau so oft wie erwartet -> nichts tun
--   sonst  -> Abbruch. Auch Abbruch, wenn manche Stellen alt und andere fertig sind.
do $$
declare
  f record; e jsonb; d text; d0 text; n_alt int; n_neu int; soll int; z_alt int; z_fertig int;
  zaehle constant text := 'select (length($1) - length(replace($1, $2, ''''))) / length($2)';
  plan constant jsonb := jsonb_build_array(
    jsonb_build_object('f', 'schule.uebung_pruefen_intern(bigint, jsonb)', 'p', jsonb_build_array(
      jsonb_build_array($a$'grund', b->>'grund', 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis', 'loesung', schule.loesung_sicht(a)$a$,
                        $a$'grund', b->>'grund', 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis', 'regelbezug', schule.regelbezug_antwort(a, p_daten->'antwort', (b->>'richtig')::boolean, true), 'loesung', schule.loesung_sicht(a)$a$, 4),
      jsonb_build_array($a$'richtig', false, 'nochmal', true, 'grund', b->>'grund', 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis'));$a$,
                        $a$'richtig', false, 'nochmal', true, 'grund', b->>'grund', 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis', 'regelbezug', schule.regelbezug_antwort(a, p_daten->'antwort', false, false)));$a$, 1),
      jsonb_build_array($a$'wiederholt', true) || jsonb_strip_nulls(jsonb_build_object('verletzt', b->>'verletzt', 'hinweis', b->>'hinweis'));$a$,
                        $a$'wiederholt', true) || jsonb_strip_nulls(jsonb_build_object('verletzt', b->>'verletzt', 'hinweis', b->>'hinweis', 'regelbezug', schule.regelbezug_antwort(a, v_alt.antwort, v_alt.richtig, true)));$a$, 1),
      jsonb_build_array($a$'nochmal', true, 'wiederholt', true, 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis'));$a$,
                        $a$'nochmal', true, 'wiederholt', true, 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis', 'regelbezug', schule.regelbezug_antwort(a, v_alt.antwort, false, false)));$a$, 1))));
begin
  for f in select x->>'f' as name, x->'p' as p from jsonb_array_elements(plan) x loop
    if to_regprocedure(f.name) is null then raise exception 'RB-S: Funktion % fehlt', f.name; end if;
    d0 := pg_get_functiondef(to_regprocedure(f.name)); d := d0; z_alt := 0; z_fertig := 0;
    for e in select * from jsonb_array_elements(f.p) loop
      soll := (e->>2)::int;
      execute zaehle into n_alt using d, e->>0;
      execute zaehle into n_neu using d, e->>1;
      if n_alt = soll and n_neu = 0 then d := replace(d, e->>0, e->>1); z_alt := z_alt + 1;
      elsif n_alt = 0 and n_neu = soll then z_fertig := z_fertig + 1;
      else raise exception 'RB-S: % ist weder im alten noch im fertigen Zustand (Stelle „%…“: alt %, neu %, erwartet %)', f.name, left(e->>0, 50), n_alt, n_neu, soll;
      end if;
    end loop;
    if z_alt > 0 and z_fertig > 0 then raise exception 'RB-S: % ist halb umgestellt (% Stellen alt, % fertig)', f.name, z_alt, z_fertig; end if;
    if d is distinct from d0 then execute d; end if;
  end loop;
end $$;
$rbmig$::text as sql, $rbmig$do $x$
declare k bigint := (select id from schule.lernender where ist_test order by id limit 1); a schule.aufgabe; o jsonb := '{}'; r jsonb;
begin
  select * into a from schule.aufgabe where id = (select min(xa.id) from schule.aufgabe xa join schule.einheit xe on xe.id = xa.einheit_id where xa.pool = 'uebung' and xa.antworttyp = 'zahl' and xa.freigegeben and xe.status = 'freigegeben' and (xa.loesung->>'wert')::numeric <> 987654 and xa.loesung->>'einheit' is null);
  if k is null or a.id is null then raise exception 'RB-S: Testkind oder Vergleichsaufgabe fehlt'; end if;
  begin
    o := o || jsonb_build_object('falsch-1', pg_temp.rb_ant(k, a.id, '987654', 1, 'rb-p-1'));
    o := o || jsonb_build_object('falsch-1-wdh', pg_temp.rb_ant(k, a.id, '987654', 1, 'rb-p-1'));
    o := o || jsonb_build_object('falsch-2', pg_temp.rb_ant(k, a.id, '987654', 2, 'rb-p-2'));
    o := o || jsonb_build_object('falsch-2-wdh', pg_temp.rb_ant(k, a.id, '987654', 2, 'rb-p-2'));
    o := o || jsonb_build_object('anders', pg_temp.rb_ant(k, a.id, '123457', null, 'rb-p-3'));
    o := o || jsonb_build_object('versuche', (select jsonb_agg(jsonb_build_array(v.client_id, to_jsonb(v) -> 'fehlbild_nr', to_jsonb(v) -> 'fehlbild') order by v.id)
                                               from schule.versuch v where v.lernender_id = k and v.client_id like 'rb-p-%'));
    -- Wirkung der übrigen Trigger (versuch_hilfe_merken, versuch_karte, versuch_lerntag, versuch_misch_verfall, versuch_sterne): vor/nach gleich
    o := o || jsonb_build_object('zeilen', (select jsonb_agg(to_jsonb(v) - 'id' - 'am' - 'fehlbild_nr' - 'fehlbild' order by v.id)
                                             from schule.versuch v where v.lernender_id = k and v.client_id like 'rb-p-%'));
    if to_regclass('schule.karte_stand') is not null then
      execute 'select to_jsonb(x) from schule.karte_stand x where x.lernender_id = $1 and x.einheit_id = $2 and x.lernziel = $3' into r using k, a.einheit_id, a.variante_gruppe;
      o := o || jsonb_build_object('karte', r);
    end if;
    if to_regclass('schule.sterne') is not null then
      execute 'select jsonb_agg(to_jsonb(x) - ''id'' order by x.grund, x.bezug) from schule.sterne x where x.lernender_id = $1' into r using k;
      o := o || jsonb_build_object('sterne', r);
    end if;
    raise exception using errcode = 'RB999', message = 'zurueck';
  exception when sqlstate 'RB999' then null;
  end;
  begin
    o := o || jsonb_build_object('richtig', pg_temp.rb_ant(k, a.id, replace(a.loesung->>'wert', '.', ','), 1, 'rb-p-4'));
    raise exception using errcode = 'RB999', message = 'zurueck';
  exception when sqlstate 'RB999' then null;
  end;
  insert into rb_aus values ('PHASE', o);
end $x$;$rbmig$::text as lauf;
create function pg_temp.rb_ant(p_k bigint, p_id bigint, p_wert text, p_anlauf int, p_cid text) returns jsonb language plpgsql as $f$
begin
  return schule.uebung_pruefen_wd(p_k, jsonb_build_object('aufgabe_id', p_id, 'client_id', p_cid, 'antwort', jsonb_build_object('wert', p_wert))
         || case when p_anlauf is null then '{}'::jsonb else jsonb_build_object('anlauf', p_anlauf) end);
end $f$;
create temp table rb_aus (phase text, o jsonb) on commit drop;
create temp table rb_stand on commit drop as select row((select md5(coalesce(string_agg(md5(ag::text), '' order by ag.id), '')) from schule.aufgabe ag), (select count(*) from schule.versuch), (select coalesce(max(id), 0) from schule.versuch))::text m;
create temp table rb_trg on commit drop as select (select string_agg(tgrelid::regclass::text || ':' || tgname || ':' || tgtype::text || ':' || tgenabled::text || ':' || tgfoid::regproc::text, ',' order by tgrelid::regclass::text, tgname) from pg_trigger where tgrelid in ('schule.versuch'::regclass, 'schule.aufgabe'::regclass) and not tgisinternal and tgname <> 'versuch_fehlbild') t;
do $p$ begin execute replace((select lauf from rb_mig), 'PHASE', 'vor'); end $p$;
do $p$ begin execute (select sql from rb_mig); end $p$;
create temp table rb_def on commit drop as select 1 lauf, (select md5(string_agg(coalesce(pg_get_functiondef(to_regprocedure(f)), 'fehlt'), '#' order by f)) from unnest(array['schule.regelbezug_schutz()', 'schule.fehlbild_finden(schule.aufgabe, jsonb)', 'schule.regelbezug_antwort(schule.aufgabe, jsonb, boolean, boolean)', 'schule.versuch_fehlbild()', 'schule.versuch_regelbezug(schule.versuch)', 'schule.fehlbild_probeantwort(schule.aufgabe, text, integer, text)', 'schule.uebung_pruefen_intern(bigint, jsonb)']) f) d, (select md5(string_agg(s.x, '#' order by s.x)) from (
       select 'trg:' || tgrelid::regclass::text || ':' || tgname from pg_trigger where tgname in ('aufgabe_regel_schutz', 'aufgabe_fehlbild_schutz', 'versuch_fehlbild', 'aufgabe_schutz')
       union all select 'idx:' || indexrelid::regclass::text from pg_index where indrelid in ('schule.aufgabe_regel'::regclass, 'schule.aufgabe_fehlbild'::regclass)
       union all select 'con:' || conname || ':' || pg_get_constraintdef(oid) from pg_constraint where conrelid in ('schule.aufgabe_regel'::regclass, 'schule.aufgabe_fehlbild'::regclass)
       union all select 'col:' || attname || ':' || format_type(atttypid, atttypmod) || ':' || attnotnull from pg_attribute where attrelid = 'schule.versuch'::regclass and attname in ('fehlbild_nr', 'fehlbild') and not attisdropped) s(x)) o;
do $p$ begin execute (select sql from rb_mig); end $p$;
insert into rb_def select 2, (select md5(string_agg(coalesce(pg_get_functiondef(to_regprocedure(f)), 'fehlt'), '#' order by f)) from unnest(array['schule.regelbezug_schutz()', 'schule.fehlbild_finden(schule.aufgabe, jsonb)', 'schule.regelbezug_antwort(schule.aufgabe, jsonb, boolean, boolean)', 'schule.versuch_fehlbild()', 'schule.versuch_regelbezug(schule.versuch)', 'schule.fehlbild_probeantwort(schule.aufgabe, text, integer, text)', 'schule.uebung_pruefen_intern(bigint, jsonb)']) f), (select md5(string_agg(s.x, '#' order by s.x)) from (
       select 'trg:' || tgrelid::regclass::text || ':' || tgname from pg_trigger where tgname in ('aufgabe_regel_schutz', 'aufgabe_fehlbild_schutz', 'versuch_fehlbild', 'aufgabe_schutz')
       union all select 'idx:' || indexrelid::regclass::text from pg_index where indrelid in ('schule.aufgabe_regel'::regclass, 'schule.aufgabe_fehlbild'::regclass)
       union all select 'con:' || conname || ':' || pg_get_constraintdef(oid) from pg_constraint where conrelid in ('schule.aufgabe_regel'::regclass, 'schule.aufgabe_fehlbild'::regclass)
       union all select 'col:' || attname || ':' || format_type(atttypid, atttypmod) || ':' || attnotnull from pg_attribute where attrelid = 'schule.versuch'::regclass and attname in ('fehlbild_nr', 'fehlbild') and not attisdropped) s(x));
do $p$ begin execute replace((select lauf from rb_mig), 'PHASE', 'nach'); end $p$;
create temp table rb_bericht (b jsonb) on commit drop;
do $p$
declare
  fehler text[] := '{}'; k bigint := (select id from schule.lernender where ist_test order by id limit 1); a schule.aufgabe; aw schule.aufgabe; al schule.aufgabe; r jsonb; vor jsonb; nach jsonb; x text; n int; d text;
  bericht jsonb := '{}';
begin
  select * into a from schule.aufgabe where id = (select min(xa.id) from schule.aufgabe xa join schule.einheit xe on xe.id = xa.einheit_id where xa.pool = 'uebung' and xa.antworttyp = 'zahl' and xa.freigegeben and xe.status = 'freigegeben' and (xa.loesung->>'wert')::numeric <> 987654 and xa.loesung->>'einheit' is null);
  select * into aw from schule.aufgabe where id = (select min(xa.id) from schule.aufgabe xa join schule.einheit xe on xe.id = xa.einheit_id where xa.pool = 'uebung' and xa.antworttyp = 'auswahl' and xa.freigegeben and xe.status = 'freigegeben');
  select * into al from schule.aufgabe where id = (select min(xa.id) from schule.aufgabe xa join schule.einheit xe on xe.id = xa.einheit_id where xa.pool = 'uebung' and xa.antworttyp = 'luecken' and xa.freigegeben and xe.status = 'freigegeben');
  -- zweiter Lauf ändert nichts
  if (select count(distinct rb_def.d) from rb_def) <> 1 or (select count(distinct rb_def.o) from rb_def) <> 1 then fehler := fehler || ('zweiter Lauf hat Definitionen oder Objekte geändert')::text; end if;
  if (select count(*) from pg_trigger where tgname in ('aufgabe_regel_schutz', 'aufgabe_fehlbild_schutz', 'versuch_fehlbild')) <> 3 then fehler := fehler || ('Trigger fehlen oder doppelt')::text; end if;
  if (select count(*) from pg_trigger where tgrelid = 'schule.aufgabe'::regclass and tgname = 'aufgabe_schutz' and tgenabled <> 'D') <> 1 then fehler := fehler || ('aufgabe_schutz fehlt oder ist aus')::text; end if;
  -- Rechte
  for x in select unnest(array['schule.aufgabe_regel', 'schule.aufgabe_fehlbild']) loop
    if not (select relrowsecurity from pg_class where oid = x::regclass) then fehler := fehler || (x || ': RLS aus')::text; end if;
    if exists (select 1 from pg_policy where polrelid = x::regclass) then fehler := fehler || (x || ': hat eine Policy')::text; end if;
    if has_table_privilege('anon', x, 'select') or has_table_privilege('authenticated', x, 'select') or has_table_privilege('authenticated', x, 'insert') then fehler := fehler || (x || ': App-Rollen haben Rechte')::text; end if;
  end loop;
  for x in select unnest(array['schule.regelbezug_schutz()', 'schule.fehlbild_finden(schule.aufgabe, jsonb)', 'schule.regelbezug_antwort(schule.aufgabe, jsonb, boolean, boolean)', 'schule.versuch_fehlbild()', 'schule.versuch_regelbezug(schule.versuch)', 'schule.fehlbild_probeantwort(schule.aufgabe, text, integer, text)']) loop
    if has_function_privilege('anon', x, 'execute') or has_function_privilege('authenticated', x, 'execute') then fehler := fehler || (x || ': für App-Rollen aufrufbar')::text; end if;
  end loop;
  -- Gegenprobe Rolle: authenticated hat live KEIN usage auf schule – damit die Probe nicht aus diesem Grund besteht, bekommt die Rolle es hier
  -- vorübergehend (Untertransaktion, wird zurückgerollt). Dann muss das Lesen an der TABELLE scheitern.
  for x in select unnest(array['aufgabe_fehlbild', 'aufgabe_regel']) loop
    begin
      grant usage on schema schule to authenticated;
      execute 'set local role authenticated';
      execute format('select count(*) from schule.%I', x);
      fehler := fehler || ('authenticated kann schule.' || x || ' lesen')::text;
      raise exception using errcode = 'RB999', message = 'zurueck';
    exception when sqlstate 'RB999' then null;
      when insufficient_privilege then
        if position(x in sqlerrm) = 0 or position('schema' in sqlerrm) > 0 then fehler := fehler || ('Gegenprobe Rolle aus dem falschen Grund: ' || sqlerrm)::text; end if;
      when others then fehler := fehler || ('Gegenprobe Rolle: ' || sqlerrm)::text;
    end;
  end loop;
  if has_schema_privilege('authenticated', 'schule', 'usage') then bericht := bericht || '{"hinweis_usage": "authenticated hat usage auf schule"}'::jsonb; end if;
  -- Trigger auf schule.versuch: versuch_fehlbild läuft als ERSTER BEFORE-INSERT-Trigger (Namensreihenfolge, vor versuch_hilfe_merken);
  -- alle übrigen Trigger (auch die AFTER-Trigger versuch_karte, versuch_lerntag, versuch_misch_verfall, versuch_sterne) unverändert
  if (select string_agg(tgname, ',' order by tgname) from pg_trigger where tgrelid = 'schule.versuch'::regclass and not tgisinternal
        and (tgtype & 2) <> 0 and (tgtype & 4) <> 0 and (tgtype & 1) <> 0) not like 'versuch_fehlbild%' then
    fehler := fehler || ('versuch_fehlbild ist nicht der erste BEFORE-INSERT-Trigger: ' || (select string_agg(tgname, ',' order by tgname) from pg_trigger where tgrelid = 'schule.versuch'::regclass and not tgisinternal and (tgtype & 2) <> 0))::text;
  end if;
  if exists (select 1 from pg_trigger where tgrelid = 'schule.versuch'::regclass and tgname = 'versuch_hilfe_merken') and 'versuch_fehlbild' > 'versuch_hilfe_merken' then
    fehler := fehler || ('Reihenfolge versuch_fehlbild/versuch_hilfe_merken')::text; end if;
  if (select t from rb_trg) is distinct from (select string_agg(tgrelid::regclass::text || ':' || tgname || ':' || tgtype::text || ':' || tgenabled::text || ':' || tgfoid::regproc::text, ',' order by tgrelid::regclass::text, tgname) from pg_trigger where tgrelid in ('schule.versuch'::regclass, 'schule.aufgabe'::regclass) and not tgisinternal and tgname <> 'versuch_fehlbild') then fehler := fehler || ('andere Trigger auf versuch/aufgabe verändert')::text; end if;
  bericht := bericht || jsonb_build_object('trigger_versuch', (select string_agg(tgname, ',' order by tgname) from pg_trigger where tgrelid = 'schule.versuch'::regclass and not tgisinternal));
  if current_user = 'authenticated' then fehler := fehler || ('Rolle nicht zurückgesetzt')::text; end if;
  -- nur erwartete Funktionen lesen die neuen Tabellen / rufen die Rückmeldung
  for x in select p.oid::regprocedure::text from pg_proc p join pg_namespace s on s.oid = p.pronamespace
            where s.nspname not in ('pg_catalog', 'information_schema') and p.prokind = 'f'
              and (p.prosrc like '%aufgabe_fehlbild%' or p.prosrc like '%regelbezug_antwort%' or p.prosrc like '%fehlbild_finden%' or p.prosrc like '%versuch_regelbezug%')
              and p.proname not in ('fehlbild_finden', 'regelbezug_antwort', 'regelbezug_schutz', 'uebung_pruefen_intern', 'versuch_fehlbild', 'versuch_regelbezug', 'wackelt_analyse', 'ww_fehlerart') and s.nspname <> 'pg_temp' and p.pronamespace <> pg_my_temp_schema() loop
    fehler := fehler || ('unerwarteter Leser der Fehlbilder: ' || x)::text;
  end loop;
  -- Bestand: ohne Daten gleiche Antworten
  select o into vor from rb_aus where phase = 'vor'; select o into nach from rb_aus where phase = 'nach';
  if vor - 'versuche' is distinct from nach - 'versuche' then fehler := fehler || ('Bestand antwortet anders: vor ' || (vor - 'versuche')::text || ' nach ' || (nach - 'versuche')::text)::text; end if;
  if exists (select 1 from jsonb_array_elements(nach->'versuche') v where v->1 <> 'null'::jsonb) then fehler := fehler || ('Versuch ohne Daten trägt ein Fehlbild')::text; end if;
  bericht := bericht || jsonb_build_object('bestand_gleich', vor - 'versuche' = nach - 'versuche');
  -- mit Probe-Daten
  begin
    insert into schule.aufgabe_regel (aufgabe_id, regel) values (a.id, 'rr.waage');
    insert into schule.aufgabe_fehlbild (aufgabe_id, nr, art, wert, beschreibung, fehlbild, regel) values (a.id, 2, 'zahl', '987654', 'RB-Probe Beschreibung', 'fb.probe.eins', 'rr.plusminus');
    begin   -- richtig (eigene Untertransaktion, damit die Karte wie im Vorher-Lauf steht)
      r := pg_temp.rb_ant(k, a.id, replace(a.loesung->>'wert', '.', ','), 1, 'rb-q-4');
      if r ? 'regelbezug' or r is distinct from (select o->'richtig' from rb_aus where phase = 'vor') then fehler := fehler || ('richtig: ' || r::text)::text; end if;
      raise exception using errcode = 'RB999', message = 'zurueck';
    exception when sqlstate 'RB999' then null;
    end;
    r := pg_temp.rb_ant(k, a.id, '987654', 1, 'rb-q-1');
    if r->'regelbezug' is distinct from '{"regel": "rr.waage"}'::jsonb or r->>'nochmal' is distinct from 'true' then fehler := fehler || ('1. Anlauf: ' || r::text)::text; end if;
    if (select (v.fehlbild_nr, v.fehlbild) is distinct from (2::smallint, 'fb.probe.eins') from schule.versuch v where v.lernender_id = k and v.client_id = 'rb-q-1') then fehler := fehler || ('1. Anlauf: Fehlbild nicht im Versuch')::text; end if;
    r := pg_temp.rb_ant(k, a.id, '987654', 1, 'rb-q-1');
    if r->'regelbezug' is distinct from '{"regel": "rr.waage"}'::jsonb then fehler := fehler || ('Wiederholung 1. Anlauf: ' || r::text)::text; end if;
    r := pg_temp.rb_ant(k, a.id, '987 654', 2, 'rb-q-2');
    if r->'regelbezug' is distinct from '{"regel": "rr.waage", "fehlbild": "fb.probe.eins", "fehlbild_nr": 2, "fehlbild_regel": "rr.plusminus", "text": "RB-Probe Beschreibung"}'::jsonb
       or r->'loesung' is null then fehler := fehler || ('2. Anlauf: ' || r::text)::text; end if;
    bericht := bericht || jsonb_build_object('beispiel_antwort', r - 'loesung' - 'loesungsweg' - 'karte');
    if pg_temp.rb_ant(k, a.id, '987654', 2, 'rb-q-2')->'regelbezug' is distinct from r->'regelbezug' then fehler := fehler || ('Wiederholung 2. Anlauf antwortet anders')::text; end if;
    r := pg_temp.rb_ant(k, a.id, '123457', null, 'rb-q-3');
    if r->'regelbezug' is distinct from '{"regel": "rr.waage"}'::jsonb then fehler := fehler || ('andere falsche Antwort: ' || r::text)::text; end if;
    if (select v.fehlbild_nr from schule.versuch v where v.lernender_id = k and v.client_id = 'rb-q-3') is not null then fehler := fehler || ('andere falsche Antwort: Fehlbild im Versuch')::text; end if;
    if (select schule.versuch_regelbezug(v) from schule.versuch v where v.lernender_id = k and v.client_id = 'rb-q-2') is distinct from r->'regelbezug' || '{"fehlbild": "fb.probe.eins", "fehlbild_nr": 2, "fehlbild_regel": "rr.plusminus", "text": "RB-Probe Beschreibung"}'::jsonb then
      fehler := fehler || ('versuch_regelbezug passt nicht')::text; end if;
    if position('RB-Probe' in schule.aufgabe_anzeige(a, true)::text) > 0 then fehler := fehler || ('aufgabe_anzeige zeigt die Beschreibung')::text; end if;
    -- doppelter Schlüssel
    begin
      insert into schule.aufgabe_fehlbild (aufgabe_id, nr, art, wert, beschreibung) values (a.id, 3, 'zahl', '987654', 'doppelt');
      fehler := fehler || ('doppelter Schlüssel angenommen')::text;
    exception when unique_violation then null;
    end;
    -- Schutz
    begin update schule.aufgabe_fehlbild set beschreibung = beschreibung where aufgabe_id = a.id; fehler := fehler || ('UPDATE Fehlbild angenommen')::text;
    exception when others then if position('unveränderlich' in sqlerrm) = 0 then fehler := fehler || ('UPDATE Fehlbild: ' || sqlerrm)::text; end if; end;
    begin delete from schule.aufgabe_regel where aufgabe_id = a.id; fehler := fehler || ('DELETE Regel angenommen')::text;
    exception when others then if position('unveränderlich' in sqlerrm) = 0 then fehler := fehler || ('DELETE Regel: ' || sqlerrm)::text; end if; end;
    begin update schule.aufgabe set tipp = tipp where id = a.id; fehler := fehler || ('aufgabe_schutz greift nicht mehr')::text;
    exception when others then if position('unveränderlich' in sqlerrm) = 0 then fehler := fehler || ('aufgabe_schutz: ' || sqlerrm)::text; end if; end;
    -- Auswahl
    if aw.id is not null then
      insert into schule.aufgabe_fehlbild (aufgabe_id, nr, art, wert, beschreibung) values (aw.id, 1, 'index', (((aw.loesung->>'index')::int + 1) % jsonb_array_length(aw.antworten))::text, 'RB-Probe Auswahl');
      if schule.fehlbild_finden(aw, jsonb_build_object('index', ((aw.loesung->>'index')::int + 1) % jsonb_array_length(aw.antworten))) is distinct from 1::smallint then fehler := fehler || ('Auswahl nicht erkannt')::text; end if;
      if schule.fehlbild_finden(aw, jsonb_build_object('index', (aw.loesung->>'index')::int)) is not null then fehler := fehler || ('Auswahl: richtige Option erkannt')::text; end if;
    end if;
    -- Lücken: nur die erste falsche Lücke
    if al.id is not null and jsonb_array_length(al.loesung->'werte') >= 2 then
      insert into schule.aufgabe_fehlbild (aufgabe_id, nr, art, luecke, wert, beschreibung) values (al.id, 1, 'luecke', 2, ((al.loesung->'werte'->>1)::numeric + 1)::text, 'RB-Probe Lücke');
      if schule.fehlbild_finden(al, schule.fehlbild_probeantwort(al, 'luecke', 2, ((al.loesung->'werte'->>1)::numeric + 1)::text)) is distinct from 1::smallint then fehler := fehler || ('Lücke 2 nicht erkannt')::text; end if;
      if schule.fehlbild_finden(al, jsonb_set(schule.fehlbild_probeantwort(al, 'luecke', 2, ((al.loesung->'werte'->>1)::numeric + 1)::text), '{werte,0}', to_jsonb((al.loesung->'werte'->>0)::numeric + 7))) is not null then
        fehler := fehler || ('Lücke 2 erkannt, obwohl Lücke 1 schon falsch')::text; end if;
      if schule.fehlbild_finden(al, jsonb_build_object('werte', al.loesung->'werte')) is not null then fehler := fehler || ('Lücken: richtige Antwort erkannt')::text; end if;
    end if;
    -- Unsinn
    if schule.fehlbild_finden(a, '"x"'::jsonb) is not null or schule.fehlbild_finden(a, '{"wert": "abc"}') is not null or schule.fehlbild_finden(a, null) is not null then fehler := fehler || ('Unsinn erkannt')::text; end if;
    raise exception using errcode = 'RB999', message = 'zurueck';
  exception
    when sqlstate 'RB999' then null;
    when others then fehler := fehler || ('Probe-Daten: ' || sqlerrm)::text;
  end;
  -- Mischstand: eine Stelle zurückgebaut -> Migration muss abbrechen
  begin
    d := pg_get_functiondef('schule.uebung_pruefen_intern(bigint, jsonb)'::regprocedure);
    execute replace(d, $q$'hinweis', b->>'hinweis', 'regelbezug', schule.regelbezug_antwort(a, p_daten->'antwort', false, false)));$q$, $q$'hinweis', b->>'hinweis'));$q$);
    begin
      execute (select sql from rb_mig);
      fehler := fehler || ('Mischstand nicht abgewiesen')::text;
    exception when others then if position('halb umgestellt' in sqlerrm) = 0 then fehler := fehler || ('Mischstand: ' || sqlerrm)::text; end if;
    end;
    raise exception using errcode = 'RB999', message = 'zurueck';
  exception
    when sqlstate 'RB999' then null;
    when others then fehler := fehler || ('Mischstand: ' || sqlerrm)::text;
  end;
  -- Ende: nichts an Aufgaben und Versuchen geändert, neue Tabellen leer
  if (select m from rb_stand) is distinct from (select row((select md5(coalesce(string_agg(md5(ag::text), '' order by ag.id), '')) from schule.aufgabe ag), (select count(*) from schule.versuch), (select coalesce(max(id), 0) from schule.versuch))::text) then fehler := fehler || ('Aufgaben oder Versuche verändert')::text; end if;
  if exists (select 1 from schule.aufgabe_regel) or exists (select 1 from schule.aufgabe_fehlbild) then fehler := fehler || ('neue Tabellen nicht leer')::text; end if;
  bericht := bericht || jsonb_build_object('basis_aufgabe', a.id, 'auswahl', aw.id, 'luecken', al.id, 'fehler', coalesce(array_length(fehler, 1), 0));
  insert into rb_bericht values (bericht);
  if array_length(fehler, 1) > 0 then raise exception 'RB-S ABBRUCH, alles zurückgerollt: %', array_to_string(fehler, ' | '); end if;
  raise notice 'RB-S eingespielt: %', (select b::text from rb_bericht);
end $p$;
