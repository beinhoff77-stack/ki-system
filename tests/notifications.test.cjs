const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
function worker(){
 const events={},shown=[],opened=[],navigated=[];
 const existing={url:'https://example.com/ki-system/#/reisen',navigate:async url=>navigated.push(url),focus:async()=>{}};
 const self={registration:{scope:'https://example.com/ki-system/',showNotification:async(...args)=>shown.push(args)},addEventListener:(name,cb)=>events[name]=cb,clients:{matchAll:async()=>[existing],openWindow:async url=>opened.push(url)}};
 vm.runInNewContext(fs.readFileSync(require('node:path').join(__dirname,'../sw.js'),'utf8'),{self,URL,Set});
 return {events,shown,opened,navigated,self};
}
test('Push displays even with an existing client and opens the internal Werkstatt link',async()=>{
 const w=worker();let pending;
 w.events.push({data:{json:()=>({titel:'Entscheidung',text:'Bitte prüfen',link:'#/werkstatt/80'})},waitUntil:p=>pending=p});await pending;
 assert.equal(w.shown.length,1);assert.equal(w.shown[0][1].data.url,'https://example.com/ki-system/#/werkstatt/80');
 let closed=false;w.events.notificationclick({notification:{data:w.shown[0][1].data,close:()=>closed=true},waitUntil:p=>pending=p});await pending;
 assert(closed);assert.deepEqual(w.navigated,['https://example.com/ki-system/#/werkstatt/80']);
});
test('Malformed push is visible; external and out-of-scope targets never open',async()=>{
 const w=worker();let pending;
 w.events.push({data:{json:()=>{throw Error('malformed');}},waitUntil:p=>pending=p});await pending;
 assert.equal(w.shown[0][0],'KI-System');
 for(const url of ['https://attacker.example/','javascript:alert(1)','https://example.com/other/']){
   w.events.notificationclick({notification:{data:{url},close(){}},waitUntil:p=>pending=p});await pending;
 }
 assert(w.navigated.every(url=>url==='https://example.com/ki-system/#/meldungen'));
 w.self.clients.matchAll=async()=>[];
 w.events.notificationclick({notification:{data:{url:'#/meldungen'},close(){}},waitUntil:p=>pending=p});await pending;
 assert.deepEqual(w.opened,['https://example.com/ki-system/#/meldungen']);
});
