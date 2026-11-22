#!/usr/bin/env bash
# WD-S 3/4, FP-S 2 (ChatGPT 919/921/924): echte Tests mit zwei GLEICHZEITIGEN Transaktionen (zwei Geräte).
#   A) dieselbe fällige Etappe zweimal: genau ein Stufenfortschritt, genau einmal Wiederholungs-Sterne.
#   B) die zwei letzten Pflicht-Etappen der Tagesrunde gleichzeitig: danach ist die Runde fertig (Abschluss unter Sperre, WD-S 4).
#   C) Antwort, während eine andere Sitzung für dasselbe Kind Sterne bucht: die Antwort meldet nur ihre eigenen Sterne (FP-S 2).
#   D) Landung gleichzeitig mit der Nachbuchung: jede Seite meldet genau ihre Sterne, die Summe stimmt (FP-S 2).
#      D2) zwei Nachbuchungen beanspruchen gleichzeitig denselben Landungs-Bonus: genau einmal gebucht, jede meldet nur ihr Eigenes (FP-S 3).
#   E) dieselbe ausgegebene Mischkarte mit zwei verschiedenen client_id: genau eine Antwort meldet misch.gueltig, ein Fortschritt (FP-S 3).
#   F) Antwort auf eine andere Aufgabe derselben Etappe läuft, dann wird die Mischkarte eingelöst: keine Misch-Bestätigung,
#      kein Wiederholungsfortschritt aus der Mischkarte, Ausgabe nicht eingelöst (FP-S 3).
#   G1/G2) Mischkarten-Antwort und normale Antwort zur SELBEN Aufgabe gleichzeitig, beide Reihenfolgen: kein Deadlock, höchstens einmal gültig,
#      gültig ⇔ eingelöst, sonst verfallen, genau ein Wiederholungsfortschritt (FP-S 4).
#   E, F, G prüfen reihenfolgeunabhängig: welches Gerät gewinnt, entscheidet die Datenbank; geprüft wird „genau einmal gültig“ und die Folgen.
# Setzt alle Migrationen bis FP-S 4 voraus.
# NUR auf einer Wegwerf-Datenbank (Kopie/Branch) – das Skript schreibt und behält Daten (Testkind, Hilfstabelle public.wd3_gleich).
# Ergebnis: Exit 0 nur, wenn alle neun Teile „ok“ melden (A, B, C, D, D2, E, F, G1, G2); jedes „FEHLER“ oder ein abgebrochener Prozess beendet mit Exit 1.
# Aufruf:  WD_WEGWERF=ja WD_DB='postgresql://…' bash supabase/tests/wd_s3_gleichzeitig.sh
set -euo pipefail
: "${WD_DB:?WD_DB = psql-Verbindung der Wegwerf-Datenbank}"
[ "${WD_WEGWERF:-}" = "ja" ] || { echo "Abbruch: nur mit WD_WEGWERF=ja (Wegwerf-Datenbank)"; exit 1; }
P=(psql "$WD_DB" -v ON_ERROR_STOP=1 -qtA)
AUSGABE=""
pruefen() { echo "$1"; AUSGABE="$AUSGABE"$'\n'"$1"; }

# Vorbereitung: Testkind, drei Etappen ohne bisherige Antworten (je zwei Auswahl-Aufgaben), Lerntage
"${P[@]}" <<'SQL'
create table if not exists public.wd3_gleich (nr int, l bigint, e bigint, lz text, a1 bigint, a2 bigint, s0 bigint);
truncate public.wd3_gleich;
insert into public.wd3_gleich (nr, l, e, lz, a1, a2)
select row_number() over (order by q.mischbar desc, q.einheit_id, q.lz), l.id, q.einheit_id, q.lz, q.ids[1], q.ids[2]
  from (select id from schule.lernender where ist_test and aktiv order by id limit 1) l,
       lateral (select a.einheit_id, a.variante_gruppe lz, array_agg(a.id order by a.stufe in (2, 3) desc, a.id) ids, bool_or(a.stufe in (2, 3)) mischbar
                  from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id and e.status = 'freigegeben' and e.id = schule.thema_einheit(e.thema_id)
                 where a.pool = 'uebung' and a.freigegeben and a.antworttyp = 'auswahl' and e.block_id is not null
                   and not exists (select 1 from schule.versuch v join schule.aufgabe b on b.id = v.aufgabe_id
                                    where v.lernender_id = l.id and b.einheit_id = a.einheit_id and b.variante_gruppe = a.variante_gruppe)
                 group by 1, 2 having count(*) >= 2 order by 4 desc, 1, 2 limit 11) q;
