"""New hand-authored pages + upgrades to existing pages. Executed by build.py (shares recs, N, CATS, C, esc, write)."""

def concierge(prefix, heading_level="h2", compact=False):
    opts_budget = "".join(f"<option>{o}</option>" for o in ["Not sure yet", "Under $1,000", "$1,000 – $2,500", "$2,500 – $5,000", "$5,000 – $10,000", "$10,000 – $25,000", "$25,000 +"])
    opts_time = "".join(f"<option>{o}</option>" for o in ["Just exploring", "Within a month", "1–3 months", "Right away"])
    return f'''<div class="concierge"><div class="cgrid">
<form class="form" id="{prefix}" method="POST" novalidate data-a="aW5mbw==" data-b="ZXlldG9hZC5jb20=">
<div class="hp" aria-hidden="true"><label>Leave this empty<input type="text" name="_honey" tabindex="-1" autocomplete="off"></label></div>
<input type="hidden" name="_subject" value="Find it for me request — bestdomainsforbusiness.com"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">
<input type="hidden" name="Domains they liked" value="">
<div class="f2"><div class="field"><label for="{prefix}-what">What does your business do?</label><input id="{prefix}-what" name="What the business does" placeholder="dentist, roofing, walk-in tubs…" autocomplete="off" required></div>
<div class="field"><label for="{prefix}-city">City or market <span class="opt">optional</span></label><input id="{prefix}-city" name="City or market" placeholder="Denver, Omaha, Maui…" autocomplete="address-level2"></div></div>
<div class="csug" aria-live="polite"><p class="csug-empty">Start typing what your business does &mdash; matching names from our portfolio show up here instantly.</p></div><p class="cpicked" aria-live="polite"></p>
<div class="f2"><div class="field"><label for="{prefix}-budget">Budget range</label><select id="{prefix}-budget" name="Budget range">{opts_budget}</select></div>
<div class="field"><label for="{prefix}-time">Timeline</label><select id="{prefix}-time" name="Timeline">{opts_time}</select></div></div>
<div class="f2"><div class="field"><label for="{prefix}-name">Your name</label><input id="{prefix}-name" name="Name" autocomplete="name" required></div>
<div class="field"><label for="{prefix}-email">Email</label><input id="{prefix}-email" type="email" name="Email" autocomplete="email" required></div></div>
<div class="field"><label for="{prefix}-phone">Phone <span class="opt">optional, but faster</span></label><input id="{prefix}-phone" type="tel" name="Phone" autocomplete="tel"></div>
{'' if compact else f'<div class="field"><label for="{prefix}-notes">Anything else <span class="opt">optional</span></label><textarea id="{prefix}-notes" name="Notes" rows="3" placeholder="A name you have in mind, names you have ruled out, a deadline…"></textarea></div>'}
<button class="btn btn-p" type="submit" style="width:100%">Find my domain</button>
<p class="formnote">Free to ask and no obligation. A real person replies, usually within one business day. Never sold or shared &mdash; <a href="/privacy/">privacy</a>.</p>
<p class="fstat" role="status" aria-live="polite"></p>
</form>
<div><div class="next3" style="grid-template-columns:1fr;margin-top:0"><div><b>1 &middot; Type your business</b><p>Names we already own that fit appear under the box. Tap any you like.</p></div><div><b>2 &middot; Send it</b><p>Budget and timeline help us suggest the right kind of name, not the most expensive one.</p></div><div><b>3 &middot; A person replies</b><p>Usually within one business day, with options &mdash; including names you can simply register.</p></div></div>
<div class="trustrow">{C.BBB}<p>Run by Eye To Ad Media in Denver. We would rather point you to a plain registration than sell you a name you do not need.</p></div></div>
</div></div>'''


def tool_page(path, title, desc, crumbs, eyebrow, h1, lede, body, faqs=None, extra_ld=()):
    main = ('<section class="hero" style="padding:40px 0 30px"><div class="wrap">' + C.crumbs_html(crumbs) +
            f'<span class="eyebrow">{eyebrow}</span><h1 style="font-size:clamp(2rem,5.2vw,3.2rem);max-width:22ch">{h1}</h1><p class="lede">{lede}</p></div></section>' + body)
    ex = list(extra_ld)
    if faqs:
        main += '<section class="tint"><div class="wrap narrow"><span class="eyebrow">Straight answers</span><h2 class="sec-h">Questions people ask.</h2>' + C.faq_html(faqs) + '</div></section>'
        ex.append(C.faq_ld(faqs))
    main += CLOSE
    write(path, C.page(path, title, desc, crumbs, main, N, ex))


def sources(links):
    return '<p class="srcs" style="margin-top:28px"><b>Sources, none of them ours:</b> ' + " &middot; ".join(f'<a href="{u}" rel="noopener" target="_blank">{t}</a>' for t, u in links) + '</p>'


ncats = len(CATS)
noncom = [r["d"] for r in recs if r["tld"] != "com"]

# ============================================================== /find-it-for-me/
tool_page("/find-it-for-me/", "Find the Perfect Domain for Your Business",
          f"Tell us what your business does and where. We match names from our {N}-domain portfolio instantly, then a person finds the best fit for your budget.",
          [("Home", "/"), ("Find it for me", "/find-it-for-me/")], "Domain concierge &middot; free to ask",
          "Tell us your business. We will find the name.",
          f"Answer four quick questions. Names from our {N}-domain portfolio that fit appear as you type &mdash; tap any you like. Then a real person checks the rest of the portfolio, whether a good name is simply available to register, and what it would take to buy one somebody else owns.",
          '<section style="padding-top:10px"><div class="wrap">' + concierge("ff") + '</div></section>'
          '<section class="tint"><div class="wrap"><span class="eyebrow">What happens next</span><h2 class="sec-h">Cheapest good outcome first. Always.</h2>'
          '<div class="next3"><div><b>1 &middot; Within a business day</b><p>A person reads your request and replies with names that fit, from our portfolio and beyond.</p></div>'
          '<div><b>2 &middot; Honest options</b><p>If a good name is unregistered, we tell you to register it yourself. If we own a fit, you get a real number on a call.</p></div>'
          '<div><b>3 &middot; Only if you want it</b><p>Names owned by someone else can be pursued through our <a href="/find-a-domain/">acquisition service</a>. No surprise fees.</p></div></div></div></section>',
          [("Is it free to ask?", "Yes. Asking costs nothing and there is no obligation. You only pay if you decide to buy a name we own, or if you choose to hire us to acquire a name owned by someone else."),
           ("Do you only suggest your own domains?", "No. If the best answer is a name that is still available to register, we will say so. That is usually the cheapest outcome and we would rather you start there."),
           ("What if I already know the exact name I want?", "Put it in the notes. If we own it, you get a price on a call. If someone else owns it, we will explain the options, including our <a href=\"/find-a-domain/\">acquisition service</a>."),
           ("How fast can I get a domain once I choose?", "For a name we own, the authorization code goes out the same business day once payment clears. Registrars control the transfer itself, which typically takes a few days for a .com.")])

