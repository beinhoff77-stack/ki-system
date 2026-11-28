// Service Worker: hält nur die App-Hülle vor (Dateien dieser Seite). Daten kommen immer live von app-api.
const CACHE_PREFIX = 'ki-system:' + self.registration.scope + ':';
const CACHE = CACHE_PREFIX + 'v189';
const HUELLE = ['./', './index.html', './stay-compare.js?v=0.96.0', './stay-refresh.js?v=0.96.0', './stay-workplace.js?v=0.96.0', './stay-notifications.js?v=0.96.0', './stay-photos.js?v=0.96.0', './stay-trips.js?v=0.96.0', './stay-review.js?v=0.96.0', './stay-desk.js?v=0.96.0', './app.js?v=0.96.0', './highlights.js?v=0.96.0', './roadbook.js?v=0.96.0', './lernen-welt.js?v=0.96.0', './lernen.js?v=0.96.0', './lernen-regeln.js?v=0.96.0', './lernen-regeln.css?v=0.96.0', './stay-tools.js?v=0.96.0', './stay-research.js?v=0.96.0', './stay-form.js?v=0.96.0', './stay-details.js?v=0.96.0', './stay-districts.js?v=0.96.0', './vendor/leaflet-1.9.4/leaflet.js', './vendor/leaflet-1.9.4/leaflet.css', './style.css?v=0.96.0', './vendor/schriften/space-grotesk.woff2', './vendor/schriften/jetbrains-mono.woff2', './manifest.webmanifest', './icon.svg', './icon-180.png', './icon-512.png'];
const HUELLE_URLS = new Set(HUELLE.map(path => new URL(path, self.registration.scope).href));
// 1175: Version dieser Hülle (alle ?v= in HUELLE gleich, Test prüft das). Release-Regel: inhalte/plan/ladezeiten.md, Abschnitt „Release-Regel“.
const HUELLE_VERSION = (HUELLE.find((p) => p.includes('?v=')) || '').split('?v=')[1] || null;

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(HUELLE.map(path => new Request(new URL(path, self.registration.scope), { cache: 'no-cache' })))).then(() => self.skipWaiting()));
});
self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k.startsWith(CACHE_PREFIX) && k !== CACHE).map((k) => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  url.hash = ''; // Hash-Routen gehören zur gleichen App-Hülle.
  // RK-App: Kartendateien (karte/*.json, karte/flaggen/*.svg) zusätzlich zwischenspeichern – Netz zuerst, bei schwachem Netz aus dem Cache
  // JW-App: Wortliste der Jugendwort-Sticker (daten/jugendwoerter.json) ebenso – Netz zuerst, sonst aus dem Cache
  // RU-App: daten/regeln-universum.json (606 kB) steht bewusst NICHT in der Hülle – gespeichert wird sie hier beim ersten Öffnen des Regel-Universums
  const karte = e.request.method === 'GET' && url.origin === new URL(self.registration.scope).origin && ['karte/', 'daten/'].some((d) => url.pathname.startsWith(new URL(d, self.registration.scope).pathname));
  const daten = karte && url.pathname.startsWith(new URL('daten/', self.registration.scope).pathname); // RU-App: nur statische Datendateien (daten/)
  if (e.request.method !== 'GET' || (!HUELLE_URLS.has(url.href) && !karte)) return; // Nur die App-Hülle und die Kartendateien speichern.
  // TEMPO: Versionierte Hüllen-Dateien (…?v=<version>, nur aus der Liste HUELLE) ändern sich nie unter derselben Adresse – ein neues Release bringt neue
  // Adressen (index.html, Netz zuerst) und einen neuen Cache-Namen (diese Datei, install lädt alles frisch). Deshalb hier zuerst aus dem Cache dieser Version,
  // nur wenn sie dort fehlt aus dem Netz. index.html, ./, Bilder ohne Version, karte/ und daten/ bleiben „Netz zuerst“.
  if (HUELLE_VERSION && HUELLE_URLS.has(url.href) && url.searchParams.get('v') === HUELLE_VERSION) { // nur genau die Version dieser Hülle
    e.respondWith(caches.open(CACHE).then((c) => c.match(e.request)).then((treffer) => treffer || fetch(e.request, { cache: 'no-cache' }).then((r) => {
      if (r.ok) { const kopie = r.clone(); e.waitUntil(caches.open(CACHE).then((c) => c.put(e.request, kopie))); }
      return r;
    })));
    return;
  }
  // Netz zuerst, bei Ausfall aus dem Cache (so kommen neue Versionen sofort an).
  e.respondWith(
    fetch(e.request, { cache: 'no-cache' }).then(async (r) => {
      if (r.ok) { const kopie = r.clone(); e.waitUntil(caches.open(CACHE).then((c) => c.put(e.request, kopie))); return r; }
      // RU-App (Werkstatt 1093): nur daten/ – vorübergehender Serverfehler (5xx) → gespeicherte Fassung, falls da; Datei entfernt (404/410) → Eintrag löschen.
      // Alle anderen Antworten (übrige 4xx, Hülle, karte/) gehen unverändert durch wie vor 0.96.0.
      if (daten && r.status >= 500) return (await (await caches.open(CACHE)).match(e.request)) || r;
      if (daten && (r.status === 404 || r.status === 410)) await (await caches.open(CACHE)).delete(e.request);
      return r;
    }).catch(async () => {
      const cache = await caches.open(CACHE);
      return await cache.match(e.request) || (e.request.mode === 'navigate' ? await cache.match(new URL('./index.html', self.registration.scope).href) : null) || Response.error();
    })
  );
});

function notificationTarget(value){
  const base=new URL(self.registration.scope),fallback=new URL('#/meldungen',base).href;
  try{const target=new URL(value||fallback,base);return target.origin===base.origin&&target.pathname.startsWith(base.pathname)?target.href:fallback;}catch{return fallback;}
}
self.addEventListener('push',event=>{
  let payload={};try{payload=event.data?.json()||{};}catch{/* Always display a notification, including malformed pushes. */}
  if(!payload||typeof payload!=='object')payload={};
  event.waitUntil(self.registration.showNotification(typeof payload.titel==='string'?payload.titel:'KI-System',{
    body:typeof payload.text==='string'?payload.text:'Neue Mitteilung im Posteingang.',
    icon:new URL('icon-180.png',self.registration.scope).href,
    data:{url:notificationTarget(payload.link||payload.url)}
  }));
});
self.addEventListener('notificationclick',event=>{
  event.notification.close();const url=notificationTarget(event.notification.data?.url);
  event.waitUntil((async()=>{
    const windows=await self.clients.matchAll({type:'window',includeUncontrolled:true});
    const scope=new URL(self.registration.scope);
    const existing=windows.find(c=>{try{const u=new URL(c.url);return u.origin===scope.origin&&u.pathname.startsWith(scope.pathname);}catch{return false;}});
    if(existing){await existing.navigate(url);await existing.focus();}else await self.clients.openWindow(url);
  })());
});
