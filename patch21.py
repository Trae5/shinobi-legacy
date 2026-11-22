# -*- coding: utf-8 -*-
import io
s = io.open('index.html', encoding='utf-8').read()
def rep(old, new, once=True):
    global s
    assert old in s, 'MISSING: ' + old[:70]
    if once: s = s.replace(old, new, 1)
    else: s = s.replace(old, new)

# 1) palette: add gold
rep("--crimson:#a8112d; --crimson-hi:#c81636; --line:rgba(255,255,255,.09);",
    "--crimson:#a8112d; --crimson-hi:#c81636; --gold:#c8a24a; --gold-dim:rgba(200,162,74,.55); --line:rgba(255,255,255,.09);")

# 2) hero bg kenburns + wrapper
rep("#herobg{position:absolute;inset:-12% 0;background:url('assets/final-form.jpg') center 30%/cover no-repeat;will-change:transform}",
"""#herowrap{position:absolute;inset:-12% 0;will-change:transform}
#herobg{position:absolute;inset:0;background:url('assets/final-form.jpg') center 30%/cover no-repeat;transform-origin:50% 38%;animation:kenburns 38s ease-in-out infinite alternate}
@keyframes kenburns{from{transform:scale(1)}to{transform:scale(1.08)}}""")

# 3) new CSS appended before </style>
NEWCSS = """
/* ---------- v2.1 the awakening ---------- */
section.block{overflow:hidden}
section.block::before{content:attr(data-kanji);position:absolute;top:clamp(24px,5vw,64px);right:1%;
  font-family:var(--serif);font-weight:900;font-size:clamp(130px,20vw,260px);line-height:1;opacity:.045;
  pointer-events:none;color:#fff;z-index:0}
.wrap{position:relative;z-index:1}
.kicker .num{color:var(--gold);margin-right:12px;font-weight:800}
.hanko{width:40px;height:40px;background:var(--crimson);color:#fff;display:flex;align-items:center;justify-content:center;
  font-family:var(--serif);font-weight:900;font-size:20px;margin:0 auto 22px;box-shadow:0 6px 24px rgba(168,17,45,.35)}
.hero-in h1 em{color:#e33}
.tagline b{color:var(--gold);font-weight:inherit}

/* clans */
.clanwrap{display:grid;grid-template-columns:minmax(260px,340px) 1fr;gap:1px;background:var(--line);border:1px solid var(--line)}
@media(max-width:880px){.clanwrap{grid-template-columns:1fr}}
.clanlist{background:var(--charcoal);display:flex;flex-wrap:wrap;gap:6px;padding:18px;align-content:flex-start;
  max-height:600px;overflow:auto}
@media(max-width:880px){.clanlist{max-height:none}}
.clanlist button{background:#0d0d11;border:1px solid var(--line);color:var(--ash);cursor:pointer;font:inherit;
  font-size:13px;font-weight:700;letter-spacing:.06em;padding:8px 13px;transition:all .25s}
.clanlist button:hover{color:#fff;border-color:rgba(255,255,255,.35)}
.clanlist button.on{color:#fff;border-color:var(--crimson);background:rgba(168,17,45,.16)}
.clanlist button.locked{border-style:dashed;color:#8d8d99}
.clanstage{background:var(--charcoal);padding:clamp(26px,4vw,44px);position:relative;min-height:420px}
.clanstage::before{content:"封";position:absolute;right:4%;bottom:2%;font-family:var(--serif);
  font-size:clamp(120px,16vw,220px);font-weight:900;opacity:.05;pointer-events:none;color:#fff}
.cs-head{display:flex;align-items:baseline;gap:16px;flex-wrap:wrap;border-bottom:1px solid var(--line);
  padding-bottom:16px;margin-bottom:22px;position:relative;z-index:1}
.cs-head h3{font-size:clamp(26px,3.6vw,40px);font-weight:900;letter-spacing:.04em}
.cs-arts{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);border:1px solid var(--line);position:relative;z-index:1}
@media(max-width:640px){.cs-arts{grid-template-columns:1fr}}
.cs-arts .art{background:#0d0d11;padding:18px 20px;position:relative}
.cs-arts .art .key{position:absolute;top:14px;right:16px;color:var(--gold);font-size:11px;letter-spacing:.18em;text-transform:uppercase}
.cs-arts .art b{display:block;font-size:16.5px;color:#fff;margin:6px 0 4px;padding-right:80px}
.cs-arts .art span{color:var(--ash);font-size:12px;letter-spacing:.16em;text-transform:uppercase}
.cs-note{color:var(--ash);font-size:14.5px;margin-top:20px;max-width:60ch;position:relative;z-index:1}
.clannotes{border:1px solid var(--line);border-left:3px solid var(--gold);background:var(--charcoal);
  padding:22px 26px;margin-top:26px;color:var(--ash);font-size:14.5px}
.clannotes p+p{margin-top:10px}
.pill.classified{border-color:rgba(200,22,54,.6);color:#ff7d92;background:rgba(168,17,45,.1)}

/* media future slot */
.gal figure.slot{border:1px dashed rgba(255,255,255,.16);background:rgba(255,255,255,.02);
  display:flex;align-items:center;justify-content:center;cursor:default;min-height:130px}
.gal figure.slot span{color:#6d6d78;font-size:11.5px;letter-spacing:.22em;text-transform:uppercase;text-align:center;padding:12px}
.gal figure.slot:hover{border-color:rgba(255,255,255,.26)}

/* developer */
.devlinks{display:flex;gap:10px;flex-wrap:wrap}
.devlinks a{border:1px solid var(--line);color:var(--paper);text-decoration:none;font-size:13px;font-weight:700;
  letter-spacing:.14em;text-transform:uppercase;padding:13px 22px;transition:all .25s;background:rgba(255,255,255,.02)}
.devlinks a:hover{border-color:var(--gold-dim);color:#fff;background:rgba(200,162,74,.07)}

/* footer glow */
footer{position:relative;overflow:hidden}
footer .wrap{position:relative;z-index:1}
.fglow{position:absolute;left:50%;bottom:-140px;transform:translateX(-50%);width:130%;height:280px;
  background:radial-gradient(50% 100% at 50% 100%,rgba(168,17,45,.22),transparent 70%);pointer-events:none}
.fv{margin-top:14px;color:var(--gold);font-size:11.5px;letter-spacing:.3em;text-transform:uppercase}
"""
rep('</style>', NEWCSS + '</style>')