# ============================================================== /domain-name-checker/
checker_js = r'''<script>
document.addEventListener("DOMContentLoaded",function(){
var COMMON="a an and the of for to in on my our your best top pro get go buy shop store home local near me now new online hub co inc usa us".split(" ");
var SERVICE="seo marketing ads advertising web design app dentist dental ortho botox spa salon hair massage glp clinic health law lawyer attorney legal divorce dui mediation real estate realty homes house condo land rent rental vacation hotel travel tour tours dive scuba fishing surf restaurant food catering taco pizza pet dog cat supplements insurance mattress furniture appliance appliances roof roofing fence deck painter painters painting plumbing hvac furnace landscaping cleaning carpet rug mover movers moving junk auto car cars tire tires glass windshield detailing mechanic rv trailer bath shower tub tubs walkin accountant cpa answering printing promo pens shirts vr ai agent agents chatbot coach training".split(" ");
var box=document.getElementById("ck-out"), inp=document.getElementById("ck-q");
function seg(s,V){var n=s.length,b=[[0,[]]];for(var i=1;i<=n;i++){b[i]=null;for(var j=Math.max(0,i-20);j<i;j++){if(!b[j])continue;var w=s.slice(j,i),c;if(V[w])c=1+(w.length===1?.6:0);else if(w.length===1)c=3;else continue;c+=b[j][0];if(!b[i]||c<b[i][0])b[i]=[c,b[j][1].concat([w])];}}return b[n][1];}
function score(raw,DB){
  var v=raw.trim().toLowerCase().replace(/^https?:\/\//,"").replace(/^www\./,"").split("/")[0];
  if(!/^[a-z0-9-]+(\.[a-z0-9-]+)+$/.test(v)) return null;
  var sld=v.split(".")[0], tld=v.slice(sld.length+1), core=sld.replace(/-/g,""), L=core.length;
  var V={}; COMMON.concat(SERVICE).forEach(function(w){V[w]=1;}); DB.vocab.forEach(function(w){V[w]=1;}); Object.keys(DB.places).forEach(function(w){V[w]=1;});
  var words=[];sld.split("-").forEach(function(p){words=words.concat(seg(p.replace(/[0-9]/g,"0"),V).map(function(x){return x;}));});
  var unknown=words.filter(function(w){return w.length===1&&!/[0-9]/.test(w);}).length;
  var wc=words.filter(function(w){return w.length>1||/[0-9]/.test(w);}).length+Math.ceil(unknown/4);
  var hy=(sld.match(/-/g)||[]).length, dig=/[0-9]/.test(sld);
  var rows=[];
  var e=tld==="com"?20:(tld==="net"||tld==="org")?12:/^(co|us|io|ai)$/.test(tld)?10:8;
  rows.push(["Extension","."+tld,e,20,tld==="com"?"People type .com by reflex, and it is the largest extension by far.":"Workable, but some visitors and emails will go to the .com version by habit. Check who owns it."]);
  var l=L<=8?20:L<=12?18:L<=15?15:L<=20?11:L<=25?6:2;
  rows.push(["Length",L+" characters",l,20,L<=15?"Short enough to say and remember easily.":L<=20?"Fine for a descriptive phrase; long for a pure brand.":"Long names get mistyped and cut off on signs."]);
  rows.push(["Hyphens",hy?hy+" hyphen"+(hy>1?"s":""):"None",hy===0?10:hy===1?4:0,10,hy?"Every hyphen has to be said out loud (“dash”) and is easy to forget.":"Nothing to explain."]);
  rows.push(["Numbers",dig?"Yes":"None",dig?3:10,10,dig?"People will not know whether to type the digit or spell the word.":"No digit-or-word confusion."]);
  var w=wc<=2?10:wc===3?8:wc===4?5:2;
  rows.push(["Words",wc+" ("+words.filter(function(x){return x.length>1;}).join(" · ")+")",w,10,wc<=3?"Easy to chunk and remember.":"Each extra word is one more thing to remember in the right order."]);
  var ph=15, why=[];
  if(hy){ph-=5;why.push("hyphen");} if(dig){ph-=5;why.push("digit");}
  if(/(^|[^a-z])(4|2|8|u|ur)([^a-z]|$)/.test(sld.replace(/([a-z])(4|2|8)/g,"$1 $2"))||/4less|4u|2go|b4/.test(sld)){ph-=3;why.push("sound-alike (4/for, 2/to, u/you)");}
  for(var i=1;i<words.length;i++){ if(words[i-1].slice(-1)===words[i][0]&&words[i].length>1&&words[i-1].length>1){ph-=3;why.push("doubled letter at a word break ("+words[i-1]+words[i]+")");break;} }
  if(L>20){ph-=3;why.push("long");}
  ph=Math.max(0,ph);
  rows.push(["Phone & radio test",ph>=12?"Passes":"Needs spelling",ph,15,why.length?"Lost points for: "+why.join(", ")+".":"Say it once and people can type it."]);
  var svc=words.some(function(x){return SERVICE.indexOf(x)>-1||/seo|dent|roof|fence|deck|paint|lawyer|attorney|realt|mover|tire|tub|shower|spa|glp|insur|mattress|applianc|clean|cater|restaur|hotel|dive|vacation|rental|pet|dog|cat/.test(x);});
  var plc=words.some(function(x){return !!DB.places[x];})||Object.keys(DB.places).some(function(k){return k.length>4&&core.indexOf(k)>-1;});
  var c=(svc?10:0)+(plc?5:0);
  rows.push(["Says what &amp; where",(svc?"Service":"No service word")+" · "+(plc?"Place":"No place"),c,15,svc?"A stranger can guess what you do from the name.":"Fine for a brand you will build — just expect to spend more teaching people what it is. See keyword vs brand."]);
  var tot=rows.reduce(function(a,r){return a+r[2];},0);
  return {v:v,words:words,rows:rows,total:tot};
}
function esc(s){return BDFB.esc(s);}
function run(){
  var list=inp.value.split(/[\s,]+/).filter(Boolean).slice(0,5);
  if(!list.length){box.innerHTML='<p>Type a domain such as <em>denverroofing.com</em>.</p>';return;}
  BDFB.load().then(function(DB){
    var out="";
    list.forEach(function(n){
      var r=score(n,DB);
      if(!r){out+='<div class="tool" style="margin-top:14px"><p style="margin:0"><b>'+esc(n)+'</b> does not look like a domain. Try <em>yourname.com</em> &mdash; no spaces or https.</p></div>';return;}
      out+='<div class="tool" style="margin-top:14px"><h2 style="font-size:1.4rem;word-break:break-word">'+esc(r.v)+'</h2><div class="score"><span class="score-n">'+r.total+'<small style="font-size:1rem;color:var(--ink-70)">/100</small></span><span class="score-bar" aria-hidden="true"><i style="width:'+r.total+'%"></i></span></div>'+
        '<p style="color:var(--ink-70);margin:0">'+(r.total>=80?"Strong on every rule we can check.":r.total>=60?"Solid, with a weak spot or two below.":"Several rules count against it &mdash; see why below.")+' This scores readability and memorability only. It is <b>not</b> a price and <b>not</b> a ranking prediction.</p>'+
        '<div style="overflow-x:auto"><table class="rules"><thead><tr><th scope="col">Rule</th><th scope="col">Result</th><th scope="col">Points</th><th scope="col">Why</th></tr></thead><tbody>'+
        r.rows.map(function(x){return '<tr><td>'+x[0]+'</td><td>'+esc(String(x[1]))+'</td><td class="pts">'+x[2]+' / '+x[3]+'</td><td>'+x[4]+'</td></tr>';}).join("")+'</tbody></table></div>';
      var q=r.words.filter(function(w){return w.length>2;}).join(" ");
      var s=q?BDFB.search(q):null, L=s&&!s.relaxed?s.list.filter(function(x){return x.d!==r.v;}).slice(0,3):[];
      if(L.length) out+='<h3 style="font-size:1.05rem;margin:18px 0 8px">Similar names we own</h3><div class="hres" style="margin-top:0">'+L.map(BDFB.cardHTML).join("")+'</div>';
      out+='</div>';
    });
    box.innerHTML=out;
  });
}
document.getElementById("ck-go").addEventListener("click",run);
inp.addEventListener("keydown",function(e){if(e.key==="Enter"){e.preventDefault();run();}});
var p=new URLSearchParams(location.search); if(p.get("d")){inp.value=p.get("d");run();}
});
</script>'''
rules_table = ('<table class="rules"><thead><tr><th scope="col">Rule</th><th scope="col">Max</th><th scope="col">How points are given</th></tr></thead><tbody>'
               '<tr><td>Extension</td><td class="pts">20</td><td>.com 20 &middot; .net/.org 12 &middot; .co/.us/.io/.ai 10 &middot; anything else 8</td></tr>'
               '<tr><td>Length</td><td class="pts">20</td><td>Characters before the dot, hyphens excluded: up to 8 = 20, 12 = 18, 15 = 15, 20 = 11, 25 = 6, longer = 2</td></tr>'
               '<tr><td>Hyphens</td><td class="pts">10</td><td>None 10 &middot; one 4 &middot; two or more 0</td></tr>'
               '<tr><td>Numbers</td><td class="pts">10</td><td>None 10 &middot; any digit 3</td></tr>'
               '<tr><td>Words</td><td class="pts">10</td><td>1&ndash;2 words 10 &middot; 3 = 8 &middot; 4 = 5 &middot; 5+ = 2 (words found with a dictionary built from our inventory)</td></tr>'
               '<tr><td>Phone &amp; radio test</td><td class="pts">15</td><td>Start at 15; minus 5 for a hyphen, 5 for a digit, 3 for sound-alikes (4/for, 2/to, u/you), 3 for a doubled letter at a word break, 3 if over 20 characters</td></tr>'
               '<tr><td>Says what &amp; where</td><td class="pts">15</td><td>10 if it contains a recognizable service word, 5 if it contains a place</td></tr></tbody></table>')