insert into schule.lerntag (lernender_id, fach, datum, zeitzone)
select distinct g.l, 'Mathematik', schule.heute_tag(g.l) - d, 'Europe/Berlin' from public.wd3_gleich g, generate_series(1, 10) d on conflict do nothing;
insert into schule.karte_stand (lernender_id, einheit_id, lernziel) select l, e, lz from public.wd3_gleich on conflict do nothing;
update schule.karte_stand k set sitzt = true, sitzt_am = now() - interval '30 days', wdh_stufe = 1, wdh_lerntage = 3, wdh_fehler = 0,
       wdh_ab = now() - interval '6 days', faellig_am = now() - interval '3 days' from public.wd3_gleich g
 where k.lernender_id = g.l and k.einheit_id = g.e and k.lernziel = g.lz and g.nr <= 3;
-- Teil C: Etappe 4 noch nicht gelandet; Teil D: Etappe 5 kurz vor der Landung, Etappe 6 früher gelandet (ohne Bonus, für die Nachbuchung)
update schule.karte_stand k set sitzt = false, gesetzt_am = null, eigene_loesungen = 0, folge = 0, gezaehlt = '{}' from public.wd3_gleich g
 where k.lernender_id = g.l and k.einheit_id = g.e and k.lernziel = g.lz and g.nr = 4;
update schule.karte_stand k set sitzt = false, gesetzt_am = null, wdh_gesetzt_am = null, gezaehlt = '{}'::jsonb, fehler_folge = 0, schwer_ok = true,
       eigene_loesungen = greatest(schule.karte_ziel(g.e, g.lz) - 1, 0), folge = greatest(least(3, schule.karte_ziel(g.e, g.lz)) - 1, 0),
       typen = coalesce((select array_agg('gl' || i) from generate_series(1, schule.karte_typen_noetig(g.e, g.lz)) i), '{}')
  from public.wd3_gleich g where k.lernender_id = g.l and k.einheit_id = g.e and k.lernziel = g.lz and g.nr = 5;
update schule.karte_stand k set sitzt = true, sitzt_am = now() - interval '20 days', gesetzt_am = null, landung = null, wdh_stufe = 2, wdh_lerntage = 7, wdh_ab = now()
  from public.wd3_gleich g where k.lernender_id = g.l and k.einheit_id = g.e and k.lernziel = g.lz and g.nr = 6;
update public.wd3_gleich g set s0 = (select count(*) from schule.sterne s where s.lernender_id = g.l and s.grund = 'wdh');
-- Teil B: Tagesrunde mit genau den Etappen 2 und 3 offen (andere Etappen einer schon vorhandenen Runde gelten als bearbeitet)
insert into schule.wdh_runde (lernender_id, tag, ziel) select l, schule.heute_tag(l), 2 from public.wd3_gleich where nr = 1 on conflict (lernender_id, tag) do update set fertig_am = null;
update schule.wdh_runde_etappe r set bearbeitet_am = coalesce(r.bearbeitet_am, now()) from public.wd3_gleich g where g.nr = 1 and r.lernender_id = g.l and r.tag = schule.heute_tag(g.l);
insert into schule.wdh_runde_etappe (lernender_id, tag, nr, einheit_id, lernziel)
select l, schule.heute_tag(l), 900 + nr, e, lz from public.wd3_gleich where nr in (2, 3)
on conflict (lernender_id, tag, einheit_id, lernziel) do update set bearbeitet_am = null;
update schule.wdh_runde w set fertig_am = null from public.wd3_gleich g where g.nr = 1 and w.lernender_id = g.l and w.tag = schule.heute_tag(g.l);
SQL

