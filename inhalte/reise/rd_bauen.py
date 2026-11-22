#!/usr/bin/env python3
"""RD-S: baut inhalte/reise/rd_einspiel_2311.sql aus inhalte/reise/aufbau-vorschlag.json.

Aufruf (aus dem Repo-Wurzelverzeichnis):  python3 -I inhalte/reise/rd_bauen.py
Prüft die JSON vorab (jedes Land/jede Stadt genau einmal, Etappen lückenlos, Koordinaten im Bereich, Reserve-Zuordnung)
und bricht bei einem Fehler mit Exit 1 ab. Die SQL-Datei löst Themen über thema_id bzw. teil_stamm + teil_nr auf
(keine festen IDs der neuen Teile), ist wiederholbar (Upsert) und enthält kein DROP und kein DELETE.
Keine Namen von Kindern, keine Schlüssel.
"""
import json
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
QUELLE = os.path.join(HIER, 'aufbau-vorschlag.json')
ZIEL = os.path.join(HIER, 'rd_einspiel_2311.sql')

# Gruppen des Reise-Aufbaus → Gruppen der Datenbank (schule.kind_gruppe)
GR = {'gym': 'gym_by', 'gym_by': 'gym_by', 'rs_I': 'rs_I', 'rs_II_III': 'rs_II_III',
      'ib_standard': 'myp_standard', 'myp_standard': 'myp_standard', 'ib_extended': 'myp_extended', 'myp_extended': 'myp_extended'}

QUELLEN = [  # Angabe für Info-Seite und Karten-Antwort; Lizenzen laut Bau-Auftrag RK
    {'schluessel': '1_geonames', 'was': 'Städte und Hauptstädte (Lage, Namen)', 'quelle': 'GeoNames', 'lizenz': 'CC BY 4.0', 'link': 'https://www.geonames.org'},
    {'schluessel': '2_natural_earth', 'was': 'Mittelpunkte der Länder und Landesteile', 'quelle': 'Natural Earth', 'lizenz': 'gemeinfrei (public domain)', 'link': 'https://www.naturalearthdata.com'},
    {'schluessel': '3_comnap', 'was': 'Antarktis-Stationen', 'quelle': 'COMNAP Antarctic Facilities 2024', 'lizenz': 'frei für Bildung, nicht kommerziell', 'link': 'https://www.comnap.aq'},
]

fehler = []


def f(msg):
    fehler.append(msg)


def koord(b, l, wo):
    if not (isinstance(b, (int, float)) and isinstance(l, (int, float)) and -90 <= b <= 90 and -180 <= l <= 180):
        f(f'{wo}: Koordinaten fehlen oder außerhalb ({b}, {l})')