tool_page("/domain-name-checker/", "Domain Name Checker: Free, Transparent Score",
          "Score any domain name out of 100 on length, extension, hyphens, numbers, word count, the phone test and clarity. Every rule is shown. Not a fake appraisal.",
          [("Home", "/"), ("Free tools", "/guides/"), ("Domain name checker", "/domain-name-checker/")], "Free tool &middot; runs in your browser",
          "Domain name checker", "Type a name &mdash; or up to five, separated by commas &mdash; and see exactly how it scores on the things that make a domain easy to say, type and remember. Every rule and every point is on this page. Nothing is sent anywhere.",
          '<section style="padding-top:10px"><div class="wrap"><div class="tool"><label for="ck-q" style="font-weight:800;display:block;margin-bottom:8px">Domain name(s) to check</label>'
          '<div class="bigsearch"><input id="ck-q" type="text" placeholder="denverroofing.com, roof-denver.net" autocomplete="off" spellcheck="false"><button type="button" id="ck-go">Score it</button></div></div>'
          '<div id="ck-out" aria-live="polite"></div></div></section>'
          '<section class="tint"><div class="wrap"><span class="eyebrow">The rules, in full</span><h2 class="sec-h">How the 100 points work.</h2>'
          '<p class="lede">We publish the scoring so you can disagree with it. These rules measure how easily a person can hear, say, type and remember a name &mdash; the things buyers and customers notice first.</p>'
          '<div style="overflow-x:auto">' + rules_table + '</div>'
          '<div class="callout"><p><b>What this score is not:</b> a dollar value or a prediction of rankings. Google has said keywords in a domain do not earn a ranking on their own, and no calculator knows which buyer needs your name. For value, use our <a href="/what-is-my-domain-worth/">honest worth checklist</a>.</p></div></div></section>' + checker_js,
          [("Is a higher score worth more money?", "Not necessarily. The score measures readability and memorability. Price depends mostly on whether a specific buyer needs that exact name. A long, specific name can be worth more to the right business than a short generic one."),
           ("Why does .com get the most points?", "Because people type .com by habit and it is the largest extension by registrations, according to Verisign's quarterly Domain Name Industry Brief. Other extensions work, but some visitors and email will drift to the .com."),
           ("Does this tool store or send what I type?", "No. The scoring runs in your browser. The only thing loaded is our own inventory file, so we can show similar names we own.")])

# ============================================================== /domain-name-ideas/
ideas_js = r'''<script>
document.addEventListener("DOMContentLoaded",function(){
var f=document.getElementById("id-form"), out=document.getElementById("id-out");
function run(e){ if(e) e.preventDefault();
  var svc=document.getElementById("id-svc").value.trim(), city=document.getElementById("id-city").value.trim(), style=document.getElementById("id-style").value;
  if(!svc){ out.innerHTML='<p>Tell us what the business does first.</p>'; document.getElementById("id-svc").focus(); return; }
  BDFB.load().then(function(DB){
    var res=BDFB.search(svc+" "+city), L=res.list.slice(0);
    if(style==="short") L.sort(function(a,b){return a.len-b.len;});
    if(style==="brand") L=L.filter(function(r){return r.t.indexOf("B")>-1;}).concat(L.filter(function(r){return r.t.indexOf("B")<0;}));
    if(style==="exact") L=L.filter(function(r){return r.t.indexOf("E")>-1;});
    L=L.slice(0,12);
    var sw=BDFB.normalize(svc).split(" "), cw=BDFB.normalize(city).replace(/ /g,"");
    if(!L.length){ out.innerHTML='<div class="callout"><p><b>Nothing in our portfolio fits that yet.</b> That is useful to know &mdash; the name may simply be available to register, or we can go find one. <a href="/find-it-for-me/?q='+encodeURIComponent(svc+" "+city)+'">Ask us to find it</a>.</p></div>'; return; }
    out.innerHTML=(res.relaxed?'<p class="callout">No name matches everything you typed, so these are the closest.</p>':'')+'<div class="reslist">'+L.map(function(r){
      var why=[];
      if(sw.some(function(w){return w.length>2&&(r.flat.indexOf(w)>-1||r.ws[w]);})) why.push("Contains your service word");
      else why.push("Related to what you do ("+BDFB.esc(r.cat[0])+")");
      if(cw&&r.place&&(r.flat.indexOf(cw)>-1||r.place.toLowerCase().replace(/ /g,"")===cw)) why.push("Names your city: "+BDFB.esc(r.place));
      else if(cw&&r.place) why.push("Same area: "+BDFB.esc(r.place));
      if(r.t.indexOf("S")>-1) why.push("Passes the phone test");
      if(r.tld==="com") why.push(".com");
      if(r.t.indexOf("X")>-1) why.push("A close variant is also available");
      if(r.t.indexOf("D")>-1) why.push("Has a live site on it");
      return '<div class="res"><h3>'+BDFB.esc(r.d)+'</h3><p>Built for '+BDFB.esc(r.b)+'</p><ul class="why">'+why.map(function(x){return "<li>"+x+"</li>";}).join("")+'</ul>'+
        '<div class="dact"><a class="dask" href="/contact/?d='+encodeURIComponent(r.d)+'" data-inquire="'+BDFB.esc(r.d)+'">Make an offer</a><a class="dmore" href="/domain-name-checker/?d='+encodeURIComponent(r.d)+'">Score it</a></div></div>';
    }).join("")+'</div><p style="margin-top:18px">Want a person to shortlist for you? <a href="/find-it-for-me/?q='+encodeURIComponent(svc+" "+city)+'">Find it for me</a>.</p>';
  });
}
f.addEventListener("submit",run);
});
</script>'''
tool_page("/domain-name-ideas/", "Business Domain Name Ideas From Real Inventory",
          f"Describe your business and get domain ideas drawn only from the {N} names we actually own, with a plain reason each one fits. No made-up suggestions.",
          [("Home", "/"), ("Free tools", "/guides/"), ("Name ideas", "/domain-name-ideas/")], "Free tool &middot; real names only",
          "Domain name ideas you can actually buy.",
          f"Most name generators invent names that are taken or worthless. This one only suggests names from our {N}-domain portfolio &mdash; every result exists, is for sale, and comes with the reason it fits.",
          '<section style="padding-top:10px"><div class="wrap"><form class="tool" id="id-form"><div class="f2">'
          '<div class="field"><label for="id-svc">What does the business do?</label><input id="id-svc" placeholder="dentist, fence company, dive shop…" required autocomplete="off"></div>'
          '<div class="field"><label for="id-city">Where? <span class="opt">optional</span></label><input id="id-city" placeholder="Denver, Omaha, Oahu…" autocomplete="off"></div></div>'
          '<div class="f2"><div class="field"><label for="id-style">Style</label><select id="id-style"><option value="">Best fit</option><option value="exact">Exact-match phrases only</option><option value="short">Shortest first</option><option value="brand">Brandable first</option></select></div>'
          '<div class="field" style="display:flex;align-items:flex-end"><button class="btn btn-p" type="submit" style="width:100%">Show me names</button></div></div></form>'
          '<div id="id-out" aria-live="polite"></div></div></section>' + ideas_js,
          [("Are these names really available?", "Every suggestion is a domain we own and will sell. None are invented. Prices are negotiable and quoted by a person."),
           ("What if nothing fits?", "Then the name you want may be unregistered, or owned by someone else. Use <a href=\"/find-it-for-me/\">find it for me</a> and we will check both, cheapest option first.")])

