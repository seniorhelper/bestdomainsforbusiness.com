/* Best Domains for Business — domain finder, search engine, inquiry modal, concierge.
   One shared file. Inventory loads from /assets/data/domains.json (built by _build/build.py).
   No tracking, no third-party calls except FormSubmit when a visitor sends a form. */
(function(){
"use strict";
var DATA_URL="/assets/data/domains.json?v=b114903b1d";
var TEL="1-800-481-8638", TELH="tel:+18004818638";
var dataP=null, DB=null;

/* ---------------- data ---------------- */
function load(){
  if(dataP) return dataP;
  dataP=fetch(DATA_URL,{credentials:"same-origin"}).then(function(r){
    if(!r.ok) throw new Error("inventory "+r.status); return r.json();
  }).then(function(j){ DB=prep(j); return DB; });
  dataP.catch(function(){ dataP=null; });
  return dataP;
}
function prep(j){
  var vocab={};
  var recs=j.d.map(function(r,i){
    var sld=r[0].split(".")[0], tld=r[0].slice(sld.length+1);
    var words=r[4].split(" ");
    var cat=j.cats[r[1]]||["Other","#4c35e8",""];
    var text=(r[3]+" "+r[5]+" "+r[6]).toLowerCase().replace(/&/g," and "), catt=cat[0].toLowerCase();
    var tw=text.replace(/[^a-z0-9 ]/g," ").split(/\s+/).filter(Boolean);
    words.forEach(function(w){ if(w.length>2) vocab[w]=1; });
    tw.forEach(function(w){ if(w.length>3) vocab[w]=1; });
    var ws={}; words.forEach(function(w){ws[w]=1;});
    var ts={}; tw.forEach(function(w){ts[w]=1;});
    return {i:i,d:r[0],sld:sld,flat:sld.replace(/-/g,""),tld:tld,c:r[1],t:r[2],b:r[3],w:words,ws:ws,place:r[5],parent:r[6],region:r[7],
      text:text,catt:catt,ts:ts,cat:cat,len:sld.replace(/-/g,"").length};
  });
  return {raw:j,recs:recs,vocab:Object.keys(vocab),cats:j.cats,regions:j.regions,places:j.places,uses:j.uses||{}};
}

/* ---------------- search engine ---------------- */
var GROUPS=[
 "dentist dentists dental orthodontist orthodontists orthodontics teeth smile","lawyer lawyers attorney attorneys law legal","divorce mediation mediator mediators",
 "dui dwi","mover movers moving relocation","realestate realty realtor realtors homes home homeforsale house houses property properties condo condos townhomes townhouses",
 "land acreage ranch","mattress mattresses bed beds furniture sleep","appliance appliances washer dryer refrigerator fridge",
 "car cars auto automotive vehicle vehicles","tire tires wheels","windshield autoglass glass","mechanic mechanics garage",
 "detail detailing","rv camper campers motorhome trailer trailers","roof roofer roofers roofing","painter painters painting paint",
 "fence fences fencing","deck decks pergola patio","hvac furnace heating","landscaping landscaper lawn yard",
 "seo marketing advertising ads advertise agency sem ppc","web website websites webdesign designer developer developers coder",
 "app apps","ai agentic agentics chatbot conversationalai automation","agent agents","hotel hotels lodging stay resort resorts",
 "vacation vacations rental rentals getaway","scuba dive diving snorkel snorkeling","fishing charter fish","surf surfing",
 "restaurant restaurants food dining catering caterer taco pizza","pet pets dog dogs cat cats puppy kitten",
 "supplement supplements vitamins probiotic probiotics chews","insurance insurer insure coverage",
 "glp1 glp semaglutide tirzepatide weightloss weight peptide peptides","spa dayspa massage massages facial facials wellness",
 "salon hair haircut barber beauty lashes waxing tanning","botox injectables medspa aesthetics filler",
 "bath bathroom bathrooms shower showers tub tubs bathtub bathtubs walkin","senior seniors elderly aging handicap accessible wheelchair mobility",
 "toilet toilets bidet","vr virtualreality virtual metaverse simulator simulators","disco silentdisco headphones dj",
 "promo promotional merch merchandise branded swag pens pen shirts","print printing printer","cleaning cleaner carpet rug maid",
 "junk removal hauling","answering receptionist callcenter","accountant accounting cpa bookkeeping tax","news media press publication",
 "comics comic cartoon animation","game games gaming","crypto bitcoin blockchain coin","art gallery artist","travel tourism tours tour attractions",
 "boat boats yacht yachts","motorcycle motorcycles bike bikes sportbike","granite countertop countertops","flooring floors floor",
 "mma gym fitness","deals coupons","nfc businesscard"
];
var ONEWAY={dentist:["botox"],dentists:["botox"],wedding:["catering"],weightloss:["glp1"],ozempic:["glp1"],wegovy:["glp1"],
  realtor:["realestate"],remodel:["bath","bathroom"],plumber:["bath","shower"],home:["realestate","homes"],agency:["seo"],
  vacationrental:["vacation"],airbnb:["vacation","rental"],tow:["mechanic"],chiropractor:["massage"],doctor:["dental","glp1","medspa"]};
var SYN={};
GROUPS.forEach(function(g){ var a=g.split(" "); a.forEach(function(w){ SYN[w]=(SYN[w]||[]).concat(a.filter(function(x){return x!==w;})); }); });
Object.keys(ONEWAY).forEach(function(k){ SYN[k]=(SYN[k]||[]).concat(ONEWAY[k]); });
var JOIN=[["real estate","realestate"],["walk in","walkin"],["roll in","rollin"],["glp 1","glp1"],["silent disco","silentdisco"],
 ["virtual reality","virtualreality"],["weight loss","weightloss"],["med spa","medspa"],["day spa","dayspa"],["call center","callcenter"],
 ["business card","businesscard"],["web design","webdesign"],["auto glass","autoglass"],["vacation rental","vacationrental"]];
var STOP={domain:1,domains:1,com:1,net:1,org:1,www:1,http:1,https:1,business:1,company:1,companies:1,website:1,site:1,name:1,names:1,
  "for":1,"in":1,the:1,a:1,an:1,of:1,and:1,or:1,my:1,i:1,need:1,want:1,looking:1,sale:1,on:1,with:1,services:1,service:1};
var SOFT={best:1,top:1,cheap:1,buy:1,near:1,me:1,local:1,find:1,online:1,"new":1,pro:1,pros:1,get:1};

function lev(a,b,max){
  if(Math.abs(a.length-b.length)>max) return max+1;
  var prev=[],cur,i,j; for(j=0;j<=b.length;j++) prev[j]=j;
  for(i=1;i<=a.length;i++){ cur=[i]; var rowMin=i;
    for(j=1;j<=b.length;j++){ cur[j]=Math.min(prev[j]+1,cur[j-1]+1,prev[j-1]+(a[i-1]===b[j-1]?0:1)); if(cur[j]<rowMin) rowMin=cur[j]; }
    if(rowMin>max) return max+1; prev=cur; }
  return prev[b.length];
}
function stem(t){
  if(t.length>4&&/ies$/.test(t)) return t.slice(0,-3)+"y";
  if(t.length>4&&/(ches|shes|xes|sses)$/.test(t)) return t.slice(0,-2);
  if(t.length>3&&/s$/.test(t)&&!/ss$/.test(t)) return t.slice(0,-1);
  return t;
}
function normalize(q){
  q=(q||"").toLowerCase().replace(/https?:\/\//g," ").replace(/&/g," and ").replace(/['’]/g,"");
  q=q.replace(/\.(com|net|org|co|io|ai|homes|one|us|info|biz)\b/g," ");
  q=q.replace(/(\w)-(\w)/g,"$1$2").replace(/[^a-z0-9]+/g," ").trim();
  JOIN.forEach(function(p){ q=q.replace(new RegExp("\\b"+p[0]+"\\b","g"),p[1]); });
  return q;
}
function placeOf(tok){
  var P=DB.places; if(P[tok]) return P[tok];
  if(tok.length>=5){ for(var k in P){ if(k.length>=5&&lev(tok,k,tok.length>=8?2:1)<=(tok.length>=8?2:1)) return P[k]; } }
  return null;
}
function parse(q){
  var n=normalize(q); if(!n) return {toks:[],places:[],raw:n};
  var parts=n.split(" "), toks=[], places=[], used={};
  for(var i=0;i<parts.length;i++){
    if(used[i]) continue;
    var p=null, span=1;
    for(var s=3;s>=2;s--){ if(i+s<=parts.length){ var g=parts.slice(i,i+s).join(""); if(DB.places[g]){ p=DB.places[g]; span=s; break; } } }
    if(!p&&!STOP[parts[i]]&&!SYN[parts[i]]) p=(parts[i].length<=3?DB.places[parts[i]]:placeOf(parts[i]))||null;
    if(p){ places.push(p); for(var k=0;k<span;k++) used[i+k]=1; continue; }
    var t=parts[i];
    if(/^\d$/.test(t)&&toks.length){ toks[toks.length-1].t+=t; continue; }
    if(STOP[t]) continue;
    toks.push({t:t,soft:!!SOFT[t]});
  }
  toks.forEach(function(o){ o.terms=terms(o.t); });
  return {toks:toks,places:places,raw:n};
}
function terms(t){
  var m={}, st=stem(t);
  m[t]=1; m[st]=1;
  (SYN[t]||SYN[st]||[]).forEach(function(s){ if(!m[s]) m[s]=0.72; });
  var known=!!SYN[t]||DB.vocab.some(function(v){ return v.indexOf(st)>-1; })||DB.recs.some(function(r){ return r.flat.indexOf(st)>-1; });
  var fz=false;
  if(!known&&t.length>=4){
    var max=t.length>=7?2:1;
    DB.vocab.forEach(function(v){ if(v.length>=3&&!m[v]&&lev(t,v,max)<=max){ m[v]=0.55; fz=true; (SYN[v]||[]).forEach(function(s){ if(!m[s]) m[s]=0.45; }); } });
  }
  return {m:m,fuzzy:fz};
}
function tokScore(r,T){
  var best=0, m=T.m;
  for(var term in m){
    var w=m[term], b=0;
    if(r.ws[term]) b=10;
    else if(term.length>=3&&r.flat.indexOf(term)>-1) b=8;
    else if(term.length>=2&&r.ts[term]) b=5;
    else if(term.length>=4&&r.text.indexOf(term)>-1) b=4;
    else if(term.length>=4&&r.catt.indexOf(term)>-1) b=3;
    if(b*w>best) best=b*w;
  }
  return best>=2.5?best:0;
}
function placeScore(r,p){
  // p = [label, region, parent]
  if(r.place===p[0]) return 10;
  if(r.parent===p[0]) return 8;
  if(p[0]==="Denver"&&r.region==="denver") return 7;
  if(p[2]&&r.place===p[2]) return 4;
  return 0;
}
function search(q,opt){
  opt=opt||{};
  var P=parse(q), out=[], relaxed=false, fuzzy=P.toks.some(function(o){return o.terms.fuzzy;});
  var req=P.toks.filter(function(o){return !o.soft;});
  if(!P.toks.length&&!P.places.length){
    out=DB.recs.map(function(r){ return {r:r,s:bonus(r)}; });
  } else {
    var partial=[];
    DB.recs.forEach(function(r){
      var s=0, hit=0, miss=0;
      P.toks.forEach(function(o){ var v=tokScore(r,o.terms); if(v>0){ s+=v; if(!o.soft) hit++; } else if(!o.soft) miss++; });
      var pm=0, pmiss=0;
      P.places.forEach(function(p){ var v=placeScore(r,p); if(v>0){ pm+=v; } else pmiss++; });
      s+=pm;
      var softOnly=!req.length&&!P.places.length;
      if(softOnly){ if(s>0) out.push({r:r,s:s+bonus(r)}); return; }
      if(!miss&&!pmiss&&(hit||pm)) out.push({r:r,s:s+bonus(r)});
      else if(hit+(pm?1:0)>0) partial.push({r:r,s:s+bonus(r),k:hit+(pm?1:0)});
    });
    if(!out.length&&partial.length){ relaxed=true; partial.sort(function(a,b){return b.k-a.k||b.s-a.s;}); out=partial; }
  }
  if(!relaxed) out.sort(function(a,b){ return b.s-a.s||a.r.len-b.r.len; });
  return {list:out.map(function(x){return x.r;}),relaxed:relaxed,fuzzy:fuzzy,parsed:P};
}
function bonus(r){ return (r.t.indexOf("C")>-1?1.2:0)+(r.t.indexOf("P")>-1?0.6:0)+(r.t.indexOf("D")>-1?0.4:0)+Math.max(0,(30-r.len))/30; }

/* ---------------- shared render helpers ---------------- */
var TAGS={P:"Premium",D:"Developed",C:"Category killer",X:"Defensive pair",B:"Brandable",I:"International"};
function esc(s){ return String(s).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c];}); }
function tagHTML(t){ return t.split("").filter(function(x){return TAGS[x];}).map(function(x){ return '<span class="tag t-'+x+'">'+TAGS[x]+'</span>'; }).join(""); }
function cardHTML(r){
  return '<article class="dcard k-'+r.c+'" data-d="'+esc(r.d)+'"><button type="button" class="dn" data-open="'+esc(r.d)+'">'+esc(r.sld)+'<span class="tld">.'+esc(r.tld)+'</span></button>'+
    '<p class="du">Built for '+esc(r.b)+'</p><p class="dt">'+tagHTML(r.t)+(r.place?'<span class="dloc">'+esc(r.place)+'</span>':'')+'</p>'+
    '<div class="dact"><a class="dask" href="/contact/?d='+encodeURIComponent(r.d)+'" data-inquire="'+esc(r.d)+'">Make an offer</a><button type="button" class="dmore" data-open="'+esc(r.d)+'">Details</button></div></article>';
}
function byDomain(d){ if(!DB) return null; for(var i=0;i<DB.recs.length;i++) if(DB.recs[i].d===d) return DB.recs[i]; return null; }
function $(s,c){ return (c||document).querySelector(s); }
function $$(s,c){ return [].slice.call((c||document).querySelectorAll(s)); }

