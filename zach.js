/* zach.js — Zach sales bot for bestdomainsforbusiness.com
   Integration: <script src="/zach.js" defer><\/script> before </body>
   Rules baked in and NOT to be softened:
     - never quotes, estimates or implies a price
     - lease is "might be available", never terms
     - every domain is for sale and negotiable, no exceptions
     - registration age only for eyetoad.com and agingsafelybaths.com (2012)
     - names not in the portfolio route to buyweburl.com
   No flashing animation anywhere; all repeating cycles 2.6s+; reduced motion honored. */
(function(){
  if (window.__zachBot) return;
  window.__zachBot = true;

  var TEL  = "1-800-481-8638";
  var TELH = "tel:+18004818638";

  /* ------------------------------------------------------------------ CSS */
  var css = `
#zbx{position:fixed;right:20px;bottom:20px;z-index:9999;font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
@media(max-width:520px){#zbx{right:14px;bottom:14px}}
#zbx .zbx-stage{position:relative;width:124px;height:150px;margin-left:auto}
@media(max-width:520px){#zbx .zbx-stage{width:112px;height:138px}}
#zbx .zbx-seal{position:absolute;right:8px;bottom:34px;width:96px;height:96px;padding:0;border:0;background:transparent;cursor:pointer;display:block}
#zbx .zbx-seal:focus-visible{outline:2px solid #e8c37a;outline-offset:6px;border-radius:50%}
#zbx .zbx-seal svg{display:block;width:100%;height:100%;overflow:visible}
#zbx .zbx-shine{animation:zbx-sweep 5.2s ease-in-out infinite;transform-origin:center}
@keyframes zbx-sweep{0%,100%{opacity:.12;transform:translateX(-26px)}50%{opacity:.4;transform:translateX(26px)}}
#zbx .zbx-breathe{animation:zbx-breathe 4.4s ease-in-out infinite;transform-origin:center}
@keyframes zbx-breathe{0%,100%{transform:scale(1)}50%{transform:scale(1.028)}}
#zbx.is-bursting .zbx-crack-l{animation:zbx-shardL .9s cubic-bezier(.3,.7,.4,1) forwards}
#zbx.is-bursting .zbx-crack-r{animation:zbx-shardR .9s cubic-bezier(.3,.7,.4,1) forwards}
@keyframes zbx-shardL{to{transform:translate(-26px,14px) rotate(-24deg);opacity:0}}
@keyframes zbx-shardR{to{transform:translate(26px,16px) rotate(22deg);opacity:0}}
#zbx.is-bursting .zbx-seal{pointer-events:none}
#zbx.is-open .zbx-seal,#zbx.is-live .zbx-seal{opacity:0;pointer-events:none;transition:opacity .5s ease}
#zbx .zbx-pill{position:absolute;right:0;bottom:0;left:0;text-align:center;background:#1b2b47;color:#e8c37a;border:1px solid rgba(200,150,62,.42);border-radius:999px;padding:6px 10px;font-size:.7rem;line-height:1.25;pointer-events:none;white-space:nowrap}
#zbx.is-bursting .zbx-pill,#zbx.is-live .zbx-pill,#zbx.is-open .zbx-pill{opacity:0;transition:opacity .35s ease}
#zbx .zbx-smoke{position:absolute;inset:-70px -60px -30px -60px;pointer-events:none;opacity:0}
#zbx.is-bursting .zbx-smoke,#zbx.is-live .zbx-smoke{opacity:1}
#zbx .zbx-puff{position:absolute;border-radius:50%;background:radial-gradient(circle at 38% 34%,rgba(255,253,247,.95),rgba(226,219,201,.6) 44%,rgba(190,182,162,0) 72%);opacity:0;transform:scale(.2)}
#zbx.is-bursting .zbx-puff{animation:zbx-puff 2.6s cubic-bezier(.18,.7,.3,1) forwards}
@keyframes zbx-puff{0%{opacity:0;transform:scale(.18) translate(0,0)}16%{opacity:.92}55%{opacity:.6}100%{opacity:0;transform:scale(2.5) translate(var(--dx,0),var(--dy,-34px))}}
#zbx .zbx-mote{position:absolute;width:5px;height:5px;border-radius:50%;background:#e8c37a;opacity:0}
#zbx.is-bursting .zbx-mote{animation:zbx-mote 3.1s ease-out forwards}
@keyframes zbx-mote{0%{opacity:0;transform:translate(0,0) scale(.5)}18%{opacity:.95}100%{opacity:0;transform:translate(var(--mx,0),var(--my,-86px)) scale(.2)}}
#zbx .zbx-guy{position:absolute;right:-6px;bottom:26px;width:132px;height:150px;opacity:0;pointer-events:none;transform:translateY(22px) scale(.86)}
@media(max-width:520px){#zbx .zbx-guy{width:118px;height:136px;right:-4px}}
#zbx.is-live .zbx-guy{animation:zbx-arrive 1.5s cubic-bezier(.2,.8,.3,1) .55s forwards;pointer-events:auto}
@keyframes zbx-arrive{0%{opacity:0;transform:translateY(22px) scale(.86)}45%{opacity:1}100%{opacity:1;transform:translateY(0) scale(1)}}
#zbx .zbx-guy svg{display:block;width:100%;height:100%;overflow:visible}
#zbx .zbx-wave{transform-origin:70px 150px}
#zbx.is-live .zbx-wave{animation:zbx-wave 3.4s ease-in-out 2.1s infinite}
@keyframes zbx-wave{0%,72%,100%{transform:rotate(0)}80%{transform:rotate(-13deg)}88%{transform:rotate(4deg)}}
#zbx .zbx-guy-btn{position:absolute;inset:0;background:transparent;border:0;padding:0;cursor:pointer}
#zbx .zbx-guy-btn:focus-visible{outline:2px solid #e8c37a;outline-offset:4px;border-radius:10px}
#zbx .zbx-balloon{position:absolute;right:104px;bottom:56px;width:264px;background:#fffdf7;color:#16202f;border:1px solid rgba(16,26,44,.18);border-radius:14px;padding:14px 16px 15px;font-size:.88rem;line-height:1.5;opacity:0;transform:translateY(8px) scale(.96);transform-origin:right bottom;pointer-events:none}
#zbx.is-live .zbx-balloon{animation:zbx-bal 1.1s cubic-bezier(.2,.8,.3,1) 1.5s forwards;pointer-events:auto}
@keyframes zbx-bal{to{opacity:1;transform:translateY(0) scale(1)}}
#zbx .zbx-balloon:after,#zbx .zbx-balloon:before{content:"";position:absolute;right:-11px;bottom:26px;width:0;height:0;border-top:9px solid transparent;border-bottom:9px solid transparent;border-left:11px solid #fffdf7}
#zbx .zbx-balloon:before{right:-13px;border-left-color:rgba(16,26,44,.18)}
#zbx .zbx-bal-name{font-family:Fraunces,Georgia,serif;font-weight:700;font-size:.95rem;color:#101a2c;margin:0 0 5px}
#zbx .zbx-balloon p{margin:0}
#zbx .zbx-bal-x{position:absolute;top:5px;right:7px;width:24px;height:24px;border:0;background:transparent;cursor:pointer;color:rgba(16,26,44,.4);font-size:1rem;line-height:1;border-radius:50%}
#zbx .zbx-bal-x:hover{color:#101a2c;background:rgba(16,26,44,.07)}
@media(max-width:640px){#zbx .zbx-balloon{right:88px;width:min(238px,calc(100vw - 130px));font-size:.84rem}}
#zbx.is-open .zbx-balloon{opacity:0;pointer-events:none;transition:opacity .3s ease}
#zbx .zbx-panel{position:fixed;right:20px;bottom:20px;width:376px;max-width:calc(100vw - 28px);height:min(586px,calc(100vh - 40px));background:#fffdf7;border:1px solid rgba(16,26,44,.2);border-radius:16px;overflow:hidden;display:none;flex-direction:column;box-shadow:0 24px 60px rgba(4,10,22,.42)}
@media(max-width:520px){#zbx .zbx-panel{right:8px;bottom:8px;max-width:calc(100vw - 16px);height:calc(100vh - 24px)}}
#zbx.is-open .zbx-panel{display:flex;animation:zbx-panel .42s cubic-bezier(.2,.8,.3,1)}
@keyframes zbx-panel{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}
#zbx .zbx-head{display:flex;align-items:center;gap:11px;background:#101a2c;color:#f5f0e4;padding:12px 13px;border-bottom:2px solid #c8963e}
#zbx .zbx-head-av{width:42px;height:42px;border-radius:50%;flex:0 0 42px;background:#1b2b47;overflow:hidden;border:1px solid rgba(200,150,62,.45)}
#zbx .zbx-head-av svg{display:block;width:100%;height:100%}
#zbx .zbx-head-txt{flex:1;min-width:0}
#zbx .zbx-head-n{font-family:Fraunces,Georgia,serif;font-weight:700;font-size:1rem}
#zbx .zbx-head-r{font-size:.73rem;color:rgba(245,240,228,.6);margin-top:1px}
#zbx .zbx-head-x{width:30px;height:30px;border:0;background:transparent;cursor:pointer;color:rgba(245,240,228,.6);font-size:1.2rem;line-height:1;border-radius:50%;flex:0 0 30px}
#zbx .zbx-head-x:hover{color:#fffdf7;background:rgba(245,240,228,.1)}
#zbx .zbx-log{flex:1;overflow-y:auto;padding:16px 14px 6px;background:#f5f0e4}
#zbx .zbx-msg{max-width:84%;margin-bottom:11px;font-size:.87rem;line-height:1.55;border-radius:13px;padding:10px 13px}
#zbx .zbx-bot{background:#fffdf7;color:#16202f;border:1px solid rgba(16,26,44,.12);border-bottom-left-radius:4px}
#zbx .zbx-me{background:#1b2b47;color:#f5f0e4;margin-left:auto;border-bottom-right-radius:4px}
#zbx .zbx-msg a{color:#8a5f14;font-weight:600}
#zbx .zbx-tel{display:inline-block;margin-top:7px;background:#c8963e;color:#16202f;font-weight:650;padding:8px 14px;border-radius:999px;text-decoration:none;font-size:.87rem}
#zbx .zbx-tel:hover{background:#e8c37a}
#zbx .zbx-chips{display:flex;flex-wrap:wrap;gap:6px;padding:8px 14px 12px;background:#f5f0e4}
#zbx .zbx-chip{background:transparent;color:#101a2c;border:1px solid rgba(16,26,44,.26);border-radius:999px;padding:6px 12px;font-size:.78rem;font-family:inherit;cursor:pointer}
#zbx .zbx-chip:hover{background:rgba(16,26,44,.07)}
#zbx .zbx-bar{display:flex;gap:8px;padding:10px 12px;background:#fffdf7;border-top:1px solid rgba(16,26,44,.12)}
#zbx .zbx-in{flex:1;border:1px solid rgba(16,26,44,.22);border-radius:999px;padding:10px 15px;font-size:.87rem;font-family:inherit;background:#fff;color:#16202f}
#zbx .zbx-in:focus{outline:2px solid #c8963e;outline-offset:-1px}
#zbx .zbx-send{width:40px;height:40px;flex:0 0 40px;border:0;border-radius:50%;background:#101a2c;color:#e8c37a;cursor:pointer;font-size:1rem}
#zbx .zbx-send:hover{background:#1b2b47}
#zbx .zbx-typing span{display:inline-block;width:6px;height:6px;border-radius:50%;background:rgba(16,26,44,.42);margin-right:4px;animation:zbx-dot 2.8s ease-in-out infinite}
#zbx .zbx-typing span:nth-child(2){animation-delay:.32s}
#zbx .zbx-typing span:nth-child(3){animation-delay:.64s}
@keyframes zbx-dot{0%,100%{opacity:.28}50%{opacity:.85}}
@media(prefers-reduced-motion:reduce){
#zbx .zbx-shine,#zbx .zbx-breathe,#zbx .zbx-wave,#zbx .zbx-typing span{animation:none!important}
#zbx.is-bursting .zbx-puff,#zbx.is-bursting .zbx-mote,#zbx.is-bursting .zbx-crack-l,#zbx.is-bursting .zbx-crack-r{animation-duration:.01ms!important}
#zbx.is-live .zbx-guy,#zbx.is-live .zbx-balloon{animation-duration:.01ms!important;animation-delay:0ms!important;opacity:1}
#zbx.is-open .zbx-panel{animation:none}}
`;

  /* ------------------------------------------------------------- artwork */
  var ART = `
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<linearGradient id="zg-hair" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f2d488"/><stop offset="1" stop-color="#c69433"/></linearGradient>
<linearGradient id="zg-suit" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2c3f61"/><stop offset="1" stop-color="#18253d"/></linearGradient>
<linearGradient id="zg-brass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#efcd85"/><stop offset=".5" stop-color="#c8963e"/><stop offset="1" stop-color="#9a6d22"/></linearGradient>
<radialGradient id="zg-sealglow" cx="50%" cy="50%" r="50%"><stop offset="55%" stop-color="rgba(200,150,62,.42)"/><stop offset="100%" stop-color="rgba(200,150,62,0)"/></radialGradient>
<symbol id="zbx-zach" viewBox="0 0 200 260">
<path d="M131 168 q22 10 25 36 l4 42 -20 4 -8-44 z" fill="#22334f"/>
<path d="M100 150 q-32 4 -44 26 -9 17 -11 84 h110 q-2-67 -11-84 -12-22 -44-26 z" fill="url(#zg-suit)"/>
<path d="M100 148 l-17 9 6 32 11 12 11-12 6-32 z" fill="#fbfaf6"/>
<path d="M83 157 l17-9 0 14 -12 12 z" fill="#eeece4"/>
<path d="M117 157 l-17-9 0 14 12 12 z" fill="#eeece4"/>
<path d="M100 153 l-6 7 6 7 6-7 z" fill="#a9761f"/>
<path d="M100 167 l-6 6 4 34 2 6 2-6 4-34 z" fill="url(#zg-brass)"/>
<path d="M83 157 q-12 5 -18 16 l22 56 8-44 z" fill="#32486d"/>
<path d="M117 157 q12 5 18 16 l-22 56 -8-44 z" fill="#32486d"/>
<path d="M128 196 l14 4 -3 8 -13-5 z" fill="#f3ede0"/>
<path d="M88 122 h24 v24 q-12 9 -24 0 z" fill="#e0a97e"/>
<path d="M88 122 h24 v10 q-12 7 -24 0 z" fill="#c9906a"/>
<ellipse cx="63" cy="90" rx="6.5" ry="9" fill="#e0a97e"/>
<ellipse cx="137" cy="90" rx="6.5" ry="9" fill="#e0a97e"/>
<ellipse cx="100" cy="84" rx="38" ry="43" fill="#edba8e"/>
<path d="M100 38 q-40 0 -40 36 0 8 2 14 3-22 12-27 2 9 8 12 -2-12 3-18 14 12 38 9 12-2 16-8 4 8 3 32 5-6 5-16 0-34 -47-34 z" fill="url(#zg-hair)"/>
<path d="M118 48 q16 6 20 22 -10-14 -26-16 z" fill="#e6c470" opacity=".7"/>
<path d="M78 74 q9-5 18-1" stroke="#b98a33" stroke-width="3.4" fill="none" stroke-linecap="round"/>
<path d="M104 73 q9-4 18 1" stroke="#b98a33" stroke-width="3.4" fill="none" stroke-linecap="round"/>
<ellipse cx="86" cy="86" rx="5" ry="5.6" fill="#fffdf7"/>
<ellipse cx="114" cy="86" rx="5" ry="5.6" fill="#fffdf7"/>
<circle cx="87" cy="87" r="2.9" fill="#2b4468"/><circle cx="115" cy="87" r="2.9" fill="#2b4468"/>
<circle cx="88.2" cy="85.6" r="1" fill="#fff"/><circle cx="116.2" cy="85.6" r="1" fill="#fff"/>
<path d="M100 90 q4 8 -2 11" stroke="#cf9468" stroke-width="2.6" fill="none" stroke-linecap="round"/>
<path d="M88 106 q12 11 24 0" stroke="#9d5f44" stroke-width="3.2" fill="none" stroke-linecap="round"/>
<path d="M90 107 q10 7 20 0 -10 3 -20 0z" fill="#fffdf7"/>
<g class="zbx-wave">
<path d="M69 168 q-22 8 -30 -12 l-9-26 19-7 10 25 z" fill="url(#zg-suit)"/>
<path d="M49 130 l19-7 4 11 -19 7 z" fill="#fbfaf6"/>
<circle cx="43" cy="116" r="13" fill="#e0a97e"/>
<path d="M36 108 q3-9 7-2 m5-2 q4-9 7 0 m4 2 q5-7 7 2" stroke="#e0a97e" stroke-width="6" fill="none" stroke-linecap="round"/>
</g></symbol>
</defs></svg>`;

  /* ---------------------------------------------------------------- HTML */
  var HTML = `
<div class="zbx-stage">
  <div class="zbx-smoke" id="zbx-smoke" aria-hidden="true"></div>
  <button class="zbx-seal" id="zbx-seal" aria-label="Open the chat and meet Zach">
    <svg viewBox="0 0 120 120" aria-hidden="true">
      <circle cx="60" cy="60" r="58" fill="url(#zg-sealglow)"/>
      <g class="zbx-breathe">
        <g class="zbx-crack-l"><path d="M60 8 a52 52 0 0 0 0 104 z" fill="url(#zg-brass)"/><path d="M60 18 a42 42 0 0 0 0 84 z" fill="#b5842f" opacity=".55"/></g>
        <g class="zbx-crack-r"><path d="M60 8 a52 52 0 0 1 0 104 z" fill="url(#zg-brass)"/><path d="M60 18 a42 42 0 0 1 0 84 z" fill="#b5842f" opacity=".55"/></g>
        <circle cx="60" cy="60" r="41" fill="none" stroke="#8d6420" stroke-width="1.6" opacity=".6"/>
        <text x="60" y="70" text-anchor="middle" font-family="Fraunces,Georgia,serif" font-weight="700" font-size="30" fill="#2b1f08">.com</text>
        <circle cx="60" cy="22" r="2.4" fill="#3a2a0c"/><circle cx="98" cy="60" r="2.4" fill="#3a2a0c"/>
        <circle cx="60" cy="98" r="2.4" fill="#3a2a0c"/><circle cx="22" cy="60" r="2.4" fill="#3a2a0c"/>
        <clipPath id="zbx-clip"><circle cx="60" cy="60" r="52"/></clipPath>
        <g clip-path="url(#zbx-clip)"><rect class="zbx-shine" x="34" y="-14" width="16" height="150" fill="#fffdf7" opacity=".22" transform="rotate(18 60 60)"/></g>
      </g>
    </svg>
  </button>
  <div class="zbx-guy" id="zbx-guy">
    <button class="zbx-guy-btn" id="zbx-guy-btn" aria-label="Open the chat with Zach"></button>
    <svg aria-hidden="true"><use href="#zbx-zach"/></svg>
  </div>
  <div class="zbx-pill">Tap the seal</div>
  <div class="zbx-balloon" id="zbx-balloon" role="status">
    <button class="zbx-bal-x" id="zbx-bal-x" aria-label="Dismiss">&times;</button>
    <p class="zbx-bal-name">Hi, I'm Zach.</p>
    <p>I'm here to help you get the best deal on a highly valuable semantic domain name. Which one caught your eye?</p>
  </div>
</div>
<div class="zbx-panel" id="zbx-panel" role="dialog" aria-label="Chat with Zach">
  <div class="zbx-head">
    <div class="zbx-head-av"><svg viewBox="34 40 132 110" aria-hidden="true"><use href="#zbx-zach"/></svg></div>
    <div class="zbx-head-txt">
      <div class="zbx-head-n">Zach</div>
      <div class="zbx-head-r">Domain acquisitions &middot; Eye To Ad Media</div>
    </div>
    <button class="zbx-head-x" id="zbx-close" aria-label="Close chat">&times;</button>
  </div>
  <div class="zbx-log" id="zbx-log"></div>
  <div class="zbx-chips" id="zbx-chips"></div>
  <div class="zbx-bar">
    <input class="zbx-in" id="zbx-in" type="text" placeholder="Ask me about a domain..." autocomplete="off">
    <button class="zbx-send" id="zbx-send" aria-label="Send">&rarr;</button>
  </div>
</div>`;

  /* ---------------------------------------------------------------- mount */
  function mount(){
    var st = document.createElement("style"); st.textContent = css;
    document.head.appendChild(st);
    var host = document.createElement("div");
    host.id = "zbx";
    host.innerHTML = ART + HTML;
    document.body.appendChild(host);
    wire(host);
  }

  function wire(root){
    var seal  = root.querySelector("#zbx-seal");
    var guyB  = root.querySelector("#zbx-guy-btn");
    var smoke = root.querySelector("#zbx-smoke");
    var bal   = root.querySelector("#zbx-balloon");
    var balX  = root.querySelector("#zbx-bal-x");
    var log   = root.querySelector("#zbx-log");
    var chips = root.querySelector("#zbx-chips");
    var inp   = root.querySelector("#zbx-in");
    var send  = root.querySelector("#zbx-send");
    var close = root.querySelector("#zbx-close");
    var arrived = false, started = false;

    function buildSmoke(){
      smoke.innerHTML = "";
      var i,d,s,a,r;
      for(i=0;i<11;i++){
        d=document.createElement("div"); d.className="zbx-puff";
        s=34+Math.random()*56; a=Math.random()*Math.PI*2; r=14+Math.random()*34;
        d.style.width=s+"px"; d.style.height=s+"px";
        d.style.left=(46+Math.cos(a)*r)+"px"; d.style.top=(78+Math.sin(a)*r*.55)+"px";
        d.style.setProperty("--dx",(Math.cos(a)*32|0)+"px");
        d.style.setProperty("--dy",(-26-Math.random()*40|0)+"px");
        d.style.animationDelay=(Math.random()*.34).toFixed(2)+"s";
        smoke.appendChild(d);
      }
      for(i=0;i<8;i++){
        d=document.createElement("div"); d.className="zbx-mote";
        d.style.left=(56+(Math.random()*54-27))+"px"; d.style.top=(96+(Math.random()*22-11))+"px";
        d.style.setProperty("--mx",((Math.random()*70-35)|0)+"px");
        d.style.setProperty("--my",(-60-Math.random()*60|0)+"px");
        d.style.animationDelay=(.1+Math.random()*.5).toFixed(2)+"s";
        smoke.appendChild(d);
      }
    }

    function arrive(openAfter){
      if(root.classList.contains("is-bursting")) return;
      buildSmoke();
      root.classList.add("is-bursting");
      setTimeout(function(){
        root.classList.add("is-live");
        arrived = true;
        if(openAfter) setTimeout(open, 1400);
      }, 620);
    }

    function open(){
      if(!arrived){ arrive(true); return; }
      root.classList.add("is-open");
      if(!started){ started = true; boot(); }
      setTimeout(function(){ inp.focus(); }, 300);
    }

    seal.addEventListener("click", function(){ arrive(true); });
    guyB.addEventListener("click", open);
    bal.addEventListener("click", open);
    balX.addEventListener("click", function(e){ e.stopPropagation(); bal.style.opacity="0"; bal.style.pointerEvents="none"; });
    close.addEventListener("click", function(){ root.classList.remove("is-open"); });
    document.addEventListener("keydown", function(e){
      if(e.key==="Escape" && root.classList.contains("is-open")) root.classList.remove("is-open");
    });

    /* proactive: seal sits quietly, Zach arrives once the visitor has read some page */
    var fired = false;
    function maybe(){
      if(fired || arrived) return;
      if(window.scrollY > window.innerHeight * 0.45){ fired = true; arrive(false); }
    }
    window.addEventListener("scroll", maybe, {passive:true});
    setTimeout(function(){ if(!fired && !arrived){ fired = true; arrive(false); } }, 26000);

    /* ------------------------------------------------------------- chat */
    function esc(s){ return String(s).replace(/[&<>"]/g,function(c){
      return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]; }); }

    function say(html, who){
      var d = document.createElement("div");
      d.className = "zbx-msg " + (who==="me" ? "zbx-me" : "zbx-bot");
      d.innerHTML = html;
      log.appendChild(d); log.scrollTop = log.scrollHeight;
    }

    function botSay(html, delay){
      var t = document.createElement("div");
      t.className = "zbx-msg zbx-bot zbx-typing";
      t.innerHTML = "<span></span><span></span><span></span>";
      log.appendChild(t); log.scrollTop = log.scrollHeight;
      setTimeout(function(){ t.remove(); say(html,"bot"); }, delay || 700);
    }

    function callBlock(){ return '<a class="zbx-tel" href="'+TELH+'">Call '+TEL+'</a>'; }

    function setChips(list){
      chips.innerHTML = "";
      list.forEach(function(c){
        var b=document.createElement("button"); b.className="zbx-chip"; b.type="button"; b.textContent=c;
        b.addEventListener("click", function(){ handle(c,true); });
        chips.appendChild(b);
      });
    }

    function boot(){
      say("Good to meet you. I'm Zach &mdash; I own this portfolio personally, so you're talking to the decision maker, not a broker passing messages.","bot");
      botSay("Before I point you anywhere: what line of work are you in? That tells me which of these is actually worth your money.",900);
      setChips(["Is this domain for sale?","How much?","Can I lease it?","What could I do with it?","I'm a contractor"]);
    }

    var USES = {
      "bestfencedenver.com":"a fence contractor in the Denver metro",
      "denvercopainting.com":"a residential painting company",
      "walkintubdenver.com":"a walk-in tub dealer or accessibility remodeler",
      "bestcarpetcleaningdenver.com":"a carpet cleaning operation",
      "restaurantsseo.com":"an agency selling marketing to restaurants",
      "besthotelshawaii.com":"a Hawaii hotel booking or affiliate site",
      "buyrealestatecolorado.com":"a Colorado real estate brokerage",
      "greeleycolawyer.com":"a law firm in Weld County",
      "omahaseopros.com":"a Nebraska marketing agency",
      "mobilemechaniccolorado.com":"a mobile mechanic service",
      "silentdiscoforrent.com":"an event rental company",
      "probioticsfordog.com":"a pet supplement brand",
      "bathremodelingdenver.com":"a bath remodeling contractor",
      "kauaipropertyforsale.com":"a Kauai real estate agent",
      "eyetoad.com":"an established marketing agency",
      "searchconverts.com":"a full-service agency brand",
      "agingsafelybaths.com":"an accessibility bath company"
    };
    var AGED = {"eyetoad.com":1,"agingsafelybaths.com":1};

    function findDomain(t){
      var m = t.match(/[a-z0-9][a-z0-9\-]*\.(com|io|ai|one|homes)/i);
      return m ? m[0].toLowerCase() : null;
    }

    function reply(t){
      var q = t.toLowerCase(), dom = findDomain(q);

      if(/how much|price|pricing|cost|what.*worth|asking|ballpark|budget|\$/.test(q))
        return "I don't publish prices, and that's deliberate &mdash; what a name is worth depends on what you'd do with it, and a number on a page only ever costs one of us money.<br><br>Give me two minutes on the phone and I'll quote you straight."+callBlock();

      if(/lease|rent|financ|payment plan|installment|monthly/.test(q))
        return "Lease options might be available depending on the name &mdash; I look at those case by case rather than promising terms up front.<br><br>Worth asking about on the call."+callBlock();

      if(/for sale|available|can i buy|is it taken|do you own|still have/.test(q)){
        if(dom) return "<strong>"+esc(dom)+"</strong> is for sale, and the price is negotiable. Every name in this portfolio is &mdash; there are no untouchables here, including the ones I use myself."+callBlock();
        return "Everything listed on this site is for sale and negotiable. All 579 of them, including eyetoad.com and searchconverts.com.<br><br>Which name are you looking at?";
      }

      if(/how old|age|aged|registered|since when|when.*regist/.test(q)){
        if(dom && AGED[dom]) return "<strong>"+esc(dom)+"</strong> has been registered and in continuous use since 2012. That history is real and it's part of what you'd be buying.";
        return "Only two names here carry an age story worth telling: eyetoad.com and agingsafelybaths.com, both held since 2012. For the rest I'd rather talk about what the name does for you than how long it's sat in an account.";
      }

      if(/what.*(use|do with|good for)|who.*buy|use case|idea/.test(q)){
        if(dom && USES[dom]) return "<strong>"+esc(dom)+"</strong> is built for "+USES[dom]+". Somebody types that phrase because they're ready to hire &mdash; you'd own the phrase, not rent it back from an ad platform every month.";
        return "Tell me the trade and the city and I'll tell you which names in the portfolio point at customers who are already reaching for their wallet.";
      }

      if(/build|develop|website|site|funnel|rank|seo|turnkey|done for you/.test(q))
        return "That's the other half of this. You can take the name and go, or I can build it out &mdash; a sales funnel engineered to rank on Google and get cited by AI engines, or a deep site designed to convert.<br><br>That's what <strong>eyetoad.com</strong> and <strong>searchconverts.com</strong> do. Same conversation, same number."+callBlock();

      if(/not on the list|don't have|don't own|dont own|do you have|different domain|something else|register|not listed/.test(q))
        return "If it's not on my list I don't own it &mdash; but you can search and register almost anything at <a href=\"https://www.buyweburl.com\" target=\"_blank\" rel=\"noopener\">buyweburl.com</a>, which is mine too.<br><br>Tell me what you searched for and I'll tell you honestly whether it's worth having.";

      if(/guarantee|rank first|page one|top of google|will it rank/.test(q))
        return "No, and anyone telling you otherwise is selling you something. Google has said outright that an exact-match name is not a ranking shortcut.<br><br>What the name buys you is clarity &mdash; somebody reads it and knows instantly what you do. The ranking comes from what gets built on top of it.";

      if(/contractor|fence|paint|roof|plumb|hvac|remodel|deck/.test(q))
        return "Good &mdash; trades are where exact-match names still hit hardest, because the search is local and the intent is immediate.<br><br>I've got depth in fences, decks, painting, roofing, bath remodels and walk-in tubs across Denver, Omaha and a dozen metros. What city?";

      if(/restaurant|food|cafe|bar\b/.test(q))
        return "Restaurant names are a cluster I've built out on purpose &mdash; linkrestaurants.com, restaurantsseo.com, restaurantsadvertising.com and the city-level ones.<br><br>Are you running a restaurant, or selling to them?";

      if(/real estate|realtor|broker|property|condo/.test(q))
        return "Real estate is the deepest section here &mdash; Colorado, Hawaii, Belize, Costa Rica and the Dominican Republic, most of them buy-intent phrases rather than browse-intent.<br><br>Which market?";

      if(/negotiate|offer|deal|discount|best you can do|too high/.test(q))
        return "Everything's negotiable, and I'd rather hear your number than guess at it. I've sold names for less than I wanted because the buyer was going to actually use it &mdash; that matters to me more than squeezing the last dollar.<br><br>Make me an offer on the phone."+callBlock();

      if(/who are you|who is this|about you|real person|are you a bot/.test(q))
        return "I'm Zach &mdash; I run Eye To Ad Media out of Denver and this portfolio is mine. This chat is an assistant trained on how I sell and what I own. The phone is me."+callBlock();

      if(/\b(hi|hello|hey|yo|sup|howdy)\b/.test(q) && q.length < 16)
        return "Hey. What brought you here &mdash; a specific name, or are you shopping?";

      if(dom)
        return "<strong>"+esc(dom)+"</strong> is in the portfolio and it's for sale. Tell me what you'd build on it and I'll tell you whether it's the right one for you &mdash; sometimes it isn't, and I'll say so.";

      return "Tell me the business and the city and I'll find you the name that already has the customers built into it. Or if you'd rather skip ahead:"+callBlock();
    }

    function handle(text, fromChip){
      if(!text || !text.trim()) return;
      say(esc(text),"me");
      if(!fromChip) inp.value = "";
      botSay(reply(text), 620 + Math.random()*420);
      setChips(["How much?","Can I lease it?","Will it rank on Google?","Can you build it out?","A name you don't own"]);
    }

    send.addEventListener("click", function(){ handle(inp.value); });
    inp.addEventListener("keydown", function(e){ if(e.key==="Enter") handle(inp.value); });

    window.openZach  = open;
    window.closeZach = function(){ root.classList.remove("is-open"); };
  }

  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", mount);
  else mount();
})();