# ============================================================== /keyword-vs-brand-domain/
QS = [("q1", "Where will most customers find you?", [("K2", "Searching for a service in my area, or calling from an ad or sign"), ("B1", "Referrals and word of mouth"), ("B1K1", "Online, across the whole country")]),
      ("q2", "Will you add new services or cities in the next three years?", [("K2", "No, this is what we do and where"), ("", "Maybe"), ("B2", "Yes, definitely")]),
      ("q3", "How much will you spend teaching people a new name?", [("K2", "Very little"), ("", "Some"), ("B2", "A real brand budget")]),
      ("q4", "Does the name have to explain itself on a truck, sign or radio spot?", [("K2", "Yes"), ("K1", "Somewhat"), ("B1", "No")]),
      ("q5", "How important is a trademark you can protect?", [("K1", "Not very"), ("B2", "Very important")]),
      ("q6", "What is the domain for?", [("K2", "A campaign, lead-gen or second website"), ("B1", "The company name itself"), ("B1K1", "Both")])]
qhtml = "".join(f'<div class="qcard"><fieldset><legend>{i+1}. {q}</legend>' + "".join(f'<label><input type="radio" name="{k}" value="{v}" required> {t}</label>' for v, t in opts) + '</fieldset></div>' for i, (k, q, opts) in enumerate(QS))
kvb_js = r'''<script>
(function(){
var f=document.getElementById("kvb"), out=document.getElementById("kvb-out");
f.addEventListener("submit",function(e){ e.preventDefault();
  var K=0,B=0,miss=0, notes=[];
  ["q1","q2","q3","q4","q5","q6"].forEach(function(n){ var c=f.querySelector('input[name="'+n+'"]:checked'); if(!c){miss++;return;}
    var v=c.value; var k=v.match(/K(\d)/), b=v.match(/B(\d)/); if(k)K+=+k[1]; if(b)B+=+b[1]; });
  if(miss){ out.innerHTML='<p class="fstat err" style="display:block">Answer all six questions to get a recommendation ('+miss+' left).</p>'; return; }
  var v, h, p;
  if(K-B>=3){ h="A keyword (exact-match) domain fits you."; p="Your answers point to a business that wins on clarity: local or campaign-driven, explaining itself on signs and calls, without a big budget to teach people a new word. A name that says what you do and where does that work for free. It will not rank you by itself &mdash; it makes every ad, sign and referral easier to act on.";}
  else if(B-K>=3){ h="A brand domain fits you."; p="Your answers point to growth: new services or markets, a budget to build recognition, and a trademark worth protecting. Descriptive phrases are generally hard to protect as trademarks and can box you in later. Pick a short, sayable brand and, if you like, add a keyword name for a specific campaign.";}
  else { h="Do both: a brand for the company, a keyword name for campaigns."; p="Your answers pull both ways. Plenty of businesses run the company under a brand and point a plain-language keyword domain at a focused landing page for one service or city. You get recognition and clarity without choosing.";}
  out.innerHTML='<div class="verdict" tabindex="-1"><p style="font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;margin:0 0 6px;opacity:.75">Keyword '+K+' &middot; Brand '+B+'</p><h3>'+h+'</h3><p>'+p+'</p><p><a href="/domains/">Search keyword names</a> &middot; <a href="/domains/?tag=B">See brandable names</a> &middot; <a href="/find-it-for-me/">Have us shortlist for you</a></p></div>';
  out.querySelector(".verdict").focus();
});
})();
</script>'''
tool_page("/keyword-vs-brand-domain/", "Keyword or Brand Domain? A 6-Question Helper",
          "Should your business use an exact-match keyword domain or a brand name? Answer six questions and get a straight recommendation with the reasoning shown.",
          [("Home", "/"), ("Free tools", "/guides/"), ("Keyword or brand?", "/keyword-vs-brand-domain/")], "Free tool &middot; decision helper",
          "Keyword domain or brand domain?",
          "There is no universal right answer, and anyone who says otherwise is selling one of the two. Answer six questions about your business and you will see which way your own situation points &mdash; and why.",
          '<section style="padding-top:10px"><div class="wrap narrow"><form id="kvb" novalidate>' + qhtml +
          '<button class="btn btn-p" type="submit">Show my recommendation</button></form><div id="kvb-out" aria-live="polite"></div>'
          '<div class="body" style="margin-top:34px"><h2 class="sec-h" style="font-size:clamp(1.4rem,3.4vw,1.9rem)">How the scoring works</h2>'
          '<p>Each answer adds points to <strong>keyword</strong>, <strong>brand</strong>, or neither. A lead of three or more points gives a single recommendation; anything closer recommends both. The weights reflect what each kind of name is genuinely good at:</p>'
          '<ul><li><strong>Keyword names</strong> explain themselves instantly, survive a phone call and a truck door, and suit one service in one market. They do not earn rankings by themselves (<a href="/does-a-keyword-domain-help-seo/">sources here</a>).</li>'
          '<li><strong>Brand names</strong> stretch across new services and cities, and are generally easier to protect as trademarks than descriptive phrases &mdash; but they cost more to teach people.</li></ul>'
          '<p>Want to test a specific name? Run it through the <a href="/domain-name-checker/">domain name checker</a>.</p></div></div></section>' + kvb_js,
          [("Can I use both?", "Yes, and many businesses do: a brand for the company and a keyword domain pointed at a landing page for one service or city."),
           ("Will a keyword domain help me rank on Google?", "Not by itself. Google has said keywords in a domain do not earn a ranking on their own. What it does help with is clarity, recall and click-through. <a href=\"/does-a-keyword-domain-help-seo/\">The full answer, with sources</a>.")])