/* ---------------- forms (FormSubmit AJAX, honeypot, timing) ---------------- */
function bindForm(f,opts){
  if(!f||f.__bound) return; f.__bound=true; opts=opts||{};
  var t0=Date.now(), interacted=false;
  ["keydown","pointerdown","input"].forEach(function(ev){ f.addEventListener(ev,function(){ interacted=true; },{passive:true}); });
  f.__reset=function(){ t0=Date.now(); };
  f.addEventListener("submit",function(e){
    e.preventDefault();
    var stat=f.querySelector(".fstat");
    function say(cls,msg){ if(stat){ stat.className="fstat "+cls; stat.innerHTML=msg; } }
    var hp=f.querySelector('input[name="_honey"]');
    if(hp&&hp.value){ done(true,true); return; }
    if(Date.now()-t0<3000||!interacted){ say("err","That was quick &mdash; give it a few seconds and press send again."); return; }
    var miss=null;
    $$("[required]",f).forEach(function(el){ el.removeAttribute("aria-invalid"); if(!miss&&!String(el.value||"").trim()) miss=el; });
    var em=f.querySelector('input[type="email"]');
    if(!miss&&em&&em.value&&!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(em.value.trim())) miss=em;
    if(miss){ miss.setAttribute("aria-invalid","true"); say("err","Please check the highlighted field."); miss.focus(); return; }
    if(opts.before) opts.before(f);
    var btn=f.querySelector('button[type="submit"]'), label=btn?btn.textContent:"";
    if(btn){ btn.disabled=true; btn.textContent="Sending…"; }
    say("","");
    var url="https://formsubmit.co/ajax/"+atob(f.dataset.a)+String.fromCharCode(64)+atob(f.dataset.b);
    fetch(url,{method:"POST",body:new FormData(f),headers:{"Accept":"application/json"}})
      .then(function(r){ return r.json().catch(function(){ return {}; }).then(function(j){ return r.ok&&(j.success===true||j.success==="true"); }); })
      .then(function(ok){ if(ok) done(true); else fail(); })
      .catch(fail);
    function fail(){ if(btn){ btn.disabled=false; btn.textContent=label||"Try again"; }
      say("err",'That did not go through. Please try again, or call <a href="'+TELH+'">'+TEL+'</a> &mdash; a person answers.'); }
  });
  function done(ok,silent){
    var box=document.createElement("div"); box.className="fdone"; box.setAttribute("role","status"); box.tabIndex=-1;
    box.innerHTML='<b>Got it &mdash; thank you.</b><p>'+(opts.thanks||"A real person at Eye To Ad Media reads every message and gets back to you, usually within one business day.")+
      '</p><p>Can&rsquo;t wait? Call <a href="'+TELH+'">'+TEL+'</a>.</p>';
    f.style.display="none"; f.parentNode.insertBefore(box,f.nextSibling); box.focus();
    if(opts.after) opts.after(f,box);
  }
}
window.BDFB=window.BDFB||{}; window.BDFB.bindForm=bindForm;

