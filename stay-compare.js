async function tripCompare(hits){
 if(hits.length<2||hits.length>4)return;
 const {d,body,status}=tripDialog('Unterkünfte vergleichen');status.textContent='Vergleich wird geladen …';
 try{const r=await tripCall('unterkunft_vergleich',{treffer_ids:hits.map(t=>t.treffer_id)});if(!d.isConnected)return;
  if(r.ok!==true||!Array.isArray(r.unterkuenfte)||!Array.isArray(r.zeilen)||r.unterkuenfte.length!==hits.length||r.unterkuenfte.some(t=>!hits.some(h=>h.treffer_id===t.treffer_id)))throw Error('Vergleich unvollständig.');
  const different=el('input',{type:'checkbox',checked:true}),tableBox=el('div',{class:'table-scroll',tabindex:0,'aria-label':'Vergleichstabelle'});
  const headings=r.unterkuenfte.map(t=>el('th',{scope:'col'},t.kennung+' · '+t.name,el('p',{class:'small'},fmtDate(t.anreise)+'–'+fmtDate(t.abreise)),t.preis_geschaetzt?el('p',{class:'small'},'Preis geschätzt'):null));
  function draw(){const table=el('table',{class:'decision-table'},el('thead',{},el('tr',{},el('th',{scope:'col'},'Merkmal'),headings))),rows=el('tbody');
   for(const f of r.zeilen){if(different.checked&&f.gleich===true)continue;
    rows.append(el('tr',{},el('th',{scope:'row'},f.label),...(Array.isArray(f.werte)?f.werte:[]).map((v,i)=>el('td',{class:!r.warnung&&f.besser===r.unterkuenfte[i]?.kennung?'comparison-best':''},v==null?'unbekannt':typeof v==='boolean'?(v?'Ja':'Nein'):String(v)+(f.einheit?' '+f.einheit:'')))));
   }table.append(rows);tableBox.replaceChildren(table);}
  different.onchange=draw;
  body.replaceChildren(...[r.warnung?el('p',{class:'warning',role:'alert'},r.warnung):null,el('label',{},different,' Nur Unterschiede und offene Angaben'),el('ul',{},(r.unterschiede||[]).filter(x=>!r.warnung||!['preis_gesamt','preis_nacht'].includes(x.feld)).map(x=>el('li',{},x.text))),el('p',{class:'small'},'↔ Tabelle seitlich wischen, um alle Unterkünfte zu vergleichen.'),tableBox,el('p',{class:'small'},r.hinweis||'Unbekannte Werte bleiben unbekannt.'),el('button',{type:'button',onclick:()=>tripSelectionMap(hits)},'Lage dieser Auswahl vergleichen')].filter(node=>node!=null));
  draw();status.textContent='';
 }catch(e){if(d.isConnected)status.textContent=e.message;}
}
function tripSelectionMap(hits){
 if(!hits.length)return;
 const {d,body}=tripDialog('Lage der Auswahl vergleichen');body.append(el('p',{},hits.length+' ausgewählte Unterkünfte. Fehlende Koordinaten werden nicht geschätzt.'));
 const map=sucheKarte(body,()=>{},t=>el('div',{},el('strong',{},t.name),el('p',{},stayField(t,'gehzeit',{})),el('a',{href:'#/suche/'+t.suchauftrag_id+'?treffer='+t.treffer_id},'Unterkunft öffnen')),{includeExcluded:true});
 map.update(hits,{});d.addEventListener('close',()=>map.destroy());
}
