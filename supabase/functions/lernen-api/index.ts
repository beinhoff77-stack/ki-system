// lernen-api (Werkstatt #150, Claude): Schnittstelle der App für „Lernen Schule“.
// Gleiche Anmeldung wie app-api (Sitzungs-Token -> app.sitzung), ruft nur die api.schule_*-Funktionen als council_mcp auf.
// Die Datenbank prüft Zugriff (schule.zugriff) und Sichtbarkeit (Entwürfe nur fürs Testkind) bei jeder Aktion.
// v0.5.0: eigene Lern-Zugänge (Code -> Lern-Sitzung, Schlüssel 'lern:<hash>' gilt nur für schule-Funktionen), Themenplan, Rückmeldungen, Zugänge.
// v0.4.0: Merkheft/Etappenfortschritt. v0.3.0: Elternübersicht. v0.2.0: Sterne-Konto, Belohnungen einlösen/pflegen, Look wählen.
// Wege: POST /lernen-api/aktion  Bearer-Token, { aktion, daten } -> { ok, ergebnis }
//       GET  /lernen-api/hilfe   Liste der Aktionen
import 'jsr:@supabase/functions-js/edge-runtime.d.ts'
import { Hono } from 'npm:hono@^4.9.7'
import postgres from 'npm:postgres@3.4.5'

const sql = postgres(Deno.env.get('SUPABASE_DB_URL')!, { prepare: false, max: 3, idle_timeout: 20 })
const VERSION = '0.5.0'

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

app.get('/hilfe', (c) => c.json({ ok: true, version: VERSION, aktionen: Object.entries(AKTIONEN).map(([aktion, parameter]) => ({ aktion, parameter })) }))

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