function hiddenFields(subject){
  return '<div class="hp" aria-hidden="true"><label>Leave this empty<input type="text" name="_honey" tabindex="-1" autocomplete="off"></label></div>'+
   '<input type="hidden" name="_subject" value="'+esc(subject)+'"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">';
}

/* ---------------- modal: details + inquiry ---------------- */
var modal=null, lastFocus=null;
function ensureModal(){
  if(modal) return modal;
  modal=document.createElement("div"); modal.className="modal"; modal.id="imod";
  modal.setAttribute("role","dialog"); modal.setAttribute("aria-modal","true"); modal.setAttribute("aria-labelledby","imod-h");
  modal.innerHTML='<div class="modal-box"><button class="modal-x" type="button" aria-label="Close">&times;</button><div id="imod-c"></div></div>';
  document.body.appendChild(modal);
  modal.addEventListener("click",function(e){ if(e.target===modal) closeModal(); });
  $(".modal-x",modal).addEventListener("click",closeModal);
  document.addEventListener("keydown",function(e){
    if(!modal.classList.contains("open")) return;
    if(e.key==="Escape") closeModal();
    if(e.key==="Tab"){ var f=$$('a[href],button:not([disabled]),input:not([type=hidden]):not([tabindex="-1"]),select,textarea',modal).filter(function(x){return x.offsetParent!==null;});
      if(!f.length) return; var a=f[0], z=f[f.length-1];
      if(e.shiftKey&&document.activeElement===a){ e.preventDefault(); z.focus(); } else if(!e.shiftKey&&document.activeElement===z){ e.preventDefault(); a.focus(); } }
  });
  return modal;
}
function openModal(html,focusSel){
  ensureModal(); lastFocus=document.activeElement;
  $("#imod-c",modal).innerHTML=html;
  modal.classList.add("open"); document.documentElement.classList.add("noscroll");
  var el=focusSel?$(focusSel,modal):null; (el||$(".modal-x",modal)).focus();
}
function closeModal(){ if(!modal) return; modal.classList.remove("open"); document.documentElement.classList.remove("noscroll"); if(lastFocus&&lastFocus.focus) lastFocus.focus(); }
function syll(s){ var m=s.replace(/[^a-z]/g,"").match(/[aeiouy]{1,2}/g); return m?m.length:1; }

