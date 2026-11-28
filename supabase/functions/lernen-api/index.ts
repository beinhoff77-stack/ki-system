// lernen-api (Werkstatt #150, Claude): Schnittstelle der App für „Lernen Schule“.
// Gleiche Anmeldung wie app-api (Sitzungs-Token -> app.sitzung), ruft nur die api.schule_*-Funktionen als council_mcp auf.
// Die Datenbank prüft Zugriff (schule.zugriff) und Sichtbarkeit (Entwürfe nur fürs Testkind) bei jeder Aktion.
// v0.10.0 (vorbereitet, NICHT ausgeliefert; erst nach ADVENT-S = 20261209_advent_s.sql in der Datenbank): Adventskalender – Kind: schule_advent_stand,
//         schule_advent_oeffnen, schule_advent_tuer_lesen, schule_advent_gutscheine, schule_advent_einloesen, schule_advent_tauschen; Eltern: schule_advent_eltern,
//         schule_advent_belegung_lesen, schule_advent_belegung_setzen, schule_advent_gutschein_eltern, schule_advent_protokoll. Rechte prüft die Datenbank
//         (Kind nur eigenes, Eltern-Aktionen nur Eltern, Öffnen/Einlösen/Tauschen durch Eltern nur fürs Testkind). Schnittstelle: inhalte/design/advent/server.md.
//         Enthält 0.9.6 (falls noch nicht ausgeliefert, kommt es mit).
// v0.9.6 (vorbereitet, NICHT ausgeliefert; erst nach WW-S3 in der Datenbank): schule_fehler_abhaken in zwei Formen – Markieren {lernender_id, versuch_ids}
//         oder Zurückholen {lernender_id, zurueck: true, markierung_ids} (holt genau diese Markierungen zurück; Zurückholen über versuch_ids gibt es nicht
//         mehr). Antworten mit stand, geaendert_ids, markierung_ids. GET /hilfe nennt die beiden Formen im Feld „hinweis“. Sonst unverändert gegenüber 0.9.5.
// v0.9.5 (vorbereitet, NICHT ausgeliefert; erst nach WW-S2 in der Datenbank): schule_wackelt_analyse, schule_fehler_abhaken (nur Eltern/Lehrer,
//         „Was wackelt“: Analyse lesen, Fehler abhaken/zurücknehmen; ohne Wirkung auf die Lernlogik). Prüfung der Rechte in der Datenbank.
//         Ersetzt den nie ausgelieferten Entwurf 0.9.4 (mit Nachüben, vom Nutzer gestrichen). Ausgeliefert ist 0.9.3.
// v0.9.3: schule_reise_karte (RD-S, Reisekarte je Kind: Kontinente → Flüge → Städte, nächster Start, Quellen); schule_expedition_spaeter (EX-S, „Später“ bis zum nächsten Lerntag).
// v0.9.2: schule_wackelt_lesen / schule_wackelt_setzen (LW-S, „Was wackelt“ mit gespeichertem Status).
// v0.7.0: schule_lernstand (Lernstand je Lernkarte für Eltern/Lehrer).
// v0.6.0: schule_lehrplan_uebersicht (alle Themen je Schulart/Klasse mit Inhaltsstand), schule_inhalt_lesen (Inhalte prüfen), schule_kind_setzen (Schulart/Klasse).
// v0.5.1: schule_wiederholung (fällige Lernkarten).
// v0.5.0: eigene Lern-Zugänge (Code -> Lern-Sitzung, Schlüssel 'lern:<hash>' gilt nur für schule-Funktionen), Themenplan, Rückmeldungen, Zugänge.
// v0.4.0: Merkheft/Etappenfortschritt. v0.3.0: Elternübersicht. v0.2.0: Sterne-Konto, Belohnungen einlösen/pflegen, Look wählen.
// Wege: POST /lernen-api/aktion  Bearer-Token, { aktion, daten } -> { ok, ergebnis }
//       GET  /lernen-api/hilfe   Liste der Aktionen
import 'jsr:@supabase/functions-js/edge-runtime.d.ts'
import { Hono } from 'npm:hono@^4.9.7'
import postgres from 'npm:postgres@3.4.5'

