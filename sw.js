// Service Worker: hält nur die App-Hülle vor (Dateien dieser Seite). Daten kommen immer live von app-api.
const CACHE = 'ki-system-v14';
const HUELLE = ['./', './index.html', './app.js', './style.css', './manifest.webmanifest', './icon.svg', './icon-180.png', './icon-512.png'];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(HUELLE)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k !== CACHE).map((k) => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  if (url.origin !== self.location.origin || e.request.method !== 'GET') return; // API und CDN: immer Netz
  // Netz zuerst, bei Ausfall aus dem Cache (so kommen neue Versionen sofort an).
  e.respondWith(
    fetch(e.request).then((r) => { if (r.ok) { const kopie = r.clone(); caches.open(CACHE).then((c) => c.put(e.request, kopie)); } return r; })
      .catch(() => caches.match(e.request).then((r) => r || (e.request.mode === 'navigate' ? caches.match('./index.html') : Response.error())))
  );
});