function showDetails(d){
  var r=byDomain(d); if(!r){ showInquiry(d); return; }
  var uses=(DB.uses[r.c]||[]).map(function(u){return "<li>"+esc(u)+"</li>";}).join("");
  var sibs=DB.recs.filter(function(x){ return x.c===r.c&&x.d!==r.d&&(r.region?x.region===r.region:true); });
  if(sibs.length<4) sibs=DB.recs.filter(function(x){ return x.c===r.c&&x.d!==r.d; });
  sibs=sibs.slice(0).sort(function(a,b){ return (a.w.filter(function(w){return r.ws[w];}).length>b.w.filter(function(w){return r.ws[w];}).length)?-1:1; }).slice(0,6);
  var phone=r.t.indexOf("S")>-1?"Passes":"Spell it";
  var note=r.t.indexOf("D")>-1?"This one is not a bare name. There is a live site behind it. Ask what comes with it before you compare it to an undeveloped domain.":
    "A domain is a name, not a marketing plan. Keywords in a domain do not earn a ranking on their own. What this name gives you is a phrase people already understand, easy to say and remember, that nobody else can register.";
  var hub=r.cat[2]?'<a href="/domains/'+r.cat[2]+'/">More '+esc(r.cat[0].toLowerCase())+' names</a>':"";
  openModal('<span class="mcat" style="--h:'+r.cat[1]+'">'+esc(r.cat[0])+(r.place?" &middot; "+esc(r.place):"")+'</span>'+
    '<h2 id="imod-h" class="mh">'+esc(r.sld)+'<span class="tld">.'+esc(r.tld)+'</span></h2>'+
    '<p class="mb">Built for '+esc(r.b)+'</p><div class="mtags">'+tagHTML(r.t)+'</div>'+
    '<div class="mfacts"><div class="mfact"><b>.'+esc(r.tld)+'</b><span>Extension</span></div><div class="mfact"><b>'+r.len+'</b><span>Characters</span></div><div class="mfact"><b>'+syll(r.flat)+'</b><span>Syllables</span></div><div class="mfact"><b>'+phone+'</b><span>Phone test</span></div></div>'+
    '<div class="btn-row" style="margin-top:6px"><button type="button" class="btn btn-p" data-inquire="'+esc(r.d)+'">Make an offer on this name</button><a class="btn btn-s" href="'+TELH+'">Call '+TEL+'</a></div>'+
    (uses?'<div class="muse"><h3>What people do with a name like this</h3><ul>'+uses+'</ul></div>':"")+
    '<p class="mnote">'+note+'</p>'+
    (sibs.length?'<div class="muse"><h3>Similar names in the portfolio</h3><div class="mrel">'+sibs.map(function(x){return '<button type="button" class="chip" data-open="'+esc(x.d)+'">'+esc(x.d)+'</button>';}).join("")+'</div>'+(hub?'<p style="margin:10px 0 0;font-size:.9rem">'+hub+'</p>':"")+'</div>':""),
    '[data-inquire]');
}
function showInquiry(d,extraMsg){
  var r=d?byDomain(d):null;
  var subj="Domain inquiry"+(d?" — "+d:"")+" (bestdomainsforbusiness.com)";
  var html='<span class="mcat">'+(d?"Make an offer &middot; ask a question":"Ask about a domain")+'</span>'+
   '<h2 id="imod-h" class="mh">'+(d?esc(d):"Tell us what you need")+'</h2>'+
   (r?'<p class="mb">Built for '+esc(r.b)+'</p>':'')+
   '<form class="form iform" method="POST" novalidate data-a="aW5mbw==" data-b="ZXlldG9hZC5jb20=">'+hiddenFields(subj)+
   '<input type="hidden" name="Domain" value="'+esc(d||"")+'"><input type="hidden" name="Page" value="'+esc(location.pathname)+'">'+
   '<div class="f2"><div class="field"><label for="iq-name">Your name</label><input id="iq-name" name="Name" autocomplete="name" required></div>'+
   '<div class="field"><label for="iq-email">Email</label><input id="iq-email" type="email" name="Email" autocomplete="email" required></div></div>'+
   '<div class="f2"><div class="field"><label for="iq-phone">Phone <span class="opt">optional</span></label><input id="iq-phone" type="tel" name="Phone" autocomplete="tel"></div>'+
   '<div class="field"><label for="iq-budget">Your budget <span class="opt">optional</span></label><select id="iq-budget" name="Budget"><option value="">Prefer to discuss</option><option>Under $1,000</option><option>$1,000 – $2,500</option><option>$2,500 – $5,000</option><option>$5,000 – $10,000</option><option>$10,000 +</option></select></div></div>'+
   '<div class="field"><label for="iq-msg">Message <span class="opt">optional</span></label><textarea id="iq-msg" name="Message" rows="3">'+esc(extraMsg||(d?"I'm interested in "+d+". ":""))+'</textarea></div>'+
   '<button class="btn btn-p" type="submit" style="width:100%">Send my inquiry</button>'+
   '<p class="formnote">No obligation and no pressure. Goes to a real inbox at Eye To Ad Media &mdash; never sold or shared. <a href="/privacy/">Privacy</a>.</p>'+
   '<p class="fstat" role="status" aria-live="polite"></p></form>'+
   (d?'<p class="mnote" style="margin-top:14px">Prefer to talk? <a href="'+TELH+'">Call '+TEL+'</a> and mention '+esc(d)+'.</p>':'');
  openModal(html,"#iq-name");
  bindForm($(".iform",modal),{thanks:"We have your inquiry"+(d?" about <b>"+esc(d)+"</b>":"")+". A real person at Eye To Ad Media will reply, usually within one business day, with a straight answer on price and next steps."});
}
document.addEventListener("click",function(e){
  var a=e.target.closest&&e.target.closest("[data-inquire],[data-open]");
  if(!a) return;
  var host=a.closest("[data-d]"), hd=host?host.getAttribute("data-d"):"";
  if(a.hasAttribute("data-inquire")){ e.preventDefault(); var d=a.getAttribute("data-inquire")||hd; load().then(function(){ showInquiry(d); },function(){ showInquiry(d); }); }
  else { e.preventDefault(); var o=a.getAttribute("data-open")||hd; load().then(function(){ showDetails(o); },function(){ showInquiry(o); }); }
});