def main():
    d = json.load(open(QUELLE, encoding='utf-8'))
    kont, laender, staedte, stationen = [], [], [], []
    land_name, land_iso, geo = {}, {}, {}

    def land_merken(name, iso, region, wo):
        if name in land_name:
            f(f'Land doppelt: {name} ({wo}, vorher {land_name[name]})')
        land_name[name] = wo
        k = (iso, region or '')
        if k in land_iso:
            f(f'Land doppelt (ISO/Region): {k} ({wo}, vorher {land_iso[k]})')
        land_iso[k] = wo

    def stadt_merken(s, wo):
        g = s.get('geonames_id')
        if not isinstance(g, int):
            f(f'{wo}: GeoNames-ID fehlt')
        elif g in geo:
            f(f'Stadt doppelt: {s.get("stadt")} ({wo}, vorher {geo[g]})')
        else:
            geo[g] = wo
        koord(s.get('breite'), s.get('laenge'), wo)

    folge = 0
    for ki, k in enumerate(d['kontinente'], 1):
        kont.append({'titel': k['themengebiet'], 'reise': k['reise'], 'reihenfolge': ki})
        for f_ in k['fluege']:
            folge += 1
            fid = f_['flug_id']
            teil = f_.get('teil')
            if teil and str(fid) != f"{f_['thema_id']}-{teil}":
                f(f'{fid}: flug_id passt nicht zu thema_id/teil')
            land_merken(f_['land'], f_['iso'], f_.get('region'), fid)
            koord(f_['mitte']['breite'], f_['mitte']['laenge'], f'{fid} Mitte')
            h = f_['hauptstadt']
            koord(h['breite'], h['laenge'], f'{fid} Hauptstadt')
            st = sorted(f_['staedte'], key=lambda s: s['etappe'])
            if [s['etappe'] for s in st] != list(range(1, len(st) + 1)):
                f(f'{fid}: Etappen nicht lückenlos 1..n')
            if f_.get('etappen') != len(st):
                f(f'{fid}: etappen={f_.get("etappen")}, aber {len(st)} Städte')
            lz = [s['lernziel'] for s in st]
            if len(set(lz)) != len(lz):
                f(f'{fid}: Lernziel doppelt')
            ins = bool(f_.get('insel_ausnahme'))
            ho = f_.get('hauptort_landesteil')
            laender.append({
                'art': 'flug', 'kontinent': k['themengebiet'], 'flug': str(fid), 'thema': f_['thema_id'], 'teil': teil,
                'name': f_['land'], 'iso': f_['iso'], 'region': f_.get('region'),
                'mb': f_['mitte']['breite'], 'ml': f_['mitte']['laenge'], 'mq': f_['mitte'].get('quelle'),
                'hn': h['name'], 'hb': h['breite'], 'hl': h['laenge'], 'hg': h.get('geonames_id'),
                'ho': ({'name': ho['stadt'], 'breite': ho['breite'], 'laenge': ho['laenge'], 'geonames_id': ho.get('geonames_id'), 'art': ho.get('art')} if ho else None),
                'kurz': bool(f_.get('kurzflug')), 'insel': ins, 'nachbar': bool(teil and teil > 1 and not ins),
                'nachbarschaft': f_.get('nachbarschaft'), 'reihenfolge': folge})
            for s in st:
                stadt_merken(s, f'{fid}/{s["lernziel"]}')
                kv = sorted({GR[g] for g in s.get('kuer_in', [])}) if s.get('kuer_in') else None
                if kv is None and s.get('kuer'):  # „kuer“ ohne Gruppen = Kür in allen Gruppen
                    kv = sorted(set(GR.values()))
                if s.get('kuer_in') and any(g not in GR for g in s['kuer_in']):
                    f(f'{fid}/{s["lernziel"]}: unbekannte Gruppe {s["kuer_in"]}')
                staedte.append({'art': 'etappe', 'land': f_['land'], 'lz': s['lernziel'], 'name': s['stadt'], 'b': s['breite'], 'l': s['laenge'],
                                'g': s['geonames_id'], 'gn': s.get('geonames_name'), 'nr': s['etappe'], 'kv': kv})
    for r in d['reserve']:
        for ld in r['laender']:
            folge += 1
            land_merken(ld['land'], ld['iso'], ld.get('region'), f'Reserve {ld["land"]}')
            koord(ld['mitte']['breite'], ld['mitte']['laenge'], f'Reserve {ld["land"]} Mitte')
            h = ld['hauptstadt']
            laender.append({'art': 'reserve', 'kontinent': next(k['themengebiet'] for k in d['kontinente'] if k['kontinent_id'] == r['kontinent_id']),
                            'flug': None, 'thema': None, 'teil': None, 'name': ld['land'], 'iso': ld['iso'], 'region': ld.get('region'),
                            'mb': ld['mitte']['breite'], 'ml': ld['mitte']['laenge'], 'mq': ld['mitte'].get('quelle'),
                            'hn': h['name'], 'hb': h['breite'], 'hl': h['laenge'], 'hg': h.get('geonames_id'), 'ho': None,
                            'kurz': False, 'insel': False, 'nachbar': False, 'nachbarschaft': None, 'reihenfolge': folge})
            for i, s in enumerate(ld['staedte'], 1):
                stadt_merken(s, f'Reserve {ld["land"]}/{s["stadt"]}')
                staedte.append({'art': 'reserve', 'land': ld['land'], 'lz': None, 'name': s['stadt'], 'b': s['breite'], 'l': s['laenge'],
                                'g': s['geonames_id'], 'gn': s.get('geonames_name'), 'nr': 100 + i, 'kv': None})
    for name, liste in d['reserve_staedte_je_land'].items():
        if name not in land_name:
            f(f'Reserve-Städte für unbekanntes Land {name}')
        for i, s in enumerate(liste, 1):
            stadt_merken(s, f'Reserve {name}/{s["stadt"]}')
            staedte.append({'art': 'reserve', 'land': name, 'lz': None, 'name': s['stadt'], 'b': s['breite'], 'l': s['laenge'],
                            'g': s['geonames_id'], 'gn': s.get('geonames_name'), 'nr': 100 + i, 'kv': None})
    exp_seen = set()
    for e in d['expeditionen']:
        if e['expedition'] in exp_seen:
            f(f'Expedition doppelt: {e["expedition"]}')
        exp_seen.add(e['expedition'])
        if not (-90 <= e['breite'] <= -60):
            f(f'Station {e["station"]} nicht in der Antarktis')
        stationen.append({'exp': e['expedition'], 'name': e['station'], 'betreiber': e.get('betreiber'), 'b': e['breite'], 'l': e['laenge']})
    for s in {x['name']: x for x in stationen}.values():
        if any(x['name'] == s['name'] and (x['b'], x['l']) != (s['b'], s['l']) for x in stationen):
            f(f'Station {s["name"]} mit verschiedenen Koordinaten')

    n_flug = sum(1 for x in laender if x['art'] == 'flug')
    n_etappe = sum(1 for x in staedte if x['art'] == 'etappe')
    sp = d.get('selbstpruefung', {})
    if sp.get('fluege') not in (None, n_flug) or sp.get('staedte') not in (None, n_etappe):
        f(f'Selbstprüfung der JSON ({sp.get("fluege")} Flüge, {sp.get("staedte")} Städte) ≠ gezählt ({n_flug}, {n_etappe})')
    if fehler:
        print('FEHLER:\n  ' + '\n  '.join(fehler), file=sys.stderr)
        sys.exit(1)

    daten = {'kontinente': kont, 'laender': laender, 'staedte': staedte, 'stationen': stationen, 'quellen': QUELLEN}
    js = json.dumps(daten, ensure_ascii=False, separators=(',', ':'))
    assert '$rd$' not in js
    n_res_l = sum(1 for x in laender if x['art'] == 'reserve')
    n_res_s = sum(1 for x in staedte if x['art'] == 'reserve')
    kopf = f"""-- RD-S Daten (Reise-Aufbau 4 → Datenbank). ERZEUGT von inhalte/reise/rd_bauen.py aus inhalte/reise/aufbau-vorschlag.json – nicht von Hand ändern.
-- Inhalt: {len(kont)} Kontinente, {n_flug} Flug-Länder, {n_etappe} Etappen-Städte, {n_res_l} Reserve-Länder, {n_res_s} Reserve-Städte, {len(stationen)} Expeditionen/Stationen.
-- Voraussetzung: Migration 20261125_rd_s_reise.sql und die Teilung (TL-S 7) sind eingespielt.
-- Themen: thema_id, bei Teilen über teil_stamm + teil_nr (keine festen IDs). Einheit = aktuelle freigegebene Einheit des Themas.
-- Wiederholbar (Upsert über Land ISO+Region, Stadt GeoNames-ID, Station Name), kein DROP, kein DELETE.
-- Bricht ab (alles zurück), wenn ein Thema/Kontinent/eine Expedition fehlt oder eine Etappe ohne Stadt bzw. eine Stadt ohne Etappe bleibt.
-- Ändert nichts an Abflugtafel, Reiseoptionen, Visum, Stempel, Sterne, Lernstand oder den bisherigen Ortsnamen.
"""
    sql = kopf + """-- Ein einziger DO-Block: läuft als Ganzes oder gar nicht (auch innerhalb eines Rauchtests mit Rollback).
do $rd$
declare v_d jsonb := $json$""" + js + """$json$::jsonb;
  v_x jsonb; v_t bigint; v_k bigint; v_l bigint; v_s bigint; v_n int; v_fehl text;
begin
  if to_regclass('schule.reise_land') is null then raise exception 'RD-S: Migration 20261125_rd_s_reise.sql fehlt'; end if;
  if not exists (select 1 from schule.thema where teil_stamm is not null and teil_nr > 1) then raise exception 'RD-S: Teilung (TL-S 7) nicht eingespielt'; end if;

  -- Kontinente über den Titel (Themengebiet)
  for v_x in select * from jsonb_array_elements(v_d->'kontinente') loop
    select id into v_k from schule.kontinent where fach = 'Mathematik' and titel = v_x->>'titel';
    if v_k is null then raise exception 'RD-S: Kontinent „%“ fehlt', v_x->>'titel'; end if;
    insert into schule.reise_kontinent (kontinent_id, reise, reihenfolge) values (v_k, v_x->>'reise', (v_x->>'reihenfolge')::int)
      on conflict (kontinent_id) do update set reise = excluded.reise, reihenfolge = excluded.reihenfolge;
  end loop;

  -- Länder (Flug und Reserve)
  for v_x in select * from jsonb_array_elements(v_d->'laender') loop
    v_t := null;
    if v_x->>'art' = 'flug' then
      if coalesce((v_x->>'teil')::int, 1) > 1 then
        select id into v_t from schule.thema where teil_stamm = (v_x->>'thema')::bigint and teil_nr = (v_x->>'teil')::int;
      else
        select id into v_t from schule.thema where id = (v_x->>'thema')::bigint and coalesce(teil_nr, 1) = 1;
      end if;
      if v_t is null then raise exception 'RD-S: Thema zu Flug % fehlt', v_x->>'flug'; end if;
    end if;
    select id into v_k from schule.kontinent where fach = 'Mathematik' and titel = v_x->>'kontinent';
    insert into schule.reise_land as l (art, kontinent_id, thema_id, flug_schluessel, name, iso, region, mitte_breite, mitte_laenge, mitte_quelle,
                                 hauptstadt_name, hauptstadt_breite, hauptstadt_laenge, hauptstadt_geonames_id, hauptort,
                                 kurzflug, insel_ausnahme, nachbarteil, nachbarschaft, reihenfolge)
    values (v_x->>'art', v_k, v_t, v_x->>'flug', v_x->>'name', v_x->>'iso', v_x->>'region', (v_x->>'mb')::numeric, (v_x->>'ml')::numeric, v_x->>'mq',
            v_x->>'hn', (v_x->>'hb')::numeric, (v_x->>'hl')::numeric, (v_x->>'hg')::bigint, nullif(v_x->'ho', 'null'::jsonb),
            (v_x->>'kurz')::boolean, (v_x->>'insel')::boolean, (v_x->>'nachbar')::boolean, v_x->>'nachbarschaft', (v_x->>'reihenfolge')::int)
    on conflict (iso, region_schluessel) do update set
      art = excluded.art, kontinent_id = excluded.kontinent_id, thema_id = excluded.thema_id, flug_schluessel = excluded.flug_schluessel, name = excluded.name,
      mitte_breite = excluded.mitte_breite, mitte_laenge = excluded.mitte_laenge, mitte_quelle = excluded.mitte_quelle,
      hauptstadt_name = excluded.hauptstadt_name, hauptstadt_breite = excluded.hauptstadt_breite, hauptstadt_laenge = excluded.hauptstadt_laenge,
      hauptstadt_geonames_id = excluded.hauptstadt_geonames_id, hauptort = excluded.hauptort, kurzflug = excluded.kurzflug,
      insel_ausnahme = excluded.insel_ausnahme, nachbarteil = excluded.nachbarteil, nachbarschaft = excluded.nachbarschaft, reihenfolge = excluded.reihenfolge;
  end loop;

  -- Städte (Etappe und Reserve); Etappen-Städte bekommen Thema und aktuelle Einheit ihres Landes
  for v_x in select * from jsonb_array_elements(v_d->'staedte') loop
    select id, thema_id into v_l, v_t from schule.reise_land where name = v_x->>'land';
    insert into schule.reise_stadt as s (art, land_id, thema_id, einheit_id, lernziel, name, breite, laenge, geonames_id, geonames_name, reihenfolge, kuer_vorschlag)
    values (v_x->>'art', v_l, case when v_x->>'art' = 'etappe' then v_t end, case when v_x->>'art' = 'etappe' then schule.thema_einheit(v_t) end,
            v_x->>'lz', v_x->>'name', (v_x->>'b')::numeric, (v_x->>'l')::numeric, (v_x->>'g')::bigint, v_x->>'gn', (v_x->>'nr')::int,
            case when jsonb_typeof(v_x->'kv') = 'array' then array(select jsonb_array_elements_text(v_x->'kv')) end)
    on conflict (geonames_id) do update set
      art = excluded.art, land_id = excluded.land_id, thema_id = excluded.thema_id, einheit_id = excluded.einheit_id, lernziel = excluded.lernziel,
      name = excluded.name, breite = excluded.breite, laenge = excluded.laenge, geonames_name = excluded.geonames_name,
      reihenfolge = excluded.reihenfolge, kuer_vorschlag = excluded.kuer_vorschlag;
  end loop;

  -- Antarktis-Stationen je Expedition
  for v_x in select * from jsonb_array_elements(v_d->'stationen') loop
    select id into v_k from schule.expedition where schluessel = v_x->>'exp';
    if v_k is null then raise exception 'RD-S: Expedition % fehlt', v_x->>'exp'; end if;
    insert into schule.reise_station as st (name, betreiber, breite, laenge) values (v_x->>'name', v_x->>'betreiber', (v_x->>'b')::numeric, (v_x->>'l')::numeric)
      on conflict (name) do update set betreiber = excluded.betreiber, breite = excluded.breite, laenge = excluded.laenge
      returning id into v_s;
    insert into schule.reise_station_expedition (expedition_id, station_id) values (v_k, v_s)
      on conflict (expedition_id) do update set station_id = excluded.station_id;
  end loop;

  -- Quellen
  for v_x in select * from jsonb_array_elements(v_d->'quellen') loop
    insert into schule.reise_quelle (schluessel, was, quelle, lizenz, link) values (v_x->>'schluessel', v_x->>'was', v_x->>'quelle', v_x->>'lizenz', v_x->>'link')
      on conflict (schluessel) do update set was = excluded.was, quelle = excluded.quelle, lizenz = excluded.lizenz, link = excluded.link;
  end loop;

  -- Regel: jede Etappe jedes freigegebenen Flugs genau eine Stadt, keine Stadt ohne Etappe, kein Flug ohne Land
  select string_agg(art || ' ' || coalesce(thema_id::text, '') || '/' || coalesce(lernziel, '') || coalesce(' ' || stadt, ''), '; '), count(*) into v_fehl, v_n
    from schule.reise_abweichung where art in ('etappe_ohne_stadt', 'stadt_ohne_etappe', 'thema_ohne_land', 'land_ohne_freigabe');
  if v_n > 0 then raise exception 'RD-S: % Abweichungen Reise ↔ Datenbank: %', v_n, v_fehl; end if;
  select count(*) into v_n from schule.reise_abweichung where art = 'reihenfolge_anders';
  if v_n > 0 then raise notice 'RD-S: % Städte mit anderer Reihenfolge als die Etappe (Karte folgt der Etappe)', v_n; end if;
  select count(*) into v_n from schule.reise_kuer_abweichung;
  raise notice 'RD-S eingespielt: % Kontinente, % Flug-Länder, % Etappen-Städte, % Reserve-Länder, % Reserve-Städte, % Stationen; Kür-Abweichungen Reise-Aufbau ↔ Pflichtliste: %',
    (select count(*) from schule.reise_kontinent), (select count(*) from schule.reise_land where art = 'flug'), (select count(*) from schule.reise_stadt where art = 'etappe'),
    (select count(*) from schule.reise_land where art = 'reserve'), (select count(*) from schule.reise_stadt where art = 'reserve'),
    (select count(*) from schule.reise_station), v_n;
end $rd$;
"""
    open(ZIEL, 'w', encoding='utf-8').write(sql)
    print(f'{os.path.relpath(ZIEL)}: {len(kont)} Kontinente, {n_flug} Flug-Länder, {n_etappe} Etappen-Städte, '
          f'{n_res_l} Reserve-Länder, {n_res_s} Reserve-Städte, {len(stationen)} Expeditionen, {len(sql)} Bytes')


if __name__ == '__main__':
    main()