const sql = postgres(Deno.env.get('SUPABASE_DB_URL')!, { prepare: false, max: 3, idle_timeout: 20 })
const VERSION = '0.10.0'

const AKTIONEN: Record<string, string[]> = {
  schule_uebersicht: [],
  schule_einheit_lesen: ['lernender_id', 'einheit_id'],
  schule_uebung_pruefen: ['lernender_id', 'aufgabe_id', 'antwort', 'client_id?', 'hilfe?'],
  schule_test_starten: ['lernender_id', 'einheit_id', 'art?'],
  schule_test_antwort: ['lernender_id', 'sitzung_id', 'aufgabe_id', 'antwort', 'client_id?'],
  schule_test_abschliessen: ['lernender_id', 'sitzung_id'],
  schule_konto: ['lernender_id'],
  schule_einloesen: ['lernender_id', 'belohnung_id'],
  schule_look_setzen: ['lernender_id', 'stil', 'welt'],
  schule_belohnung_setzen: ['id?', 'titel?', 'beschreibung?', 'kosten_sterne?', 'kosten_stempel?', 'lernender_id?', 'aktiv?'],
  schule_einloesung_entscheiden: ['id', 'status'],
  schule_eltern: [],
  schule_merkheft: ['lernender_id'],
  schule_ich: [],
  schule_plan_lesen: ['lernender_id'],
  schule_plan_setzen: ['lernender_id', 'eintraege', 'revision?'],
  schule_notiz_setzen: ['lernender_id', 'text'],
  schule_zugaenge: [],
  schule_zugang_anlegen: ['name', 'rolle', 'lernender_id?'],
  schule_zugang_sperren: ['id'],
  schule_rueckmeldung_geben: ['art', 'text', 'block_id?', 'einheit_id?', 'lernziel?', 'aufgabe_id?', 'lernender_id?'],
  schule_rueckmeldungen: [],
  schule_wiederholung: ['lernender_id', 'anzahl?'],
  schule_wiederholung_runde_fertig: ['lernender_id'],
  schule_landung_nachbuchung_gesehen: ['lernender_id'],
  schule_wackelt_lesen: ['lernender_id'],
  schule_wackelt_setzen: ['lernender_id', 'thema_id', 'status', 'einheit_id?', 'lernziel?'],
  schule_reise_karte: ['lernender_id'],
  schule_expedition_spaeter: ['lernender_id', 'expedition_id'],
  schule_lehrplan_uebersicht: [],
  schule_lehrplan_matrix: ['lernender_id?', 'mit_testkind?'],
  schule_lehrplan_thema: ['thema_id', 'lernender_id?'],
  schule_inhalt_lesen: ['einheit_id'],
  schule_kind_setzen: ['lernender_id', 'schulart?', 'klasse?'],
  schule_lernstand: ['lernender_id'],
  schule_wackelt_analyse: ['lernender_id', 'tage?', 'erledigt?'],
  // zwei Formen (siehe HINWEISE): Markieren lernender_id + versuch_ids; Zurückholen lernender_id + zurueck (true) + markierung_ids
  schule_fehler_abhaken: ['lernender_id', 'versuch_ids?', 'zurueck?', 'markierung_ids?'],
  // ADVENT-S (0.10.0): Adventskalender
  schule_advent_stand: ['lernender_id'],
  schule_advent_oeffnen: ['lernender_id', 'client_id'],
  schule_advent_tuer_lesen: ['lernender_id', 'nr'],
  schule_advent_gutscheine: ['lernender_id'],
  schule_advent_einloesen: ['lernender_id', 'gutschein_id'],
  schule_advent_tauschen: ['lernender_id', 'tauschkarte_id', 'mein_gutschein_id', 'fremder_gutschein_id', 'client_id'],
  schule_advent_eltern: ['protokoll?'],
  schule_advent_belegung_lesen: ['lernender_id?'],
  schule_advent_belegung_setzen: ['lernender_id?', 'lernender_ids?', 'tueren', 'nur_geschlossene?'],
  schule_advent_gutschein_eltern: ['gutschein_id', 'aktion'],
  schule_advent_protokoll: ['lernender_id?', 'anzahl?'],
}

