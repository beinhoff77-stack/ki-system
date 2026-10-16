// Service Worker: hält nur die App-Hülle vor (Dateien dieser Seite). Daten kommen immer live von app-api.
const CACHE_PREFIX = 'ki-system:' + self.registration.scope + ':';
const CACHE = CACHE_PREFIX + 'v21';
const HUELLE = ['./', './index.html', './app.js?v=0.14.0', './stay-tools.js?v=0.14.0', './stay-research.js?v=0.14.0', './stay-form.js?v=0.14.0', './stay-details.js?v=0.14.0', './vendor/leaflet-1.9.4/leaflet.js', './vendor/leaflet-1.9.4/leaflet.css', './style.css?v=0.14.0', './manifest.webmanifest', './icon.svg', './icon-180.png', './icon-512.png'];
const HUELLE_URLS = new Set(HUELLE.map(path => new URL(path, self.registration.scope).href));

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(HUELLE.map(path => new Request(new URL(path, self.registration.scope), { cache: 'no-cache' })))).then(() => self.skipWaiting()));
});
self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k.startsWith(CACHE_PREFIX) && k !== CACHE).map((k) => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  url.hash = ''; // Hash-Routen gehören zur gleichen App-Hülle.
  if (e.request.method !== 'GET' || !HUELLE_URLS.has(url.href)) return; // Nur die explizite App-Hülle speichern.
  // Netz zuerst, bei Ausfall aus dem Cache (so kommen neue Versionen sofort an).
  e.respondWith(
    fetch(e.request, { cache: 'no-cache' }).then((r) => {
      if (r.ok) { const kopie = r.clone(); e.waitUntil(caches.open(CACHE).then((c) => c.put(e.request, kopie))); }
      return r;
    }).catch(async () => {
      const cache = await caches.open(CACHE);
      return await cache.match(e.request) || (e.request.mode === 'navigate' ? await cache.match(new URL('./index.html', self.registration.scope).href) : null) || Response.error();
    })
  );
});
