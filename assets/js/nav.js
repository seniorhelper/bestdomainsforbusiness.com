
(function(){
  var tog = document.querySelector("[data-navtog]"), nav = document.getElementById("nav"), hdr = tog && tog.closest(".hdr");
  function fit(){ if(!nav.classList.contains("open")) return; var h=(hdr||nav.parentNode).getBoundingClientRect().bottom; nav.style.maxHeight=Math.max(240,window.innerHeight-h)+"px"; }
  function setOpen(o, refocus){
    nav.classList.toggle("open",o); document.body.classList.toggle("nav-open",o); document.documentElement.classList.toggle("nav-open",o);
    tog.setAttribute("aria-expanded",o?"true":"false"); tog.setAttribute("aria-label",o?"Close menu":"Open menu");
    if(o){ fit(); nav.scrollTop=0; var f=nav.querySelector("a,button"); if(f) f.focus({preventScroll:true}); }
    else { nav.style.maxHeight=""; if(refocus) tog.focus(); }
  }
  if(tog && nav){
    tog.addEventListener("click", function(e){ e.stopPropagation(); setOpen(!nav.classList.contains("open"), false); });
    window.addEventListener("resize", function(){ if(nav.classList.contains("open") && getComputedStyle(tog).display==="none") setOpen(false,false); else fit(); });
    document.addEventListener("keydown",function(e){
      if(!nav.classList.contains("open")) return;
      if(e.key==="Escape"){ setOpen(false,true); return; }
      if(e.key==="Tab"){ // keep focus inside toggle + menu while open
        var items=[tog].concat([].slice.call(nav.querySelectorAll("a[href],button:not([disabled])")).filter(function(x){return x.offsetParent!==null;}));
        var i=items.indexOf(document.activeElement);
        if(e.shiftKey && i<=0){ e.preventDefault(); items[items.length-1].focus(); }
        else if(!e.shiftKey && i===items.length-1){ e.preventDefault(); items[0].focus(); }
      }
    });
    document.addEventListener("click",function(e){ if(nav.classList.contains("open") && !nav.contains(e.target) && !tog.contains(e.target)) setOpen(false,false); });
    nav.addEventListener("click",function(e){ var a=e.target.closest("a"); if(a&&a.getAttribute("href")&&a.getAttribute("href").indexOf("#")>-1&&nav.classList.contains("open")) setOpen(false,false); });
  }
  document.querySelectorAll("[data-drop]").forEach(function(d){
    var b=d.querySelector("button");
    b.addEventListener("click",function(e){ e.stopPropagation(); document.querySelectorAll("[data-drop].open").forEach(function(x){ if(x!==d){ x.classList.remove("open"); x.querySelector("button").setAttribute("aria-expanded","false"); } }); var o=d.classList.toggle("open"); b.setAttribute("aria-expanded",o?"true":"false"); });
  });
  document.addEventListener("click",function(){ document.querySelectorAll("[data-drop].open").forEach(function(d){ d.classList.remove("open"); d.querySelector("button").setAttribute("aria-expanded","false"); }); });
  document.addEventListener("keydown",function(e){ if(e.key==="Escape") document.querySelectorAll("[data-drop].open").forEach(function(d){ d.classList.remove("open"); }); });
})();

/* Form handling moved to /assets/js/finder.js (FormSubmit AJAX endpoint, honeypot, timing + interaction checks). */