antwort() { # $1 = Etappe (nr), $2 = Aufgaben-Spalte, $3 = Gerät, $4 = Wartezeit in der Transaktion, $5 = Mischkarte (true/false); gibt die ganze Antwort aus
  "${P[@]}" <<SQL
begin;
select 'Gerät $3: ' || schule.uebung_pruefen_wd(g.l, jsonb_build_object('aufgabe_id', g.$2, 'client_id', 'gleichzeitig-$3-' || gen_random_uuid(), 'misch', ${5:-false},
         'antwort', jsonb_build_object('index', (select (a.loesung->>'index')::int from schule.aufgabe a where a.id = g.$2))))::text
  from public.wd3_gleich g where g.nr = $1;
select pg_sleep($4);
commit;
SQL
}
zwei() { # zwei Befehle gleichzeitig (der zweite 0,5 s später), jeder Prozess einzeln abgewartet
  ( eval "$1" ) > /tmp/wd3_g1.$$ 2>&1 & local p1=$!
  sleep 0.5
  ( eval "$2" ) > /tmp/wd3_g2.$$ 2>&1 & local p2=$!
  local f=0; wait $p1 || f=1; wait $p2 || f=1
  cat /tmp/wd3_g1.$$ /tmp/wd3_g2.$$
  if [ $f -ne 0 ]; then pruefen "FEHLER: ein Prozess ist abgebrochen"; fi
}

# Teil A: Etappe 1 von zwei Geräten
zwei "antwort 1 a1 A 2" "antwort 1 a2 B 0"
pruefen "$("${P[@]}" <<'SQL'
select case when k.wdh_stufe = 2 and (select count(*) from schule.sterne s where s.lernender_id = g.l and s.grund = 'wdh' and s.bezug like 'wdh:' || g.e || ':' || g.lz || ':%') = 1
            then 'ok A gleichzeitig: genau ein Fortschritt (Stufe 1 → 2), einmal Wiederholungs-Sterne'
            else 'FEHLER A gleichzeitig: Stufe ' || k.wdh_stufe end
  from public.wd3_gleich g join schule.karte_stand k on k.lernender_id = g.l and k.einheit_id = g.e and k.lernziel = g.lz where g.nr = 1;
SQL
)"

# Teil B: die zwei letzten Pflicht-Etappen der Runde gleichzeitig
zwei "antwort 2 a1 C 2" "antwort 3 a1 D 0"
pruefen "$("${P[@]}" <<'SQL'
select case when w.fertig_am is not null and (select count(*) from schule.wdh_runde_etappe r where r.lernender_id = w.lernender_id and r.tag = w.tag and r.bearbeitet_am is null) = 0
            then 'ok B gleichzeitig: Runde fertig (beide letzten Etappen bearbeitet)'
            else 'FEHLER B gleichzeitig: Runde nicht fertig (offen: ' || (select count(*) from schule.wdh_runde_etappe r where r.lernender_id = w.lernender_id and r.tag = w.tag and r.bearbeitet_am is null) || ')' end
  from public.wd3_gleich g join schule.wdh_runde w on w.lernender_id = g.l and w.tag = schule.heute_tag(g.l) where g.nr = 1;
SQL
)"

# Teil C: eine andere Sitzung bucht Sterne für dasselbe Kind, während die Antwort läuft (sie hält die Karte der Etappe 4 gesperrt)
fremd() {
  "${P[@]}" <<'SQL'
begin;
select 1 from schule.karte_stand k join public.wd3_gleich g on g.l = k.lernender_id and g.e = k.einheit_id and g.lz = k.lernziel where g.nr = 4 for update of k;
insert into schule.sterne (lernender_id, menge, grund, bezug) select l, 7, 'bonus', 'gleichzeitig-fremd-' || gen_random_uuid() from public.wd3_gleich where nr = 1;
select pg_sleep(2);
commit;
SQL
}
zwei "fremd" "antwort 4 a1 E 0" > /tmp/wd3_c.$$
cat /tmp/wd3_c.$$
C_STERNE=$(grep -o 'Gerät E: .*' /tmp/wd3_c.$$ | sed 's/^Gerät E: //' | python3 -c 'import sys,json; print(json.loads(sys.stdin.read()).get("sterne"))')
C_SOLL=$("${P[@]}" -c "select schule.sterne_regel('sterne_uebung_richtig')")
if [ "$C_STERNE" = "$C_SOLL" ]; then pruefen "ok C gleichzeitig: Antwort meldet nur ihre eigenen Sterne ($C_STERNE)"; else pruefen "FEHLER C gleichzeitig: Antwort meldet $C_STERNE statt $C_SOLL"; fi