# ============================================================== /domain-buyer-checklist/
CHK = [("Before you make an offer", [
        ("Check it is not simply available", "Search it at any registrar first. People overpay for names that were never registered.", ("Register a domain", "/register-a-domain/")),
        ("Look up the registration record", "Registrar, creation and expiry dates, and whether the contact is redacted.", ("ICANN Lookup", "https://lookup.icann.org/")),
        ("See how it was used before", "Old snapshots show spam, adult or abandoned history you would inherit.", ("Wayback Machine", "https://web.archive.org/")),
        ("Search for trademark conflicts", "A name that matches someone's registered mark can be taken from you.", ("USPTO Trademark Search", "https://tmsearch.uspto.gov/")),
        ("Run it through the phone test", "Say it once to someone and see if they can type it.", ("Domain name checker", "/domain-name-checker/"))]),
       ("Before you pay", [
        ("Agree how money and the name move", "Use a neutral escrow service on any meaningful purchase, or a seller you can verify.", ("How escrow works", "/blog/how-a-domain-transfer-actually-works/")),
        ("Ask when it was last registered or transferred", "Registrars can refuse a transfer within 60 days of registration or a prior transfer.", ("ICANN Transfer Policy", "https://www.icann.org/resources/pages/transfer-policy-2016-06-01-en")),
        ("Ask the seller not to edit the contact details", "Changing the registrant can trigger a 60-day transfer lock at many registrars.", None),
        ("Get the deal in writing", "Name, price, who pays fees, and what is included (site, content, email) &mdash; in one email both sides confirm.", None)]),
       ("During and after the transfer", [
        ("Unlock + authorization code", "The seller unlocks the name and sends the auth code privately; you start the transfer at your registrar.", None),
        ("Recreate DNS and email records first", "If the name had email or a site, copy the records before the switch.", ("Email &amp; DNS guide", "/guides/domain-email-dns-transfer/")),
        ("Turn on lock, auto-renew and 2-factor", "Most lost domains are expired or hijacked accounts, not legal disputes.", None),
        ("Update your contact details and keep them current", "Registrars send renewal and verification notices to the registrant email.", None)])]
chk_html = ""
i = 0
for grp, items in CHK:
    chk_html += f'<h2 class="sec-h" style="font-size:clamp(1.3rem,3vw,1.7rem);margin-top:30px">{grp}</h2><ul class="checklist">'
    for t, d, link in items:
        i += 1
        lk = (f' <a href="{link[1]}"' + (' target="_blank" rel="noopener"' if link[1].startswith("http") else "") + f'>{link[0]}</a>') if link else ""
        chk_html += f'<li><label><input type="checkbox" data-k="c{i}"><span><b>{t}</b><span>{d}{lk}</span></span></label></li>'
    chk_html += '</ul>'
chk_js = r'''<script>
(function(){
var K="bdfb_buyer_checklist", st={}; try{ st=JSON.parse(localStorage.getItem(K)||"{}"); }catch(e){}
var boxes=[].slice.call(document.querySelectorAll(".checklist input")), pr=document.getElementById("chk-pr");
function upd(){ var n=boxes.filter(function(b){return b.checked;}).length; pr.textContent=n+" of "+boxes.length+" done"+(n===boxes.length?" — you are ready.":"."); }
boxes.forEach(function(b){ b.checked=!!st[b.dataset.k]; b.addEventListener("change",function(){ st[b.dataset.k]=b.checked; try{ localStorage.setItem(K,JSON.stringify(st)); }catch(e){} upd(); }); });
document.getElementById("chk-print").addEventListener("click",function(){ window.print(); });
document.getElementById("chk-reset").addEventListener("click",function(){ boxes.forEach(function(b){b.checked=false;}); st={}; try{ localStorage.removeItem(K); }catch(e){} upd(); });
upd();
})();
</script>'''
tool_page("/domain-buyer-checklist/", "Domain Buyer's Checklist: 13 Checks Before You Pay",
          "A free, printable checklist for buying a domain: availability, ownership record, history, trademarks, escrow, the 60-day transfer rules, DNS and security.",
          [("Home", "/"), ("Guides", "/guides/"), ("Buyer's checklist", "/domain-buyer-checklist/")], "Free checklist &middot; saves in your browser",
          "The domain buyer&rsquo;s checklist.",
          "Thirteen checks, in the order they matter, whether you buy from us or anyone else. Tick them off as you go &mdash; your progress stays in this browser only.",
          '<section style="padding-top:10px"><div class="wrap narrow">' + chk_html +
          '<p class="progress" id="chk-pr" aria-live="polite"></p><div class="btn-row"><button type="button" class="btn btn-s" id="chk-print">Print this checklist</button><button type="button" class="btn btn-s" id="chk-reset">Start over</button><a class="btn btn-p" href="/domains/">Browse our names</a></div>'
          '<p class="srcs" style="margin-top:24px">This is general information, not legal advice. Transfer rules are set by ICANN and applied by each registrar; ICANN has been revising its Transfer Policy, so check the current version and your registrar&rsquo;s help pages for exact timing.</p></div></section>' + chk_js)

# ============================================================== guides
GUIDES = []
def guide(slug, title, desc, h1, lede, sections, faqs, srcs, minutes):
    path = f"/guides/{slug}/"
    toc = '<nav class="toc" aria-label="On this page"><h2 style="font-family:var(--sans);font-size:.74rem;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-70);margin-bottom:10px">On this page</h2><ol>' + "".join(f'<li><a href="#{a}">{h}</a></li>' for a, h, _ in sections) + '</ol></nav>'
    body = "".join(f'<h2 id="{a}">{h}</h2>{b}' for a, h, b in sections)
    main = ('<section class="hero" style="padding:40px 0 24px"><div class="wrap">' + C.crumbs_html([("Home", "/"), ("Guides", "/guides/"), (h1, path)]) +
            f'<span class="eyebrow">Guide &middot; {minutes} min read</span><h1 style="font-size:clamp(1.9rem,5vw,3rem);max-width:24ch">{h1}</h1><p class="lede">{lede}</p>'
            f'<p class="artmeta"><span>By Zachary Tye Wennstedt, Eye To Ad Media</span><span>Updated October 2026</span></p></div></section>'
            f'<section style="padding-top:10px"><div class="wrap"><div class="article">{toc}{body}' + sources(srcs) +
            '<div class="related"><h2 style="font-size:1.2rem">Keep going</h2><div class="hubstrip"><a href="/domain-buyer-checklist/">Buyer&rsquo;s checklist</a><a href="/blog/how-a-domain-transfer-actually-works/">How transfers work</a><a href="/guides/">All guides</a><a href="/domains/">Search our names</a></div></div>'
            '</div></div></section><section class="tint"><div class="wrap narrow"><span class="eyebrow">Straight answers</span><h2 class="sec-h">Questions people ask.</h2>' + C.faq_html(faqs) + '</div></section>' + CLOSE)
    art = {"@type": "Article", "headline": h1, "description": desc, "author": {"@type": "Person", "name": "Zachary Tye Wennstedt"},
           "publisher": {"@id": C.SITE + "/#org"}, "dateModified": TODAY, "mainEntityOfPage": C.SITE + path}
    write(path, C.page(path, title, desc, [("Home", "/"), ("Guides", "/guides/"), (h1, path)], main, N, [art, C.faq_ld(faqs)]))
    GUIDES.append((path, h1, desc))