/* ---------------- typeahead (header bar + home hero) ---------------- */
function typeahead(form){
  var input=$("input[type=search]",form), box=$(".qdrop",form.parentNode)||$(".qdrop",form);
  if(!input||!box) return;
  var sel=-1, items=[];
  input.setAttribute("role","combobox"); input.setAttribute("aria-autocomplete","list"); input.setAttribute("aria-expanded","false");
  input.setAttribute("aria-controls",box.id);
  function hide(){ box.hidden=true; input.setAttribute("aria-expanded","false"); sel=-1; }
  function render(){
    var q=input.value.trim();
    if(q.length<2){ hide(); return; }
    var res=search(q), L=res.list.slice(0,6); items=L;
    var all="/domains/?q="+encodeURIComponent(q);
    if(!L.length){ box.innerHTML='<div class="qnone">No exact match in our '+DB.recs.length+' names. <a href="/find-it-for-me/?q='+encodeURIComponent(q)+'">Let us find one for you &rarr;</a></div>'; }
    else box.innerHTML=(res.relaxed?'<div class="qhint">Closest matches</div>':'')+L.map(function(r,i){
      return '<div class="qitem" role="option" id="'+box.id+'-'+i+'" aria-selected="false"><button type="button" class="qname" data-open="'+esc(r.d)+'">'+esc(r.sld)+'<span class="tld">.'+esc(r.tld)+'</span><small>'+esc(r.cat[0])+(r.place?" &middot; "+esc(r.place):"")+'</small></button><a class="qask" href="/contact/?d='+encodeURIComponent(r.d)+'" data-inquire="'+esc(r.d)+'">Ask</a></div>';
    }).join("")+'<a class="qall" href="'+all+'">See all '+res.list.length+' matches &rarr;</a>';
    box.hidden=false; input.setAttribute("aria-expanded","true"); sel=-1;
  }
  var tm; input.addEventListener("input",function(){ clearTimeout(tm); tm=setTimeout(function(){ load().then(render); },60); });
  input.addEventListener("focus",function(){ load(); if(input.value.trim().length>1) load().then(render); });
  input.addEventListener("keydown",function(e){
    if(box.hidden) return;
    var opts=$$(".qitem",box);
    if(e.key==="ArrowDown"||e.key==="ArrowUp"){ e.preventDefault(); sel=e.key==="ArrowDown"?Math.min(opts.length-1,sel+1):Math.max(-1,sel-1);
      opts.forEach(function(o,i){ o.setAttribute("aria-selected",i===sel?"true":"false"); o.classList.toggle("on",i===sel); });
      if(sel>-1) input.setAttribute("aria-activedescendant",opts[sel].id); else input.removeAttribute("aria-activedescendant"); }
    else if(e.key==="Enter"&&sel>-1){ e.preventDefault(); var pick=items[sel]; hide(); if(pick) showDetails(pick.d); }
    else if(e.key==="Escape"){ hide(); }
  });
  document.addEventListener("click",function(e){ if(!form.parentNode.contains(e.target)) hide(); });
}