# Teil D: Landung (Etappe 5) gleichzeitig mit der Nachbuchung (bucht Etappe 6; hält die Karte der Etappe 5 gesperrt)
S0=$("${P[@]}" -c "select coalesce(sum(s.menge), 0) from schule.sterne s join public.wd3_gleich g on g.l = s.lernender_id and g.nr = 1")
nach() {
  "${P[@]}" <<'SQL'
begin;
select 'Nachbuchung: ' || coalesce(sum(n.sterne), 0) from public.wd3_gleich g, schule.landung_bonus_nachbuchen(g.l) n where g.nr = 1;
select 1 from schule.karte_stand k join public.wd3_gleich g on g.l = k.lernender_id and g.e = k.einheit_id and g.lz = k.lernziel where g.nr = 5 for update of k;
select pg_sleep(2);
commit;
SQL
}
zwei "nach" "antwort 5 a1 F 0" > /tmp/wd3_d.$$
cat /tmp/wd3_d.$$
D_ANTWORT=$(grep -o 'Gerät F: .*' /tmp/wd3_d.$$ | sed 's/^Gerät F: //' | python3 -c 'import sys,json; j=json.loads(sys.stdin.read()); print(j.get("sterne"), (j.get("landung") or {}).get("bonus"))')
D_NACH=$(grep -o 'Nachbuchung: .*' /tmp/wd3_d.$$ | sed 's/^Nachbuchung: //')
S1=$("${P[@]}" -c "select coalesce(sum(s.menge), 0) from schule.sterne s join public.wd3_gleich g on g.l = s.lernender_id and g.nr = 1")
read -r D_STERNE D_BONUS <<<"$D_ANTWORT"
if [ "$D_BONUS" != "None" ] && [ "$D_STERNE" = "$(( C_SOLL + D_BONUS ))" ] && [ "$D_NACH" -gt 0 ] && [ "$(( S1 - S0 ))" = "$(( D_STERNE + D_NACH ))" ]; then
  pruefen "ok D gleichzeitig: Landung meldet $D_STERNE (Übung + Bonus $D_BONUS), Nachbuchung $D_NACH, Summe +$(( S1 - S0 ))"
else pruefen "FEHLER D gleichzeitig: Antwort $D_ANTWORT, Nachbuchung $D_NACH, Summe +$(( S1 - S0 ))"; fi
# Teil D2: zwei Nachbuchungen gleichzeitig, beide finden denselben fehlenden Landungs-Bonus (Etappe 9)
"${P[@]}" <<'SQL'
update schule.karte_stand k set sitzt = true, sitzt_am = now() - interval '20 days', gesetzt_am = null, landung = null, wdh_stufe = 2, wdh_lerntage = 7, wdh_ab = now()
  from public.wd3_gleich g where k.lernender_id = g.l and k.einheit_id = g.e and k.lernziel = g.lz and g.nr = 9;
SQL
nach2() { # $1 = Wartezeit in der Transaktion
  "${P[@]}" <<SQL
begin;
select 'Nachbuchung: ' || coalesce(sum(n.sterne), 0) from public.wd3_gleich g, schule.landung_bonus_nachbuchen(g.l) n where g.nr = 1;
select pg_sleep($1);
commit;
SQL
}
S0=$("${P[@]}" -c "select coalesce(sum(s.menge), 0) from schule.sterne s join public.wd3_gleich g on g.l = s.lernender_id and g.nr = 1")
zwei "nach2 2" "nach2 0" > /tmp/wd3_d2.$$
cat /tmp/wd3_d2.$$
D2_SUMME=$(grep -o 'Nachbuchung: .*' /tmp/wd3_d2.$$ | sed 's/^Nachbuchung: //' | paste -sd+ | bc)
S1=$("${P[@]}" -c "select coalesce(sum(s.menge), 0) from schule.sterne s join public.wd3_gleich g on g.l = s.lernender_id and g.nr = 1")
D2_ZEILEN=$("${P[@]}" -c "select count(*) from schule.sterne s join public.wd3_gleich g on g.l = s.lernender_id and s.grund = 'landung' and s.bezug = 'landung:' || g.e || ':' || g.lz where g.nr = 9")
if [ "$D2_ZEILEN" = "1" ] && [ "$D2_SUMME" -gt 0 ] && [ "$(( S1 - S0 ))" = "$D2_SUMME" ]; then
  pruefen "ok D2 gleichzeitig: Landungs-Bonus einmal gebucht, Meldungen zusammen $D2_SUMME = Summe +$(( S1 - S0 ))"