guide("domain-email-dns-transfer", "Domain Transfers: What Happens to Email and DNS",
      "Buying or moving a domain? What happens to its email, website and DNS records during a transfer, and the steps that keep everything working.",
      "What happens to email and DNS when a domain changes hands.",
      "The domain registration is only one of three things that make a name work. The other two &mdash; DNS and the services it points to &mdash; are where most transfer problems actually happen.",
      [("three", "Three separate things, often at three companies",
        "<p>A working domain involves three layers, and they are frequently held at different companies:</p><ul><li><strong>The registration</strong> &mdash; who holds the name, at which registrar, and until when. This is what a transfer moves.</li>"
        "<li><strong>DNS</strong> &mdash; the records that say where the website, email and other services live. They are hosted by whoever runs the domain&rsquo;s nameservers: often the registrar, sometimes a separate DNS provider or the web host.</li>"
        "<li><strong>The services</strong> &mdash; the web host, the email provider, any apps. They keep running wherever they are; DNS just points to them.</li></ul>"
        "<p>A registrar transfer moves the first layer. Whether the second layer survives depends on where it is hosted.</p>"),
       ("dns", "When DNS survives a transfer, and when it does not",
        "<p>If the domain uses nameservers at an independent DNS provider or web host, a registrar transfer normally leaves them in place and nothing visible changes.</p>"
        "<p>If it uses the old registrar&rsquo;s free DNS, the records live in the old registrar&rsquo;s account. Depending on that registrar, they may be removed once the domain leaves &mdash; and the website and email go dark until the records are recreated somewhere else.</p>"
        "<p>The fix is boring and reliable: <strong>copy every DNS record before the transfer</strong>, recreate them at the new DNS host, confirm they match, then switch nameservers. Lowering the record TTLs a day ahead makes any change take effect faster.</p>"),
       ("email", "Email is the part that bites",
        "<p>Email depends on a handful of DNS records: <strong>MX</strong> records that say which server accepts mail, plus <strong>TXT</strong> records for SPF, DKIM and DMARC that tell other mail systems which senders are legitimate. Miss one and mail bounces or lands in spam.</p>"
        "<p>When you <strong>buy</strong> a domain that had email on it, the previous owner&rsquo;s addresses stop working for them the moment DNS points elsewhere &mdash; and mail sent to those addresses may start arriving at whatever you set up. Do not set up a catch-all inbox on a name you just bought, and do not read mail that was clearly meant for the previous owner.</p>"
        "<p>When you <strong>sell</strong> a domain, change the login email on every account that uses an address at that domain <em>before</em> you hand it over. Whoever controls the domain&rsquo;s email can request password resets.</p>"),
       ("site", "The website and its security certificate",
        "<p>A website keeps running on its host, but the HTTPS certificate is tied to proof of control of the domain. After a change of owner or DNS, expect the new owner&rsquo;s host to issue a fresh certificate. Most hosts do this automatically once DNS points at them.</p>"
        "<p>Buying a <a href=\"/developed-assets/\">developed name</a> with a live site? Agree in writing what moves with it: hosting account, files, content, analytics and email &mdash; they are separate from the domain registration.</p>"),
       ("steps", "A safe order of operations",
        "<ol><li>Export or screenshot every DNS record (A, AAAA, CNAME, MX, TXT, SRV).</li><li>Set up the new DNS host and recreate the records; lower TTLs a day ahead.</li>"
        "<li>Seller unlocks the domain and sends the authorization code privately.</li><li>Buyer starts the transfer at their registrar; it completes when the old registrar releases it.</li>"
        "<li>Point nameservers to the new DNS host if they are not already there.</li><li>Test: website over HTTPS, send and receive email, check SPF/DKIM/DMARC.</li>"
        "<li>Turn on the registrar lock, auto-renew and two-factor login.</li></ol>"
        "<p>Want the transfer mechanics &mdash; auth codes, escrow and the 60-day rules &mdash; in depth? Read <a href=\"/blog/how-a-domain-transfer-actually-works/\">how a domain transfer actually works</a>. Need a website built on your new name? <a href=\"https://eyetoad.com\" rel=\"noopener\">Eye To Ad Media</a> builds custom-coded sites and handles the SEO side.</p>")],
      [("Will my website go down during a domain transfer?", "Usually not, if the domain's nameservers are at an independent DNS provider or host. If DNS is hosted at the old registrar, copy the records and recreate them elsewhere first."),
       ("Does buying a domain give me the previous owner's email?", "No. Mailboxes live with the email provider, not the domain. But once you control DNS, new mail sent to old addresses may reach you, so handle it responsibly."),
       ("How long does DNS take to update?", "It depends on each record's TTL (time to live). Lowering TTLs a day before a change helps updates take effect faster.")],
      [("ICANN Lookup", "https://lookup.icann.org/"), ("ICANN Transfer Policy", "https://www.icann.org/resources/pages/transfer-policy-2016-06-01-en")], 6)

guide("com-vs-other-extensions", "Should Your Business Domain Be a .com?",
      ".com, .net, a country code or a new extension? How each is treated by people and by Google, what to watch for, and when a non-.com is fine.",
      "Should your business domain be a .com?",
      "Usually, yes &mdash; but not for the reasons people assume. Here is what the extension actually changes, what it does not, and when something else is the better call.",
      [("why", "Why .com is still the default",
        "<p>.com is the largest top-level domain by registrations, and has been for decades &mdash; Verisign, which operates .com, publishes the figures every quarter in its <a href=\"https://www.dnib.com/\" rel=\"noopener\" target=\"_blank\">Domain Name Industry Brief</a>. That scale is the whole argument: people assume .com, type .com by habit, and phones and email apps autocomplete it.</p>"
        "<p>The practical cost of a non-.com is leakage. If you own <em>yourname.net</em> and someone else owns <em>yourname.com</em>, a share of visitors and emails meant for you will go to them. Before buying any non-.com, look up who owns the .com.</p>"),
       ("google", "What Google does and does not care about",
        "<p>Google has said that new generic extensions are treated like other generic extensions &mdash; no built-in boost and no penalty for being a .homes or a .agency rather than a .com.</p>"
        "<p>Country-code extensions are different: Google treats a ccTLD as a signal that a site targets that country. Google&rsquo;s documentation notes that some country codes, such as .tv and .me, are treated as generic because people use them that way. If you serve the U.S., a foreign country code you picked for its letters can send the wrong signal; check Google&rsquo;s list before you commit.</p>"
        "<p>Some country codes also restrict who can register them, for example by requiring a local presence. Read the registry&rsquo;s rules first.</p>"),
       ("when", "When a non-.com is the right call",
        "<ul><li>You serve one country and its country code is what locals expect.</li><li>The .com is unaffordable, and you also control or can live with who owns it.</li>"
        "<li>It is a campaign or product name where the extension is part of the brand.</li><li>You are a nonprofit (.org) or a tech product where .io or .ai is the norm in your field.</li></ul>"
        f"<p>Of the {N} names in our portfolio, {N - len(noncom)} are .com. The others are {', '.join(noncom)}.</p>"),
       ("test", "Quick test before you decide",
        "<p>Say the full name, extension included, to someone who has never heard it and ask them to type it. If they type .com instead, you have your answer. Our <a href=\"/domain-name-checker/\">domain name checker</a> scores the extension along with length, hyphens and the phone test, and shows every rule.</p>")],
      [("Is .com better for SEO?", "Not by itself. Google treats generic extensions alike; the advantage of .com is human habit and less leakage to someone else's site."),
       ("Should I buy the .net and .org too?", "Only if leakage or impersonation is a real risk for your business. For most small businesses, owning the .com and the most common misspelling is enough.")],
      [("Verisign Domain Name Industry Brief", "https://www.dnib.com/"), ("Google: managing multi-regional sites", "https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites"),
       ("Google: handling of new top-level domains", "https://developers.google.com/search/blog/2015/07/googles-handling-of-new-top-level")], 5)

# guides hub
TOOLS = [("/find-it-for-me/", "Find it for me", "Tell us your business; we match a name from the portfolio or go find one."),
         ("/domain-name-checker/", "Domain name checker", "A transparent 100-point readability score. Every rule shown."),
         ("/domain-name-ideas/", "Name ideas from our portfolio", "Only real names we own, each with the reason it fits."),
         ("/keyword-vs-brand-domain/", "Keyword or brand domain?", "Six questions, a straight recommendation, reasoning visible."),
         ("/what-is-my-domain-worth/", "What is my domain worth?", "The factors that move price, an honest checklist, a free written read."),
         ("/who-owns-this-domain/", "Who owns this domain?", "Open the ICANN record, read it, and understand the transfer rules."),
         ("/domain-buyer-checklist/", "Domain buyer&rsquo;s checklist", "Thirteen checks before you pay, saved in your browser.")]
READS = [("/does-a-keyword-domain-help-seo/", "Does a keyword domain help SEO?"), ("/buy-a-domain/", "How buying a domain from us works"),
         ("/blog/how-a-domain-transfer-actually-works/", "How a domain transfer actually works"), ("/blog/how-to-buy-a-domain-someone-else-owns/", "How to buy a domain someone else owns"),
         ("/blog/check-a-domains-history-before-you-buy/", "Check a domain&rsquo;s history before you buy"), ("/blog/what-a-domain-name-is-actually-worth/", "What a domain name is actually worth"),
         ("/blog/picking-a-business-name-that-passes-the-phone-test/", "Picking a name that passes the phone test"), ("/blog/buying-a-website-that-already-works/", "Buying a website that already works")]
