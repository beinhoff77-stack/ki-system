document.querySelectorAll('[data-regel]').forEach((k) => k.addEventListener('click', () => oeffneRegel(+k.dataset.regel, P.get('kontext') || 'frei', true)));
document.querySelector('.kopf-zurueck').addEventListener('click', () => { location.href = 'uebersicht-a.html?' + P.toString(); });
entwurfsSchalter(SEITEN);
if (P.get('auf') !== '0') setTimeout(() => oeffneRegel(+(P.get('auf') || 4), P.get('kontext') || 'frei', true), 50);