else pruefen "FEHLER D2 gleichzeitig: $D2_ZEILEN Bonus-Zeilen, Meldungen $D2_SUMME, Summe +$(( S1 - S0 ))"; fi

# Teil E/F/G: Etappen 7, 8, 10, 11 gelandet und fällig, je eine Mischkarte (Aufgabe a1) ausgegeben, Lage: Etappe 1
"${P[@]}" <<'SQL'
do $$ begin
  if (select count(*) from public.wd3_gleich g join schule.aufgabe a on a.id = g.a1 where g.nr in (7, 8, 10, 11) and a.stufe in (2, 3)) <> 4 then
    raise exception 'FEHLER Vorbereitung E/F/G: keine vier Etappen mit Misch-Aufgabe (Stufe 2/3)'; end if;
end $$;
update schule.karte_stand k set sitzt = true, sitzt_am = now() - interval '30 days', gesetzt_am = null, wdh_stufe = 1, wdh_lerntage = 3, wdh_fehler = 0,
       wdh_ab = now() - interval '6 days', faellig_am = now() - interval '3 days' from public.wd3_gleich g
 where k.lernender_id = g.l and k.einheit_id = g.e and k.lernziel = g.lz and g.nr in (7, 8, 10, 11);
update schule.misch_ausgabe m set verfallen_am = now() from public.wd3_gleich g
 where g.nr in (7, 8, 10, 11) and m.lernender_id = g.l and m.aufgabe_id = g.a1 and m.eingeloest_am is null and m.verfallen_am is null;
insert into schule.misch_ausgabe (lernender_id, aufgabe_id, einheit_id, lernziel)
select g.l, g.a1, h.e, h.lz from public.wd3_gleich g, public.wd3_gleich h where g.nr in (7, 8, 10, 11) and h.nr = 1
on conflict (lernender_id, aufgabe_id) where eingeloest_am is null do update set ausgegeben_am = now(), verfallen_am = null, einheit_id = excluded.einheit_id, lernziel = excluded.lernziel;
SQL
misch_lage() { # $1 = Etappe (nr): Stufe, eingelöst, verfallen, Mischkarten-Versuche, wdh-Sterne (Ausgaben der letzten Stunde)
  "${P[@]}" -c "select k.wdh_stufe || ' ' || (select count(*) from schule.misch_ausgabe m where m.lernender_id = g.l and m.aufgabe_id = g.a1 and m.eingeloest_am is not null and m.ausgegeben_am > now() - interval '1 hour')
       || ' ' || (select count(*) from schule.misch_ausgabe m where m.lernender_id = g.l and m.aufgabe_id = g.a1 and m.eingeloest_am is null and m.verfallen_am is not null and m.ausgegeben_am > now() - interval '1 hour')
       || ' ' || (select count(*) from schule.versuch v where v.lernender_id = g.l and v.aufgabe_id = g.a1 and v.misch)
       || ' ' || (select count(*) from schule.sterne s where s.lernender_id = g.l and s.grund = 'wdh' and s.bezug like 'wdh:' || g.e || ':' || g.lz || ':%')
  from public.wd3_gleich g join schule.karte_stand k on k.lernender_id = g.l and k.einheit_id = g.e and k.lernziel = g.lz where g.nr = $1"
}
misch_gueltig_aus() { grep -o "Gerät $1: .*" "$2" | sed "s/^Gerät $1: //" | python3 -c 'import sys,json; print(str((json.loads(sys.stdin.read()).get("misch") or {}).get("gueltig")).lower())'; }

# Teil E: dieselbe Mischkarte von zwei Geräten (zwei client_id)
zwei "antwort 7 a1 G 2 true" "antwort 7 a1 H 0 true" > /tmp/wd3_e.$$
cat /tmp/wd3_e.$$
E_G=$(misch_gueltig_aus G /tmp/wd3_e.$$); E_H=$(misch_gueltig_aus H /tmp/wd3_e.$$)
E_PRUEF=$(misch_lage 7)
E_ANZ=$(( $([ "$E_G" = "true" ] && echo 1 || echo 0) + $([ "$E_H" = "true" ] && echo 1 || echo 0) ))
if [ "$E_ANZ" = "1" ] && [ "$E_PRUEF" = "2 1 0 1 1" ]; then
  pruefen "ok E gleichzeitig: eine Mischkarte, zwei Geräte – genau eine Bestätigung (G=$E_G, H=$E_H), ein Fortschritt (Stufe 1 → 2), einmal eingelöst"