# 4) nav brandmark + links
rep('<span class="brandmark">Official Site</span>',
    '<span class="brandmark">Official Site &middot; v2.1 The Awakening</span>')
rep("""    <a href="#home">Home</a>
    <a href="#game">The Game</a>
    <a href="#world">World</a>
    <a href="#updates">Updates</a>
    <a href="#roadmap">Roadmap</a>
    <a href="#media">Media</a>
    <a href="#playsec" class="play">Play</a>""",
"""    <a href="#home">Home</a>
    <a href="#world">The World</a>
    <a href="#game">Features</a>
    <a href="#clans">Clans</a>
    <a href="#media">Media</a>
    <a href="#updates">Updates</a>
    <a href="#playsec" class="play">Play</a>""")

# 5) hero
rep('  <div id="herobg"></div>', '  <div id="herowrap"><div id="herobg"></div></div>')
rep("""  <div class="hero-in">
    <div class="kicker">A 3D Ninja Browser MMORPG</div>
    <h1>SHINOBI <em>LEGACY</em></h1>
    <div class="tagline">YOUR LEGACY BEGINS HERE.</div>
    <div class="btnrow">
      <a class="btn" href="#playsec">Enter the World</a>
      <a class="btn ghost" href="#game">Explore the Game</a>
    </div>
    <div class="hversion">Current build <b>v1.122.0</b> &middot; free to play</div>
  </div>""",
"""  <div class="hero-in">
    <div class="hanko" aria-hidden="true">忍</div>
    <div class="kicker">A 3D Ninja Browser MMORPG</div>
    <h1>SHINOBI <em>LEGACY</em></h1>
    <div class="tagline">Forge Your Legacy.</div>
    <div class="btnrow">
      <a class="btn" href="https://shinobi-legacy.sites.tab.bot" target="_blank" rel="noopener">Play Now</a>
      <a class="btn ghost" href="#world">Explore</a>
    </div>
    <div class="hversion">Current build <b>v1.122.0</b> &middot; free to play</div>
  </div>""")

# 6) section kanji + numbered kickers
rep('<section class="block" id="game"><div class="wrap">',
    '<section class="block" id="game" data-kanji="闘"><div class="wrap">')
rep('<section class="block" id="world"><div class="wrap">',
    '<section class="block" id="world" data-kanji="界"><div class="wrap">')
rep('<section class="block" id="updates"><div class="wrap">',
    '<section class="block" id="updates" data-kanji="史"><div class="wrap">')
