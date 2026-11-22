#!/usr/bin/env bash
# WD-S 3, ChatGPT 919 „Sollte“: echter Test mit zwei GLEICHZEITIGEN Transaktionen (zwei Geräte beantworten dieselbe fällige Etappe).
# Erwartet: genau ein Stufenfortschritt, genau einmal Wiederholungs-Sterne; die zweite Antwort (Gerät B) wartet auf die Zeilensperre und
# ist danach keine Wiederholung mehr (Antwort ohne „wiederholung“ bzw. mit bestanden = false).
# NUR auf einer Wegwerf-Datenbank (Kopie/Branch) – das Skript schreibt und behält Daten (Testkind, eigene Hilfstabelle public.wd3_gleich).
# Aufruf:  WD_WEGWERF=ja WD_DB='postgresql://…' bash supabase/tests/wd_s3_gleichzeitig.sh
set -euo pipefail
: "${WD_DB:?WD_DB = psql-Verbindung der Wegwerf-Datenbank}"
[ "${WD_WEGWERF:-}" = "ja" ] || { echo "Abbruch: nur mit WD_WEGWERF=ja (Wegwerf-Datenbank)"; exit 1; }
P=(psql "$WD_DB" -v ON_ERROR_STOP=1 -qtA)

"${P[@]}" <<'SQL'
create table if not exists public.wd3_gleich (l bigint, e bigint, lz text, a1 bigint, a2 bigint, s0 bigint, ab timestamptz);
truncate public.wd3_gleich;
insert into public.wd3_gleich (l, e, lz, a1, a2)
select l.id, q.einheit_id, q.lz, q.ids[1], q.ids[2]
  from schule.lernender l,
       lateral (select a.einheit_id, a.variante_gruppe lz, array_agg(a.id order by a.id) ids
                  from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id and e.status = 'freigegeben' and e.id = schule.thema_einheit(e.thema_id)
                 where a.pool = 'uebung' and a.freigegeben and a.antworttyp = 'auswahl' and e.block_id is not null
                   and not exists (select 1 from schule.versuch v where v.lernender_id = l.id and v.aufgabe_id = a.id)
                 group by 1, 2 having count(*) >= 2 order by 1, 2 limit 1) q
 where l.ist_test and l.aktiv order by l.id limit 1;
insert into schule.lerntag (lernender_id, fach, datum, zeitzone)
select g.l, 'Mathematik', schule.heute_tag(g.l) - d, 'Europe/Berlin' from public.wd3_gleich g, generate_series(1, 10) d on conflict do nothing;
insert into schule.karte_stand (lernender_id, einheit_id, lernziel) select l, e, lz from public.wd3_gleich on conflict do nothing;
update schule.karte_stand k set sitzt = true, sitzt_am = now() - interval '30 days', wdh_stufe = 1, wdh_lerntage = 3, wdh_fehler = 0,
       wdh_ab = now() - interval '6 days', faellig_am = now() - interval '3 days' from public.wd3_gleich g
 where k.lernender_id = g.l and k.einheit_id = g.e and k.lernziel = g.lz;
update public.wd3_gleich g set s0 = (select count(*) from schule.sterne s where s.lernender_id = g.l and s.grund = 'wdh'),
       ab = (select k.wdh_ab from schule.karte_stand k where k.lernender_id = g.l and k.einheit_id = g.e and k.lernziel = g.lz);
SQL

antwort() { # $1 = Aufgaben-Spalte, $2 = Gerät, $3 = Wartezeit in der Transaktion
  "${P[@]}" <<SQL
begin;
select 'Gerät $2: ' || coalesce((schule.uebung_pruefen_wd(g.l, jsonb_build_object('aufgabe_id', g.$1, 'client_id', 'gleichzeitig-$2-' || gen_random_uuid(),
         'antwort', jsonb_build_object('index', (select (a.loesung->>'index')::int from schule.aufgabe a where a.id = g.$1))))->'wiederholung')::text, 'keine Wiederholung')
  from public.wd3_gleich g;
select pg_sleep($3);
commit;
SQL
}
antwort a1 A 2 &                       # Gerät A hält die Sperre 2 Sekunden
sleep 0.5
antwort a2 B 0 &                       # Gerät B antwortet währenddessen
wait

"${P[@]}" <<'SQL'
select case when k.wdh_stufe = 2 and (select count(*) from schule.sterne s where s.lernender_id = g.l and s.grund = 'wdh') - g.s0 = 1
            then 'ok gleichzeitig: genau ein Fortschritt (Stufe 1 → 2), einmal Wiederholungs-Sterne'
            else 'FEHLER gleichzeitig: Stufe ' || k.wdh_stufe || ', Wiederholungs-Sterne +' || ((select count(*) from schule.sterne s where s.lernender_id = g.l and s.grund = 'wdh') - g.s0) end
  from public.wd3_gleich g join schule.karte_stand k on k.lernender_id = g.l and k.einheit_id = g.e and k.lernziel = g.lz;
SQL
