-- W150: Realschul-Klasse (rs_by) und IB-MYP-Jahr (ib_myp) je Thema fest eintragen (Entscheidung Sebastian, 18.11.2026).
-- Grund: thema_jahrgang nahm je Schulart die früheste Zuordnung, auch Neben-Zuordnungen; 860 von 862 Zuordnungen sind ungeprüft.
-- Quelle der Werte: inhalte/pruefung/klassen/vorschlag-mindeststand.md, Punkt 1 (RS korrigiert nach vorschlag-rsib.md; IB = Vorschlag rsib, sonst heutiger Wert).
-- null = diese Schulart hat das Thema nicht; die Angabe aus den Zuordnungen wird dann unterdrückt. Gymnasium (gym_by) bleibt unverändert.
create or replace function schule.thema_jahrgang(p_thema bigint)
 returns jsonb
 language sql
 stable
 set search_path to ''
as $function$
  select jsonb_strip_nulls(coalesce((select jsonb_object_agg(x.schulart, x.jahr) from (
    select q.schulart, min(q.jahr_von) jahr from schule.zuordnung z join schule.eintrag e on e.id = z.eintrag_id join schule.quelle q on q.id = e.quelle_id
     where z.thema_id = p_thema and q.aktiv and q.rolle = 'basis' and not e.archiviert group by q.schulart) x), '{}'::jsonb)
    || coalesce((select t.klasse_fest from schule.thema t where t.id = p_thema), '{}'::jsonb));
$function$;

do $$
declare n int;
begin
  update schule.thema t set klasse_fest = coalesce(t.klasse_fest, '{}'::jsonb) || jsonb_build_object('rs_by', v.rs, 'ib_myp', v.ib)
    from (values
      ('abbildungen.aehnlichkeit',9,3),
      ('abbildungen.determinanten2',7,null),
      ('abbildungen.kongruenz',6,3),
      ('abbildungen.matrizen',10,5),
      ('abbildungen.vektoren',7,null),
      ('bruch.brueche',6,1),
      ('bruch.dezimal',6,1),
      ('bruch.prozent',6,1),
      ('bruch.prozent_grundwert',7,3),
      ('bruch.rechnen',6,2),
      ('daten.boxplot',7,4),
      ('daten.darstellen',5,1),
      ('daten.kennwerte',7,2),
      ('daten.normalverteilung',null,5),
      ('daten.standardabweichung',null,5),
      ('daten.stichproben',7,2),
      ('daten.zweidimensional',null,5),
      ('finanzen.zinsen',7,4),
      ('finanzen.zinseszins',null,4),
      ('funktionen.betrag',null,5),
      ('funktionen.exponential_log',10,5),
      ('funktionen.folgen',null,5),
      ('funktionen.ganzrational',null,5),
      ('funktionen.gebrochen',null,4),
      ('funktionen.grundbegriffe',8,4),
      ('funktionen.linear',8,3),
      ('funktionen.potenz',10,4),
      ('funktionen.quadratisch',9,4),
      ('funktionen.reihen',null,5),
      ('funktionen.scharen',8,null),
      ('funktionen.transformation',9,5),
      ('funktionen.trig',10,5),
      ('funktionen.umkehr',10,5),
      ('geometrie.grundbegriffe',5,1),
      ('geometrie.konstruktion',7,3),
      ('geometrie.kreis',7,4),
      ('geometrie.ortslinien',7,null),
      ('geometrie.winkel',5,1),
      ('geometrie.winkelsaetze',7,2),
      ('gleichungen.bruch',8,4),
      ('gleichungen.einfach',6,1),
      ('gleichungen.exponential',10,5),
      ('gleichungen.formeln',null,4),
      ('gleichungen.lgs2',9,4),
      ('gleichungen.lgs3',null,null),
      ('gleichungen.linear',7,2),
      ('gleichungen.polynom',null,null),
      ('gleichungen.potenz',10,4),
      ('gleichungen.quadratisch',9,4),
      ('gleichungen.reinquadratisch',9,4),
      ('gleichungen.trig',10,5),
      ('gleichungen.ungleichungen',7,4),
      ('gleichungen.wurzel',9,null),
      ('groessen.einheiten',5,2),
      ('groessen.indirekt',7,4),
      ('groessen.proportional',6,2),
      ('groessen.verhaeltnisse',null,2),
      ('mengen.grundbegriffe',null,3),
      ('messen.flaechen',5,1),
      ('messen.flaechen_vielecke',6,null),
      ('messen.koerper_berechnung',6,1),
      ('messen.koerper_darstellung',5,3),
      ('messen.kreisberechnung',9,3),
      ('messen.prisma_zylinder',9,null),
      ('messen.volumen',6,null),
      ('raum.pyramide_kegel_kugel',9,3),
      ('raum.schraegbilder',8,4),
      ('sonder.graphentheorie',null,4),
      ('sonder.logik',null,4),
      ('sonder.optimierung',null,5),
      ('stochastik.bedingt',null,5),
      ('stochastik.grundbegriffe',9,2),
      ('stochastik.kombinatorik',5,2),
      ('stochastik.mehrstufig',10,4),
      ('stochastik.simulation',9,2),
      ('stochastik.verknuepft',9,4),
      ('terme.aufstellen',6,1),
      ('terme.bruchterme',8,4),
      ('terme.potenzgesetze',7,3),
      ('terme.quadratische_extreme',8,null),
      ('terme.umformen',7,3),
      ('trigo.allgemein',10,4),
      ('trigo.pythagoras',9,3),
      ('trigo.rechtwinklig',9,4),
      ('zahlen.ganz',5,2),
      ('zahlen.intervalle',7,4),
      ('zahlen.natuerlich',5,1),
      ('zahlen.potenzen_basis',5,1),
      ('zahlen.potenzen_zehner',7,4),
      ('zahlen.rationale_exponenten',10,5),
      ('zahlen.rechengesetze',5,1),
      ('zahlen.reell',9,4),
      ('zahlen.schranken',null,5),
      ('zahlen.teilbarkeit',5,1),
      ('zahlen.wurzeln_basis',9,1)
    ) v(k, rs, ib)
   where t.schluessel = v.k;
  get diagnostics n = row_count;
  if n <> 95 then raise exception 'erwartet 95 Themen, geändert %', n; end if;
end $$;
