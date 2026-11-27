-- SJ-S (Auftrag SJ, 23.11. 03:10): „Wie viel ist noch?“ je Schuljahr – Feld schuljahr_stand je Kind in schule_konto und schule_uebersicht.
-- Klassen: Klasse des Kindes (Hauptklasse), dazu −1 und +1, soweit es sie gibt (5–10; IB: MYP-Jahr = Klasse − 5). Schulart des Kindes.
-- Rechnung wie der Ring der Lehrer-Ansicht (lernLwRing, lernen.js):
--   Pflicht-Flüge der Klasse = Themen mit freigegebener Einheit, deren Jahrgang in der Schulart des Kindes die Klasse ist und die eine aktive
--   Basis-Lehrplanquelle dieser Schulart haben (IB: alle mit MYP-Jahr); Zusatz-Teile der Gruppe des Kindes (thema.zusatz) nicht mitgezählt.
--   Etappen je Flug = alle Etappen der Einheit (etappen_anzahl der Matrix; 0 → Etappen der Stufe → 1).
--   Fertig = Stufe „komplett“ (kann er, auch gesetzt) oder „wiederholung“ → zählt mit allen Etappen; sonst gelandete Etappen (höchstens alle).
--   Prozent = gelandet ÷ gesamt, gerundet.
--   Zusatz (übrige Themen der Klasse mit Einheit) getrennt: gleiche Rechnung, dazu eingeplant (ZP-S).
--   SJ-S 2 (vorbereitet, Entscheidung des Nutzers offen): je Klasse zusätzlich etappen_pflicht (nur Pflicht-Etappen der Gruppe des Kindes,
--   wie thema_stufe.etappen) mit prozent_pflicht, und kuer (übrige Etappen der Pflicht-Flüge). Die App wählt die Zählung ohne neue Migration.
-- Nur lesend. Baut auf LZ-S und ZP-S auf. Wiederholbar; kein DROP, kein DELETE.

do $$ begin
  if position('-- LZ-S' in pg_get_functiondef('schule.thema_stufe(bigint, bigint)'::regprocedure)) = 0 then
    raise exception 'SJ-S: zuerst 20261126_lz_s_ladezeit.sql einspielen'; end if;
  if to_regclass('schule.zusatz_geschafft') is null or position('ZP-S' in pg_get_functiondef('schule.thema_stufe(bigint, bigint)'::regprocedure)) = 0 then
    raise exception 'SJ-S: zuerst 20261126_zp_s_zusatz_plan.sql einspielen'; end if;
end $$;

-- Je Thema der Klassen −1/Haupt/+1: Pflicht oder Zusatz, Etappen, gelandet, fertig (eine Stelle für alle Anzeigen).
-- SJ-S 2 (vorbereitet, Entscheidung offen): zusätzlich Pflicht-Etappen der Gruppe des Kindes (stufe_etappen, wie thema_stufe) und Kür-Etappen
-- (übrige Etappen der Einheit). Fertige Flüge zählen in beiden Teilen mit allen Etappen.
create or replace function schule.schuljahr_fluege(p_l bigint)
 returns table (klasse int, thema_id bigint, pflicht boolean, eingeplant boolean, stufe text, etappen int, gelandet int, fertig boolean,
                etappen_pflicht int, gelandet_pflicht int, kuer int, gelandet_kuer int)
 language sql stable set search_path to ''
as $$
  with k as (select l.id, coalesce(l.schulart, 'gym_by') sa, l.klasse kl, schule.kind_gruppe(l.id) gr from schule.lernender l where l.id = p_l),
  t as (
    select t.id, k.sa, k.gr, (j.jg + case when k.sa = 'ib_myp' then 5 else 0 end) klasse, ein.id e,
           array(select x->>'lernziel' from jsonb_array_elements(coalesce(ein.inhalt->'etappen', '[]'::jsonb)) x) lz_alle,
           (k.sa = 'ib_myp' or exists (select 1 from (select z0.eintrag_id from schule.zuordnung z0 where z0.thema_id = t.id offset 0) z
                                         join schule.eintrag e on e.id = z.eintrag_id join schule.quelle ql on ql.id = e.quelle_id
                                        where ql.aktiv and ql.rolle = 'basis' and not coalesce(e.archiviert, false) and ql.schulart = k.sa)) pfl_sa,
           coalesce(k.gr = any(t.zusatz), false) zus
      from k cross join schule.thema t
      cross join lateral (select (schule.thema_jahrgang(t.id)->>k.sa)::int jg) j
      join schule.einheit ein on ein.id = schule.thema_einheit(t.id)
     where t.fach = 'Mathematik' and j.jg is not null
       and (j.jg + case when k.sa = 'ib_myp' then 5 else 0 end) between greatest(k.kl - 1, 5) and least(k.kl + 1, 10))
  select t.klasse, t.id, t.pfl_sa and not t.zus, coalesce((s.st->>'zusatz_eingeplant')::boolean, false), s.st->>'stufe', n.n,
         case when f.fertig then n.n else least(n.n, coalesce((s.st->>'gelandet')::int, 0)) end,
         f.fertig,
         cardinality(p.pf), case when f.fertig then cardinality(p.pf) else g.pf end,
         cardinality(t.lz_alle) - cardinality(p.pf), case when f.fertig then cardinality(t.lz_alle) - cardinality(p.pf) else g.kuer end
    from t cross join lateral (select schule.thema_stufe(p_l, t.id) st offset 0) s
    cross join lateral (select coalesce(nullif(cardinality(t.lz_alle), 0), nullif((s.st->>'etappen')::int, 0), 1) n) n
    cross join lateral (select coalesce(s.st->>'stufe' in ('komplett', 'wiederholung'), false) fertig) f
    cross join lateral (select schule.stufe_etappen(p_l, t.e) pf) p
    cross join lateral (select count(*) filter (where ks.lernziel = any(p.pf))::int pf, count(*) filter (where not (ks.lernziel = any(p.pf)))::int kuer
                          from schule.karte_stand ks where ks.lernender_id = p_l and ks.einheit_id = t.e and ks.sitzt and ks.lernziel = any(t.lz_alle)) g;