hub = ('<section style="padding-top:10px"><div class="wrap"><span class="eyebrow">Free tools</span><h2 class="sec-h">Use one in under a minute.</h2><div class="grid g3">' +
       "".join(f'<a class="card" href="{u}"><h3>{t}</h3><p>{d}</p><span class="more">Open</span></a>' for u, t, d in TOOLS) + '</div>'
       '<span class="eyebrow" style="margin-top:46px">New guides</span><div class="grid g2">' +
       "".join(f'<a class="card" href="{u}"><h3>{t}</h3><p>{esc(d)}</p><span class="more">Read</span></a>' for u, t, d in GUIDES) + '</div>'
       '<span class="eyebrow" style="margin-top:46px">Long reads</span><div class="hubstrip">' + "".join(f'<a href="{u}">{t}</a>' for u, t in READS) + '</div>'
       '<div class="callout" style="margin-top:36px"><p><b>The transfer timeline in one paragraph:</b> once a price is agreed and paid, the seller unlocks the name and sends an authorization code; the buyer starts the transfer at their own registrar; the old registrar has a short window to release it (typically a few days for a .com). Registrars may refuse a transfer within 60 days of a new registration or a previous transfer, and a change of registrant can trigger a 60-day lock at many registrars. Details: <a href="/blog/how-a-domain-transfer-actually-works/">how transfers work</a>.</p></div>'
       '<p style="margin-top:20px">Looking for authoritative outside sources? See <a href="/resources/">resources</a>.</p></div></section>')
tool_page("/guides/", "Domain Buying Guides and Free Tools",
          "Plain-English guides and free tools for choosing, checking, buying and transferring a business domain. Sourced, no ranking promises, no fake appraisals.",
          [("Home", "/"), ("Guides", "/guides/")], "Guides &amp; tools", "Everything you need to pick and buy the right domain.",
          "Free tools, short guides and long reads, written by people who sell domains for a living and will tell you when you should not buy one.", hub)

# resources
RES = [("Look up and transfer", [("ICANN Lookup", "https://lookup.icann.org/", "The official registration-data lookup for any domain."),
                                  ("ICANN Transfer Policy", "https://www.icann.org/resources/pages/transfer-policy-2016-06-01-en", "The rules registrars follow when a domain moves."),
                                  ("ICANN UDRP", "https://www.icann.org/resources/pages/help/dndr/udrp-en", "The dispute process for domains that infringe a trademark.")]),
       ("Search and names", [("Google SEO Starter Guide", "https://developers.google.com/search/docs/fundamentals/seo-starter-guide", "Google&rsquo;s own basics, including what domains do and do not do."),
                             ("Google: site names in search", "https://developers.google.com/search/docs/appearance/site-names", "How Google chooses the name shown for your site."),
                             ("Google spam policies", "https://developers.google.com/search/docs/essentials/spam-policies", "What gets sites demoted &mdash; worth reading before buying a used name.")]),
       ("Facts and protection", [("Verisign Domain Name Industry Brief", "https://www.dnib.com/", "Quarterly registration figures for .com and the whole market."),
                                 ("USPTO Trademark Search", "https://tmsearch.uspto.gov/", "Check a name against U.S. registered trademarks."),
                                 ("Wayback Machine", "https://web.archive.org/", "See how a domain was used before you buy it."),
                                 ("FTC: report fraud", "https://reportfraud.ftc.gov/", "Where to report domain and website scams in the U.S.")])]
res = '<section style="padding-top:10px"><div class="wrap">'
for grp, items in RES:
    res += f'<h2 class="sec-h" style="font-size:clamp(1.3rem,3vw,1.8rem);margin-top:24px">{grp}</h2><div class="reslist">' + "".join(
        f'<div class="res"><h3>{t}</h3><p>{d}</p><a class="go" href="{u}" target="_blank" rel="noopener">Open {t.split(":")[0]} &rarr;</a></div>' for t, u, d in items) + '</div>'
res += ('<h2 class="sec-h" style="font-size:clamp(1.3rem,3vw,1.8rem);margin-top:40px">After you buy</h2>'
        '<p class="lede">Get listed where local customers search: <a href="https://usabusinesssearch.com" rel="noopener" target="_blank">USABusinessSearch.com</a> nationally and <a href="https://cobusinesslist.com" rel="noopener" target="_blank">COBusinessList.com</a> in Colorado &mdash; both business directories run by the same owner as this site.</p>'
        '<p style="font-size:.9rem;color:var(--ink-70)">We link to these because they are useful and authoritative, not because anyone paid us. None of them are affiliated with us except the two directories named above.</p></div></section>')
tool_page("/resources/", "Domain Resources: ICANN, Google, USPTO and More",
          "Authoritative, non-commercial resources for domain buyers: ICANN Lookup and transfer policy, Google Search Central, Verisign's industry brief, USPTO, FTC.",
          [("Home", "/"), ("Resources", "/resources/")], "Outside resources", "The sources we trust, in one place.",
          "Official lookups, policies and data you can check yourself &mdash; the same places we send our own buyers.", res)


# ============================================================== upgrades to existing pages
def edit(fn, fnc):
    s = open(fn).read(); s2 = fnc(s)
    if s2 != s: open(fn, "w").write(s2)

POPQ = ["dentist", "denver", "walk in tub", "hawaii", "belize", "fence omaha", "ai agent", "glp-1"]
def home(s):
    hero = ('<div class="hfind" id="hero-finder"><!--hf--><form class="bigsearch" action="/domains/" method="get" role="search">'
            f'<label class="vh" for="hq">Search {N} business domains</label><input id="hq" type="search" name="q" placeholder="What does your business do? Try dentist, denver…" autocomplete="off" enterkeyhint="search"><button type="submit">Search</button></form>'
            f'<p class="hcount"><b>{N} names</b> across {ncats} industries &mdash; search by service, city or state. Typos are fine.</p>'
            '<div class="popq"><span>Try:</span>' + "".join(f'<button type="button" data-q="{q}">{q}</button>' for q in POPQ) + '</div>'
            '<div class="hres" aria-live="polite" hidden></div><a class="hall" href="/domains/" hidden>See all</a><!--/hf--></div>')
    s = re.sub(r'<form class="bigsearch" action="/domains/" method="get" role="search" style="margin-top:28px">.*?</form>', lambda m: hero, s, count=1, flags=re.S)
    s = re.sub(r'<div class="hfind" id="hero-finder"><!--hf-->.*?<!--/hf--></div>', lambda m: hero, s, count=1, flags=re.S)
    s = s.replace('<div class="btn-row"><a class="btn btn-p" href="/domains/">Browse the portfolio</a><a class="btn btn-s" href="tel:+18004818638">Call 1-800-481-8638</a></div>',
                  '<div class="btn-row"><a class="btn btn-p" href="/find-it-for-me/">Let us find it for you</a><a class="btn btn-s" href="/domains/">Browse the portfolio</a></div>')
    sec = ('<!--concierge--><section class="tint" id="find"><div class="wrap"><span class="eyebrow">Domain concierge &middot; free to ask</span>'
           '<h2 class="sec-h">Not sure what to search? Tell us about the business.</h2>'
           '<p class="lede" style="margin-bottom:24px">Matching names from the portfolio appear as you type. Tap any you like, send it, and a real person replies with options for your budget &mdash; including when the right move is to register a name yourself.</p>'
           + concierge("hc", compact=True) + '</div></section><!--/concierge-->')
    if "<!--concierge-->" in s:
        s = re.sub(r'<!--concierge-->.*?<!--/concierge-->', lambda m: sec, s, count=1, flags=re.S)
    else:
        s = s.replace('</div></section>\n\n<section class="tint" style="padding:60px 0">', '</div></section>\n' + sec + '\n<section style="padding:60px 0">', 1)
    s = re.sub(r'(<a class="cw" href="[^"]*" style="[^"]*") aria-label="[^"]*"', r'\1', s)
    s = s.replace("Exact-match names across fourteen categories.", f"Exact-match names across {ncats} categories.")
    hubs = f'<h2 class="sec-h">{ncats} categories. Start where your business lives.</h2>\n<!--hubs-->' + hubstrip() + '<h3 style="margin:26px 0 0;font-size:1.15rem">Or start with a place</h3>' + placestrip() + '<!--/hubs-->'
    if "<!--hubs-->" in s:
        s = re.sub(r'<h2 class="sec-h">[^<]*</h2>\n<!--hubs-->.*?<!--/hubs-->', lambda m: hubs, s, count=1, flags=re.S)
    else:
        s = re.sub(r'<h2 class="sec-h">\w+ categories\. Start where your business lives\.</h2>\n<div class="hubstrip">.*?</div>', lambda m: hubs, s, count=1, flags=re.S)
    s = s.replace('<span class="creds-i"><b>A+</b><span>BBB accredited</span></span>', '<span class="creds-i"><b>A+</b><span>BBB accredited (Eye To Ad Media)</span></span>')
    return s
