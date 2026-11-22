# -*- coding: utf-8 -*-
import io
s = io.open('index.html', encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, 'MISSING: ' + old[:70]
    s = s.replace(old, new, 1)

# CSS before </style>
NEWCSS = """
/* ---------- live status ---------- */
.statusrow{margin-top:18px;display:flex;justify-content:center}
.statuswrap{position:relative;display:inline-block}
.statuspill{display:inline-flex;align-items:center;gap:9px;background:rgba(255,255,255,.04);
  border:1px solid var(--line);border-radius:999px;padding:8px 18px;cursor:pointer;font:inherit;
  color:var(--paper);transition:border-color .25s}
.statuspill:hover{border-color:rgba(255,255,255,.32)}
.sdot{width:8px;height:8px;border-radius:50%;position:relative;flex:0 0 auto}
.sdot::after{content:"";position:absolute;inset:-4px;border-radius:50%;animation:pulse 2.2s ease-out infinite}
.s-online .sdot,.sdot.s-online{background:#3fbf6f;box-shadow:0 0 9px rgba(63,191,111,.75)}
.s-online .sdot::after,.sdot.s-online::after{border:1px solid rgba(63,191,111,.9)}
.s-updating .sdot,.sdot.s-updating{background:#d9a441;box-shadow:0 0 9px rgba(217,164,65,.75)}
.s-updating .sdot::after,.sdot.s-updating::after{border:1px solid rgba(217,164,65,.9)}
.s-offline .sdot,.sdot.s-offline{background:#d84343;box-shadow:0 0 9px rgba(216,67,67,.75)}
.s-offline .sdot::after,.sdot.s-offline::after{border:1px solid rgba(216,67,67,.9)}
@keyframes pulse{0%{transform:scale(.55);opacity:.75}100%{transform:scale(1.7);opacity:0}}
.statuspill .stext{font-size:11.5px;font-weight:800;letter-spacing:.24em;text-transform:uppercase}
.statuspop{position:absolute;z-index:70;top:calc(100% + 10px);left:50%;
  transform:translateX(-50%) translateY(6px);width:min(340px,84vw);background:#121216;
  border:1px solid var(--line);border-top:2px solid #555;padding:18px 20px;text-align:left;
  opacity:0;visibility:hidden;transition:opacity .25s,transform .25s,visibility .25s;
  box-shadow:0 18px 50px rgba(0,0,0,.6)}
.statuspop.on{opacity:1;visibility:visible;transform:translateX(-50%) translateY(0)}
.s-online .statuspop{border-top-color:#3fbf6f}
.s-updating .statuspop{border-top-color:#d9a441}
.s-offline .statuspop{border-top-color:#d84343}
.statuspop h4{display:flex;align-items:center;gap:9px;font-size:12.5px;font-weight:800;
  letter-spacing:.24em;text-transform:uppercase;margin:0 0 9px;color:#fff}
.statuspop .sdesc{color:var(--ash);font-size:13.5px;line-height:1.55;margin:0}
.statuspop .sptime{margin-top:11px;padding-top:11px;border-top:1px solid var(--line);
  font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:#6d6d78}
@media(max-width:640px){.statuspop{left:50%}}
"""
rep('</style>', NEWCSS + '</style>')

# hero: status pill under version line
rep('    <div class="hversion">Current build <b>v1.122.0</b> &middot; free to play</div>\n  </div>',
"""    <div class="hversion">Current build <b>v1.122.0</b> &middot; free to play</div>
    <div class="statusrow">
      <span class="statuswrap">
        <button class="statuspill s-updating" type="button" aria-haspopup="true"><span class="sdot"></span><span class="stext">Updating</span></button>
        <div class="statuspop"><h4><span class="sdot s-updating"></span><span class="sword">Updating</span></h4><p class="sdesc"></p><div class="sptime"></div></div>
      </span>
    </div>
  </div>""")

# launch box: same pill after the lv line
rep('    <div class="lv">Build v1.122.0 &middot; runs in your browser</div>',
"""    <div class="lv">Build v1.122.0 &middot; runs in your browser</div>
    <div class="statusrow" style="margin:14px 0 2px">
      <span class="statuswrap">
        <button class="statuspill s-updating" type="button" aria-haspopup="true"><span class="sdot"></span><span class="stext">Updating</span></button>
        <div class="statuspop"><h4><span class="sdot s-updating"></span><span class="sword">Updating</span></h4><p class="sdesc"></p><div class="sptime"></div></div>
      </span>
    </div>""")

# JS: config at the very top of the script
rep("""(function(){
  var nav=document.getElementById("top"),burger=document.getElementById("burger"),links=document.getElementById("navlinks");""",
"""(function(){
  /* ============================================================
     LIVE STATUS - EDIT THIS BLOCK ONLY
     status:     "online" | "updating" | "offline"
     message:    your own line, or "" to use the default for the status
     lastUpdated: when you changed it, e.g. "Nov 22, 2026"
     Everything on the site (both indicators + popups) reads this.
     ============================================================ */
  var STATUS={
    status:"updating",
    message:"Servers are down for an update while the new Story Mode build is finished. The test build stays playable meanwhile.",
    lastUpdated:"Nov 22, 2026"
  };
  var SMETA={
    online:{cls:"s-online",word:"Online",desc:"All systems operational. Shinobi Legacy is ready to play."},
    updating:{cls:"s-updating",word:"Updating",desc:"Shinobi Legacy is currently receiving updates. Please check back shortly."},
    offline:{cls:"s-offline",word:"Offline",desc:"Shinobi Legacy is currently unavailable."}
  };
  var meta=SMETA[STATUS.status]||SMETA.offline;
  document.querySelectorAll(".statuspill").forEach(function(pill){
    pill.classList.remove("s-online","s-updating","s-offline");
    pill.classList.add(meta.cls);
    pill.querySelector(".stext").textContent=meta.word;
    var pop=pill.parentNode.querySelector(".statuspop");
    pop.querySelector(".sdot").className="sdot "+meta.cls;
    pop.querySelector(".sword").textContent=meta.word;
    pop.querySelector(".sdesc").textContent=STATUS.message||meta.desc;
    pop.querySelector(".sptime").textContent="Last updated "+STATUS.lastUpdated+" \\u00b7 set manually by the developer";
    pill.addEventListener("click",function(e){
      e.stopPropagation();
      var wasOpen=pop.classList.contains("on");
      document.querySelectorAll(".statuspop.on").forEach(function(x){x.classList.remove("on")});
      if(!wasOpen)pop.classList.add("on");
    });
  });
  document.addEventListener("click",function(e){
    if(!e.target.closest(".statuswrap"))document.querySelectorAll(".statuspop.on").forEach(function(x){x.classList.remove("on")});
  });
  document.addEventListener("keydown",function(e){
    if(e.key==="Escape")document.querySelectorAll(".statuspop.on").forEach(function(x){x.classList.remove("on")});
  });

  var nav=document.getElementById("top"),burger=document.getElementById("burger"),links=document.getElementById("navlinks");""")
io.open('index.html','w',encoding='utf-8').write(s)
print('ok', len(s.encode('utf-8')))