$$;
revoke all on function schule.schuljahr_fluege(bigint) from public, anon, authenticated;

create or replace function schule.schuljahr_stand(p_l bigint)
 returns jsonb language sql stable set search_path to ''
as $$
  with l as (select coalesce(l.schulart, 'gym_by') sa, l.klasse kl from schule.lernender l where l.id = p_l),
  x as (select * from schule.schuljahr_fluege(p_l)),
  kl as (select distinct x.klasse from x)   -- Klassen mit Flügen (Pflicht oder Zusatz)
  select jsonb_build_object('schulart', l.sa, 'klasse', l.kl,
    'rechnung', 'Prozent = gelandete Etappen ÷ alle Etappen der Pflicht-Flüge der Klasse. Fertige Flüge (Wiederholung oder „kann er“) zählen mit allen Etappen. Zusatz-Flüge zählen nicht mit.',
    'klassen', coalesce((select jsonb_agg(jsonb_build_object(
        'klasse', kl.klasse, 'myp_jahr', case when l.sa = 'ib_myp' then kl.klasse - 5 end, 'haupt', kl.klasse = l.kl,
        'fluege', jsonb_build_object('gesamt', p.n, 'fertig', p.f, 'offen', p.n - p.f),
        'etappen', jsonb_build_object('gesamt', p.e, 'gelandet', p.g, 'offen', p.e - p.g),
        'prozent', case when p.e > 0 then round(100.0 * p.g / p.e)::int end,
        -- SJ-S 2 (vorbereitet): nur Pflicht-Etappen der Gruppe des Kindes, Kür getrennt
        'etappen_pflicht', jsonb_build_object('gesamt', p.ep, 'gelandet', p.gp, 'offen', p.ep - p.gp),
        'prozent_pflicht', case when p.ep > 0 then round(100.0 * p.gp / p.ep)::int end,
        'kuer', jsonb_build_object('gesamt', p.ek, 'gelandet', p.gk, 'offen', p.ek - p.gk),
        'ring', jsonb_build_object('kann', p.kann, 'wdh', p.wdh, 'an', p.g - p.kann - p.wdh),
        'zusatz', jsonb_build_object('fluege', jsonb_build_object('gesamt', z.n, 'fertig', z.f, 'offen', z.n - z.f, 'eingeplant', z.ein),
                                     'etappen', jsonb_build_object('gesamt', z.e, 'gelandet', z.g, 'offen', z.e - z.g)))
        order by kl.klasse)
      from kl
      cross join lateral (select count(*)::int n, count(*) filter (where x.fertig)::int f, coalesce(sum(x.etappen), 0)::int e, coalesce(sum(x.gelandet), 0)::int g,
                                 coalesce(sum(x.etappen) filter (where x.stufe = 'komplett'), 0)::int kann, coalesce(sum(x.etappen) filter (where x.stufe = 'wiederholung'), 0)::int wdh,
                                 coalesce(sum(x.etappen_pflicht), 0)::int ep, coalesce(sum(x.gelandet_pflicht), 0)::int gp,
                                 coalesce(sum(x.kuer), 0)::int ek, coalesce(sum(x.gelandet_kuer), 0)::int gk
                            from x where x.klasse = kl.klasse and x.pflicht) p
      cross join lateral (select count(*)::int n, count(*) filter (where x.fertig)::int f, count(*) filter (where x.eingeplant)::int ein,
                                 coalesce(sum(x.etappen), 0)::int e, coalesce(sum(x.gelandet), 0)::int g
                            from x where x.klasse = kl.klasse and not x.pflicht) z), '[]'::jsonb))
  from l;
$$;
revoke all on function schule.schuljahr_stand(bigint) from public, anon, authenticated;

-- schule_konto
do $$
declare d text;
  a text := $a$'konto', schule.konto_wd(v_l),$a$;
  n text := $a$'konto', schule.konto_wd(v_l), 'schuljahr_stand', schule.schuljahr_stand(v_l), /* SJ-S */$a$;
begin
  d := pg_get_functiondef('api.schule_konto(text, jsonb)'::regprocedure);
  if position('SJ-S' in d) > 0 then raise notice 'schule_konto schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'SJ-S: Anker in schule_konto nicht genau einmal gefunden'; end if;
  execute replace(d, a, n);
end $$;

-- schule_uebersicht: je Kind
do $$
declare d text;
  a text := $a$'expeditionen_stand', schule.expedition_stand(l.id), /* EX-S */$a$;
  n text := $a$'expeditionen_stand', schule.expedition_stand(l.id), /* EX-S */ 'schuljahr_stand', schule.schuljahr_stand(l.id), /* SJ-S */$a$;
begin
  d := pg_get_functiondef('api.schule_uebersicht(text, jsonb)'::regprocedure);
  if position('SJ-S' in d) > 0 then raise notice 'schule_uebersicht schon umgestellt'; return; end if;
  if (length(d) - length(replace(d, a, ''))) / length(a) <> 1 then raise exception 'SJ-S: Anker in schule_uebersicht nicht genau einmal gefunden'; end if;
  execute replace(d, a, n);
end $$;
