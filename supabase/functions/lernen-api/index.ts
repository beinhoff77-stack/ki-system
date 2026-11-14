// lernen-api (Werkstatt #150, Claude): Schnittstelle der App für „Lernen Schule“.
// Gleiche Anmeldung wie app-api (Sitzungs-Token -> app.sitzung), ruft nur die api.schule_*-Funktionen als council_mcp auf.
// Die Datenbank prüft Zugriff (schule.zugriff) und Sichtbarkeit (Entwürfe nur fürs Testkind) bei jeder Aktion.
// Wege: POST /lernen-api/aktion  Bearer-Token, { aktion, daten } -> { ok, ergebnis }
//       GET  /lernen-api/hilfe   Liste der Aktionen
import 'jsr:@supabase/functions-js/edge-runtime.d.ts'
import { Hono } from 'npm:hono@^4.9.7'
import postgres from 'npm:postgres@3.4.5'

const sql = postgres(Deno.env.get('SUPABASE_DB_URL')!, { prepare: false, max: 3, idle_timeout: 20 })
const VERSION = '0.1.0'

const AKTIONEN: Record<string, string[]> = {
  schule_uebersicht: [],
  schule_einheit_lesen: ['lernender_id', 'einheit_id'],
  schule_uebung_pruefen: ['lernender_id', 'aufgabe_id', 'antwort', 'client_id?', 'hilfe?'],
  schule_test_starten: ['lernender_id', 'einheit_id', 'art?'],
  schule_test_antwort: ['lernender_id', 'sitzung_id', 'aufgabe_id', 'antwort', 'client_id?'],
  schule_test_abschliessen: ['lernender_id', 'sitzung_id'],
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

async function sitzung(c: any): Promise<string | null> {
  const t = (c.req.header('authorization') ?? '').replace(/^Bearer\s+/i, '').trim()
  if (!t) return null
  const [row] = await sql`select app.sitzung(${t}) as h`
  return row?.h ?? null
}

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