/* ---------------- catalog app (/domains/) ---------------- */
function catalog(root){
  var grid=$("#grid"), cards={}, order=[];
  $$(".dcard",grid).forEach(function(c){ cards[c.dataset.d]=c; order.push(c.dataset.d); });
  var q=$("#srch"), fCat=$("#f-cat"), fLoc=$("#f-loc"), fType=$("#f-type"), fTld=$("#f-tld"), fSort=$("#f-sort"), tally=$("#tally"), empty=$("#empty"), hint=$("#qhint");
  var tagOn=null;
  var p=new URLSearchParams(location.search);
  if(p.get("q")) q.value=p.get("q");
  if(p.get("cat")&&fCat.querySelector('option[value="'+p.get("cat")+'"]')) fCat.value=p.get("cat");
  if(p.get("loc")&&fLoc.querySelector('option[value="'+p.get("loc")+'"]')) fLoc.value=p.get("loc");
  if(p.get("type")) fType.value=p.get("type");
  if(p.get("tld")) fTld.value=p.get("tld");
  if(p.get("sort")) fSort.value=p.get("sort");
  if(p.get("tag")){ tagOn=p.get("tag"); var tb=$('#tagchips .chip[data-tag="'+tagOn+'"]'); if(tb){ tb.classList.add("on"); tb.setAttribute("aria-pressed","true"); } }
  function apply(push){
    var res=search(q.value), list=res.list;
    list=list.filter(function(r){
      if(fCat.value&&r.c!==fCat.value) return false;
      if(fLoc.value&&r.region!==fLoc.value&&!(fLoc.value==="co-all"&&(r.region==="denver"||r.region==="colorado"))) return false;
      if(fType.value==="dev"&&r.t.indexOf("D")<0) return false;
      if(fType.value==="bare"&&r.t.indexOf("D")>-1) return false;
      if(fTld.value==="com"&&r.tld!=="com") return false;
      if(fTld.value==="other"&&r.tld==="com") return false;
      if(tagOn&&r.t.indexOf(tagOn)<0) return false;
      return true;
    });
    var s=fSort.value;
    if(s==="az") list.sort(function(a,b){return a.d<b.d?-1:1;});
    else if(s==="short") list.sort(function(a,b){return a.len-b.len||(a.d<b.d?-1:1);});
    else if(s==="cat") list.sort(function(a,b){return a.cat[0]<b.cat[0]?-1:a.cat[0]>b.cat[0]?1:(a.d<b.d?-1:1);});
    else if(!q.value.trim()) list.sort(function(a,b){return order.indexOf(a.d)-order.indexOf(b.d);});
    var show={}; list.forEach(function(r){ show[r.d]=1; });
    var frag=document.createDocumentFragment();
    list.forEach(function(r){ var c=cards[r.d]; if(c){ c.hidden=false; frag.appendChild(c); } });
    order.forEach(function(d){ if(!show[d]){ cards[d].hidden=true; frag.appendChild(cards[d]); } });
    grid.appendChild(frag);
    var narrowed=q.value.trim()||fCat.value||fLoc.value||fType.value||fTld.value||tagOn;
    tally.textContent=!narrowed?"Showing the full portfolio":(list.length===1?"1 match":list.length+" matches")+(q.value.trim()?" for \u201c"+q.value.trim()+"\u201d":"");
    empty.hidden=list.length>0;
    var eq=$("#empty-q"); if(eq) eq.textContent=q.value.trim()?"“"+q.value.trim()+"”":"those filters";
    var cf=$("#empty-cta"); if(cf) cf.href="/find-it-for-me/?q="+encodeURIComponent(q.value.trim());
    hint.hidden=!(res.relaxed||res.fuzzy)||!list.length;
    hint.textContent=res.relaxed?"No name matches every word, so these are the closest matches.":"Including close spellings of your search.";
    var u=new URL(location.href);
    [["q",q.value.trim()],["cat",fCat.value],["loc",fLoc.value],["type",fType.value],["tld",fTld.value],["sort",fSort.value==="rel"?"":fSort.value],["tag",tagOn||""]].forEach(function(kv){ kv[1]?u.searchParams.set(kv[0],kv[1]):u.searchParams.delete(kv[0]); });
    history.replaceState(null,"",u);
  }
  var tm; q.addEventListener("input",function(){ clearTimeout(tm); tm=setTimeout(apply,50); });
  $("#finder-form").addEventListener("submit",function(e){ e.preventDefault(); apply(); q.blur(); grid.scrollIntoView({behavior:"smooth",block:"start"}); });
  [fCat,fLoc,fType,fTld,fSort].forEach(function(el){ el.addEventListener("change",function(){ apply(); }); });
  $$("#tagchips .chip").forEach(function(b){ b.addEventListener("click",function(){
    var v=b.dataset.tag; $$("#tagchips .chip").forEach(function(x){ x.classList.remove("on"); x.setAttribute("aria-pressed","false"); });
    if(tagOn===v) tagOn=null; else { tagOn=v; b.classList.add("on"); b.setAttribute("aria-pressed","true"); } apply(); }); });
  $$("[data-q]").forEach(function(b){ b.addEventListener("click",function(){ q.value=b.dataset.q; apply(); q.focus(); }); });
  $("#clr").addEventListener("click",function(){ q.value=""; fCat.value=fLoc.value=fType.value=fTld.value=""; fSort.value="rel"; tagOn=null; $$("#tagchips .chip").forEach(function(x){x.classList.remove("on");x.setAttribute("aria-pressed","false");}); apply(); q.focus(); });
  load().then(function(){ apply(); root.classList.add("ready"); });
}

