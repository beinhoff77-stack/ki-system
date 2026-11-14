-- W150 (Claude): Themen-Datei (inhalte/themen/*.json, geprüft mit tools/inhalt_pruefen.py) als Entwurf einspielen.
-- Aufruf nur durch Claude nach Sebastians Okay:
--   select net.http_get('https://raw.githubusercontent.com/beinhoff77-stack/ki-system/<zweig>/inhalte/themen/<datei>.json');  -> id
--   select schule.einheit_importieren((select content::jsonb from net._http_response where id = <id>));
-- Legt nichts an, wenn das Thema schon eine Einheit hat. Status 'entwurf': sichtbar nur fürs Testkind und für Eltern/Lehrer („in Prüfung“).
create or replace function schule.einheit_importieren(p jsonb) returns jsonb
language plpgsql security definer set search_path to '' as $$
declare v_t bigint := (p->>'thema_id')::bigint; v_b bigint := (p->>'block_id')::bigint; v_e bigint; v_n int; v_soll int := jsonb_array_length(p->'aufgaben'); v_auf jsonb;
begin
  if not exists (select 1 from schule.thema t where t.id = v_t and t.schluessel = p->>'thema_schluessel') then
    raise exception 'thema_id % passt nicht zu Schlüssel %', v_t, p->>'thema_schluessel'; end if;
  if not exists (select 1 from schule.block_thema where thema_id = v_t and block_id = v_b) then
    raise exception 'thema_id % gehört nicht zu block_id %', v_t, v_b; end if;
  if exists (select 1 from schule.einheit where thema_id = v_t and status <> 'ersetzt') then
    raise exception 'Thema % hat schon eine Einheit', v_t; end if;
  if jsonb_array_length(coalesce(p->'inhalt'->'etappen', '[]'::jsonb)) < 3 or v_soll < 30 then raise exception 'Datei unvollständig'; end if;
  insert into schule.einheit (thema_id, block_id, status, inhalt, erstellt_von)
  values (v_t, v_b, 'entwurf',
          (p->'inhalt') || jsonb_build_object('quellen', coalesce(p->'inhalt'->'quellen', '{}'::jsonb) || jsonb_build_object('aufgaben',
            'Programmgesteuert erzeugt, Lösungen berechnet und nachgerechnet (' || coalesce(p->>'autor', '?') || '). Keine Schulbuchaufgaben.')),
          left(coalesce(p->>'autor', 'Claude'), 80))
  returning id into v_e;
  -- Reihenfolge wie bisher: Übung 1.., Test 101.., Korrektur 201.., Sicherung 301..
  select jsonb_agg((x.a - 'c' - 'zahl') || jsonb_build_object('r', x.basis + x.nr) order by x.ord) into v_auf from (
    select a, ord, case a->>'p' when 'uebung' then 0 when 'test' then 100 when 'korrektur' then 200 else 300 end as basis,
           row_number() over (partition by a->>'p' order by ord) as nr
    from jsonb_array_elements(p->'aufgaben') with ordinality q(a, ord)) x;
  v_n := schule.aufgaben_einfuegen(v_e, v_auf);
  if v_n <> v_soll then raise exception 'nur % von % Aufgaben eingefügt', v_n, v_soll; end if;
  return jsonb_build_object('einheit_id', v_e, 'thema', p->>'thema_schluessel', 'lernkarten', jsonb_array_length(p->'inhalt'->'etappen'), 'aufgaben', v_n);
end $$;
revoke all on function schule.einheit_importieren(jsonb) from public, anon, authenticated;
