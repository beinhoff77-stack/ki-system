// Service Worker: hält nur die App-Hülle vor (Dateien dieser Seite). Daten kommen immer live von app-api.
const CACHE_PREFIX = 'ki-system:' + self.registration.scope + ':';
const CACHE = CACHE_PREFIX + 'v57';
const HUELLE = ['./', './index.html', './stay-compare.js?v=0.36.3', './stay-refresh.js?v=0.36.3', './stay-workplace.js?v=0.36.3', './stay-notifications.js?v=0.36.3', './stay-photos.js?v=0.36.3', './stay-trips.js?v=0.36.3', './stay-review.js?v=0.36.3', './stay-desk.js?v=0.36.3', './app.js?v=0.36.3', './stay-tools.js?v=0.36.3', './stay-research.js?v=0.36.3', './stay-form.js?v=0.36.3', './stay-details.js?v=0.36.3', './stay-districts.js?v=0.36.3', './vendor/leaflet-1.9.4/leaflet.js', './vendor/leaflet-1.9.4/leaflet.css', './style.css?v=0.36.3', './manifest.webmanifest', './icon.svg', './icon-180.png', './icon-512.png'];
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