// Zusatz für GET /hilfe bei Aktionen mit mehreren Aufrufformen (die Parameterliste allein kann „entweder – oder“ nicht ausdrücken)
const HINWEISE: Record<string, string> = {
  schule_fehler_abhaken: 'Markieren: lernender_id, versuch_ids. Zurückholen: lernender_id, zurueck = true, markierung_ids (ohne versuch_ids).',
  schule_advent_belegung_setzen: 'Ein Kind: lernender_id. Beide zugleich: lernender_ids [..]. tueren: [{nr, art, variante?, titel?, text?, sterne?, motiv?}]. nur_geschlossene = true überspringt offene Türchen.',
  schule_advent_gutschein_eltern: 'aktion: einloesen | zurueckholen (Gutschein, Tauschkarte) oder erledigt | noch_nicht (Krampus).',
}

const CORS = { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'Content-Type, Authorization', 'Access-Control-Allow-Methods': 'GET, POST, OPTIONS' }
const app = new Hono({ strict: false }).basePath('/lernen-api')
app.use('*', async (c, next) => {
  if (c.req.method === 'OPTIONS') return c.body(null, 204, CORS)
  await next()
  for (const [k, v] of Object.entries(CORS)) c.header(k, v)
})

function fehlertext(e: any): string {
  if (e?.code === 'P0001') return String(e.message)
  console.error('lernen-api Fehler', e?.code, e?.message)
  return 'Interner Fehler – bitte später erneut versuchen.'
}

function bearer(c: any): string {
  return (c.req.header('authorization') ?? '').replace(/^Bearer\s+/i, '').trim()
}

// App-Sitzung (Eltern, ganze App) oder Lern-Sitzung (nur Lernen). Lern-Sitzungen kennt app-api nicht.
async function sitzung(c: any): Promise<string | null> {
  const t = bearer(c)
  if (!t) return null
  const [row] = await sql`select app.sitzung(${t}) as h`
  if (row?.h) return row.h
  const [l] = await sql`select schule.lern_sitzung_pruefen(${t}) as h`
  return l?.h ?? null
}

app.post('/anmelden', async (c) => {
  let b: any
  try { b = await c.req.json() } catch { return c.json({ ok: false, fehler: 'Ungültiges JSON' }, 400) }
  const code = String(b?.code ?? '').slice(0, 40)
  if (!code.trim()) return c.json({ ok: false, fehler: 'Code fehlt' }, 400)
  try {
    const [row] = await sql`select schule.lern_anmelden(${code}) as r`
    return c.json({ ok: true, ergebnis: row.r })
  } catch (e) { return c.json({ ok: false, fehler: fehlertext(e) }, 400) }
})

app.post('/abmelden', async (c) => {
  const t = bearer(c)
  if (t) { try { await sql`select schule.lern_abmelden(${t})` } catch (e) { console.error('abmelden', e) } }
  return c.json({ ok: true })
})

app.get('/hilfe', (c) => c.json({ ok: true, version: VERSION, aktionen: Object.entries(AKTIONEN).map(([aktion, parameter]) => ({ aktion, parameter, ...(HINWEISE[aktion] ? { hinweis: HINWEISE[aktion] } : {}) })) }))

app.post('/aktion', async (c) => {
  const h = await sitzung(c)
  if (!h) return c.json({ ok: false, fehler: 'Nicht angemeldet' }, 401)
  let b: any
  try { b = await c.req.json() } catch { return c.json({ ok: false, fehler: 'Ungültiges JSON' }, 400) }
  const name = String(b?.aktion ?? '')
  if (!(name in AKTIONEN)) return c.json({ ok: false, fehler: `Unbekannte Aktion "${name}"` }, 400)
  const daten = b?.daten && typeof b.daten === 'object' && !Array.isArray(b.daten) ? b.daten : {}
  try {
    const r = await sql.begin(async (tx) => {
      await tx`set local role council_mcp`
      const z = await tx.unsafe(`select api.${name}($1::text, $2::text::jsonb) as r`, [h, JSON.stringify(daten)])
      return z[0].r
    })
    return c.json({ ok: true, ergebnis: r })
  } catch (e) { return c.json({ ok: false, fehler: fehlertext(e) }, 400) }
})

Deno.serve(app.fetch)