/* ---------------- home hero live results ---------------- */
function heroFinder(root){
  var form=$("form",root), input=$("input[type=search]",root), out=$(".hres",root), all=$(".hall",root);
  function render(){
    var v=input.value.trim();
    if(v.length<2){ out.innerHTML=""; out.hidden=true; all.hidden=true; return; }
    var res=search(v), L=res.list.slice(0,6);
    out.hidden=false;
    out.innerHTML=L.length?L.map(cardHTML).join(""):'<p class="qnone">Nothing in our '+DB.recs.length+' names matches that yet. <a href="/find-it-for-me/?q='+encodeURIComponent(v)+'">Let us find one for you &rarr;</a></p>';
    all.hidden=!L.length; all.href="/domains/?q="+encodeURIComponent(v); all.textContent=(res.relaxed?"See the closest ":"See all ")+res.list.length+" matches →";
  }
  var tm; input.addEventListener("input",function(){ clearTimeout(tm); tm=setTimeout(function(){ load().then(render); },60); });
  input.addEventListener("focus",function(){ load(); },{once:true});
  $$("[data-q]",root).forEach(function(b){ b.addEventListener("click",function(){ input.value=b.dataset.q; load().then(render); }); });
  form.addEventListener("submit",function(e){ if(!input.value.trim()){ e.preventDefault(); input.focus(); } });
}