edit("index.html", home)

def worth(s):
    if "<!--worthcheck-->" in s: s = re.sub(r"<!--worthcheck-->.*?<!--/worthcheck-->\n?", "", s, flags=re.S)
    items = [("It is a .com", "People type .com by habit; buyers price other extensions lower."),
             ("Under about 15 characters", "Short names are easier to say, type and fit on a sign."),
             ("No hyphens or numbers", "Nothing to explain out loud."),
             ("Passes the phone test", "Say it once; can a stranger type it?"),
             ("Real commercial meaning", "It names a service, product or market people pay for."),
             ("A specific kind of business would want it", "You can name at least one type of buyer who needs exactly this."),
             ("Clean history", "No spam, adult or penalty past in the Wayback Machine or a site: search."),
             ("No trademark conflict", "It does not match someone else&rsquo;s registered mark."),
             ("Something live behind it", "A working site with real content and history is a bigger asset."),
             ("The .com is not owned by a competitor", "If yours is a non-.com, who owns the .com matters.")]
    sec = ('<!--worthcheck--><section><div class="wrap narrow"><span class="eyebrow">Honest value checklist</span><h2 class="sec-h">Ten factors. No made-up dollar figure.</h2>'
           '<p class="lede">Tick what is true of your name. You get a count of factors in your favor and what it means &mdash; never an invented price.</p><ul class="checklist" id="wck">' +
           "".join(f'<li><label><input type="checkbox"><span><b>{t}</b><span>{d}</span></span></label></li>' for t, d in items) +
           '</ul><p class="progress" id="wck-out" aria-live="polite">0 of 10 factors in your favor.</p>'
           '<p style="font-size:.95rem;color:var(--ink-70)">Even 10 of 10 does not set a price &mdash; one motivated buyer does. Use the form below for a free written read from a person, or <a href="/domain-name-checker/">score the name&rsquo;s readability</a>.</p></div></section>'
           '<script>(function(){var b=[].slice.call(document.querySelectorAll("#wck input")),o=document.getElementById("wck-out");function u(){var n=b.filter(function(x){return x.checked;}).length;o.textContent=n+" of 10 factors in your favor. "+(n>=8?"That is a strong set of fundamentals; value now depends on finding the buyer who needs it.":n>=5?"Solid fundamentals with real gaps; the right buyer still matters most.":n?"Several factors work against it; it may be worth more to you in use than for sale.":"");}b.forEach(function(x){x.addEventListener("change",u);});})();</script><!--/worthcheck-->')
    anchor = '<section><div class="wrap">\n<div class="grid g2" style="align-items:start;gap:36px">\n<div class="body">\n<span class="eyebrow">Send it over</span>'
    return s.replace(anchor, sec + "\n" + anchor, 1) if anchor in s else s
edit("what-is-my-domain-worth/index.html", worth)

def whoowns(s):
    if "<!--xfer-->" in s: s = re.sub(r"<!--xfer-->.*?<!--/xfer-->\n?", "", s, flags=re.S)
    sec = ('<!--xfer--><section><div class="wrap"><div class="grid g2" style="align-items:start;gap:36px"><div class="body"><span class="eyebrow">After you agree a price</span>'
           '<h2 class="sec-h">How the transfer actually works.</h2><ol class="numlist" style="padding:0;margin-top:20px">'
           '<li><h3>Agree terms in writing</h3><p>Name, price, who pays fees, and what is included. Use escrow on a meaningful purchase.</p></li>'
           '<li><h3>Seller unlocks and sends the auth code</h3><p>The authorization (EPP) code proves control. It should be sent privately, never posted.</p></li>'
           '<li><h3>Buyer starts the transfer</h3><p>At the buyer&rsquo;s own registrar. The old registrar has a short window to release it &mdash; typically a few days for a .com.</p></li>'
           '<li><h3>Lock it down</h3><p>Registrar lock on, auto-renew on, two-factor login on, contact details current.</p></li></ol></div>'
           '<div class="card" style="padding:26px"><h3 style="margin-bottom:10px">The 60-day rules</h3><p>Under ICANN&rsquo;s Transfer Policy, a registrar may refuse a transfer to another registrar within 60 days of the domain&rsquo;s initial registration or of a previous transfer. Separately, changing the registrant&rsquo;s details can trigger a 60-day transfer lock at many registrars unless the registrant opted out beforehand.</p>'
           '<p style="margin-bottom:0">Ask when the name was last registered or transferred <em>before</em> you set a closing date, and ask the seller not to edit contact details mid-deal. ICANN has been revising this policy, so confirm the current rules with the <a href="https://www.icann.org/resources/pages/transfer-policy-2016-06-01-en" target="_blank" rel="noopener">ICANN Transfer Policy</a> and your registrar.</p>'
           '<div class="btn-row"><a class="btn btn-s" href="/domain-buyer-checklist/">Buyer&rsquo;s checklist</a><a class="btn btn-s" href="/guides/domain-email-dns-transfer/">Email &amp; DNS guide</a></div></div></div></div></section><!--/xfer-->')
    anchor = '<section id="acq">'
    return s.replace(anchor, sec + "\n" + anchor, 1) if anchor in s else s
edit("who-owns-this-domain/index.html", whoowns)

def contact(s):
    if "<!--ctrust-->" in s: return s
    return s.replace('<p class="formnote">Goes straight to a real inbox at Eye To Ad Media.', '<!--ctrust--><div class="trustrow" style="margin:0 0 14px">' + C.BBB + '<p>Eye To Ad Media is BBB accredited.</p></div><p class="formnote">Goes straight to a real inbox at Eye To Ad Media.', 1)
edit("contact/index.html", contact)

def finda(s):
    if "/find-it-for-me/" in s.split('<main')[1].split('</section>')[0]: return s
    return s.replace('<div class="btn-row"><a class="btn btn-p" href="#start">Start a search</a><a class="btn btn-s" href="tel:+18004818638">Or call 1-800-481-8638</a></div>',
                     '<div class="btn-row"><a class="btn btn-p" href="#start">Start a search</a><a class="btn btn-s" href="tel:+18004818638">Or call 1-800-481-8638</a><a class="btn btn-s" href="/find-it-for-me/">Not sure of the name? Let us match one</a></div>', 1)
edit("find-a-domain/index.html", finda)
