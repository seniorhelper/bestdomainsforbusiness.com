/* Zach — domain assistant for bestdomainsforbusiness.com
   v2: X dismisses to a side tab and stays dismissed across pages.
   Single universal file — never inline this on a page. */
(function(){
var ART = "\n<svg width=\"0\" height=\"0\" style=\"position:absolute\" aria-hidden=\"true\"><defs>\n<linearGradient id=\"zg-hair\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\"><stop offset=\"0\" stop-color=\"#f2d488\"/><stop offset=\"1\" stop-color=\"#c69433\"/></linearGradient>\n<linearGradient id=\"zg-suit\" x1=\"0\" y1=\"0\" x2=\"0\" y2=\"1\"><stop offset=\"0\" stop-color=\"#2c3f61\"/><stop offset=\"1\" stop-color=\"#18253d\"/></linearGradient>\n<linearGradient id=\"zg-brass\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\"><stop offset=\"0\" stop-color=\"#efcd85\"/><stop offset=\".5\" stop-color=\"#c8963e\"/><stop offset=\"1\" stop-color=\"#9a6d22\"/></linearGradient>\n<radialGradient id=\"zg-sealglow\" cx=\"50%\" cy=\"50%\" r=\"50%\"><stop offset=\"55%\" stop-color=\"rgba(200,150,62,.42)\"/><stop offset=\"100%\" stop-color=\"rgba(200,150,62,0)\"/></radialGradient>\n<symbol id=\"zbx-zach\" viewBox=\"0 0 200 260\">\n<path d=\"M131 168 q22 10 25 36 l4 42 -20 4 -8-44 z\" fill=\"#22334f\"/>\n<path d=\"M100 150 q-32 4 -44 26 -9 17 -11 84 h110 q-2-67 -11-84 -12-22 -44-26 z\" fill=\"url(#zg-suit)\"/>\n<path d=\"M100 148 l-17 9 6 32 11 12 11-12 6-32 z\" fill=\"#fbfaf6\"/>\n<path d=\"M83 157 l17-9 0 14 -12 12 z\" fill=\"#eeece4\"/>\n<path d=\"M117 157 l-17-9 0 14 12 12 z\" fill=\"#eeece4\"/>\n<path d=\"M100 153 l-6 7 6 7 6-7 z\" fill=\"#a9761f\"/>\n<path d=\"M100 167 l-6 6 4 34 2 6 2-6 4-34 z\" fill=\"url(#zg-brass)\"/>\n<path d=\"M83 157 q-12 5 -18 16 l22 56 8-44 z\" fill=\"#32486d\"/>\n<path d=\"M117 157 q12 5 18 16 l-22 56 -8-44 z\" fill=\"#32486d\"/>\n<path d=\"M128 196 l14 4 -3 8 -13-5 z\" fill=\"#f3ede0\"/>\n<path d=\"M88 122 h24 v24 q-12 9 -24 0 z\" fill=\"#e0a97e\"/>\n<path d=\"M88 122 h24 v10 q-12 7 -24 0 z\" fill=\"#c9906a\"/>\n<ellipse cx=\"63\" cy=\"90\" rx=\"6.5\" ry=\"9\" fill=\"#e0a97e\"/>\n<ellipse cx=\"137\" cy=\"90\" rx=\"6.5\" ry=\"9\" fill=\"#e0a97e\"/>\n<ellipse cx=\"100\" cy=\"84\" rx=\"38\" ry=\"43\" fill=\"#edba8e\"/>\n<path d=\"M100 38 q-40 0 -40 36 0 8 2 14 3-22 12-27 2 9 8 12 -2-12 3-18 14 12 38 9 12-2 16-8 4 8 3 32 5-6 5-16 0-34 -47-34 z\" fill=\"url(#zg-hair)\"/>\n<path d=\"M118 48 q16 6 20 22 -10-14 -26-16 z\" fill=\"#e6c470\" opacity=\".7\"/>\n<path d=\"M78 74 q9-5 18-1\" stroke=\"#b98a33\" stroke-width=\"3.4\" fill=\"none\" stroke-linecap=\"round\"/>\n<path d=\"M104 73 q9-4 18 1\" stroke=\"#b98a33\" stroke-width=\"3.4\" fill=\"none\" stroke-linecap=\"round\"/>\n<ellipse cx=\"86\" cy=\"86\" rx=\"5\" ry=\"5.6\" fill=\"#fffdf7\"/>\n<ellipse cx=\"114\" cy=\"86\" rx=\"5\" ry=\"5.6\" fill=\"#fffdf7\"/>\n<circle cx=\"87\" cy=\"87\" r=\"2.9\" fill=\"#2b4468\"/><circle cx=\"115\" cy=\"87\" r=\"2.9\" fill=\"#2b4468\"/>\n<circle cx=\"88.2\" cy=\"85.6\" r=\"1\" fill=\"#fff\"/><circle cx=\"116.2\" cy=\"85.6\" r=\"1\" fill=\"#fff\"/>\n<path d=\"M100 90 q4 8 -2 11\" stroke=\"#cf9468\" stroke-width=\"2.6\" fill=\"none\" stroke-linecap=\"round\"/>\n<path d=\"M88 106 q12 11 24 0\" stroke=\"#9d5f44\" stroke-width=\"3.2\" fill=\"none\" stroke-linecap=\"round\"/>\n<path d=\"M90 107 q10 7 20 0 -10 3 -20 0z\" fill=\"#fffdf7\"/>\n<g class=\"zbx-wave\">\n<path d=\"M69 168 q-22 8 -30 -12 l-9-26 19-7 10 25 z\" fill=\"url(#zg-suit)\"/>\n<path d=\"M49 130 l19-7 4 11 -19 7 z\" fill=\"#fbfaf6\"/>\n<circle cx=\"43\" cy=\"116\" r=\"13\" fill=\"#e0a97e\"/>\n<path d=\"M36 108 q3-9 7-2 m5-2 q4-9 7 0 m4 2 q5-7 7 2\" stroke=\"#e0a97e\" stroke-width=\"6\" fill=\"none\" stroke-linecap=\"round\"/>\n</g></symbol>\n</defs></svg>";
var HTML = "\n<div class=\"zbx-stage\" id=\"zbx-stage\">\n  <div class=\"zbx-smoke\" id=\"zbx-smoke\" aria-hidden=\"true\"></div>\n  <button class=\"zbx-seal\" id=\"zbx-seal\" aria-label=\"Open the chat and meet Zach\">\n    <svg viewBox=\"0 0 120 120\" aria-hidden=\"true\">\n      <circle cx=\"60\" cy=\"60\" r=\"58\" fill=\"url(#zg-sealglow)\"/>\n      <g class=\"zbx-breathe\">\n        <g class=\"zbx-crack-l\"><path d=\"M60 8 a52 52 0 0 0 0 104 z\" fill=\"url(#zg-brass)\"/><path d=\"M60 18 a42 42 0 0 0 0 84 z\" fill=\"#b5842f\" opacity=\".55\"/></g>\n        <g class=\"zbx-crack-r\"><path d=\"M60 8 a52 52 0 0 1 0 104 z\" fill=\"url(#zg-brass)\"/><path d=\"M60 18 a42 42 0 0 1 0 84 z\" fill=\"#b5842f\" opacity=\".55\"/></g>\n        <circle cx=\"60\" cy=\"60\" r=\"41\" fill=\"none\" stroke=\"#8d6420\" stroke-width=\"1.6\" opacity=\".6\"/>\n        <text x=\"60\" y=\"70\" text-anchor=\"middle\" font-family=\"Fraunces,Georgia,serif\" font-weight=\"700\" font-size=\"30\" fill=\"#2b1f08\">.com</text>\n        <circle cx=\"60\" cy=\"22\" r=\"2.4\" fill=\"#3a2a0c\"/><circle cx=\"98\" cy=\"60\" r=\"2.4\" fill=\"#3a2a0c\"/>\n        <circle cx=\"60\" cy=\"98\" r=\"2.4\" fill=\"#3a2a0c\"/><circle cx=\"22\" cy=\"60\" r=\"2.4\" fill=\"#3a2a0c\"/>\n        <clipPath id=\"zbx-clip\"><circle cx=\"60\" cy=\"60\" r=\"52\"/></clipPath>\n        <g clip-path=\"url(#zbx-clip)\"><rect class=\"zbx-shine\" x=\"34\" y=\"-14\" width=\"16\" height=\"150\" fill=\"#fffdf7\" opacity=\".22\" transform=\"rotate(18 60 60)\"/></g>\n      </g>\n    </svg>\n  </button>\n  <div class=\"zbx-guy\">\n    <button class=\"zbx-guy-btn\" id=\"zbx-guy-btn\" aria-label=\"Chat with Zach\">\n      <svg viewBox=\"34 26 132 152\" aria-hidden=\"true\"><use href=\"#zbx-zach\"/></svg>\n    </button>\n    <div class=\"zbx-balloon\" id=\"zbx-balloon\" role=\"button\" tabindex=\"0\">\n      <button class=\"zbx-bal-x\" id=\"zbx-bal-x\" aria-label=\"Dismiss the assistant\">&times;</button>\n      <strong>Need help finding the perfect domain?</strong>\n      <span id=\"zbx-bal-txt\">Ask me about any name here.</span>\n    </div>\n    <button class=\"zbx-kill\" id=\"zbx-kill\" aria-label=\"Dismiss the assistant\" title=\"Dismiss\">&times;</button>\n  </div>\n  <div class=\"zbx-panel\" id=\"zbx-panel\" role=\"dialog\" aria-label=\"Chat with Zach\">\n    <div class=\"zbx-head\">\n      <div class=\"zbx-head-av\"><svg viewBox=\"34 40 132 110\" aria-hidden=\"true\"><use href=\"#zbx-zach\"/></svg></div>\n      <div class=\"zbx-head-txt\">\n        <div class=\"zbx-head-n\">Zach</div>\n        <div class=\"zbx-head-r\">Domain acquisitions &middot; Eye To Ad Media</div>\n      </div>\n      <button class=\"zbx-head-min\" id=\"zbx-min\" aria-label=\"Minimize chat\" title=\"Minimize\">&#8211;</button>\n      <button class=\"zbx-head-x\" id=\"zbx-close\" aria-label=\"Dismiss the assistant for good\" title=\"Dismiss\">&times;</button>\n    </div>\n    <div class=\"zbx-log\" id=\"zbx-log\"></div>\n    <div class=\"zbx-chips\" id=\"zbx-chips\"></div>\n    <div class=\"zbx-bar\">\n      <input class=\"zbx-in\" id=\"zbx-in\" aria-label=\"Ask Zach about a domain\" type=\"text\" placeholder=\"Ask me about a domain...\" autocomplete=\"off\">\n      <button class=\"zbx-send\" id=\"zbx-send\" aria-label=\"Send\">&rarr;</button>\n    </div>\n  </div>\n</div>\n<button class=\"zbx-tab\" id=\"zbx-tab\" aria-label=\"Open the domain assistant\"><span class=\"tdot\" aria-hidden=\"true\"></span>Need a domain?</button>\n<div class=\"zbx-hint\" id=\"zbx-hint\" aria-hidden=\"true\">Need help finding the perfect domain?</div>\n";
var CSS = "\n#zbx{position:fixed;right:20px;bottom:20px;z-index:9999;font-family:ui-sans-serif,system-ui,-apple-system,\"Segoe UI\",Roboto,Helvetica,Arial,sans-serif}\n@media(max-width:520px){#zbx{right:14px;bottom:14px}}\n#zbx .zbx-stage{position:relative;width:124px;height:150px;margin-left:auto}\n@media(max-width:520px){#zbx .zbx-stage{width:112px;height:138px}}\n#zbx .zbx-seal{position:absolute;right:8px;bottom:34px;width:96px;height:96px;padding:0;border:0;background:transparent;cursor:pointer;display:block}\n#zbx .zbx-seal:focus-visible{outline:2px solid #e8c37a;outline-offset:6px;border-radius:50%}\n#zbx .zbx-seal svg{display:block;width:100%;height:100%;overflow:visible}\n#zbx .zbx-shine{animation:zbx-sweep 5.2s ease-in-out infinite;transform-origin:center}\n@keyframes zbx-sweep{0%,100%{opacity:.12;transform:translateX(-26px)}50%{opacity:.4;transform:translateX(26px)}}\n#zbx .zbx-breathe{animation:zbx-breathe 4.4s ease-in-out infinite;transform-origin:center}\n@keyframes zbx-breathe{0%,100%{transform:scale(1)}50%{transform:scale(1.028)}}\n#zbx.is-bursting .zbx-crack-l{animation:zbx-shardL .9s cubic-bezier(.3,.7,.4,1) forwards}\n#zbx.is-bursting .zbx-crack-r{animation:zbx-shardR .9s cubic-bezier(.3,.7,.4,1) forwards}\n@keyframes zbx-shardL{to{transform:translate(-26px,14px) rotate(-24deg);opacity:0}}\n@keyframes zbx-shardR{to{transform:translate(26px,16px) rotate(22deg);opacity:0}}\n#zbx.is-bursting .zbx-seal{pointer-events:none}\n#zbx.is-open .zbx-seal,#zbx.is-live .zbx-seal{opacity:0;pointer-events:none;transition:opacity .5s ease}\n#zbx .zbx-pill{position:absolute;right:0;bottom:0;left:0;text-align:center;background:#1b2b47;color:#e8c37a;border:1px solid rgba(200,150,62,.42);border-radius:999px;padding:6px 10px;font-size:.7rem;line-height:1.25;pointer-events:none;white-space:nowrap}\n#zbx.is-bursting .zbx-pill,#zbx.is-live .zbx-pill,#zbx.is-open .zbx-pill{opacity:0;transition:opacity .35s ease}\n#zbx .zbx-smoke{position:absolute;inset:-70px -60px -30px -60px;pointer-events:none;opacity:0}\n#zbx.is-bursting .zbx-smoke,#zbx.is-live .zbx-smoke{opacity:1}\n#zbx .zbx-puff{position:absolute;border-radius:50%;background:radial-gradient(circle at 38% 34%,rgba(255,253,247,.95),rgba(226,219,201,.6) 44%,rgba(190,182,162,0) 72%);opacity:0;transform:scale(.2)}\n#zbx.is-bursting .zbx-puff{animation:zbx-puff 2.6s cubic-bezier(.18,.7,.3,1) forwards}\n@keyframes zbx-puff{0%{opacity:0;transform:scale(.18) translate(0,0)}16%{opacity:.92}55%{opacity:.6}100%{opacity:0;transform:scale(2.5) translate(var(--dx,0),var(--dy,-34px))}}\n#zbx .zbx-mote{position:absolute;width:5px;height:5px;border-radius:50%;background:#e8c37a;opacity:0}\n#zbx.is-bursting .zbx-mote{animation:zbx-mote 3.1s ease-out forwards}\n@keyframes zbx-mote{0%{opacity:0;transform:translate(0,0) scale(.5)}18%{opacity:.95}100%{opacity:0;transform:translate(var(--mx,0),var(--my,-86px)) scale(.2)}}\n#zbx .zbx-guy{position:absolute;right:-6px;bottom:26px;width:132px;height:150px;opacity:0;pointer-events:none;transform:translateY(22px) scale(.86)}\n@media(max-width:520px){#zbx .zbx-guy{width:118px;height:136px;right:-4px}}\n#zbx.is-live .zbx-guy{animation:zbx-arrive 1.5s cubic-bezier(.2,.8,.3,1) .55s forwards;pointer-events:auto}\n@keyframes zbx-arrive{0%{opacity:0;transform:translateY(22px) scale(.86)}45%{opacity:1}100%{opacity:1;transform:translateY(0) scale(1)}}\n#zbx .zbx-guy svg{display:block;width:100%;height:100%;overflow:visible}\n#zbx .zbx-wave{transform-origin:70px 150px}\n#zbx.is-live .zbx-wave{animation:zbx-wave 3.4s ease-in-out 2.1s infinite}\n@keyframes zbx-wave{0%,72%,100%{transform:rotate(0)}80%{transform:rotate(-13deg)}88%{transform:rotate(4deg)}}\n#zbx .zbx-guy-btn{position:absolute;inset:0;background:transparent;border:0;padding:0;cursor:pointer}\n#zbx .zbx-guy-btn:focus-visible{outline:2px solid #e8c37a;outline-offset:4px;border-radius:10px}\n#zbx .zbx-balloon{position:absolute;right:104px;bottom:56px;width:264px;background:#fffdf7;color:#16202f;border:1px solid rgba(16,26,44,.18);border-radius:14px;padding:14px 16px 15px;font-size:.88rem;line-height:1.5;opacity:0;transform:translateY(8px) scale(.96);transform-origin:right bottom;pointer-events:none}\n#zbx.is-live .zbx-balloon{animation:zbx-bal 1.1s cubic-bezier(.2,.8,.3,1) 1.5s forwards;pointer-events:auto}\n@keyframes zbx-bal{to{opacity:1;transform:translateY(0) scale(1)}}\n#zbx .zbx-balloon:after,#zbx .zbx-balloon:before{content:\"\";position:absolute;right:-11px;bottom:26px;width:0;height:0;border-top:9px solid transparent;border-bottom:9px solid transparent;border-left:11px solid #fffdf7}\n#zbx .zbx-balloon:before{right:-13px;border-left-color:rgba(16,26,44,.18)}\n#zbx .zbx-bal-name{font-family:Fraunces,Georgia,serif;font-weight:700;font-size:.95rem;color:#101a2c;margin:0 0 5px}\n#zbx .zbx-balloon p{margin:0}\n#zbx .zbx-bal-x{position:absolute;top:5px;right:7px;width:24px;height:24px;border:0;background:transparent;cursor:pointer;color:rgba(16,26,44,.4);font-size:1rem;line-height:1;border-radius:50%}\n#zbx .zbx-bal-x:hover{color:#101a2c;background:rgba(16,26,44,.07)}\n@media(max-width:640px){#zbx .zbx-balloon{right:88px;width:min(238px,calc(100vw - 130px));font-size:.84rem}}\n#zbx.is-open .zbx-balloon{opacity:0;pointer-events:none;transition:opacity .3s ease}\n#zbx .zbx-panel{position:fixed;right:20px;bottom:20px;width:376px;max-width:calc(100vw - 28px);height:min(586px,calc(100vh - 40px));background:#fffdf7;border:1px solid rgba(16,26,44,.2);border-radius:16px;overflow:hidden;display:none;flex-direction:column;box-shadow:0 24px 60px rgba(4,10,22,.42)}\n@media(max-width:520px){#zbx .zbx-panel{right:8px;bottom:8px;max-width:calc(100vw - 16px);height:calc(100vh - 24px)}}\n#zbx.is-open .zbx-panel{display:flex;animation:zbx-panel .42s cubic-bezier(.2,.8,.3,1)}\n@keyframes zbx-panel{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}\n#zbx .zbx-head{display:flex;align-items:center;gap:11px;background:#101a2c;color:#f5f0e4;padding:12px 13px;border-bottom:2px solid #c8963e}\n#zbx .zbx-head-av{width:42px;height:42px;border-radius:50%;flex:0 0 42px;background:#1b2b47;overflow:hidden;border:1px solid rgba(200,150,62,.45)}\n#zbx .zbx-head-av svg{display:block;width:100%;height:100%}\n#zbx .zbx-head-txt{flex:1;min-width:0}\n#zbx .zbx-head-n{font-family:Fraunces,Georgia,serif;font-weight:700;font-size:1rem}\n#zbx .zbx-head-r{font-size:.73rem;color:rgba(245,240,228,.6);margin-top:1px}\n#zbx .zbx-head-x{width:30px;height:30px;border:0;background:transparent;cursor:pointer;color:rgba(245,240,228,.6);font-size:1.2rem;line-height:1;border-radius:50%;flex:0 0 30px}\n#zbx .zbx-head-x:hover{color:#fffdf7;background:rgba(245,240,228,.1)}\n#zbx .zbx-log{flex:1;overflow-y:auto;padding:16px 14px 6px;background:#f5f0e4}\n#zbx .zbx-msg{max-width:84%;margin-bottom:11px;font-size:.87rem;line-height:1.55;border-radius:13px;padding:10px 13px}\n#zbx .zbx-bot{background:#fffdf7;color:#16202f;border:1px solid rgba(16,26,44,.12);border-bottom-left-radius:4px}\n#zbx .zbx-me{background:#1b2b47;color:#f5f0e4;margin-left:auto;border-bottom-right-radius:4px}\n#zbx .zbx-msg a{color:#8a5f14;font-weight:600}\n#zbx .zbx-tel{display:inline-block;margin-top:7px;background:#c8963e;color:#16202f;font-weight:650;padding:8px 14px;border-radius:999px;text-decoration:none;font-size:.87rem}\n#zbx .zbx-tel:hover{background:#e8c37a}\n#zbx .zbx-chips{display:flex;flex-wrap:wrap;gap:6px;padding:8px 14px 12px;background:#f5f0e4}\n#zbx .zbx-chip{background:transparent;color:#101a2c;border:1px solid rgba(16,26,44,.26);border-radius:999px;padding:6px 12px;font-size:.78rem;font-family:inherit;cursor:pointer}\n#zbx .zbx-chip:hover{background:rgba(16,26,44,.07)}\n#zbx .zbx-bar{display:flex;gap:8px;padding:10px 12px;background:#fffdf7;border-top:1px solid rgba(16,26,44,.12)}\n#zbx .zbx-in{flex:1;border:1px solid rgba(16,26,44,.22);border-radius:999px;padding:10px 15px;font-size:.87rem;font-family:inherit;background:#fff;color:#16202f}\n#zbx .zbx-in:focus{outline:2px solid #c8963e;outline-offset:-1px}\n#zbx .zbx-send{width:40px;height:40px;flex:0 0 40px;border:0;border-radius:50%;background:#101a2c;color:#e8c37a;cursor:pointer;font-size:1rem}\n#zbx .zbx-send:hover{background:#1b2b47}\n#zbx .zbx-typing span{display:inline-block;width:6px;height:6px;border-radius:50%;background:rgba(16,26,44,.42);margin-right:4px;animation:zbx-dot 2.8s ease-in-out infinite}\n#zbx .zbx-typing span:nth-child(2){animation-delay:.32s}\n#zbx .zbx-typing span:nth-child(3){animation-delay:.64s}\n@keyframes zbx-dot{0%,100%{opacity:.28}50%{opacity:.85}}\n@media(prefers-reduced-motion:reduce){\n#zbx .zbx-shine,#zbx .zbx-breathe,#zbx .zbx-wave,#zbx .zbx-typing span{animation:none!important}\n#zbx.is-bursting .zbx-puff,#zbx.is-bursting .zbx-mote,#zbx.is-bursting .zbx-crack-l,#zbx.is-bursting .zbx-crack-r{animation-duration:.01ms!important}\n#zbx.is-live .zbx-guy,#zbx.is-live .zbx-balloon{animation-duration:.01ms!important;animation-delay:0ms!important;opacity:1}\n#zbx.is-open .zbx-panel{animation:none}}\n\n/* ---- v2: dismiss tab + tidy ---- */\n.zbx-tab{position:fixed;right:0;bottom:120px;z-index:9998;display:none;align-items:center;gap:8px;\n background:#141230;color:#fffcf5;border:0;border-radius:14px 0 0 14px;padding:14px 11px;cursor:pointer;\n font-family:\"Plus Jakarta Sans\",system-ui,sans-serif;font-size:.8rem;font-weight:800;letter-spacing:.04em;\n writing-mode:vertical-rl;text-orientation:mixed;box-shadow:-6px 6px 22px rgba(20,18,48,.26)}\n.zbx-tab:hover{background:#4c35e8}\n.zbx-tab.show{display:flex}\n.zbx-tab .tdot{writing-mode:horizontal-tb;width:8px;height:8px;border-radius:50%;background:#69e08a;flex:none}\n.zbx-hint{position:fixed;right:52px;bottom:118px;z-index:9997;display:none;background:#fffcf5;color:#141230;\n border:1px solid rgba(20,18,48,.14);border-radius:12px;padding:9px 13px;font-family:\"Plus Jakarta Sans\",system-ui,sans-serif;\n font-size:.8rem;font-weight:700;box-shadow:0 10px 26px rgba(20,18,48,.14);max-width:190px;line-height:1.35}\n.zbx-hint.show{display:block}\n#zbx .zbx-balloon{right:138px!important;bottom:74px!important;width:min(228px,calc(100vw - 180px))!important;\n font-size:.85rem!important;padding:12px 30px 13px 14px!important}\n#zbx .zbx-balloon strong{display:block;margin-bottom:3px}\n#zbx .zbx-balloon:after,#zbx .zbx-balloon:before{bottom:18px}\n@media(max-width:520px){#zbx .zbx-balloon{right:104px!important;width:min(190px,calc(100vw - 150px))!important;font-size:.79rem!important}}\n#zbx .zbx-kill{position:absolute;top:0;right:0;z-index:4;width:26px;height:26px;border-radius:50%;\n border:1px solid rgba(20,18,48,.18);background:#fffdf7;color:#5c5872;font-size:1rem;line-height:1;\n cursor:pointer;padding:0;opacity:0;pointer-events:none;transition:opacity .3s ease}\n#zbx.is-live .zbx-kill{opacity:.85;pointer-events:auto}\n#zbx.is-open .zbx-kill{opacity:0;pointer-events:none}\n#zbx .zbx-kill:hover{background:#141230;color:#fffcf5;opacity:1}\n.zbx-head-x{font-size:1.5rem;line-height:1}\n.zbx-head-min{background:none;border:0;color:inherit;font-size:1.05rem;cursor:pointer;opacity:.7;padding:0 4px;line-height:1}\n.zbx-head-min:hover{opacity:1}\n@media(max-width:600px){.zbx-tab{bottom:96px;font-size:.74rem;padding:12px 9px}.zbx-hint{display:none!important}}\n";
window.__ZBX_ART__ = ART; window.__ZBX_HTML__ = HTML; window.__ZBX_CSS__ = CSS;
})();

