-- „Flug geschafft“ als einmaliges Ereignis (AUFTRAEGE.md „Rückläufer 21.11. morgens“, Teil C; ChatGPT 896). Ersetzt den Entwurf mit schule.flug_fertig_nach
-- (nie eingespielt): Die Rekonstruktion aus alten Sitzungen war nicht verlässlich (heutige Pflichtliste; Lesen einer alten Sitzung schreibt false fest).
-- Neu: schule.flug_erstabschluss – je Kind und Flug höchstens eine Zeile, angelegt, wenn der Flug zum ersten Mal fertig ist.
--   flug_geschafft einer Sitzung = dieser Aufruf schließt sie ab (Flug-Test oder Verbessern), der Flug ist danach fertig, war es davor nicht,
--   UND die Zeile in flug_erstabschluss konnte neu angelegt werden (insert … on conflict do nothing → found).
--   Damit höchstens ein „Flug geschafft“ je Kind und Flug – unabhängig von später hinzugefügten Pflicht-Etappen (Nachtragstest), vom erneuten Lesen
--   alter Sitzungen und von gleichzeitig laufenden Sitzungen (der Primärschlüssel entscheidet).
-- Einmalig nachgetragen: alle Flüge, die JETZT fertig sind (alle Pflicht-Etappen nachgewiesen/korrigiert/gesichert), und alle mit einer abgeschlossenen
--   Flug-Test-/Verbessern-Sitzung mit flug_geschafft = true (sitzung_id = früheste solche Sitzung, sonst null).
-- Setzt 20261120_ab_s_flug_abschluss_einmal.sql voraus (eingespielt seit 20.11.). Nicht ausgeführt – der Haupt-Chat spielt ein.
-- Kein DROP, kein DELETE; Bestand: nur neue Tabelle + Nachtrag. Wiederholt ausführbar.

create table if not exists schule.flug_erstabschluss (
  lernender_id bigint not null references schule.lernender(id),
  einheit_id bigint not null references schule.einheit(id),
  sitzung_id bigint references schule.testsitzung(id),
  am timestamptz not null default now(),
  primary key (lernender_id, einheit_id)
);
comment on table schule.flug_erstabschluss is 'Flug erstmals geschafft (je Kind und Flug höchstens einmal); sitzung_id null = vor dem Einspielen fertig oder ohne Flug-Test fertig geworden';
alter table schule.flug_erstabschluss enable row level security;
revoke all on table schule.flug_erstabschluss from public, anon, authenticated;

-- Nachtrag (auch für den Rauchtest mit p_l = Testkind). Liefert die Zahl neu angelegter Zeilen.
create or replace function schule.flug_erstabschluss_nachtragen(p_l bigint default null)
 returns integer language plpgsql set search_path to ''
as $function$
declare v_n integer;
begin
  insert into schule.flug_erstabschluss (lernender_id, einheit_id, sitzung_id, am)
  select k.lernender_id, k.einheit_id, k.sitzung_id, coalesce(k.am, now())
    from (
      select f.lernender_id, f.einheit_id,
             (select min(x.id) from schule.testsitzung x where x.lernender_id = f.lernender_id and x.einheit_id = f.einheit_id
                and x.art in ('blocktest', 'korrektur') and x.status = 'abgeschlossen' and x.flug_geschafft) sitzung_id,
             (select min(x.abgeschlossen_am) from schule.testsitzung x where x.lernender_id = f.lernender_id and x.einheit_id = f.einheit_id
                and x.art in ('blocktest', 'korrektur') and x.status = 'abgeschlossen' and x.flug_geschafft) am
        from (select s.lernender_id, s.einheit_id from schule.lernziel_stand s
               where (p_l is null or s.lernender_id = p_l)
               group by s.lernender_id, s.einheit_id
              having bool_or(s.pflicht) and bool_and(not s.pflicht or s.status in ('nachgewiesen', 'korrigiert', 'gesichert'))
              union
              select ts.lernender_id, ts.einheit_id from schule.testsitzung ts
               where (p_l is null or ts.lernender_id = p_l) and ts.einheit_id is not null
                 and ts.art in ('blocktest', 'korrektur') and ts.status = 'abgeschlossen' and ts.flug_geschafft) f
    ) k
  on conflict (lernender_id, einheit_id) do nothing;
  get diagnostics v_n = row_count;
  return v_n;
end $function$;
revoke all on function schule.flug_erstabschluss_nachtragen(bigint) from public, anon, authenticated;

do $mig$
declare v_n integer;
begin
  v_n := schule.flug_erstabschluss_nachtragen(null);
  raise notice 'flug_erstabschluss: % Flüge nachgetragen', v_n;
end $mig$;

-- test_abschliessen_intern: flug_geschafft über flug_erstabschluss (die Stelle aus 20261120_ab_s_flug_abschluss_einmal.sql wird ersetzt)
do $mig$
declare d text; v_alt text; v_neu text;
begin
  d := pg_get_functiondef('schule.test_abschliessen_intern(bigint, jsonb)'::regprocedure);
  if position('schule.flug_erstabschluss' in d) > 0 then return; end if; -- schon eingespielt
  v_alt := $a$    t.flug_geschafft := v_jetzt and t.art in ('blocktest', 'korrektur') and coalesce(v_einheit_fertig, false) and not v_vorher_fertig
      and not exists (select 1 from schule.testsitzung x where x.lernender_id = p_lernender and x.einheit_id = t.einheit_id and x.art in ('blocktest', 'korrektur')
                       and x.status = 'abgeschlossen' and x.id < t.id and x.flug_geschafft is distinct from false);
$a$;
  v_neu := $a$    t.flug_geschafft := false;
    -- flug_erstabschluss (Rückläufer 21.11., C): je Kind und Flug höchstens einmal; war der Flug schon fertig, nur festhalten (sitzung_id null)
    if v_jetzt and t.art in ('blocktest', 'korrektur') and coalesce(v_einheit_fertig, false) then
      insert into schule.flug_erstabschluss (lernender_id, einheit_id, sitzung_id, am)
      values (p_lernender, t.einheit_id, case when v_vorher_fertig then null else t.id end, now())
      on conflict (lernender_id, einheit_id) do nothing;
      t.flug_geschafft := found and not v_vorher_fertig;
    end if;
$a$;
  if (length(d) - length(replace(d, v_alt, ''))) / length(v_alt) <> 1 then
    raise exception 'test_abschliessen_intern: Stelle nicht genau einmal gefunden (ist 20261120_ab_s_flug_abschluss_einmal.sql eingespielt?)'; end if;
  execute replace(d, v_alt, v_neu);
end $mig$;
