-- W150 (Claude): „Was wackelt?“ – Lernstand je Lernkarte für Eltern/Lehrer, mit den echten falschen Antworten.
create or replace function api.schule_lernstand(p_schluessel text, p_daten jsonb) returns jsonb
language plpgsql stable security definer set search_path to '' as $$
declare v_l bigint := nullif(p_daten->>'lernender_id','')::bigint; v_k schule.lernender;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  select * into v_k from schule.lernender where id = v_l and aktiv;
  if v_k.id is null then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  return jsonb_build_object('ok', true,
    'kind', jsonb_build_object('id', v_k.id, 'name', v_k.anzeigename, 'klasse', v_k.klasse),
    'lerntage', (select coalesce(jsonb_agg(d.datum order by d.datum desc), '[]'::jsonb) from (select distinct datum from schule.lerntag where lernender_id = v_l and datum > current_date - 28) d),
    'woche', (select jsonb_build_object('aufgaben', count(*), 'richtig', count(*) filter (where v.richtig), 'mit_tipp', count(*) filter (where v.hilfe > 0))
              from schule.versuch v where v.lernender_id = v_l and v.am > now() - interval '7 days'),
    'einheiten', (select coalesce(jsonb_agg(x.j order by x.zuletzt desc nulls last), '[]'::jsonb) from (
      select max(ks.zuletzt) zuletzt, jsonb_build_object('einheit_id', e.id, 'titel', t.unterthema, 'ort', b.stadt, 'status', e.status,
        'zuletzt', max(ks.zuletzt),
        'karten', (select jsonb_agg(jsonb_build_object('lernziel', et->>'lernziel', 'titel', et->>'titel',
              'serie', coalesce(k.serie, 0), 'ziel', schule.karte_ziel(e.id, et->>'lernziel'), 'sitzt', coalesce(k.sitzt, false),
              'richtig', coalesce(k.richtig, 0), 'falsch', coalesce(k.falsch, 0), 'zuletzt', k.zuletzt,
              'faellig', coalesce(k.sitzt and k.faellig_am <= now(), false),
              'mit_tipp', (select count(*) from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id where v.lernender_id = v_l and a.einheit_id = e.id and a.variante_gruppe = et->>'lernziel' and v.hilfe > 0),
              'fehler', (select coalesce(jsonb_agg(f.j), '[]'::jsonb) from (
                 select jsonb_build_object('frage', a.frage->>'text', 'antwort', v.antwort, 'antworttyp', a.antworttyp, 'antworten', a.antworten, 'loesung', a.loesung, 'schablone', a.frage->>'schablone', 'grafik', a.frage->'grafik', 'am', v.am) j
                   from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                  where v.lernender_id = v_l and a.einheit_id = e.id and a.variante_gruppe = et->>'lernziel' and not v.richtig order by v.am desc limit 3) f))
            order by ord)
          from jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) with ordinality q(et, ord)
          left join schule.karte_stand k on k.lernender_id = v_l and k.einheit_id = e.id and k.lernziel = et->>'lernziel')) j
      from schule.einheit e join schule.thema t on t.id = e.thema_id left join schule.block b on b.id = e.block_id
      join schule.karte_stand ks on ks.einheit_id = e.id and ks.lernender_id = v_l
      group by e.id, t.unterthema, b.stadt) x));
end $$;
grant execute on function api.schule_lernstand(text, jsonb) to council_mcp;
revoke all on function api.schule_lernstand(text, jsonb) from public, anon, authenticated;