(function(){
if (window.__ZBX__) return; window.__ZBX__ = 1;

var ART=window.__ZBX_ART__, HTML=window.__ZBX_HTML__, CSS=window.__ZBX_CSS__;
var TEL="1-800-481-8638", TELH="tel:+18004818638";
var KEY_DISMISS="bdfb_zach_dismissed_v2", KEY_MIN="bdfb_zach_min_v2";

function ls(k,v){ try{ if(v===undefined) return localStorage.getItem(k); localStorage.setItem(k,v);}catch(e){return null;} }
function lsdel(k){ try{ localStorage.removeItem(k); }catch(e){} }

var IDX = [["24-7answeringservice.com","prof","PE"],["acreageforsaleincolorado.com","realestate","PGE"],["actionglobalnews.com","events","PDES"],["advertisecastlerock.com","marketing","PDGES"],["advertisingforcontractors.com","marketing","PDE"],["advertisingforrestaurant.com","marketing","PDE"],["affordabledenverseo.com","marketing","PDGES"],["agenciaseoencostarica.com","marketing","PDIGE"],["agenticsseo.com","marketing","DES"],["aiagentdenver.com","ai","PXGES"],["aiagentforadvertising.com","ai","PDE"],["aiagentforseo.com","ai","PES"],["aiagentsadvertising.com","ai","PE"],["aiagentsdenver.com","ai","PXGES"],["aiagentsforaccounting.com","ai","PE"],["ailifeboard.com","ai","DBS"],["aiodenver.com","marketing","PDGES"],["allinclusivemauiresorts.com","travel","PGE"],["allinclusiveresortshawaii.com","travel","PGE"],["allinclusiveresortsoahu.com","travel","PGE"],["allofus.one","events","DBS"],["allofuscoin.com","events","BS"],["anotherdimensionvr.com","vr","PDBS"],["answeringservicesforbusiness.com","prof","PCE"],["apartmentsforsalenearme.com","realestate","PE"],["apoemaboutlove.com","events","PDBS"],["appdevelopmentmobile.com","marketing","PCE"],["appliancedealsonline.com","home","PES"],["appliancesdenver.com","home","PGES"],["attorneygreeleyco.com","legal","PGES"],["attractionhawaii.com","travel","PGES"],["attractionsdenver.com","travel","PGES"],["attractionsoahu.com","travel","PDGES"],["auroradeckbuilder.com","trades","PXGES"],["auroradeckbuilders.com","trades","PXGES"],["autodetailomahane.com","auto","PGES"],["autoglassreplacementdenverco.com","auto","PGE"],["bathforseniors.com","bath","PES"],["bathremodelcontractorsnearme.com","bath","PCE"],["bathremodelingdenver.com","bath","PGE"],["bathrenovationcontractors.com","bath","PE"],["bathroomremodellittletonco.com","bath","PDGE"],["bathroomrenovationdenver.com","bath","PGE"],["bathrooms4less.com","bath","PCE"],["bathtubs4less.com","bath","PCE"],["bedlinersfortrucks.com","auto","PES"],["bedsdenver.com","home","PGES"],["belize-seo.com","marketing","PGE"],["belizeadvertising.com","marketing","PDGES"],["belizecondosforrent.com","realestate","PDGES"],["belizefishingcharter.com","travel","PDGE"],["belizeislandexpeditions.com","travel","PGE"],["belizemonthlyrentals.com","travel","PDGE"],["belizerestaurantsguide.com","food","PDGE"],["belizeseoagency.com","marketing","PDGES"],["belizetourspackages.com","travel","PGES"],["bestaiagentforbusiness.com","ai","PCE"],["bestansweringservices.com","prof","PCE"],["bestappdesigners.com","marketing","PCES"],["bestbeacheshawaii.com","travel","PDGES"],["bestbeachesincostarica.com","travel","PDGE"],["bestbelizeadventures.com","travel","PDGE"],["bestbrandranker.com","marketing","BS"],["bestcarpetcleaningcompanydenver.com","cleanmove","PGE"],["bestcarpetcleaningdenver.com","cleanmove","PGE"],["bestcoloradoinsurances.com","insurance","PGE"],["bestcoloradomassage.com","health","PGES"],["bestcoloradomovers.com","cleanmove","PGES"],["bestcpacolorado.com","prof","PGES"],["bestdentistdenverco.com","health","PGES"],["bestdenveraccountant.com","prof","PGE"],["bestdenverhotel.com","travel","PGES"],["bestdenvermassages.com","health","PGES"],["bestdenvermover.com","cleanmove","PGES"],["bestdenvermovingcompany.com","cleanmove","PGE"],["bestdivinghawaii.com","travel","PDGES"],["bestdivinginhawaii.com","travel","PGES"],["bestdivinginmaui.com","travel","PGES"],["bestdivinginoahu.com","travel","PDGES"],["bestdoghampoo.com","pets","ES"],["bestdomainsforbusiness.com","marketing","PDCE"],["bestfencecolorado.com","trades","PGES"],["bestfencecompanycolorado.com","trades","PGE"],["bestfencecompanydenver.com","trades","PGE"],["bestfencecompanyinomaha.com","trades","PGE"],["bestfencedenver.com","trades","PGES"],["bestfenceomaha.com","trades","PGES"],["bestglp-1forweightloss.com","health","PE"],["besthawaiisnorkeling.com","travel","PGE"],["besthawaiivacationrental.com","travel","PGE"],["besthotelinhawaii.com","travel","PGES"],["besthotelsbelize.com","travel","PDGES"],["besthotelscostarica.com","travel","PDGES"],["besthotelshawaii.com","travel","PDGES"],["besthotelsincolorado.com","travel","PGE"],["bestluxuryyachtsforsale.com","auto","PE"],["bestmassagehonolulu.com","health","PGES"],["bestmobileappdesigner.com","marketing","PCE"],["bestmoversdenver.com","cleanmove","PGES"],["bestoahumassages.com","health","PGES"],["bestpaintersindenver.com","trades","PGE"],["bestpizzainhawaii.com","food","PGES"],["bestplacestodiveinbelize.com","travel","PDGE"],["bestplacestostayhawaii.com","travel","PGE"],["bestplacestostayinkauai.com","travel","PGE"],["bestplacestostayinoahu.com","travel","PGE"],["bestplacestostaymaui.com","travel","PGE"],["bestprobioticforcats.com","pets","PE"],["bestrestaurantcolorado.com","food","PDGE"],["bestrestaurantdenver.com","food","PDGE"],["bestrestaurantsbelize.com","food","PDGE"],["bestrestaurantsinoahu.com","food","PGE"],["bestroofersdenverco.com","trades","PGES"],["bestscubadivinginhawaii.com","travel","PGE"],["bestscubadivinginkauai.com","travel","PGE"],["bestscubadivinginmaui.com","travel","PGE"],["bestscubadivingoahu.com","travel","PGES"],["bestscubahawaii.com","travel","PGES"],["bestseocompanyamerica.com","marketing","PCGE"],["bestseocompanydenverco.com","marketing","PDGE"],["bestshowerkit.com","bath","PDES"],["bestsilentdisco.com","events","PBS"],["bestsnorkelingbelize.com","travel","PDGE"],["besttacotruckdenver.com","food","PGES"],["bestthingstodoinoahu.com","travel","PGE"],["bestusaseo.com","marketing","PCGES"],["bestvacationrentalsoahu.com","travel","PGE"],["bestvrstores.com","vr","PES"],["bestvrworlds.com","vr","PBS"],["bestwebsitecoder.com","marketing","PCES"],["bigislandseo.com","marketing","PDGES"],["bogotaseo.com","marketing","PGES"],["bookhotelandflights.com","travel","PDES"],["bookvacationpackage.com","travel","PES"],["bostonwalkintub.com","bath","PGES"],["botoxlongmont.com","health","PDGES"],["bouldercobotox.com","health","PGES"],["bouldercoloradorealestateprices.com","realestate","PGE"],["bouldercopainters.com","trades","PDGES"],["bouldercoseo.com","marketing","PDGES"],["boulderpropertiesforsale.com","realestate","PGE"],["brandedcustompens.com","promo","PES"],["brandedgolfshirts.com","promo","PES"],["brandedsweatshirts.com","promo","PES"],["brandsincolorado.com","events","PGES"],["brightonbeautysalon.com","health","PGES"],["brightonbotox.com","health","PGES"],["brightoncarinsurance.com","insurance","PGE"],["brightoncodentist.com","health","PGES"],["brightoncohairsalon.com","health","PDGES"],["brightoncoorthodontics.com","health","PGE"],["brightondayspa.com","health","PGES"],["brightonfacials.com","health","PGES"],["brightonhaircut.com","health","PDGES"],["brightonlashes.com","health","PGES"],["brightonorthodontist.com","health","PDGE"],["brightontanning.com","health","PGES"],["brightontire.com","auto","PXGES"],["brightontirerepair.com","auto","PGES"],["brightontires.com","auto","PXGES"],["brightontireshop.com","auto","PGES"],["brightonwaxing.com","health","PGES"],["businesscardtap.com","marketing","PBS"],["businessdirectorynow.com","marketing","PCE"],["businessdomainforsale.com","marketing","PCE"],["buyappliancesnearme.com","home","PES"],["buyboatnearme.com","auto","PES"],["buybrandedmerchandise.com","promo","PCE"],["buybrandedshirts.com","promo","PES"],["buycondobelize.com","realestate","PGES"],["buycondocaberete.com","realestate","PGES"],["buycondocostarica.com","realestate","PGES"],["buycondohawaii.com","realestate","PGES"],["buycondopuertoplata.com","realestate","PGES"],["buycondososua.com","realestate","PGES"],["buyhousecostarica.com","realestate","PDGES"],["buyhousehawaii.com","realestate","PGES"],["buyhousekauai.com","realestate","PGES"],["buypropertybelize.com","realestate","PGES"],["buypropertycabarete.com","realestate","PGES"],["buypropertypuertoplata.com","realestate","PGE"],["buypropertysosua.com","realestate","PGES"],["buyrealestatecaberete.com","realestate","PGE"],["buyrealestatecolorado.com","realestate","PGE"],["buyrealestateinbelize.com","realestate","PGE"],["buyrealestatepuertoplata.com","realestate","PGE"],["buyrealestatesosua.com","realestate","PGES"],["buysmarttoilet.com","bath","PES"],["buywasheranddryer.com","home","PCES"],["buyweburl.com","marketing","PDBS"],["cabaretebeachdominicanrepublic.com","travel","PDGE"],["cabaretecondosforsale.com","realestate","PDGE"],["cabareterealty.com","realestate","PGES"],["cabareterestaurants.com","food","PDGES"],["cabusinesslist.com","marketing","PGES"],["calmingdogsupplements.com","pets","PE"],["campersforsaledenver.com","auto","PGE"],["carinsurancedenverco.com","insurance","PGE"],["carinsurancelovelandco.com","insurance","PGE"],["carpetcleanerinomaha.com","cleanmove","PDXGE"],["carpetcleanerinomahane.com","cleanmove","PXGE"],["carpetcleaningdenvercolorado.com","cleanmove","PGE"],["carpetshampoodenver.com","cleanmove","PGES"],["carsforsalelongmont.com","auto","PGES"],["carwindshieldreplacementdenver.com","auto","PGE"],["castlerock-seo.com","marketing","PDGE"],["cateardrop.com","pets","PBS"],["cateringcompanycolorado.com","food","PGE"],["cateringcompanydenver.com","food","PGE"],["cateringdenverco.com","food","PGES"],["catsupplementsonline.com","pets","PCE"],["centennialdeck.com","trades","PGES"],["cheapflightshotel.com","travel","PES"],["cheapmobilemechanicnearme.com","auto","PE"],["cheaptiresdenver.com","auto","PGES"],["cheapvacationrentalshawaii.com","travel","PGE"],["cobusinesslist.com","marketing","PDGES"],["colombia-seo.com","marketing","PGE"],["coloradobuyhouse.com","realestate","PGES"],["coloradocampingspots.com","travel","PDGE"],["coloradocustomdeck.com","trades","PGES"],["coloradofences.com","trades","PGES"],["coloradoglp-1.com","health","PXGE"],["coloradoglp1.com","health","PXGE"],["coloradomovingco.com","cleanmove","PGES"],["coloradospringsdeck.com","trades","PGES"],["coloradowhatsup.com","travel","DBS"],["coloradowhattodo.com","travel","DGES"],["comicscomealive.com","events","DBS"],["comicsonlinefree.com","events","ES"],["condoforsaledenver.com","realestate","PGES"],["condosforsaleboulderco.com","realestate","PGE"],["conversationalaibot.com","ai","PDCES"],["costarica-seo.com","marketing","PDGE"],["costaricaattraction.com","travel","PGES"],["costaricaentertainment.com","travel","PGE"],["crotchrocketsforsale.com","auto","PE"],["customizepromotionalproducts.com","promo","PDCE"],["customnfcbusinesscards.com","marketing","PE"],["custompenwithlogo.com","promo","PES"],["customtentwithlogos.com","promo","PES"],["daconocorealestate.com","realestate","PGES"],["daconohomesforsale.com","realestate","PGES"],["dealscolorado.com","prof","GES"],["deckcolorado.com","trades","PGES"],["deckcontractordenver.com","trades","PGE"],["decksaurora.com","trades","PGES"],["deckscoloradosprings.com","trades","PGE"],["deepseafishingbelize.com","travel","PGE"],["dentistbrightonco.com","health","PGES"],["denver-seo.ai","marketing","PXGE"],["denver-webdesign.com","marketing","PDGE"],["denverappdevelopment.com","marketing","PGE"],["denverappliancestore.com","home","PGE"],["denverartmap.com","events","GES"],["denvercampers.com","auto","PGES"],["denvercateringtrucks.com","food","PGE"],["denvercoappliancerepair.com","home","PGE"],["denvercoautoglass.com","auto","PGES"],["denvercobathroomremodel.com","bath","PGE"],["denvercobotox.com","health","PGES"],["denvercodentist.com","health","PGES"],["denvercodivorcemediators.com","legal","PGE"],["denvercofence.com","trades","PGES"],["denvercofurnacerepair.com","trades","PGE"],["denvercofurniture.com","home","PGES"],["denvercohouseforsale.com","realestate","PGE"],["denvercojunkremoval.com","trades","PGES"],["denvercolandscaping.com","trades","PGES"],["denvercoloradothingstodo.com","travel","PDGE"],["denvercomediator.com","legal","PXGES"],["denvercomediators.com","legal","PXGES"],["denvercomover.com","cleanmove","PXGES"],["denvercomovers.com","cleanmove","PXGES"],["denvercoorthodontics.com","health","PGE"],["denvercopainting.com","trades","PDGES"],["denvercorv.com","auto","PGES"],["denvercoseoagency.com","marketing","PGES"],["denvercospa.com","health","PGES"],["denvercotires.com","auto","PGES"],["denvercowindshieldreplacement.com","auto","PGE"],["denverglp-1.com","health","PGE"],["denvermattresssale.com","home","PGES"],["denvermattressstore.com","home","PGES"],["denverpaintcontractors.com","trades","PDGE"],["denverpavingcompanies.com","trades","PGE"],["denverprintsolutions.com","promo","PGE"],["denversearchenginemarketing.com","marketing","PGE"],["denversearchengineoptimization.com","marketing","PGE"],["denverseo.io","marketing","PDXGES"],["denverseoblog.com","marketing","PGES"],["denvertopseocompany.com","marketing","PGES"],["denverwalkintub.com","bath","PGES"],["discountappliancesdenver.com","home","PGE"],["distributepressreleases.com","marketing","PDE"],["divorceattorneygreeley.com","legal","PGE"],["divorcelawyersgreeley.com","legal","PGE"],["divorcemediatorsdenver.com","legal","PXGE"],["divorcemediatorsdenverco.com","legal","PXGE"],["dogeardrops.com","pets","PBS"],["dognutritionsupplements.com","pets","PDE"],["dogsupplementsonline.com","pets","PCE"],["dogtreatchews.com","pets","PES"],["dominicanrealestatetour.com","realestate","PDGE"],["dominicanrepublicplacestovisit.com","travel","DGE"],["dominicanrepublicseo.com","marketing","PGE"],["dominicanrepublicvacationspots.com","travel","DGE"],["duiattorneygreeley.com","legal","PGES"],["duilawyersingreeleyco.com","legal","PGE"],["educationalgamewebsites.com","events","E"],["estesparkcorealestate.com","realestate","PGE"],["eyetoad.com","marketing","PDBS"],["familylawattorneygreeley.com","legal","PXGE"],["familylawattorneygreeleyco.com","legal","PXGE"],["familymediationdenver.com","legal","PGE"],["fencebuildersdenver.com","trades","PGES"],["fencecontractoromaha.com","trades","PGE"],["fenceinstallationdenver.com","trades","PGE"],["fencescolorado.com","trades","PGES"],["fencesdenver.com","trades","PXGES"],["fencesdenverco.com","trades","PXGES"],["fencesomaha.com","trades","PGES"],["findbestautoinsurance.com","insurance","PE"],["firestonehomesforsale.com","realestate","PGE"],["fishingguidecolorado.com","travel","PXGE"],["fishingguidehawaii.com","travel","PXGES"],["fishingguidescolorado.com","travel","PXGE"],["fishingguideshawaii.com","travel","PXGES"],["flbusinesslist.com","marketing","PGES"],["flighthotelpackage.com","travel","PDES"],["flooringcastlerock.com","trades","PGES"],["foodtruckcateringdenverco.com","food","PGE"],["frederickcorealestate.com","realestate","PGE"],["fungamewebsite.com","events","ES"],["funthingstodoindenver.com","travel","PGE"],["gabusinesslist.com","marketing","PGES"],["geodenver.com","marketing","PBS"],["globalactionnews.com","events","PES"],["globalpeacepromise.com","events","BS"],["globalvrmall.com","vr","PXES"],["glp-1-peptides.com","health","PE"],["glp-1colorado.com","health","PGE"],["glp-1denver.com","health","PXGE"],["glp-1littleton.com","health","PXGE"],["glp1agonistmeds.com","health","PE"],["glp1denver.com","health","PDXGE"],["glp1littleton.com","health","PXGE"],["greeleycoduiattorney.com","legal","PGE"],["greeleycoduilawyer.com","legal","PGES"],["greeleycolawyer.com","legal","PGES"],["greeleymediator.com","legal","PGES"],["handicapbathtubs.com","bath","PDCES"],["handicaprollinshower.com","bath","PCE"],["hawaiidiveshops.com","travel","PGES"],["hawaiiscubashops.com","travel","PGES"],["highlandsranchdecks.com","trades","PGES"],["hightechtoilet.com","bath","PES"],["higueyseo.com","marketing","PGES"],["homeforsalebelize.com","realestate","PGES"],["homeforsaleboulder.com","realestate","PXGES"],["homeforsaleboulderco.com","realestate","PXGE"],["homeforsalecostarica.com","realestate","PGE"],["homesforsaleerie.com","realestate","PGES"],["homesforsaleindaconoco.com","realestate","PGE"],["homesforsaleindenverco.com","realestate","PGE"],["homesforsaleinfirestoneco.com","realestate","PGE"],["homesforsaleinfrederickco.com","realestate","PGE"],["homesforsalelongmontco.com","realestate","PGE"],["housepaintersbrightonco.com","trades","PGE"],["housepaintersdenverco.com","trades","PDGE"],["housesforsalefirestoneco.com","realestate","PGE"],["housesforsaleindaconoco.com","realestate","PGE"],["housesforsaleinfrederickco.com","realestate","PGE"],["howtosaveonvacations.com","travel","E"],["howtosetupaiagent.com","ai","PXES"],["howtosetupaiagents.com","ai","PXE"],["ilbusinesslist.com","marketing","PGES"],["ilovemybrands.com","promo","BS"],["insurancebrighton.com","insurance","PGES"],["insuranceloveland.com","insurance","PGES"],["kauaidiveshops.com","travel","PGES"],["kauaihirealestate.com","realestate","PGES"],["kauaipropertyforsale.com","realestate","PGE"],["landforsaleinco.com","realestate","PES"],["landtobuyincolorado.com","realestate","PGES"],["laromanaseo.com","marketing","PGES"],["lawyergreeley.com","legal","PGES"],["lawyersingreeleyco.com","legal","PGES"],["learntouseaiagents.com","ai","PE"],["linkrestaurants.com","food","PDCES"],["littletonautoglass.com","auto","PGES"],["littletonbathroomremodel.com","bath","PGE"],["littletoncoseo.com","marketing","PGES"],["littletondeck.com","trades","PGES"],["littletonglp-1.com","health","PGE"],["littletongranite.com","trades","PGES"],["littletonmattress.com","home","PGES"],["localdealsfinder.com","prof","ES"],["localfoodnearme.com","food","PDES"],["localmoverdenver.com","cleanmove","PGES"],["localseoforrestaurant.com","marketing","PE"],["longdistancemoversdenver.com","cleanmove","PGE"],["longmontcolandscaping.com","trades","PGE"],["longmontcomedspa.com","health","PGES"],["longmonthousecleaning.com","cleanmove","PGE"],["longmontusedcars.com","auto","PGES"],["losangelesseopro.com","marketing","PGES"],["lovelandcoinsurance.com","insurance","PGES"],["lovelandhealthinsurance.com","insurance","PGE"],["lyonscorealestate.com","realestate","PGES"],["madeinusawalkintubs.com","bath","PDGES"],["mao-seo.com","marketing","PB"],["marketingforrestaurant.com","marketing","PE"],["massageshonolulu.com","health","PDGES"],["mattresscolorado.com","home","PGES"],["mattressesdenver.com","home","PGES"],["mattresslittleton.com","home","PGES"],["mattresssaledenver.com","home","PGES"],["maui-seo.com","marketing","PDGE"],["medellinseo.com","marketing","PGES"],["mediationdenverco.com","legal","PGES"],["mediationservicesdenver.com","legal","PGE"],["melatoninforcats.com","pets","PES"],["mmadenver.com","events","PGES"],["mobileautodetailingomaha.com","auto","PGE"],["mobilecardetailingomaha.com","auto","PGE"],["mobilecarrepairnearme.com","auto","PE"],["mobilemechaniccolorado.com","auto","PGE"],["mobilewindshieldreplacementdenver.com","auto","PGE"],["monumentcowebdesigner.com","marketing","PDGE"],["monumentdeck.com","trades","PGES"],["monumentseo.com","marketing","PDGES"],["monumentwebdesigner.com","marketing","PGES"],["motorcyclescolorado.com","auto","PGES"],["motorhomerentaldenver.com","travel","PGE"],["moversdenverco.com","cleanmove","PGES"],["movingcompaniesdenverco.com","cleanmove","PGE"],["movinghelpdenver.com","cleanmove","PGES"],["mysaleshelp.com","marketing","PDBS"],["nebusinesslist.com","marketing","PGES"],["nederlandcorealestate.com","realestate","PGE"],["neurallinkchildrensbooks.com","events","BX"],["neurolinkchildrensbooks.com","events","BX"],["neurolinkkidsbooks.com","events","BX"],["nvbusinesslist.com","marketing","PGES"],["nybusinesslist.com","marketing","PGES"],["oahufishingguides.com","travel","PDGES"],["oahurealestate.homes","realestate","PGES"],["ohaurealestate.com","realestate","GES"],["omahamobiledetailing.com","auto","PDGE"],["omahanecarpetcleaning.com","cleanmove","PDGE"],["omahaseopros.com","marketing","PDGES"],["onarollseo.com","marketing","PBS"],["pabusinesslist.com","marketing","PGES"],["painterhotline.com","trades","PDBS"],["paintersarvada.com","trades","PDGES"],["paintersgoldenco.com","trades","PDGES"],["painterslakewood.com","trades","PDGES"],["painterswheatridge.com","trades","PDGES"],["paintingbrighton.com","trades","PDGES"],["pawcreamfordogs.com","pets","PBS"],["pergolabuildersdenver.com","trades","PGE"],["personalizedpensforbusiness.com","promo","PCE"],["petdentalcleanse.com","pets","PBS"],["peteardrops.com","pets","PBS"],["pethealthsupplement.com","pets","PCES"],["petssupplement.com","pets","PES"],["phoenixsworld.com","events","DB"],["placestovisitincolorado.com","travel","PGE"],["placestovisitincostarica.com","travel","PDGE"],["pressreleaseforbusiness.com","marketing","PDE"],["probioticchewsfordogs.com","pets","PE"],["probioticsforcat.com","pets","PES"],["probioticsfordog.com","pets","PES"],["probioticsfordogsguthealth.com","pets","PE"],["propertiesforsalecolorado.com","realestate","PGE"],["puertoplata-realestate.com","realestate","PGE"],["puertoplata-realty.com","realestate","PGE"],["puertoplatarealstate.com","realestate","GE"],["puertoplatarestaurants.com","food","PDGE"],["puertoplataseo.com","marketing","PDGES"],["puertorico-seo.com","marketing","PDGE"],["ranchhousesforsale.com","realestate","PES"],["realestateerieco.com","realestate","PGES"],["realestateforsalebouldercolorado.com","realestate","PGE"],["realestateforsalekauai.com","realestate","PGE"],["realestatelongmontco.com","realestate","PGE"],["realestatenederland.com","realestate","PGES"],["realestateniwot.com","realestate","PXGES"],["realestateniwotco.com","realestate","PXGES"],["realestatesosua.com","realestate","PDGES"],["realtyboulderco.com","realestate","PGES"],["realtysosua.com","realestate","PGES"],["rentsilentdiscoheadphones.com","events","PE"],["rentvacationhomehawaii.com","travel","PGE"],["restaurantesenpuertoplata.com","food","PIGE"],["restauranthonolulu.com","food","PDGES"],["restaurantlocalseo.com","marketing","PES"],["restaurantmaui.com","food","PGES"],["restaurantsadvertising.com","marketing","PDCE"],["restaurantsadvertisingideas.com","marketing","PE"],["restaurantsbelize.com","food","PIGES"],["restaurantscostarica.com","food","PIGE"],["restaurantsmarketingstrategies.com","marketing","PE"],["restaurantsoahu.com","food","PGES"],["restaurantspuertoplata.com","food","PGE"],["restaurantsseo.com","marketing","PDCES"],["rockitwears.com","events","PBS"],["roll-in-showers.com","bath","PDCE"],["roofcontractordenverco.com","trades","PGE"],["roofersdenvercolorado.com","trades","PGE"],["roofingcompaniesdenver.com","trades","PGE"],["rugcleaningdenverco.com","cleanmove","PGES"],["rugcleaningomahane.com","cleanmove","PGES"],["rvsalesdenver.com","auto","PGES"],["salestrainingtool.com","marketing","PCES"],["sanpedrosnorkelingtours.com","travel","PDGE"],["santodomingoseo.com","marketing","PDGES"],["searchconverts.com","marketing","PDBS"],["seniorbathroomsafety.com","bath","PCE"],["seniorcareideas.com","health","PES"],["seniorwalkinbathtubs.com","bath","PDE"],["seniorwalkintub.com","bath","PDES"],["seo-hawaii.com","marketing","PGE"],["seoagencyhawaii.com","marketing","PGES"],["seoboulderco.com","marketing","PGES"],["seobroomfield.com","marketing","PDGES"],["seocompanyaurora.com","marketing","PDGES"],["seocompanyhawaii.com","marketing","PGES"],["seodenverco.com","marketing","PGES"],["seodominicanrepublic.com","marketing","PDGE"],["seoexpertsdenver.com","marketing","PDGES"],["seoinmaui.com","marketing","PGES"],["seolittletonco.com","marketing","PDGES"],["seomarketingdenver.com","marketing","PGES"],["seooahu.com","marketing","PGES"],["seothornton.com","marketing","PDGES"],["seounitedstates.com","marketing","PDCGES"],["seowebdevelopers.com","marketing","PCES"],["shorttermrentalscostarica.com","travel","PGE"],["shower4less.com","bath","PXE"],["showerpackages.com","bath","PCES"],["showerremodelingnearme.com","bath","PCE"],["showers4less.com","bath","PXCE"],["showersforelderly.com","bath","PDCES"],["showersforless.com","bath","PCES"],["showerwallskit.com","bath","PDES"],["sickmindsgroup.com","events","DBS"],["silentdancepartyheadphones.com","events","E"],["silentdiscodenverco.com","events","PGES"],["silentdiscoforrent.com","events","PES"],["silentdiscopartynearme.com","events","PE"],["socialmybusiness.com","marketing","PDBS"],["spabrighton.com","health","PGES"],["supplementsdogs.com","pets","PES"],["supplementsforcat.com","pets","PES"],["supplementsfordog.com","pets","PES"],["surfingclasseshawaii.com","travel","PGE"],["surfinglessonscostarica.com","travel","PGE"],["surflessonhonolulu.com","travel","PDGES"],["theartyoulove.com","events","PBS"],["thecryptoguider.com","events","BS"],["thedenverdayspa.com","health","PGES"],["therestaurantslist.com","food","PCES"],["thevrgalaxy.com","vr","PDBS"],["thingstodobelize.com","travel","PDGES"],["thingstodoinmauihawaii.com","travel","PGE"],["thingstodoinpuertoplata.com","travel","PDGE"],["thorntondecks.com","trades","PGES"],["thorntonmechanic.com","auto","PGES"],["thorntonmobilemechanic.com","auto","PGE"],["tiresbrightonco.com","auto","PGES"],["tiresdenverco.com","auto","PGES"],["tireshopsdenver.com","auto","PGES"],["tirestoresdenver.com","auto","PGES"],["townhomesforsaledenver.com","realestate","PGE"],["townhousesforsalenearme.com","realestate","PE"],["trailersdenver.com","auto","PGES"],["trailersforsalecolorado.com","auto","PGE"],["txbusinesslist.com","marketing","PGES"],["txsautoinsurance.com","insurance","PES"],["unitedstatesseo.com","marketing","PCGES"],["usabusinesssearch.com","marketing","PDCGES"],["usawalkintub.com","bath","PGES"],["usedcarslongmontco.com","auto","PGES"],["utahwalkintubs.com","bath","PDGES"],["vacationapartmenthawaii.com","travel","PGE"],["vacationcondohawaii.com","travel","PGES"],["vacationcondohonolulu.com","travel","PGE"],["vacationcondooahu.com","travel","PDGES"],["vacationhomeoahu.com","travel","PXGES"],["vacationhomeshonolulu.com","travel","PGE"],["vacationhomesoahu.com","travel","PXGES"],["vacationrentalbelize.com","travel","PGE"],["virtualrealityadventure.com","vr","PDE"],["virtualrealityflightsimulators.com","vr","PE"],["virtualrealitymalls.com","vr","PES"],["vivirencostarica.com","realestate","PDIGES"],["vrflyingsimulator.com","vr","PDES"],["vrmallglobal.com","vr","PXES"],["vrmallworld.com","vr","PXES"],["wabusinesslist.com","marketing","PGES"],["walkintubdenver.com","bath","PDGES"],["walkintubguide.com","bath","PCES"],["walkintubny.com","bath","PDES"],["walkintubs4less.com","bath","PDCE"],["walkintubsarizona.com","bath","PDGES"],["walkintubscalifornia.com","bath","PDGE"],["walkintubschicago.com","bath","PDGES"],["walkintubsflorida.com","bath","PDGES"],["walkintubsforelderly.com","bath","PDCE"],["walkintubshouston.com","bath","PDGES"],["walkintubsmiami.com","bath","PGES"],["walkintubsokc.com","bath","PGES"],["walkintubsomaha.com","bath","PGES"],["walkintubstexas.com","bath","PDGES"],["walkintubswithjets.com","bath","PDES"],["walkintubwithshower.com","bath","PDES"],["webdesigndenvercolorado.com","marketing","PGE"],["webdesignmonument.com","marketing","PDGES"],["websitedesignercoloradosprings.com","marketing","PDGE"],["websitedesignerdenverco.com","marketing","PGE"],["weddingcateringdenverco.com","food","PGE"],["weightlossglp-1.com","health","PDE"],["westminsterseo.com","marketing","PDGES"],["whatsagentics.com","ai","ES"],["whatsglp-1.com","health","PDE"],["wheatridgeseo.com","marketing","PDGES"],["wheelchairaccessibleshower.com","bath","PCE"],["windshieldchiprepairdenverco.com","auto","PGE"],["windshieldreplacementlittletonco.com","auto","PGE"],["worldbusinesssearch.com","marketing","PCES"],["worldvrmall.com","vr","PDXBS"]];
var CATN = {"marketing": "marketing and seo", "ai": "ai and agents", "realestate": "real estate", "travel": "travel and hospitality", "bath": "bath and accessibility", "trades": "home services and trades", "home": "mattresses, furniture and appliances", "health": "health and beauty", "auto": "automotive", "insurance": "insurance", "food": "restaurants and food", "pets": "pet and supplements", "prof": "professional services", "events": "media, events and tech", "vr": "virtual reality", "legal": "legal and mediation", "cleanmove": "cleaning and moving", "promo": "promotional products"};
var CATHUB = {"marketing": "seo-marketing", "ai": "ai-agents", "realestate": "real-estate", "travel": "travel", "bath": "accessible-bath", "trades": "home-services", "home": "mattresses-furniture-appliances", "health": "health-beauty", "auto": "automotive", "insurance": "insurance", "food": "restaurants", "pets": "pets", "prof": "professional", "events": "media-tech", "vr": "virtual-reality", "legal": "legal", "cleanmove": "cleaning-moving", "promo": "promotional"};
var TAGN={"P":"Premium","D":"Developed — there is a live site on it","C":"Category killer","X":"a close variant is also available",
"G":"Geo-locked to a real place","B":"Brandable","I":"International","E":"Exact match","S":"passes the phone test"};

/* ---------- no-repeat response pools ---------- */
var USED = {};
function pick(key, arr){
  USED[key] = USED[key] || [];
  if (USED[key].length >= arr.length) USED[key] = [];
  var open = arr.filter(function(_,i){ return USED[key].indexOf(i) < 0; });
  var choice = open[Math.floor(Math.random()*open.length)];
  USED[key].push(arr.indexOf(choice));
  return choice;
}

var GREET = [
 "Hey! What are you working on?",
 "Hi there. Looking for a name, or just seeing what is here?",
 "Hey &mdash; glad you stopped by. What do you sell?",
 "Hello! Give me the short version or the whole story, either works.",
 "What's up. Tell me what you need and I'll point you the right way.",
 "Hi! I know every name on this site. Where should we start?",
 "Hey there. Start anywhere, even if you are not sure yet.",
 "Good to see you. What kind of business are we naming?"
];
var ASSETS = [
 ["eyetoad.com","SEO, AIO and GEO agency work out of Denver, plus custom-coded sites","https://eyetoad.com"],
 ["searchconverts.com","conversion optimization, video, copy, branding, PPC and remarketing","https://searchconverts.com"],
 ["buyweburl.com","domain registration and website plans if the name is still available","https://www.buyweburl.com"],
 ["conversationalaibot.com","AI chatbots for business, like the one you are talking to","https://conversationalaibot.com"],
 ["mysaleshelp.com","sales training and objection handling","https://mysaleshelp.com"],
 ["pressreleaseforbusiness.com","press release publishing when you have something to announce","https://pressreleaseforbusiness.com"],
 ["businessdirectorynow.com","a national business directory listing","https://businessdirectorynow.com"]
];
var SITECROSS = [
 'Bought the name? You are going to need a website with it. <a href="https://eyetoad.com" rel="noopener">Eye To Ad Media builds them</a>.',
 'A name without a site does nothing. <a href="/domain-and-website/">Here is what it costs to have one built on it.</a>',
 'Worth knowing: <a href="https://searchconverts.com" rel="noopener">Search Converts</a> handles the part after they arrive — offer, message, tracking, follow-up.',
 'Launching under a new name? <a href="https://pressreleaseforbusiness.com" rel="noopener">Announce it properly.</a>',
 'Still checking availability? <a href="https://www.buyweburl.com" rel="noopener">Search it at BuyWebURL</a> — cheapest outcome there is.',
 'Want a bot like me on your own site? <a href="https://conversationalaibot.com" rel="noopener">That is a thing we build.</a>'
];
var ACK = ["That makes sense.","Got it.","Fair question.","Good point.","I hear you.","That helps.","Understood.","Okay &mdash; now I see what you mean.","Thanks for being direct.","That gives me a clearer picture."];
var JOKES = [
 "Why did the domain go to therapy? Unresolved issues.",
 "I tried to buy a name with a hyphen in it. Long story, lot of spelling.",
 "A URL walks into a bar. The bartender says, sorry, we don't serve your type &mdash; no slashes.",
 "I told my buddy his domain was too long. He said he'd get back to me in a few characters.",
 "Two domains walk into a registrar. Only one comes out renewed.",
 "What do you call a domain nobody renewed? Available. Briefly.",
 "My favorite extension is .com. My second favorite is also .com.",
 "I named my dog after my first domain. He does not come when called either."
];
var CTA = [
 "Want a real number on it? "+telLink(),
 "If you want to talk it through, "+telLink()+".",
 "Easiest way to get a price is "+telLink()+" &mdash; a person answers.",
 "When you are ready, "+telLink()+" and we will talk about it.",
 "No pressure at all. "+telLink()+" whenever you want the number."
];
function telLink(){ return '<a class="zbx-tel" href="'+TELH+'">call '+TEL+'</a>'; }

/* ---------- knowledge ---------- */
function findDomains(t){
  var q = t.toLowerCase().replace(/[^a-z0-9 .]/g," ").trim();
  if (q.length < 3) return [];
  var exact = IDX.filter(function(r){ return r[0].indexOf(q.replace(/\s+/g,"")) === 0 || r[0] === q; });
  if (exact.length) return exact.slice(0,6);
  var words = q.split(/\s+/).filter(function(w){ return w.length > 2; });
  if (!words.length) return [];
  return IDX.filter(function(r){
    return words.every(function(w){ return r[0].indexOf(w) > -1; });
  }).slice(0,6);
}
function domLine(r){
  var tags = r[2].split("").filter(function(t){ return "PDCX".indexOf(t)>-1; })
              .map(function(t){ return TAGN[t]; }).join(", ");
  return "<strong>"+r[0]+"</strong> &mdash; "+CATN[r[1]]+(tags? ". "+tags : "");
}

var KB = [
 [/\b(price|pricing|cost|how much|what.*charge|quote)\b/, function(){
   return "No prices are published anywhere on this site, and that is on purpose &mdash; the same name costs one thing bare, another with a site built on it, and another as part of a cluster. Every number is negotiable and given on a call. "+telLink()+" and you will get a straight figure.";
 }],
 [/\b(15%|commission|engagement fee|1500|1,500|acquisition|acquire|someone else owns|already (taken|owned|registered))\b/, function(){
   return "If somebody else owns the name you want, that is our acquisition service. It is $1,500 to engage &mdash; that buys ownership research, a written valuation with comparable sales, a documented approach to the owner and their actual answer in writing, whether or not it closes. If it does close, 15% of the purchase price, or $1,500, whichever is greater.<br><br><strong>No promises on the outcome.</strong> Plenty of owners never reply and some will not sell at any price. We charge for the work, not for a maybe. <a href='/find-a-domain/'>Full detail here.</a>";
 }],
 [/\b(rank|ranking|seo|google|first page|number one|#1|cited|chatgpt|ai overview)\b/, function(){
   return "Straight answer: a keyword in your domain does not earn you a ranking. Google removed that benefit years ago and has said so repeatedly. I am not going to tell you otherwise just to move a name.<br><br>What a good name actually does &mdash; says what you do before anyone clicks, survives a phone call and a truck door, creates branded searches nobody can outbid you for, and nobody else can ever register it. <a href='/does-a-keyword-domain-help-seo/'>The long version is here, with sources.</a>";
 }],
 [/\b(guarantee|promise|will i rank|can you get me)\b/, function(){
   return "No. Nobody can guarantee a ranking &mdash; Google's own guidance says so. What we commit to is working on your business like it is ours, giving you the technology and skill we have, and telling you honestly what is working. Anyone promising you position one is either uninformed or counting on you being uninformed.";
 }],
 [/\b(who owns|whois|who.?is|lookup|find the owner|registrant)\b/, function(){
   return "You can look that up free in about four seconds &mdash; <a href='/who-owns-this-domain/'>this page</a> opens the public records for you through ICANN and who.is. Fair warning: most records are behind privacy protection now, so you will often get a forwarder instead of a person. That is normal, and it is the point where most people get stuck.";
 }],
 [/\b(worth|valuation|appraisal|value|how much is my)\b/, function(){
   return "A domain is worth what one specific buyer will pay for it, and no calculator knows who that buyer is. <a href='/what-is-my-domain-worth/'>This page</a> shows you what buyers actually look at first, and you can send the name over for a written read from a person. Free, and if the honest answer is that it is worth less than you hoped, you will get that too.";
 }],
 [/\b(sell|selling|i own|i have a domain|buy (my|mine)|portfolio for sale)\b/, function(){
   return "We buy some names outright and broker the rest. Send it over on <a href='/sell-your-domain/'>this page</a> and you will get a written read on what it has going for it, whether we want to buy it, and what a realistic range looks like. Sometimes the honest answer is keep it and build on it &mdash; we say that more than you would expect.";
 }],
 [/\b(register|available|is it taken|new domain|buyweburl)\b/, function(){
   return "Check availability first &mdash; people overpay for variations of names that were sitting unregistered the whole time. Search it at <a href='https://www.buyweburl.com' rel='noopener'>BuyWebURL</a>. If it is free, register it and save your money. If it is taken, come back and we will talk about what we own or about going to get it.";
 }],
 [/\b(website|site|build|develop|design|99|web design|code)\b/, function(){
   return "Yes &mdash; custom-coded, from $99 a month with a buyout option at 24 to 36 months. Built around the name, structured for search and for AI engines, with a real conversion path. <a href='/domain-and-website/'>Details here.</a> If you already run WordPress, Shopify or Wix, we will work in that instead rather than pushing a migration you did not ask for.";
 }],
 [/\b(host|hosting|server|ssl|cpanel|email address)\b/, function(){
   return "The domain is the address, hosting is the building &mdash; you need both before anything shows up. <a href='/hosting/'>Here is the hosting side</a>, including why the very cheapest option usually costs more than it saves.";
 }],
 [/\b(transfer|auth code|epp|how long|move it)\b/, function(){
   return "Once funds clear you get the registrar authorization code and transfer instructions the same business day. After that the registrars control the clock &mdash; a .com usually completes in a few days. Nothing transfers before payment clears, which protects both sides.";
 }],
 [/\b(trademark|udrp|infringe|legal|lawyer|attorney)\b/, function(){
   return "I am not a lawyer and this is not legal advice &mdash; take that seriously rather than as a formality. If a name shadows somebody's live mark, buying it is how people lose the name and the money together. Talk to a trademark attorney who actually practices in domain and internet law before you make an offer, because an offer can change the picture.";
 }],
 [/\b(developed|live site|already built|existing site|aged)\b/, function(){
   return "Some names here come with a live site already on them &mdash; real pages, real structure, real history. That is a business asset rather than a domain purchase and it prices differently. <a href='/developed-assets/'>They are all on this page.</a> One honest caveat: search positions are not property and they do not transfer like a title.";
 }],
 [/\b(tag|premium|category killer|defensive|geo.?lock|brandable|say.?it.?once|what do the tags)\b/, function(){
   return "Every tag on the catalog is something you can check yourself by looking at the name &mdash; no scores, no grades, no predictions. Premium, Developed, Category killer, Defensive pair, Geo-locked, Brandable, International, Exact match, and Say-it-once, which just means it passes the phone test. <a href='/domains/'>They are all explained on the catalog page.</a>";
 }],
 [/\b(lease|finance|financing|payment plan|rent)\b/, function(){
   return "Lease and owner-carry may be available on some names &mdash; it depends on the name and the deal, so I am not going to quote terms I cannot stand behind. Ask on the call and you will get a real answer for your situation. "+telLink()+".";
 }],
 [/\b(eyetoad|eye to ad|search ?converts|who are you guys|what else do you|other (sites|services|companies)|agency)\b/, function(){
   return "Best Domains for Business is the domain side of <a href='https://eyetoad.com' rel='noopener'>Eye To Ad Media</a> in Denver &mdash; search visibility and custom-coded sites since 2012. <a href='https://searchconverts.com' rel='noopener'>Search Converts</a> handles conversion, creative and campaigns.<br><br>"+pick("cross",SITECROSS);
 }],
 [/\b(broker|brokerage|office|walk in|pitch)\b/, function(){
   return "There is a whole office for that &mdash; <a href='/domain-broker/'>walk in here</a> and Marlowe will give you the pitch in about ninety seconds. You can tell him no at any point.";
 }],
 [/\b(blog|article|read more|guide|learn)\b/, function(){
   return "We write long-form on this properly &mdash; <a href='/blog/'>the blog is here</a>. Acquisition playbook, what a name is really worth, transfers and escrow, and how to pick one that survives a phone call.";
 }],
 [/\b(joke|funny|laugh|bored|entertain)\b/, function(){
   return pick("joke", JOKES)+"<br><br>Want another, or should we find you a name?";
 }],
 [/\b(human|person|real person|talk to someone|call me|representative)\b/, function(){
   return "Of course. "+telLink()+" &mdash; a real person answers. Or use <a href='/contact/'>the contact form</a> and someone gets back to you, usually within one business day.";
 }],
 [/\b(are you (a )?(real|human|bot|robot)|is this a bot)\b/, function(){
   return "I am an AI assistant for Best Domains for Business, not a person. I can answer what I actually know and hand you to a human the second it matters. "+telLink()+" gets you a real one.";
 }],
 [/\b(how are you|how.s it going|what.s up|hows it going|you good)\b/, function(){
   return "Doing well and ready to help. How are things on your end &mdash; starting something new, or fixing something that exists?";
 }],
 [/\b(thank|thanks|thx|appreciate)\b/, function(){
   return "Anytime. If anything else comes up I am right here, and "+telLink()+" if you would rather just talk it through.";
 }],
 [/\b(bye|later|goodbye|all set|that.s all|im out)\b/, function(){
   return "Take care. The number stays the same whenever you want it &mdash; "+TEL+".";
 }]
];

function reply(t){
  var s = (t||"").toLowerCase();

  var hits = findDomains(t);
  if (hits.length){
    if (hits.length === 1){
      var r = hits[0];
      return "Yes, that one is ours. "+domLine(r)+".<br><br>No figure is published anywhere &mdash; "+telLink()+" and you get a real one.<br><br>"+pick("cross",SITECROSS);
    }
    return "Found "+hits.length+":<br><br>" + hits.map(function(r){ return "&bull; "+domLine(r); }).join("<br>") +
      "<br><br>Which one? Or "+telLink()+" and we go through them out loud.";
  }

  for (var i=0;i<KB.length;i++){ if (KB[i][0].test(s)) return KB[i][1](); }

  if (/^(hi|hey|hello|yo|howdy|sup|hiya|good (morning|afternoon|evening))\b/.test(s)) return pick("greet", GREET);

  if (s.length < 4) return "Say a bit more and I will point you the right way &mdash; a trade, a city, or a name you have your eye on all work.";

  return pick("ack", ACK) + " Give me the trade and the market and I will check what we own &mdash; or "+telLink()+" and a person will.";
}

/* ---------- mount ---------- */
function mount(){
  var st = document.createElement("style"); st.textContent = CSS;
  document.head.appendChild(st);
  var host = document.createElement("div");
  host.id = "zbx";
  host.innerHTML = ART + HTML;
  document.body.appendChild(host);
  wire(host);
}

function wire(root){
  var seal=root.querySelector("#zbx-seal"), guyB=root.querySelector("#zbx-guy-btn"),
      smoke=root.querySelector("#zbx-smoke"), bal=root.querySelector("#zbx-balloon"),
      balX=root.querySelector("#zbx-bal-x"), log=root.querySelector("#zbx-log"),
      chips=root.querySelector("#zbx-chips"), inp=root.querySelector("#zbx-in"),
      send=root.querySelector("#zbx-send"), close=root.querySelector("#zbx-close"),
      minb=root.querySelector("#zbx-min"), stage=root.querySelector("#zbx-stage"),
      tab=root.querySelector("#zbx-tab"), hint=root.querySelector("#zbx-hint"),
      kill=root.querySelector("#zbx-kill");
  var arrived=false, started=false;

  if (ls(KEY_DISMISS) === "1"){
    stage.style.display = "none";
    tab.classList.add("show");
  }

  function buildSmoke(){
    smoke.innerHTML="";
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
    if(root.querySelector(".zbx-stage").classList.contains("is-bursting")) return;
    buildSmoke(); root.classList.add("is-bursting"); stage.classList.add("is-bursting");
    setTimeout(function(){ root.classList.add("is-live"); stage.classList.add("is-live"); arrived=true;
      if(openAfter) setTimeout(open,1200); },620);
  }
  function open(){
    if(!arrived){ arrive(true); return; }
    lsdel(KEY_MIN);
    root.classList.add("is-open"); stage.classList.add("is-open");
    if(!started){ started=true; boot(); }
    setTimeout(function(){ inp.focus(); },300);
  }
  function minimize(){
    root.classList.remove("is-open"); stage.classList.remove("is-open");
    ls(KEY_MIN,"1");
  }
  function dismiss(){
    ls(KEY_DISMISS,"1");
    bal.style.opacity="0"; bal.style.pointerEvents="none";
    root.classList.remove("is-open","is-live","is-bursting");
    stage.classList.remove("is-open","is-live","is-bursting");
    stage.style.display="none";
    tab.classList.add("show");
    hint.classList.add("show");
    setTimeout(function(){ hint.classList.remove("show"); }, 4200);
  }
  function restore(){
    lsdel(KEY_DISMISS);
    root.classList.remove("is-open");
    bal.style.opacity=""; bal.style.pointerEvents="";
    stage.style.display="";
    tab.classList.remove("show"); hint.classList.remove("show");
    if(arrived){ open(); } else { arrive(true); }
  }

  seal.addEventListener("click",function(){ arrive(true); });
  guyB.addEventListener("click",open);
  bal.addEventListener("click",function(e){ if(e.target===balX) return; open(); });
  bal.addEventListener("keydown",function(e){ if(e.key==="Enter"||e.key===" "){ e.preventDefault(); open(); } });
  balX.addEventListener("click",function(e){ e.preventDefault(); e.stopPropagation(); dismiss(); });
  if(kill) kill.addEventListener("click",function(e){ e.preventDefault(); e.stopPropagation(); dismiss(); });
  minb.addEventListener("click",minimize);
  close.addEventListener("click",dismiss);
  tab.addEventListener("click",restore);
  document.addEventListener("keydown",function(e){
    if(e.key==="Escape" && root.classList.contains("is-open")) minimize();
  });

  /* proactive arrival — never when dismissed */
  var fired=false;
  function maybe(){
    if(fired||arrived||ls(KEY_DISMISS)==="1") return;
    if(window.scrollY > window.innerHeight*0.45){ fired=true; arrive(false); }
  }
  window.addEventListener("scroll",maybe,{passive:true});
  setTimeout(function(){ if(!fired&&!arrived&&ls(KEY_DISMISS)!=="1"){ fired=true; arrive(false); } },26000);

  /* ---- conversation ---- */
  function esc(s){ return String(s).replace(/[&<>"]/g,function(c){
    return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]; }); }
  function say(html,who){
    var d=document.createElement("div");
    d.className="zbx-msg zbx-"+(who||"bot");
    d.innerHTML=html; log.appendChild(d); log.scrollTop=log.scrollHeight;
  }
  function botSay(html,delay){
    var t=document.createElement("div"); t.className="zbx-msg zbx-bot zbx-typing";
    t.innerHTML="<span></span><span></span><span></span>";
    log.appendChild(t); log.scrollTop=log.scrollHeight;
    setTimeout(function(){ t.remove(); say(html,"bot"); }, delay||620);
  }
  function setChips(list){
    chips.innerHTML="";
    list.forEach(function(c){
      var b=document.createElement("button"); b.className="zbx-chip"; b.type="button";
      b.textContent=c; b.addEventListener("click",function(){ handle(c,true); });
      chips.appendChild(b);
    });
  }
  var CHIPSETS=[
    ["Find me a name","What do the tags mean?","Someone owns the one I want","Just give me the number"],
    ["Show me what you own","How much does a name cost?","Can you build the site too?","Tell me a joke"],
    ["I want to sell a domain","What is mine worth?","Who owns a domain?","Talk to a person"],
    ["Walk me into the office","Will it help me rank?","What else do you do?","Show me the blog"],
    ["I need hosting too","How does transfer work?","Got anything developed?","Just the number please"]
  ];
  function boot(){
    botSay(pick("greet",GREET),420);
    setTimeout(function(){ setChips(pick("chips",CHIPSETS)); },700);
  }
  function handle(text,fromChip){
    if(!text||!text.trim()) return;
    say(esc(text),"me");
    inp.value=""; chips.innerHTML="";
    var r=reply(text);
    botSay(r, 520+Math.min(900,r.length*3));
    setTimeout(function(){ setChips(pick("chips",CHIPSETS)); }, 1100);
  }
  send.addEventListener("click",function(){ handle(inp.value); });
  inp.addEventListener("keydown",function(e){ if(e.key==="Enter"){ e.preventDefault(); handle(inp.value); } });

  window.openZach=open; window.closeZach=minimize; window.dismissZach=dismiss;
}

if(document.readyState==="loading") document.addEventListener("DOMContentLoaded",mount);
else mount();
})();