rep('<section class="block" id="roadmap"><div class="wrap">',
    '<section class="block" id="roadmap" data-kanji="道"><div class="wrap">')
rep('<section class="block" id="media"><div class="wrap">',
    '<section class="block" id="media" data-kanji="影"><div class="wrap">')
rep('<section class="block" id="playsec"><div class="wrap">',
    '<section class="block" id="playsec" data-kanji="戦"><div class="wrap">')
rep('<span class="kicker">The World</span>', '<span class="kicker"><b class="num">01</b>The World</span>')
rep('<span class="kicker">The Game</span>', '<span class="kicker"><b class="num">02</b>Features</span>')
rep('<span class="kicker">Media</span>', '<span class="kicker"><b class="num">04</b>Media</span>')
rep('<span class="kicker">Update Log</span>', '<span class="kicker"><b class="num">05</b>Update Log</span>')
rep('<span class="kicker">Roadmap</span>', '<span class="kicker"><b class="num">06</b>Roadmap</span>')
rep('<span class="kicker">Enter</span>', '<span class="kicker"><b class="num">08</b>Enter</span>')

# 7) clans section before UPDATES
CLANS_HTML = u"""<!-- CLANS -->
<section class="block" id="clans" data-kanji="族"><div class="wrap">
  <div class="sechead reveal">
    <span class="kicker"><b class="num">03</b>Clan Archive</span>
    <h2>Choose your <em>bloodline.</em></h2>
    <p>The real clan bar, straight from the game: every clan carries its own four clan arts on Shift+1 through Shift+4, unlocked as clan mastery grows. Select a clan to read its arts.</p>
    <div class="rule"></div>
  </div>
  <div class="clanwrap reveal">
    <div class="clanlist" id="clanlist" aria-label="Select a clan"></div>
    <div class="clanstage" id="clanstage">
      <div class="cs-head"><h3 id="cs-name"></h3><span class="pill" id="cs-tag">Clan arts</span></div>
      <div class="cs-arts" id="cs-arts"></div>
      <p class="cs-note" id="cs-note"></p>
    </div>
  </div>
  <div class="clannotes reveal">
    <p>Keys: Shift+1 to Shift+4. Arts unlock at clan mastery 1 / 3 / 5 / 7. Rin and the pack clans (Gojo, Toji, Jin-Woo, Anos, Rimuru) keep their own bars, with Gojo and Toji arriving in v1.121.0.</p>
    <p>Every clan eye is locked to its home clan: the Uchiha Sharingan, the Hyuga Byakugan, the Otsutsuki Rinnegan and Tenseigan, the Gojo Six Eyes and more, each with real abilities that drain chakra while they're active.</p>
  </div>
</div></section>

<!-- UPDATES -->"""
rep('\n<!-- UPDATES -->', '\n' + CLANS_HTML)

# 8) media future slot
rep("""    <figure><img src="assets/title-card.jpg" alt="Shinobi Legacy title card" loading="lazy"><figcaption>Title card</figcaption></figure>
  </div>""",
"""    <figure><img src="assets/title-card.jpg" alt="Shinobi Legacy title card" loading="lazy"><figcaption>Title card</figcaption></figure>
    <figure class="slot"><span>New captures land here as new content ships</span></figure>
  </div>""")

# 9) developer section before PLAY
DEV_HTML = u"""<!-- DEVELOPER -->
<section class="block" id="dev" data-kanji="忍"><div class="wrap">
  <div class="sechead reveal">
    <span class="kicker"><b class="num">07</b>Developer</span>
    <h2>Built by <em>Trae.</em></h2>
    <p>Shinobi Legacy is built and run by Trae: the world, the systems and every piece of 3D gear. Official project links below.</p>
    <div class="rule"></div>
  </div>
  <div class="devlinks reveal">
    <a href="https://github.com/trae5" target="_blank" rel="noopener">GitHub &mdash; Trae5</a>
    <a href="https://github.com/trae5/shinobi-legacy" target="_blank" rel="noopener">Website source</a>
    <a href="https://www.tomo.ai/pages/d45b682c1a2836a0d12f359722a3f50aa274f0de5c4daee291cc8c7722e1c39e" target="_blank" rel="noopener">Bug list</a>
    <a href="https://trae5.github.io/shinobi-sprint/" target="_blank" rel="noopener">Test build</a>
  </div>
</div></section>

<!-- PLAY -->"""
rep('\n<!-- PLAY -->', '\n' + DEV_HTML)

