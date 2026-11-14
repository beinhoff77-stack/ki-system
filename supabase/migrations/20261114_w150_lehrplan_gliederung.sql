-- W150 (Claude): Lehrplan-Übersicht liefert je Thema Beschreibung und Gliederung (Titel der Lernkarten). Eingespielt 14.11.
do $$
declare d text;
begin
  select pg_get_functiondef('api.schule_lehrplan_uebersicht(text,jsonb)'::regprocedure) into d;
  d := replace(d, $x$'jahrgang', schule.thema_jahrgang(t.id),
          'einheit',$x$, $x$'jahrgang', schule.thema_jahrgang(t.id), 'beschreibung', t.beschreibung,
          'gliederung', (select coalesce((select jsonb_agg(x->>'titel') from jsonb_array_elements(coalesce(e.inhalt->'etappen','[]'::jsonb)) x), '[]'::jsonb)
                         from schule.einheit e where e.thema_id = t.id order by (e.status in ('geprueft','freigegeben')) desc, e.version desc limit 1),
          'einheit',$x$);
  if position('''gliederung''' in d) = 0 then raise exception 'lehrplan_uebersicht nicht angepasst'; end if;
  execute d;
end $$;
