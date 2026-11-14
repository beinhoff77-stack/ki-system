-- W150 (Claude): Lehrplan-Übersicht für Eltern/Lehrer und Stand je Jahrgang für die Kinder.

-- Alle Themen mit Jahrgang je Schulart, Inhaltszustand und Stand je Kind (Eltern/Lehrer).
create or replace function api.schule_lehrplan_uebersicht(p_schluessel text, p_daten jsonb default null) returns jsonb
language plpgsql stable security definer set search_path to '' as $$
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  return jsonb_build_object('ok', true,
    'kinder', (select coalesce(jsonb_agg(jsonb_build_object('id', l.id, 'name', l.anzeigename, 'klasse', l.klasse, 'schulart', l.schulart) order by l.id), '[]'::jsonb)
               from schule.lernender l where l.aktiv and not l.ist_test),
    'themen', (select coalesce(jsonb_agg(x.j order by x.k, x.b, x.t), '[]'::jsonb) from (
      select k.reihenfolge k, b.reihenfolge b, coalesce(bt.reihenfolge, 0) * 1000 + t.reihenfolge t,
        jsonb_build_object('thema_id', t.id, 'titel', t.unterthema, 'gebiet', k.titel, 'ort', b.stadt, 'block_id', b.id,
          'jahrgang', schule.thema_jahrgang(t.id),
          'einheit', (select jsonb_build_object('id', e.id, 'status', e.status,
                        'karten', jsonb_array_length(coalesce(e.inhalt->'etappen','[]'::jsonb)),
                        'aufgaben', (select count(*) from schule.aufgabe a where a.einheit_id = e.id),
                        'neu', (select count(*) from schule.aufgabe a where a.einheit_id = e.id and not a.freigegeben))
                      from schule.einheit e where e.thema_id = t.id order by (e.status in ('geprueft','freigegeben')) desc, e.version desc limit 1),
          'stand', (select coalesce(jsonb_object_agg(l.id, schule.thema_stand(l.id, t.id)), '{}'::jsonb) from schule.lernender l where l.aktiv and not l.ist_test),
          'geplant', (select coalesce(jsonb_agg(r.lernender_id), '[]'::jsonb) from schule.route r where r.block_id = b.id and schule.ist_plan(r)),
          'rueckmeldungen', (select count(*) from schule.rueckmeldung m where (m.einheit_id in (select id from schule.einheit where thema_id = t.id) or m.block_id = b.id) and m.status in ('offen','in_arbeit'))) j
      from schule.thema t join schule.block_thema bt on bt.thema_id = t.id join schule.block b on b.id = bt.block_id
      left join schule.kontinent k on k.id = b.kontinent_id where t.fach = 'Mathematik') x));
end $$;
grant execute on function api.schule_lehrplan_uebersicht(text, jsonb) to council_mcp;
revoke all on function api.schule_lehrplan_uebersicht(text, jsonb) from public, anon, authenticated;

-- Konto: Stand der Zielschulart in der Klasse des Kindes (Themen gesamt / mit Inhalt / geschafft).
do $$
declare d text;
begin
  select pg_get_functiondef('schule.konto'::regproc) into d;
  d := replace(d, $x$    'lerntage', (select count(*) from schule.lerntag where lernender_id = p_lernender))$x$,
    $x$    'lerntage', (select count(*) from schule.lerntag where lernender_id = p_lernender),
    'jahrgang', (select jsonb_build_object('schulart', l.schulart, 'klasse', l.klasse,
                   'themen', count(t.id), 'mit_inhalt', count(t.id) filter (where schule.thema_stand(l.id, t.id) <> 'keine_einheit'),
                   'geschafft', count(t.id) filter (where schule.thema_stand(l.id, t.id) = 'erledigt'))
                 from schule.lernender l left join schule.thema t on t.fach = 'Mathematik' and (schule.thema_jahrgang(t.id)->>l.schulart)::int = l.klasse
                 where l.id = p_lernender group by l.schulart, l.klasse, l.id))$x$);
  if position('''jahrgang''' in d) = 0 then raise exception 'konto nicht angepasst'; end if;
  execute d;
end $$;