# 10) footer
fstart = s.index('<footer>'); fend = s.index('</footer>') + len('</footer>')
NEWFOOT = u"""<footer><div class="wrap">
  <div class="fglow" aria-hidden="true"></div>
  <div class="fgrid">
    <div>
      <div class="flogo">SHINOBI <em>LEGACY</em></div>
      <p>Forge your legacy. A 3D ninja browser MMORPG, built and run by Trae.</p>
      <div class="fv">Website v2.1 &middot; The Awakening</div>
    </div>
    <div class="fcol">
      <b>Site</b>
      <a href="#world">The World</a>
      <a href="#game">Features</a>
      <a href="#clans">Clans</a>
      <a href="#media">Media</a>
      <a href="#updates">Updates</a>
      <a href="#roadmap">Roadmap</a>
    </div>
    <div class="fcol">
      <b>Play</b>
      <a href="#playsec">Launch the game</a>
      <a href="https://shinobi-legacy.sites.tab.bot" target="_blank" rel="noopener">Main game</a>
      <a href="https://trae5.github.io/shinobi-sprint/" target="_blank" rel="noopener">Test build</a>
      <b style="margin-top:18px">Project</b>
      <a href="https://github.com/trae5" target="_blank" rel="noopener">GitHub</a>
      <a href="https://www.tomo.ai/pages/d45b682c1a2836a0d12f359722a3f50aa274f0de5c4daee291cc8c7722e1c39e" target="_blank" rel="noopener">Bug list</a>
    </div>
  </div>
  <div class="fbase">
    <span>&copy; <span id="yr"></span> Shinobi Legacy</span>
    <span>Game build v1.122.0</span>
  </div>
</div></footer>"""
s = s[:fstart] + NEWFOOT + s[fend:]

# 11) JS patches
rep('var hero=document.getElementById("home"),bg=document.getElementById("herobg");',
    'var hero=document.getElementById("home"),bg=document.getElementById("herowrap");')
rep('var secs=["home","game","world","updates","roadmap","media","playsec"];',
    'var secs=["home","world","game","clans","media","updates","roadmap","dev","playsec"];')
rep('var shots=[].slice.call(document.querySelectorAll(".gal figure"));',
    'var shots=[].slice.call(document.querySelectorAll(".gal figure:not(.slot)"));')

# 12) clan archive JS, inserted before final })();  (game launcher block end)
CLAN_JS = u"""
  // clan archive
  var CLANS=[
   {n:"Uchiha",a:["Ember Talon","Crimson Gaze Lock","Phoenix Wing Sweep","Inferno Crown"]},
   {n:"Hyuga",a:["Air Palm Shot","Vein Seal","Hundred-Point Rush","Clear Sky Dome"]},
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
   {n:"Otsutsuki",a:["Moon Orb","Heavenly Seal","Void Pull","Celestial Palm"]},
   {n:"Karma",a:["Seal Spike","Mark of Ruin","Portal Strike","Karma Flare"]},
   {n:"Shiba",a:["Spirit Rocket","Festival Ward","Spark Shower","Lantern Burst"]},
   {n:"Kuchiki",a:["Blossom Blade","Noble Step","Petal Veil","Sakura Gale"]},
   {n:"Shihōin",a:["Flash Kick","Storm Mantle","Swift Clones","Thunder Palm"]},
   {n:"Shihōin Royal",a:["Royal Spark","Crown Step","Sovereign Mantle","Throne Thunder"]},
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
      CNOTE=document.getElementById("cs-note");
  function artCell(key,name,lvl){
    var d=document.createElement("div");d.className="art";
    var k=document.createElement("span");k.className="key";k.textContent=key;
    var b=document.createElement("b");b.textContent=name;
    var m=document.createElement("span");m.textContent=lvl;
    d.appendChild(k);d.appendChild(b);d.appendChild(m);
    return d;
  }
  function showClan(c){
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
  CLANS.forEach(function(c){
    var b=document.createElement("button");
    b.textContent=c.n;
    if(c.locked)b.classList.add("locked");
    b.addEventListener("click",function(){
      CLIST.querySelectorAll("button").forEach(function(x){x.classList.toggle("on",x===b)});
      showClan(c);
    });
    CLIST.appendChild(b);
    if(c===CLANS[0]){b.classList.add("on");showClan(c);}
  });
"""
rep("""    }
  });
})();""", """    }
  });
""" + CLAN_JS + "})();")

io.open('index.html','w',encoding='utf-8').write(s)
print('patched ok, bytes:', len(s.encode('utf-8')))
