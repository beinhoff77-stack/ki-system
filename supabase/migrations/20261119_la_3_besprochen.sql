-- Bau-Auftrag LA-3 (Lehrer-Aufbau, „Was wackelt“): „Besprochen ✓“ je Kind + Etappe, häufigster Fehler und „Kurz gesagt“ im Lernstand.
-- Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE. Lernstände bleiben unverändert.
--
-- Neu: Tabelle schule.besprochen (Kind, Einheit, Lernkarte, wer, wann) – eine Zeile je Kind + Etappe, „Besprochen“ erneut setzen überschreibt Zeit und Person.
--      Gilt, solange es danach keine neue endgültig falsche Antwort in dieser Etappe gibt (sonst holt die App die Etappe zurück nach „Zu tun“).
-- Setzen: über die bestehende Aktion schule_notiz_setzen mit {lernender_id, besprochen: {einheit_id, lernziel}} – keine neue Aktion in lernen-api.
--      Lehrer und Eltern dürfen setzen (ist_leiter); Zugriff auf das Kind wird geprüft.
-- schule_lernstand liefert je Etappe zusätzlich: regel („Kurz gesagt“), besprochen_am, besprochen_von (nur solange gültig),
--      fehler_gruende {grund: Anzahl} über alle falschen Antworten (grund wie beim Prüfen: vorzeichen, komma, vertauscht, gerundet, falsche_einheit),
--      und in fehler[] je Antwort grund.

create table if not exists schule.besprochen (
  lernender_id bigint not null references schule.lernender(id),
  einheit_id bigint not null references schule.einheit(id),
  lernziel text not null,
  von text not null,
  am timestamptz not null default now(),
  primary key (lernender_id, einheit_id, lernziel)
);
alter table schule.besprochen enable row level security; -- nur über die api-Funktionen (security definer), wie die übrigen schule-Tabellen
comment on table schule.besprochen is 'LA-3: Etappe mit dem Kind besprochen (Lehrer/Eltern); gilt bis zur nächsten endgültig falschen Antwort in dieser Etappe';

-- gültiges „besprochen“: es gibt danach keine endgültig falsche Antwort (1. Versuch mit zweiter Chance zählt nicht)
create or replace function schule.besprochen_aktiv(p_l bigint, p_e bigint, p_lz text)
 returns schule.besprochen language sql stable set search_path to ''
as $function$
  select b.* from schule.besprochen b
   where b.lernender_id = p_l and b.einheit_id = p_e and b.lernziel = p_lz
     and not exists (select 1 from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                      where v.lernender_id = p_l and a.einheit_id = p_e and a.variante_gruppe = p_lz and not v.richtig
                        and not (coalesce(v.anlauf, 0) = 1 and v.testsitzung_id is null) and v.am > b.am);
$function$;

-- häufigste Fehlerart je Etappe (aus dem Prüfen der gespeicherten Antwort, nichts erfunden)
create or replace function schule.fehler_gruende(p_l bigint, p_e bigint, p_lz text)
 returns jsonb language sql stable set search_path to ''
as $function$
  select coalesce(jsonb_object_agg(q.g, q.n), '{}'::jsonb) from (
    select schule.antwort_bewerten(a, v.antwort)->>'grund' g, count(*) n
      from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
     where v.lernender_id = p_l and a.einheit_id = p_e and a.variante_gruppe = p_lz and not v.richtig
     group by 1) q
   where q.g is not null;
$function$;

do $$
declare d text;
begin
  -- schule_notiz_setzen: Zweig „besprochen“
  d := pg_get_functiondef('api.schule_notiz_setzen(text, jsonb)'::regprocedure);
  if position('if length(v_t) not between 1 and 2000 then raise exception ''Notiz leer oder zu lang'' using errcode = ''P0001''; end if;' in d) = 0 then
    raise exception 'Stelle in schule_notiz_setzen nicht gefunden'; end if;
  d := replace(d, 'if length(v_t) not between 1 and 2000 then raise exception ''Notiz leer oder zu lang'' using errcode = ''P0001''; end if;',
    $r$if p_daten ? 'besprochen' then -- LA-3: Etappe besprochen
    perform schule.zugriff(p_schluessel, v_l);
    if nullif(p_daten->'besprochen'->>'einheit_id', '') is null or coalesce(p_daten->'besprochen'->>'lernziel', '') = '' then
      raise exception 'besprochen braucht einheit_id und lernziel' using errcode = 'P0001'; end if;
    insert into schule.besprochen(lernender_id, einheit_id, lernziel, von, am)
    values (v_l, (p_daten->'besprochen'->>'einheit_id')::bigint, p_daten->'besprochen'->>'lernziel',
            coalesce((select i.rolle || ':' || i.name from schule.lern_ich(p_schluessel) i where schule.ist_lern(p_schluessel)), 'eltern:App'), now())
    on conflict (lernender_id, einheit_id, lernziel) do update set von = excluded.von, am = excluded.am;
    return jsonb_build_object('ok', true, 'besprochen_am', now());
  end if;
  if length(v_t) not between 1 and 2000 then raise exception 'Notiz leer oder zu lang' using errcode = 'P0001'; end if;$r$);
  execute d;

  -- schule_lernstand: Kurz gesagt, besprochen, Fehlerarten
  d := pg_get_functiondef('api.schule_lernstand(text, jsonb)'::regprocedure);
  if position('''fehler'', (select coalesce(jsonb_agg(f.j), ''[]''::jsonb) from (' in d) = 0
     or position('''grafik'', a.frage->''grafik'', ''am'', v.am) j' in d) = 0 then raise exception 'Stellen in schule_lernstand nicht gefunden'; end if;
  d := replace(d, '''fehler'', (select coalesce(jsonb_agg(f.j), ''[]''::jsonb) from (',
    $r$'regel', et->>'regel',
              'besprochen_am', (schule.besprochen_aktiv(v_l, e.id, et->>'lernziel')).am, 'besprochen_von', (schule.besprochen_aktiv(v_l, e.id, et->>'lernziel')).von,
              'fehler_gruende', schule.fehler_gruende(v_l, e.id, et->>'lernziel'),
              'fehler', (select coalesce(jsonb_agg(f.j), '[]'::jsonb) from ($r$);
  d := replace(d, '''grafik'', a.frage->''grafik'', ''am'', v.am) j', '''grafik'', a.frage->''grafik'', ''am'', v.am, ''grund'', schule.antwort_bewerten(a, v.antwort)->>''grund'') j');
  execute d;
end $$;