/* ---------------- concierge ("find it for me") ---------------- */
function concierge(root){
  var f=$("form",root), what=$("[name='What the business does']",f), city=$("[name='City or market']",f), sug=$(".csug",root), picked={};
  var hid=$("[name='Domains they liked']",f);
  var p=new URLSearchParams(location.search); if(p.get("q")&&what&&!what.value) what.value=p.get("q");
  function render(){
    var q=(what.value+" "+(city?city.value:"")).trim();
    if(q.length<3){ sug.innerHTML='<p class="csug-empty">Start typing what your business does &mdash; matching names from our portfolio show up here instantly.</p>'; return; }
    var res=search(q), L=res.list.slice(0,8);
    if(!L.length){ sug.innerHTML='<p class="csug-empty">Nothing in the portfolio fits that yet &mdash; which is exactly what this form is for. Send it and we will go looking.</p>'; return; }
    sug.innerHTML='<p class="csug-h">'+(res.relaxed?"Closest names we already own":"Names we already own that fit")+' <span>tap to add to your request</span></p><div class="csug-list">'+L.map(function(r){
      var on=picked[r.d]; return '<button type="button" class="cpick'+(on?" on":"")+'" aria-pressed="'+(on?"true":"false")+'" data-pick="'+esc(r.d)+'"><b>'+esc(r.sld)+'<span class="tld">.'+esc(r.tld)+'</span></b><small>'+esc(r.cat[0])+(r.place?" &middot; "+esc(r.place):"")+'</small></button>';
    }).join("")+'</div>';
  }
  sug.addEventListener("click",function(e){ var b=e.target.closest("[data-pick]"); if(!b) return; var d=b.dataset.pick;
    if(picked[d]) delete picked[d]; else picked[d]=1; b.classList.toggle("on"); b.setAttribute("aria-pressed",picked[d]?"true":"false");
    hid.value=Object.keys(picked).join(", "); var c=$(".cpicked",root); if(c) c.textContent=Object.keys(picked).length?Object.keys(picked).length+" name(s) added to your request":""; });
  var tm; [what,city].forEach(function(el){ if(el) el.addEventListener("input",function(){ clearTimeout(tm); tm=setTimeout(function(){ load().then(render); },80); }); });
  load().then(render);
  bindForm(f,{before:function(){ hid.value=Object.keys(picked).join(", "); },
    thanks:"Your request is in. A real person will look through the portfolio and the open market for you and reply, usually within one business day, with options that fit your business and budget."});
}

/* ---------------- tools hooks ---------------- */
window.BDFB.load=load; window.BDFB.search=function(q){ return search(q); }; window.BDFB.cardHTML=cardHTML;
window.BDFB.esc=esc; window.BDFB.showDetails=showDetails; window.BDFB.showInquiry=showInquiry; window.BDFB.normalize=normalize;

/* ---------------- boot ---------------- */
$$("form.qform").forEach(typeahead);
var cat=$("#finder-app"); if(cat) catalog(cat);
var hero=$("#hero-finder"); if(hero) heroFinder(hero);
$$(".concierge").forEach(concierge);
$$("form[data-a]").forEach(function(f){ if(!f.closest(".concierge")) bindForm(f); });
})();
