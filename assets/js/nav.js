
(function(){
  var tog = document.querySelector("[data-navtog]"), nav = document.getElementById("nav");
  function fit(){ if(!nav.classList.contains("open")) return; var h=nav.parentNode.getBoundingClientRect().bottom; nav.style.maxHeight=Math.max(240,window.innerHeight-h)+"px"; }
  if(tog && nav){
    tog.addEventListener("click", function(){ var o=nav.classList.toggle("open"); document.body.classList.toggle("nav-open",o); tog.setAttribute("aria-expanded",o?"true":"false"); tog.setAttribute("aria-label",o?"Close menu":"Menu"); if(o) fit(); else document.querySelectorAll("[data-drop].open").forEach(function(d){ d.classList.remove("open"); }); });
    window.addEventListener("resize", fit);
    document.addEventListener("keydown",function(e){ if(e.key==="Escape"&&nav.classList.contains("open")){ nav.classList.remove("open"); document.body.classList.remove("nav-open"); tog.setAttribute("aria-expanded","false"); tog.setAttribute("aria-label","Menu"); tog.focus(); } });
    nav.addEventListener("click",function(e){ var a=e.target.closest("a"); if(a&&a.getAttribute("href")&&a.getAttribute("href").indexOf("#")>-1&&nav.classList.contains("open")){ nav.classList.remove("open"); tog.setAttribute("aria-expanded","false"); } });
  }
  document.querySelectorAll("[data-drop]").forEach(function(d){
    var b=d.querySelector("button");
    b.addEventListener("click",function(e){ e.stopPropagation(); document.querySelectorAll("[data-drop].open").forEach(function(x){ if(x!==d){ x.classList.remove("open"); x.querySelector("button").setAttribute("aria-expanded","false"); } }); var o=d.classList.toggle("open"); b.setAttribute("aria-expanded",o?"true":"false"); });
  });
  document.addEventListener("click",function(){ document.querySelectorAll("[data-drop].open").forEach(function(d){ d.classList.remove("open"); d.querySelector("button").setAttribute("aria-expanded","false"); }); });
  document.addEventListener("keydown",function(e){ if(e.key==="Escape") document.querySelectorAll("[data-drop].open").forEach(function(d){ d.classList.remove("open"); }); });
})();

/* Form handling moved to /assets/js/finder.js (FormSubmit AJAX endpoint, honeypot, timing + interaction checks). */
