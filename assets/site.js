/* Shinobi Legacy official site — site.js v3.0.0 */
(function(){
  "use strict";

  /* ============================================================
     SITE GATE - EDIT THIS BLOCK ONLY
     on:     true shows the full-screen gate, false hides it (site visible)
     state:  "updating" | "testing" | "down"
     message: your own line, or "" to use the default for the state
     Tip: add ?dev=1 to the URL to see the real site while the gate is on.
     ============================================================ */
  var GATE={on:true,state:"updating",message:""};
  (function(){
    var g=document.getElementById("sitegate");if(!g)return;
    if(!GATE.on||location.search.indexOf("dev=1")>-1){g.style.display="none";return}
    document.body.classList.add("gatelock");
    var words={updating:"Updating",testing:"Testing",down:"Down for a while"};
    var subs={updating:"The site is getting an update right now. Check back shortly.",
              testing:"We\u2019re testing changes behind the scenes. Back soon.",
              down:"The site is down for a while. We\u2019ll be back soon."};
    var s=GATE.state||"updating";
    document.getElementById("gateState").textContent=words[s]||words.updating;
    document.getElementById("gateSub").textContent=GATE.message||subs[s]||subs.updating;
  })();

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

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
  document.querySelectorAll(".statuspill:not(.ubpill)").forEach(function(pill){
    pill.classList.remove("s-online","s-updating","s-offline");
    pill.classList.add(meta.cls);
    pill.querySelector(".stext").textContent=meta.word;
    var pop=pill.parentNode.querySelector(".statuspop");
    pop.querySelector(".sdot").className="sdot "+meta.cls;
    pop.querySelector(".sword").textContent=meta.word;
    pop.querySelector(".sdesc").textContent=STATUS.message||meta.desc;
    pop.querySelector(".sptime").textContent="Last updated "+STATUS.lastUpdated+" \u00b7 set manually by the developer";
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

  /* ============================================================
     LIFE UNBOUND LIVE STATUS - EDIT THIS BLOCK ONLY
     status:       "auto" (reads the game's own version file) | "online" | "updating" | "offline"
     knownVersion: the version you last announced on this site
     message:      your own line, or "" to use the default
     lastUpdated:  when you changed it, e.g. "Nov 22, 2026"
     ============================================================ */
  var UB={
    status:"auto",
    knownVersion:"1.4.3",
    message:"",
    lastUpdated:"Nov 24, 2026"
  };
  var UBMETA={
    online:{cls:"s-online",word:"Online",desc:"Life Unbound is live and playable."},
    updating:{cls:"s-updating",word:"Updating",desc:"A new version just shipped and is rolling out. Refresh the game in a few minutes."},
    offline:{cls:"s-offline",word:"Offline",desc:"Life Unbound is currently unavailable."}
  };
  (function(){
    var pills=document.querySelectorAll(".statuspill.ubpill");
    if(!pills.length)return;
    function ubApply(word,cls,desc,ptime){
      pills.forEach(function(pill){
        var pop=pill.parentNode.querySelector(".statuspop");
        pill.classList.remove("s-online","s-updating","s-offline");
        pill.classList.add(cls);
        pill.querySelector(".stext").textContent=word;
        pop.querySelector(".sdot").className="sdot "+cls;
        pop.querySelector(".sword").textContent=word;
        pop.querySelector(".sdesc").textContent=desc;
        pop.querySelector(".sptime").textContent=ptime;
      });
    }
    pills.forEach(function(pill){
      var pop=pill.parentNode.querySelector(".statuspop");
      pill.addEventListener("click",function(e){
        e.stopPropagation();
        var wasOpen=pop.classList.contains("on");
        document.querySelectorAll(".statuspop.on").forEach(function(x){x.classList.remove("on")});
        if(!wasOpen)pop.classList.add("on");
      });
    });
    if(UB.status==="auto"){
      fetch("https://trae5.github.io/shinobi-sprint/version.json?cb="+Date.now()).then(function(r){
        if(!r.ok)throw 0;
        return r.json();
      }).then(function(j){
        var v=(j&&(j.v||j.version))||"";
        var chip=document.querySelector("#unbound .uv");
        if(chip&&v)chip.textContent=chip.textContent.replace(/Version [0-9.]+/,"Version "+v);
        if(v&&UB.knownVersion&&v!==UB.knownVersion){
          ubApply(UBMETA.updating.word,UBMETA.updating.cls,UBMETA.updating.desc,"Live \u00b7 reads the game's version file");
        }else{
          ubApply(UBMETA.online.word,UBMETA.online.cls,UB.message||UBMETA.online.desc,"Live \u00b7 reads the game's version file");
        }
      }).catch(function(){
        ubApply(UBMETA.online.word,UBMETA.online.cls,UB.message||UBMETA.online.desc,"Live \u00b7 reads the game's version file");
      });
    }else{
      var m=UBMETA[UB.status]||UBMETA.offline;
      ubApply(m.word,m.cls,UB.message||m.desc,"Last updated "+UB.lastUpdated+" \u00b7 set manually by the developer");
    }
  })();

  /* ---------- nav ---------- */
  var nav=document.getElementById("top"),burger=document.getElementById("burger"),links=document.getElementById("navlinks");
  var hero=document.getElementById("home"),bg=document.getElementById("herowrap");
  document.getElementById("yr").textContent=new Date().getFullYear();

  function closeMenu(){links.classList.remove("open");burger.classList.remove("x");document.body.style.overflow="";}
  burger.addEventListener("click",function(){
    var open=links.classList.toggle("open");
    burger.classList.toggle("x",open);
    document.body.style.overflow=open?"hidden":"";
  });

  function anchorScroll(a){
    var href=a.getAttribute("href")||"";
    if(href.charAt(0)!=="#")return false;
    var t=null;
    try{t=document.querySelector(href)}catch(e){}
    if(!t)return false;
    try{t.scrollIntoView({behavior:reduced?"auto":"smooth",block:"start"})}catch(err){t.scrollIntoView()}
    if(history.replaceState)history.replaceState(null,"",href);else location.hash=href.slice(1);
    return true;
  }
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener("click",function(e){
      closeMenu();
      if(anchorScroll(a))e.preventDefault();
    });
  });

  function onScroll(){
    nav.classList.toggle("solid",window.scrollY>40);
    if(!reduced&&window.scrollY<window.innerHeight){
      bg.style.transform="translateY("+(window.scrollY*0.25)+"px)";
    }
  }
  window.addEventListener("scroll",onScroll,{passive:true});onScroll();

  /* ---------- hero embers ---------- */
  var emberBox=hero&&hero.querySelector(".embers");
  if(emberBox&&!reduced&&window.matchMedia("(min-width: 700px)").matches){
    for(var i=0;i<14;i++){
      var e=document.createElement("i");
      e.className="ember";
      e.style.left=(3+Math.random()*94)+"%";
      e.style.animationDuration=(9+Math.random()*12)+"s";
      e.style.animationDelay=(-Math.random()*18)+"s";
      e.style.transform="scale("+(0.6+Math.random()*1.1)+")";
      emberBox.appendChild(e);
    }
  }

  /* ---------- active section in nav ---------- */
  var secs=["home","world","game","clans","media","unbound","updates","roadmap","news","guide","playsec"];
  var secsEl=secs.map(function(id){return document.getElementById(id)});
  var io=new IntersectionObserver(function(es){
    es.forEach(function(en){
      if(en.isIntersecting){
        links.querySelectorAll("a").forEach(function(a){
          a.classList.toggle("active",a.getAttribute("href")==="#"+en.target.id);
        });
      }
    });
  },{rootMargin:"-45% 0px -50% 0px"});
  secsEl.forEach(function(s){if(s)io.observe(s)});

  /* ---------- reveal on scroll ---------- */
  var rio=new IntersectionObserver(function(es){
    es.forEach(function(en){if(en.isIntersecting){en.target.classList.add("in");rio.unobserve(en.target)}});
  },{threshold:.12});
  document.querySelectorAll(".reveal").forEach(function(el){rio.observe(el)});
  function sweep(){
    var vh=window.innerHeight;
    document.querySelectorAll(".reveal:not(.in)").forEach(function(el){
      var r=el.getBoundingClientRect();
      if(r.top<vh*0.94&&r.bottom>0)el.classList.add("in");
    });
  }
  var sweepT=setInterval(function(){
    sweep();
    if(!document.querySelector(".reveal:not(.in)"))clearInterval(sweepT);
  },600);sweep();

  /* ---------- villages ---------- */
  var tabs=document.getElementById("villtabs"),stage=document.getElementById("villstage");
  if(tabs&&stage){
    tabs.addEventListener("click",function(e){
      var b=e.target.closest("button");if(!b)return;
      tabs.querySelectorAll("button").forEach(function(x){x.classList.toggle("on",x===b)});
      stage.querySelectorAll(".vpanel").forEach(function(p){p.classList.toggle("on",p.dataset.v===b.dataset.v)});
    });
  }

  /* ---------- clan archive ---------- */
  var CLANS=[
   {n:"Uchiha",eye:true,a:["Ember Talon","Crimson Gaze Lock","Phoenix Wing Sweep","Inferno Crown"]},
   {n:"Hyuga",eye:true,a:["Air Palm Shot","Vein Seal","Hundred-Point Rush","Clear Sky Dome"]},
   {n:"Uzumaki",a:["Seal Chain Lash","Spiral Lance","Whirl Seal","Whirlpool Heart"]},
   {n:"Nara",a:["Shade Needle","Dusk Snare","Long Shadow Cut","Nightfall Field"]},
   {n:"Senju",a:["Rootspear","Thorn Cage","Verdant Mend","Forest Wall"]},
   {n:"Kaguya",a:["Marrow Bullet","Spine Lance","Ivory Thicket","Bone Shell"]},
   {n:"Kaze",a:["Gale Cutter","Wind Step","Cyclone Ring","Sky Splitter"]},
   {n:"Mori",a:["Leaf Dart","Moss Bind","Grove Bloom","Old Oak Guard"]},
   {n:"Tetsu",a:["Iron Fist Rush","Chain Hook","Steel Skin","Anvil Drop"]},
   {n:"Hoshino",a:["Star Shot","Comet Dash","Constellation Rain","Nova Heart"]},
   {n:"Raiko",a:["Spark Bolt","Static Net","Arc Lance","Thunderhead"]},
   {n:"Kuro",a:["Night Fang","Ink Blade","Shade Clones","Black Mist"]},
   {n:"Shirogane",a:["Frost Shard","Rime Snare","Silver Gale","Glacier Heart"]},
   {n:"Arashi",a:["Squall Bolt","Gust Shield","Tempest Dash","Hurricane Eye"]},
   {n:"Tsukino",a:["Moonbeam","Lunar Veil","Tide Pull","Crescent Rain"]},
   {n:"Ryujin",a:["Wyrm Fire","Dragon Claw","Scale Guard","Sky Dragon Roar"]},
   {n:"Amateru",a:["Sunspear","Dawn Mend","Solar Wheel","Noon Blaze"]},
   {n:"Ketsuryu",a:["Blood Needle","Crimson Chain","Vein Burst","Red Tide"]},
   {n:"Patel",a:["Thorn Petal","Rose Ward","Petal Twins","Garden Gale"]},
   {n:"Ventura",a:["Fold Shot","Gravity Lock","Phase Clones","Rift Rain"]},
   {n:"Akimichi",a:["Rolling Boulder","Iron Belly","Feast Recovery","Giant Palm"]},
   {n:"Inuzuka",a:["Claw Rush","Scent Snare","Hound Clones","Pack Howl"]},
   {n:"Aburame",a:["Beetle Shot","Carapace","Swarm Clones","Hive Cloud"]},
   {n:"Sarutobi",a:["Flame Shuriken","Smoke Ring","Staff Sweep","Hearth Fire"]},
   {n:"Hozuki",a:["Tide Bullet","Liquid Body","Riptide","Wave Crash"]},
   {n:"Yuki",a:["Snow Dart","Mirror Twins","Blizzard Ring","Ice Bloom"]},
   {n:"Fuma",a:["Spinning Star","Blade Wire","Steel Twins","Kunai Rain"]},
   {n:"Otsutsuki",eye:true,a:["Moon Orb","Heavenly Seal","Void Pull","Celestial Palm"]},
   {n:"Karma",a:["Seal Spike","Mark of Ruin","Portal Strike","Karma Flare"]},
   {n:"Shiba",a:["Spirit Rocket","Festival Ward","Spark Shower","Lantern Burst"]},
   {n:"Kuchiki",a:["Blossom Blade","Noble Step","Petal Veil","Sakura Gale"]},
   {n:"Shih\u014din",a:["Flash Kick","Storm Mantle","Swift Clones","Thunder Palm"]},
   {n:"Shih\u014din Royal",a:["Royal Spark","Crown Step","Sovereign Mantle","Throne Thunder"]},
   {n:"Kurosaki",a:["Crescent Edge","Void Burst","Twin Soul","Black Edge Nova"]},
   {n:"Ishida",a:["Light Arrow","Spirit Snare","Silver Vein","Arrow Storm"]},
   {n:"Royal Soul",a:["Soul Lance","Crown Pressure","Regal Mend","Royal Decree"]},
   {n:"Vex",a:["Void Shard","Null Snare","Void Twins","Collapse"]},
   {n:"Ryukami",a:["Star Dragon Fang","Heaven Ward","Celestial Rain","Dragon Sun"]},
   {n:"Goku Clan",locked:true,tag:"Secret Mythic",note:"Hidden in the world, never rollable. Its arts stay classified until you find it in-game."}
  ];
  var KEYS=["Shift + 1","Shift + 2","Shift + 3","Shift + 4"];
  var LVL=["Mastery 1","Mastery 3","Mastery 5","Mastery 7"];
  var CLIST=document.getElementById("clanlist"),CNAME=document.getElementById("cs-name"),
      CTAG=document.getElementById("cs-tag"),CARTS=document.getElementById("cs-arts"),
      CNOTE=document.getElementById("cs-note"),CQ=document.getElementById("clanq"),
      CCHIPS=document.getElementById("clanchips");
  var cFilter="all",cQuery="",current=null;
  function artCell(key,name,lvl){
    var d=document.createElement("div");d.className="art";
    var k=document.createElement("span");k.className="key";k.textContent=key;
    var b=document.createElement("b");b.textContent=name;
    var m=document.createElement("span");m.textContent=lvl;
    d.appendChild(k);d.appendChild(b);d.appendChild(m);
    return d;
  }
  function showClan(c){
    current=c;
    CNAME.textContent=c.n;
    CTAG.textContent=c.locked?(c.tag||"Classified"):"Clan arts";
    CTAG.classList.toggle("classified",!!c.locked);
    CARTS.textContent="";
    for(var i=0;i<4;i++){
      CARTS.appendChild(artCell(KEYS[i],c.locked?"Classified":c.a[i],LVL[i]));
    }
    CNOTE.textContent=c.note||"";
    CNOTE.style.display=c.note?"":"none";
  }
  function clanMatches(c){
    if(cFilter==="eye"&&!c.eye)return false;
    if(cFilter==="secret"&&!c.locked)return false;
    if(cQuery&&c.n.toLowerCase().indexOf(cQuery)<0)return false;
    return true;
  }
  function buildClans(){
    CLIST.textContent="";
    var shown=0;
    CLANS.forEach(function(c){
      if(!clanMatches(c))return;
      shown++;
      var b=document.createElement("button");
      b.textContent=c.n;
      if(c.locked)b.classList.add("locked");
      if(c===current)b.classList.add("on");
      b.addEventListener("click",function(){
        CLIST.querySelectorAll("button").forEach(function(x){x.classList.toggle("on",x===b)});
        showClan(c);
      });
      CLIST.appendChild(b);
    });
    if(!shown){
      var d=document.createElement("div");
      d.className="cempty";
      d.textContent="No clans match that search.";
      CLIST.appendChild(d);
    }
  }
  if(CLIST&&CNAME){
    current=CLANS[0];
    buildClans();
    showClan(current);
    if(CQ)CQ.addEventListener("input",function(){cQuery=CQ.value.trim().toLowerCase();buildClans()});
    if(CCHIPS)CCHIPS.addEventListener("click",function(e){
      var b=e.target.closest("button");if(!b)return;
      cFilter=b.dataset.f;
      CCHIPS.querySelectorAll("button").forEach(function(x){x.classList.toggle("on",x===b)});
      buildClans();
    });
  }

  /* ---------- update log search ---------- */
  var upq=document.getElementById("updq");
  if(upq){
    var items=[].slice.call(document.querySelectorAll("#uptimeline .titem"));
    upq.addEventListener("input",function(){
      var q=upq.value.trim().toLowerCase();
      items.forEach(function(t){
        t.style.display=!q||t.textContent.toLowerCase().indexOf(q)>-1?"":"none";
      });
    });
  }

  /* ---------- gallery lightbox ---------- */
  var shots=[].slice.call(document.querySelectorAll(".gal figure:not(.slot)"));
  var lb=document.getElementById("lightbox"),lbimg=document.getElementById("lbimg"),lbcap=document.getElementById("lbcap"),idx=0;
  function show(i){idx=(i+shots.length)%shots.length;var im=shots[idx].querySelector("img");lbimg.src=im.src;lbimg.alt=im.alt;lbcap.textContent=shots[idx].querySelector("figcaption").textContent}
  shots.forEach(function(f,i){f.addEventListener("click",function(){show(i);lb.classList.add("on")})});
  document.getElementById("lb-x").addEventListener("click",function(){lb.classList.remove("on")});
  document.getElementById("lb-prev").addEventListener("click",function(){show(idx-1)});
  document.getElementById("lb-next").addEventListener("click",function(){show(idx+1)});
  lb.addEventListener("click",function(e){if(e.target===lb)lb.classList.remove("on")});
  document.addEventListener("keydown",function(e){
    if(!lb.classList.contains("on"))return;
    if(e.key==="Escape")lb.classList.remove("on");
    if(e.key==="ArrowLeft")show(idx-1);
    if(e.key==="ArrowRight")show(idx+1);
  });

  /* ---------- game launcher ---------- */
  var loadBtn=document.getElementById("loadgame"),frame=document.getElementById("gameframe"),wrap=document.getElementById("gamewrap"),st=document.getElementById("loadst"),loading=false;
  if(loadBtn){
    loadBtn.addEventListener("click",function(){
      if(loading)return;loading=true;
      wrap.classList.remove("on");frame.style.display="none";
      document.getElementById("launchload").style.display="flex";
      st.textContent="Loading the world";
      frame.src=frame.dataset.src;
      var waited=0;
      var t=setInterval(function(){
        waited+=400;
        try{if(frame.contentDocument&&frame.contentDocument.readyState==="complete"&&waited>1400){done();}}
        catch(err){if(waited>2200){done();}}
        if(waited>9000){done();}
      },400);
      function done(){
        clearInterval(t);
        st.textContent="Enter the world";
        setTimeout(function(){
          document.getElementById("launchload").style.display="none";
          frame.style.display="block";wrap.classList.add("on");
        },500);
      }
    });
  }

  /* ---------- enter the world ---------- */
  var veil=document.getElementById("veil");
  if(veil){
    var vst=document.getElementById("veilst"),vbar=document.getElementById("veilbar");
    var msgs=["Opening the gates","Weaving chakra threads","Preparing the launch bay"];
    document.getElementById("enterworld").addEventListener("click",function(){
      if(veil.classList.contains("on"))return;
      veil.classList.add("on");document.body.classList.add("veillock");
      var i=0;
      var t1=setInterval(function(){i=(i+1)%msgs.length;vst.textContent=msgs[i]},850);
      var pr=0;
      var t2=setInterval(function(){pr=Math.min(94,pr+9+Math.random()*12);vbar.style.width=pr+"%"},190);
      setTimeout(function(){
        clearInterval(t1);clearInterval(t2);vbar.style.width="100%";
        setTimeout(function(){
          veil.classList.remove("on");document.body.classList.remove("veillock");
          var target=document.getElementById("playsec");
          if(target)target.scrollIntoView({behavior:"smooth"});
          var lb2=document.getElementById("loadgame");
          if(lb2){lb2.classList.add("pulse");setTimeout(function(){lb2.classList.remove("pulse")},3600)}
        },420);
      },2400);
    });
    document.addEventListener("keydown",function(e){
      if(e.key==="Escape"&&veil.classList.contains("on")){veil.classList.remove("on");document.body.classList.remove("veillock")}
    });
  }

  /* ---------- news: live from the community hub ---------- */
  (function(){
    var grid=document.getElementById("newsgrid");if(!grid)return;
    var NURL="https://firestore.googleapis.com/v1/projects/shinobi-life-unbound/databases/(default)/documents/community_announcements?pageSize=12&key=AIzaSyA6EnB41g34TnhhLNJcx8OA2vmTrShwoi4";
    var filter="all";
    function esc(x){return String(x||"").replace(/[&<>"']/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]})}
    function ago(iso){var t=new Date(iso).getTime();if(!t)return"";var d=Math.floor((Date.now()-t)/1000);if(d<0)d=0;if(d<3600)return Math.max(1,Math.floor(d/60))+" min ago";if(d<86400)return Math.floor(d/3600)+" h ago";var days=Math.floor(d/86400);return days===1?"yesterday":days+" days ago"}
    function gname(g){return g==="legacy"?"Shinobi Legacy":g==="unbound"?"Life Unbound":g==="both"?"Both games":g||"News"}
    var ALL=[];
    function passes(a){return filter==="all"||a.game===filter||(filter==="patch"&&a.type==="Patch notes")||(filter==="event"&&a.type==="Event")}
    function render(){
      var list=ALL.filter(passes).slice(0,9);
      if(!list.length){grid.innerHTML='<div class="newsempty">Nothing here yet. When the developer posts news, it lands here.</div>';return}
      grid.innerHTML=list.map(function(a){
        return '<article class="ncard"><div class="top"><h4>'+esc(a.title)+'</h4><div>'+(a.type?'<span class="nbadge">'+esc(a.type)+"</span>":"")+'<span class="nbadge">'+esc(gname(a.game))+'</span></div></div>'
          +(a.image?'<img src="'+esc(a.image)+'" alt="" loading="lazy" onerror="this.style.display=\'none\'">':"")
          +'<p>'+esc(a.body.length>320?a.body.slice(0,320)+"\u2026":a.body)+'</p><div class="nwhen">'+esc(a.author||"Developer")+" \u00b7 "+esc(ago(a.when))+"</div></article>";
      }).join("");
    }
    document.getElementById("nchips").addEventListener("click",function(e){
      var b=e.target.closest("button");if(!b)return;
      filter=b.dataset.f;
      document.querySelectorAll("#nchips button").forEach(function(x){x.classList.toggle("on",x===b)});
      render();
    });
    fetch(NURL).then(function(r){return r.json()}).then(function(j){
      ALL=(j.documents||[]).map(function(d){var f=d.fields||{};
        function val(k){var v=f[k];if(!v)return"";return v.stringValue!==undefined?v.stringValue:(v.integerValue!==undefined?v.integerValue:"")}
        return{title:val("title"),body:val("body"),type:val("type"),game:val("game"),image:val("image"),when:val("when"),author:val("author"),hidden:f.hidden&&f.hidden.booleanValue};
      }).filter(function(a){return a.title&&!a.hidden})
        .sort(function(a,b){return new Date(b.when)-new Date(a.when)});
      render();
    }).catch(function(){grid.innerHTML='<div class="newsempty">Couldn\u2019t load the news feed right now. Refresh in a minute.</div>'});
  })();

  /* ---------- event countdown - EDIT THIS BLOCK ONLY ---------- */
  (function(){
    var EVENT={title:"",iso:"",url:""}; /* set iso like "2026-12-05T18:00:00-06:00" to show the countdown */
    var box=document.getElementById("countdown");if(!box||!EVENT.iso)return;
    var t=new Date(EVENT.iso).getTime();if(!t)return;
    box.hidden=false;
    document.getElementById("cdtitle").textContent=EVENT.title||"Event incoming";
    var lk=document.getElementById("cdlink");if(EVENT.url){lk.hidden=false;lk.href=EVENT.url}
    function tick(){
      var s=Math.max(0,Math.floor((t-Date.now())/1000));
      var d=Math.floor(s/86400),h=Math.floor(s%86400/3600),m=Math.floor(s%3600/60);
      function pad(n){return(n<10?"0":"")+n}
      document.getElementById("cddigits").innerHTML=
        "<div><b>"+d+"</b><span>days</span></div><div><b>"+pad(h)+"</b><span>hrs</span></div><div><b>"+pad(m)+"</b><span>min</span></div><div><b>"+pad(s%60)+"</b><span>sec</span></div>";
      if(!s){clearInterval(iv);document.getElementById("cdtitle").textContent="It's happening now"}
    }
    tick();var iv=setInterval(tick,1000);
  })();

  /* ---------- guide: mirror the live status ---------- */
  (function(){
    var el=document.getElementById("guidestat");if(!el)return;
    var pill=document.querySelector(".statuspill:not(.ubpill)");
    var cls=(pill&&pill.className.match(/s-(online|updating|offline)/)||[])[1]||"updating";
    var words={online:"Online",updating:"Updating",offline:"Offline"};
    el.innerHTML='<span class="sdot s-'+cls+'"></span>Shinobi Legacy \u00b7 '+(words[cls]||"Updating");
  })();
})();
