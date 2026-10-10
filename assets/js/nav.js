
(function(){
  var tog = document.querySelector("[data-navtog]"), nav = document.getElementById("nav");
  if(tog && nav){ tog.addEventListener("click", function(){ var o=nav.classList.toggle("open"); tog.setAttribute("aria-expanded",o?"true":"false"); if(!o) document.querySelectorAll("[data-drop].open").forEach(function(d){ d.classList.remove("open"); }); }); }
  document.querySelectorAll("[data-drop]").forEach(function(d){
    var b=d.querySelector("button");
    b.addEventListener("click",function(e){ e.stopPropagation(); document.querySelectorAll("[data-drop].open").forEach(function(x){ if(x!==d){ x.classList.remove("open"); x.querySelector("button").setAttribute("aria-expanded","false"); } }); var o=d.classList.toggle("open"); b.setAttribute("aria-expanded",o?"true":"false"); });
  });
  document.addEventListener("click",function(){ document.querySelectorAll("[data-drop].open").forEach(function(d){ d.classList.remove("open"); d.querySelector("button").setAttribute("aria-expanded","false"); }); });
  document.addEventListener("keydown",function(e){ if(e.key==="Escape") document.querySelectorAll("[data-drop].open").forEach(function(d){ d.classList.remove("open"); }); });
})();

/* Form handling moved to /assets/js/finder.js (FormSubmit AJAX endpoint, honeypot, timing + interaction checks). */