else pruefen "FEHLER E gleichzeitig: G=$E_G, H=$E_H, Stufe/eingelöst/verfallen/Misch-Versuche/wdh-Sterne $E_PRUEF (soll genau eine Bestätigung, 2 1 0 1 1)"; fi

# Teil F: Gerät I beantwortet eine andere Aufgabe der Etappe 8 (hält 2 s), Gerät J löst währenddessen die Mischkarte der Etappe 8 ein.
# Reihenfolgeunabhängig: gewinnt J die Sperre doch zuerst, ist die Mischkarte gültig und eingelöst; sonst weder gültig noch eingelöst. Fortschritt genau einmal.
zwei "antwort 8 a2 I 2" "antwort 8 a1 J 0 true" > /tmp/wd3_f.$$
cat /tmp/wd3_f.$$
F_J=$(misch_gueltig_aus J /tmp/wd3_f.$$)
F_PRUEF=$(misch_lage 8)
if { [ "$F_J" = "false" ] && [ "$F_PRUEF" = "2 0 1 0 1" ]; } || { [ "$F_J" = "true" ] && [ "$F_PRUEF" = "2 1 0 1 1" ]; }; then
  pruefen "ok F gleichzeitig: andere Aufgabe derselben Etappe – Mischkarte nur gültig, wenn sie wirklich zuerst kam (J=$F_J), ein Fortschritt"
else pruefen "FEHLER F gleichzeitig: J=$F_J, Stufe/eingelöst/verfallen/Misch-Versuche/wdh-Sterne $F_PRUEF (soll false + 2 0 1 0 1 oder true + 2 1 0 1 1)"; fi

# Teil G1/G2: Mischkarten-Antwort und normale Antwort zur SELBEN Aufgabe (a1) gleichzeitig, beide Reihenfolgen (FP-S 4: gleiche Sperrfolge, kein Deadlock)
g_pruefen() { # $1 = Teil, $2 = Etappe, $3 = Gerät mit Mischkarte, $4 = Ausgabe-Datei
  local GU; GU=$(misch_gueltig_aus "$3" "$4"); local GP; GP=$(misch_lage "$2")
  if { [ "$GU" = "true" ] && [ "$GP" = "2 1 0 1 1" ]; } || { [ "$GU" = "false" ] && [ "$GP" = "2 0 1 0 1" ]; }; then
    pruefen "ok $1 gleichzeitig: Mischkarte gegen normale Antwort zur selben Aufgabe – kein Deadlock, gültig=$GU, gültig ⇔ eingelöst (sonst verfallen), ein Fortschritt"
  else pruefen "FEHLER $1 gleichzeitig: gültig=$GU, Stufe/eingelöst/verfallen/Misch-Versuche/wdh-Sterne $GP (soll true + 2 1 0 1 1 oder false + 2 0 1 0 1)"; fi
}
zwei "antwort 10 a1 K 2 true" "antwort 10 a1 L 0" > /tmp/wd3_g1x.$$   # Mischkarte zuerst
cat /tmp/wd3_g1x.$$
g_pruefen G1 10 K /tmp/wd3_g1x.$$
zwei "antwort 11 a1 M 2" "antwort 11 a1 N 0 true" > /tmp/wd3_g2x.$$   # normale Antwort zuerst
cat /tmp/wd3_g2x.$$
g_pruefen G2 11 N /tmp/wd3_g2x.$$
rm -f /tmp/wd3_g1.$$ /tmp/wd3_g2.$$ /tmp/wd3_c.$$ /tmp/wd3_d.$$ /tmp/wd3_d2.$$ /tmp/wd3_e.$$ /tmp/wd3_f.$$ /tmp/wd3_g1x.$$ /tmp/wd3_g2x.$$

if grep -q "FEHLER" <<<"$AUSGABE" || [ "$(grep -c '^ok' <<<"$AUSGABE")" -ne 9 ]; then echo "Ergebnis: FEHLER"; exit 1; fi
echo "Ergebnis: ok"
