-- W150 Umbau D2 (Freigabe Sebastian 16.11., Vorschlag inhalte/pruefung/klassen/vorschlag.md im Zweig daten-klassen):
-- jeder der 13 Orte bekommt genau eine Klasse; zwei Flüge ziehen um; zwei Themen gelten am Gymnasium als Klasse 10.
-- Noch NICHT enthalten: Umzug „Lineare Gleichungen“ (Delhi → Samarkand) – wartet auf Entscheidung (ein Kind hat Samarkand schon abgeschlossen).

-- 1) Feste Klasse je Thema, wenn die Lehrplan-Zuordnung (kleinste Jahrgangsstufe) nicht die Hauptklasse trifft
alter table schule.thema add column if not exists klasse_fest jsonb;
comment on column schule.thema.klasse_fest is 'Übersteuert schule.thema_jahrgang je Schulart, z. B. {"gym_by": 10} (Hauptklasse laut Lehrplan-Abgleich D1)';
create or replace function schule.thema_jahrgang(p_thema bigint)
 returns jsonb language sql stable set search_path to ''
as $function$
  select coalesce((select jsonb_object_agg(x.schulart, x.jahr) from (
    select q.schulart, min(q.jahr_von) jahr from schule.zuordnung z join schule.eintrag e on e.id = z.eintrag_id join schule.quelle q on q.id = e.quelle_id
     where z.thema_id = p_thema and q.aktiv and q.rolle = 'basis' and not e.archiviert group by q.schulart) x), '{}'::jsonb)
    || coalesce((select t.klasse_fest from schule.thema t where t.id = p_thema), '{}'::jsonb);
$function$;
update schule.thema set klasse_fest = '{"gym_by": 10}' where schluessel in ('raum.schraegbilder', 'stochastik.simulation');

-- 2) Titel: Die Etappen von geometrie.winkel sind Klasse-5-Stoff; Winkelsätze (Klasse 7) werden ein eigener Flug
update schule.thema set unterthema = 'Mit Winkeln rechnen', beschreibung = 'Winkel messen, zeichnen und berechnen; Winkel an Geraden.' where schluessel = 'geometrie.winkel';

-- 3) Klassen und Titel der Orte
update schule.block set ziel_klasse = 8 where stadt in ('Vancouver', 'Cusco');
update schule.block set ziel_klasse = 7 where stadt in ('Teheran', 'Marrakesch');
update schule.block set ziel_klasse = 5 where stadt in ('Timbuktu', 'Rio de Janeiro');
update schule.block set ziel_klasse = 10 where stadt in ('Brasília', 'Santiago de Chile');
update schule.block set ziel_klasse = 6 where stadt in ('Adelaide', 'New York');
update schule.block set titel = 'Kreis' where stadt = 'Alexandria';

-- 4) Umzüge: Zehnerpotenzen Rom → Paris, Ortslinien Alexandria → Kairo
update schule.einheit e set block_id = (select id from schule.block where stadt = 'Paris')
  from schule.thema t where t.id = e.thema_id and t.schluessel = 'zahlen.potenzen_zehner' and e.status <> 'ersetzt';
update schule.einheit e set block_id = (select id from schule.block where stadt = 'Kairo')
  from schule.thema t where t.id = e.thema_id and t.schluessel = 'geometrie.ortslinien' and e.status <> 'ersetzt';

-- 5) Folge für einen bestehenden Plan (Klasse 5): Alexandria enthält jetzt nur noch Klasse-7-Stoff und fällt aus diesem Plan; Ortslinien liegen in Kairo, das im Plan steht
update schule.route r set status = 'entfernt', revision = r.revision + 1, geaendert_von = 'eltern:Claude (D2 Klassen-Zuordnung 16.11.)', geaendert_am = now()
 where r.block_id = (select id from schule.block where stadt = 'Alexandria') and r.art = 'normal' and r.status = 'offen' and not r.kann_schon
   and exists (select 1 from schule.lernender l where l.id = r.lernender_id and l.klasse = 5);
