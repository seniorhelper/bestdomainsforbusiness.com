
(function(){
  var tog = document.querySelector("[data-navtog]"), nav = document.getElementById("nav");
  if(tog && nav){ tog.addEventListener("click", function(){ var o=nav.classList.toggle("open"); tog.setAttribute("aria-expanded",o?"true":"false"); }); }
  document.querySelectorAll("[data-drop]").forEach(function(d){
    var b=d.querySelector("button");
    b.addEventListener("click",function(e){ e.stopPropagation(); var o=d.classList.toggle("open"); b.setAttribute("aria-expanded",o?"true":"false"); });
  });
  document.addEventListener("click",function(){ document.querySelectorAll("[data-drop].open").forEach(function(d){ d.classList.remove("open"); d.querySelector("button").setAttribute("aria-expanded","false"); }); });
  document.addEventListener("keydown",function(e){ if(e.key==="Escape") document.querySelectorAll("[data-drop].open").forEach(function(d){ d.classList.remove("open"); }); });
})();

(function(){
  var READY = {}, TOUCHED = {};
  function ep(f){ return "https://formsubmit.co/" + atob(f.dataset.a) + String.fromCharCode(64) + atob(f.dataset.b); }
  document.querySelectorAll("form.form").forEach(function(f){
    var id = f.id;
    READY[id] = false; TOUCHED[id] = false;
    setTimeout(function(){ READY[id] = true; }, 3600);
    ["keydown","pointerdown"].forEach(function(ev){
      f.addEventListener(ev, function(){ TOUCHED[id] = true; }, {once:true});
    });
    f.addEventListener("submit", function(e){
      e.preventDefault();
      var stat = document.getElementById(id + "-stat");
      var hp = f.querySelector('input[name="_honey"]');
      if(hp && hp.value){ return; }
      if(!READY[id] || !TOUCHED[id]){ return; }
      var miss = null;
      f.querySelectorAll("[required]").forEach(function(el){
        if(!el.value.trim() && !miss) miss = el;
      });
      if(miss){ stat.className="fstat err"; stat.textContent="Please fill in the highlighted field."; miss.focus(); return; }
      var btn = f.querySelector('button[type="submit"]');
      btn.disabled = true; btn.textContent = "Sending…";
      stat.className = "fstat"; stat.textContent = "";
      fetch(ep(f), {method:"POST", body:new FormData(f), headers:{"Accept":"application/json"}})
        .then(function(r){
          if(r.ok){
            stat.className="fstat ok";
            stat.textContent="Got it — that came through. Someone will get back to you. If it is urgent, call 1-800-481-8638.";
            f.querySelectorAll("input:not([type=hidden]),select,textarea").forEach(function(el){el.value="";});
            btn.textContent="Sent";
          } else {
            stat.className="fstat err";
            stat.textContent="That did not go through. Please call 1-800-481-8638 and we will take it down by phone.";
            btn.disabled=false; btn.textContent="Try again";
          }
        })
        .catch(function(){
          stat.className="fstat err";
          stat.textContent="That did not go through. Please call 1-800-481-8638 and we will take it down by phone.";
          btn.disabled=false; btn.textContent="Try again";
        });
    });
  });
})();
