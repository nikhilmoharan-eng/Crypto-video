"""Crypto Stories EP 01 · Bitcoin Pizza Day — premium purple style (HyperFrames).

Caption blocks are stacked lines: s = small regular, b = big semibold white, g = big gradient.
Each line reveals word by word inside its [start, end] window.
"""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 59.2

BLOCKS = [  # (start, end, [(style, text, t0, t1), ...])
    (0.0, 6.2, [("s", "22 May 2010.", 0.0, 1.7), ("s", "Florida mein ek programmer ne", 2.8, 4.3), ("b", "2 pizza", 4.64, 5.2), ("s", "order kiye.", 5.2, 5.8)]),
    (6.2, 9.9, [("s", "Aur payment kiya…", 6.49, 7.33), ("g", "10,000 BTC mein.", 7.76, 9.25)]),
    (9.9, 12.9, [("s", "Uska naam tha,", 10.11, 10.88), ("b", "Laszlo Hanyecz.", 11.11, 12.34)]),
    (12.9, 20.1, [("s", "Online forum pe likha:", 13.09, 14.69), ("b", "\"2 pizza bhejo,", 15.39, 17.02), ("g", "10,000 BTC lo.\"", 17.38, 19.53)]),
    (20.1, 27.1, [("s", "Us waqt bitcoin ki", 20.33, 21.5), ("b", "keemat hi nahi thi.", 21.5, 22.73), ("s", "10,000 BTC ≈", 23.32, 24.48), ("g", "sirf $40", 24.73, 26.36)]),
    (27.1, 34.7, [("s", "4 din baad, deal hui.", 27.2, 28.61), ("b", "Pizza aaye.", 29.29, 29.9), ("s", "Pehli baar bitcoin se", 30.27, 31.61), ("g", "asli khareedari.", 31.92, 34.05)]),
    (34.7, 40.0, [("b", "Aaj?", 35.01, 35.34), ("s", "Wahi 10,000 BTC", 35.93, 37.26), ("g", "hazaaron crore ke.", 37.58, 39.15)]),
    (40.0, 47.5, [("s", "Par Laszlo ko", 40.38, 41.1), ("b", "afsos nahi.", 41.1, 41.8), ("s", "Pizza ne dikhaya, bitcoin", 42.52, 45.58), ("g", "paisa ban sakta hai.", 46.0, 46.99)]),
    (47.5, 54.1, [("s", "Har saal 22 May ko", 47.87, 49.86), ("s", "crypto duniya manaati hai", 50.44, 51.85), ("g", "Bitcoin Pizza Day.", 52.2, 53.49)]),
    (54.1, DUR, [("s", "Aur crypto kahaniyan chahiye?", 54.54, 56.14), ("b", "Comment", 56.71, 57.27), ("g", "PIZZA", 57.77, 58.2)]),
]

PIZZA = '''<svg viewBox="0 0 120 120" width="{s}" height="{s}"><rect x="6" y="6" width="108" height="108" rx="14" fill="#2A1636" stroke="rgba(255,255,255,.35)" stroke-width="3"/>
<circle cx="60" cy="60" r="40" fill="#E9A84B"/><circle cx="60" cy="60" r="34" fill="#C8452F"/><circle cx="46" cy="50" r="6" fill="#FFE2A6"/><circle cx="70" cy="46" r="6" fill="#FFE2A6"/><circle cx="64" cy="72" r="6" fill="#FFE2A6"/><circle cx="44" cy="72" r="5" fill="#7A1E14"/><circle cx="78" cy="64" r="5" fill="#7A1E14"/></svg>'''

PROPS = [
    ("p1", 0.0, 6.2, '''<div class="card" style="width:600px">
        <div class="lab">FLORIDA · USA</div>
        <div class="cal"><div class="ct">MAY</div><div class="cd" id="p1d">22</div><div class="cy">2010</div></div>
        <div class="row c" id="p1z">''' + PIZZA.format(s=150) + PIZZA.format(s=150) + '''</div></div>'''),
    ("p2", 6.2, 9.9, '''<div class="card" style="width:640px">
        <div class="hd"><div class="coin">₿</div><div><div class="t">Pizza Order</div><div class="s">FLORIDA · MAY 2010</div></div></div>
        <div class="scr"><div class="sl">PAID IN BITCOIN</div><div class="sv"><span id="p2n">0</span> BTC</div></div>
        <div class="stamp" id="p2s" style="position:static;display:inline-block;margin-top:24px">PAID IN BTC</div></div>'''),
    ("p3", 9.9, 12.9, '''<div class="card" style="width:620px">
        <div class="hd"><div class="av">LH</div><div><div class="t" style="font-size:52px">Laszlo Hanyecz</div><div class="s">PROGRAMMER · FLORIDA</div></div></div>
        <div class="chips"><span>Early bitcoin miner</span><span>2010</span></div></div>'''),
    ("p4", 12.9, 20.1, '''<div class="card" style="width:680px">
        <div class="lab">BITCOIN FORUM · MAY 2010</div>
        <div class="post"><div class="pa">laszlo</div><div class="pt" id="p4t">"I'll pay 10,000 bitcoins for a couple of pizzas…"</div></div>
        <div class="deal"><div class="dl" id="p4a">''' + PIZZA.format(s=110) + PIZZA.format(s=110) + '''</div><div class="eq">⇄</div><div class="dr" id="p4b">10,000 ₿</div></div></div>'''),
    ("p5", 20.1, 27.1, '''<div class="card" style="width:640px">
        <div class="lab">BTC PRICE · 2010</div>
        <div class="scr"><div class="sl">1 BTC</div><div class="sv" style="font-size:72px">≈ $0.004</div></div>
        <div class="calc" id="p5c"><span>10,000 × $0.004</span><b>≈ $40</b></div></div>'''),
    ("p6", 27.1, 34.7, '''<div class="card" style="width:620px">
        <div class="lab">4 DIN BAAD · DELIVERED</div>
        <div class="row c" id="p6z">''' + PIZZA.format(s=170) + PIZZA.format(s=170) + '''</div>
        <div class="stamp" id="p6s" style="position:static;margin-top:26px;display:inline-block">FIRST BTC PURCHASE</div></div>'''),
    ("p7", 34.7, 40.0, '''<div class="card" style="width:660px">
        <div class="lab">10,000 BTC KI VALUE</div>
        <svg width="600" height="300" viewBox="0 0 600 300"><defs><linearGradient id="gl" x1="0" x2="1"><stop offset="0" stop-color="#C858C6"/><stop offset="1" stop-color="#9D14FF"/></linearGradient></defs>
          <g stroke="rgba(255,255,255,.1)"><line x1="0" y1="100" x2="600" y2="100"/><line x1="0" y1="200" x2="600" y2="200"/></g>
          <polyline id="p7l" points="10,285 120,282 220,276 300,262 380,226 450,170 520,80 590,18" fill="none" stroke="url(#gl)" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="900" stroke-dashoffset="900"/>
          <text x="10" y="260" font-family="SM" font-size="22" fill="#A99BB3">2010 · $40</text><text x="590" y="58" text-anchor="end" font-family="SM" font-weight="700" font-size="24" fill="#E7B6FF" id="p7t" opacity="0">AAJ · ₹ HAZAARON CR</text></svg></div>'''),
    ("p8", 40.0, 47.5, '''<div class="card" style="width:640px">
        <div class="lab">LASZLO KA NAZARIYA</div>
        <div class="li" id="p8a"><span class="x">✕</span><div class="t">Afsos?</div></div>
        <div class="li ok" id="p8b"><span class="x">✓</span><div class="t">Bitcoin = asli paisa</div></div></div>'''),
    ("p9", 47.5, 54.1, '''<div class="card" style="width:620px">
        <div class="cal"><div class="ct">HAR SAAL</div><div class="cd">22</div><div class="cy">MAY</div></div>
        <div class="pd" id="p9t">Bitcoin Pizza Day</div><div class="row c">''' + PIZZA.format(s=90) + PIZZA.format(s=90) + PIZZA.format(s=90) + '''</div></div>'''),
    ("p10", 54.1, DUR, '''<div class="card" style="width:660px">
        <div class="lab">COMMENTS</div>
        <div class="cin"><div class="av" style="width:64px;height:64px;font-size:26px">U</div><div class="ctx"><span id="p10t"></span><i id="p10c">|</i></div><div class="cpost">Post</div></div>
        <div class="reply" id="p10r"><div class="av" style="width:64px;height:64px;font-size:22px;background:linear-gradient(135deg,#9D14FF,#C858C6)">₿</div>
          <div><div class="t" style="font-size:30px">niks.crypto</div><div class="s" style="letter-spacing:.02em;font-family:SG;font-size:26px;color:#E7B6FF">Agli crypto kahani aa rahi hai ✨</div></div></div></div>'''),
]


def line_html(bi, li, st, text, t0, t1):
    ws = text.split()
    w = [max(2, len(x)) for x in ws]
    tot, acc, out = sum(w), 0, []
    for x, wi in zip(ws, w):
        out.append(f'<span class="w" data-t="{round(t0 + (t1 - t0) * acc / tot, 2)}">{x}</span>')
        acc += wi
    return f'<div class="ln l{st}">{" ".join(out)}</div>'


def build():
    caps = []
    for i, (a, b, lines) in enumerate(BLOCKS):
        inner = "".join(line_html(i, j, *l) for j, l in enumerate(lines))
        caps.append(f'      <div id="cap{i}" class="clip capb" data-start="{a}" data-duration="{round(b-a,2)}" data-track-index="5"><div class="cbx" id="cbx{i}">{inner}</div></div>')
    props = "\n".join(f'      <div id="{k}" class="clip prop" data-start="{a}" data-duration="{round(b-a,2)}" data-track-index="3"><div class="pw" id="{k}w">{h[:-6]}<div class="sweep"></div></div></div></div>'
                      for k, a, b, h in PROPS)
    parts = "".join(f'<i class="pt" style="left:{(i*137)%1040+20}px;top:{(i*263)%1800+60}px;width:{3+(i%3)*2}px;height:{3+(i%3)*2}px"></i>' for i in range(46))

    html = f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="assets/gsap.min.js"></script>
    <style>
      @font-face {{ font-family:"SG"; font-weight:400; src:url("assets/fonts/space-grotesk-latin-400-normal.woff2"); }}
      @font-face {{ font-family:"SG"; font-weight:500; src:url("assets/fonts/space-grotesk-latin-500-normal.woff2"); }}
      @font-face {{ font-family:"SG"; font-weight:600; src:url("assets/fonts/space-grotesk-latin-600-normal.woff2"); }}
      @font-face {{ font-family:"SG"; font-weight:700; src:url("assets/fonts/space-grotesk-latin-700-normal.woff2"); }}
      @font-face {{ font-family:"SM"; font-weight:400; src:url("assets/fonts/space-mono-latin-400-normal.woff2"); }}
      @font-face {{ font-family:"SM"; font-weight:700; src:url("assets/fonts/space-mono-latin-700-normal.woff2"); }}
      * {{ margin:0; padding:0; box-sizing:border-box; }}
      html, body {{ width:1080px; height:1920px; overflow:hidden; background:#06040A; }}
      #root {{ position:absolute; inset:0; font-family:"SG",sans-serif; color:#fff; overflow:hidden; }}
      #bg {{ position:absolute; inset:0; background:linear-gradient(180deg,#06040A 0%,#0B0610 26%,#1E0B2C 48%,#4A1670 70%,#8E1EC8 92%,#9D14FF 100%); }}
      .gb {{ position:absolute; border-radius:50%; filter:blur(60px); }}
      #grid {{ position:absolute; left:100px; right:100px; top:640px; height:880px; opacity:.6;
        background-image:linear-gradient(rgba(200,88,198,.16) 1px,transparent 1px),linear-gradient(90deg,rgba(200,88,198,.16) 1px,transparent 1px); background-size:60px 60px;
        -webkit-mask-image:radial-gradient(ellipse at center,#000 30%,transparent 75%); mask-image:radial-gradient(ellipse at center,#000 30%,transparent 75%); }}
      .pt {{ position:absolute; border-radius:50%; background:rgba(231,182,255,.55); box-shadow:0 0 10px rgba(200,88,198,.8); }}
      #vig {{ position:absolute; inset:0; background:radial-gradient(ellipse at 50% 45%,transparent 55%,rgba(0,0,0,.55)); }}
      #grain {{ position:absolute; inset:0; opacity:.07; mix-blend-mode:overlay; }}
      #handle {{ position:absolute; left:0; right:0; top:240px; text-align:center; font-weight:500; font-size:30px; color:rgba(255,255,255,.5); }}
      #handle b {{ color:#C858C6; font-weight:600; }}
      #stl {{ position:absolute; left:80px; right:80px; top:1680px; padding:28px 34px 54px; border-radius:30px; background:rgba(18,9,23,.45); border:1.5px solid rgba(255,255,255,.16); backdrop-filter:blur(16px); }}
      .stl-h {{ display:flex; justify-content:space-between; font-family:"SM"; font-size:20px; letter-spacing:.14em; color:#A99BB3; }}
      .stl-r {{ position:relative; margin:34px 20px 0; height:6px; }}
      .stl-l {{ position:absolute; inset:0; border-radius:3px; background:rgba(255,255,255,.14); }}
      .stl-f {{ position:absolute; inset:0; border-radius:3px; background:linear-gradient(90deg,#C858C6,#9D14FF); transform-origin:0 50%; box-shadow:0 0 16px rgba(200,88,198,.7); }}
      .stl-d {{ position:absolute; top:-9px; width:0; }}
      .stl-d i {{ position:absolute; left:-12px; width:24px; height:24px; border-radius:50%; background:#2A1636; border:3px solid rgba(255,255,255,.3); }}
      .stl-d b {{ position:absolute; left:-90px; width:180px; top:34px; text-align:center; font-family:"SM"; font-weight:400; font-size:17px; color:#A99BB3; white-space:nowrap; }}
      .capb {{ position:absolute; left:50px; right:50px; top:300px; text-align:center; }}
      .ln {{ line-height:1.08; }}
      .ln.ls {{ font-weight:400; font-size:50px; color:rgba(255,255,255,.88); margin-top:6px; }}
      .ln.lb {{ font-weight:600; font-size:100px; letter-spacing:-.04em; }}
      .ln.lg {{ font-weight:700; font-size:100px; letter-spacing:-.04em; }}
      .ln.lg .w {{ background:linear-gradient(90deg,#E7B6FF,#C858C6 45%,#9D14FF); -webkit-background-clip:text; color:transparent; }}
      .w {{ display:inline-block; opacity:.25; }}
      .prop {{ position:absolute; inset:0; }}
      .pw {{ position:absolute; left:0; right:0; top:740px; display:flex; justify-content:center; }}
      .card {{ zoom:1.32; position:relative; border-radius:34px; background:linear-gradient(180deg,rgba(255,255,255,.11),rgba(255,255,255,.04)); backdrop-filter:blur(24px);
        border:1.5px solid rgba(255,255,255,.22); box-shadow:0 40px 90px rgba(0,0,0,.55), inset 0 1px 0 rgba(255,255,255,.08); padding:38px 42px; overflow:hidden; }}
      .sweep {{ position:absolute; top:-200px; left:-400px; width:160px; height:1200px; transform:rotate(20deg); background:linear-gradient(90deg,transparent,rgba(255,255,255,.18),transparent); pointer-events:none; }}
      .lab {{ font-family:"SM"; font-size:22px; letter-spacing:.14em; color:#A99BB3; }}
      .hd {{ display:flex; align-items:center; gap:22px; }}
      .coin {{ width:86px; height:86px; border-radius:50%; background:radial-gradient(circle at 35% 30%,#E7B6FF,#9D14FF 60%,#4A0A80); display:flex; align-items:center; justify-content:center; font-weight:700; font-size:48px; }}
      .av {{ width:100px; height:100px; flex:none; border-radius:50%; background:linear-gradient(135deg,#C858C6,#670707); display:flex; align-items:center; justify-content:center; font-weight:700; font-size:40px; }}
      .t {{ font-weight:600; font-size:42px; }}
      .s {{ font-family:"SM"; font-size:22px; letter-spacing:.12em; color:#A99BB3; margin-top:4px; }}
      .scr {{ margin-top:30px; border-radius:20px; background:#120917; border:1px solid rgba(255,255,255,.08); padding:24px 28px; }}
      .sl {{ font-family:"SM"; font-size:20px; letter-spacing:.14em; color:#A99BB3; }}
      .sv {{ font-family:"SM"; font-weight:700; font-size:84px; text-align:right; margin-top:8px; white-space:nowrap; color:#E7B6FF; text-shadow:0 0 34px rgba(200,88,198,.6); }}
      .stamp {{ position:absolute; right:30px; top:24px; transform:rotate(-8deg); font-family:"SM"; font-weight:700; font-size:28px; letter-spacing:.12em; color:#C858C6; border:4px solid #C858C6; border-radius:40px; padding:8px 24px; background:rgba(18,9,23,.8); }}
      .cal {{ margin:26px auto 0; width:260px; border-radius:26px; overflow:hidden; background:#120917; border:1.5px solid rgba(255,255,255,.2); text-align:center; }}
      .ct {{ background:linear-gradient(90deg,#9D14FF,#C858C6); font-family:"SM"; font-weight:700; font-size:28px; letter-spacing:.16em; padding:12px 0; }}
      .cd {{ font-weight:700; font-size:150px; line-height:1.1; }}
      .cy {{ font-family:"SM"; font-size:28px; color:#A99BB3; padding-bottom:16px; letter-spacing:.14em; }}
      .row.c {{ display:flex; justify-content:center; gap:24px; margin-top:28px; }}
      .chips {{ display:flex; gap:16px; margin-top:28px; }} .chips span {{ border:1.5px solid rgba(255,255,255,.25); border-radius:40px; padding:12px 24px; font-size:30px; }}
      .post {{ margin-top:22px; border-radius:20px; background:#120917; padding:26px 28px; border-left:6px solid #9D14FF; }}
      .pa {{ font-family:"SM"; font-weight:700; font-size:24px; color:#C858C6; }}
      .pt {{ }}
      .post .pt {{ position:static; width:auto; height:auto; background:none; box-shadow:none; border-radius:0; font-size:40px; margin-top:8px; line-height:1.25; }}
      .deal {{ display:flex; align-items:center; justify-content:center; gap:30px; margin-top:30px; }}
      .dl {{ display:flex; gap:14px; }} .eq {{ font-size:70px; color:#C858C6; }}
      .dr {{ white-space:nowrap; font-family:"SM"; font-weight:700; font-size:50px; color:#E7B6FF; }}
      .calc {{ display:flex; justify-content:space-between; align-items:center; margin-top:28px; font-family:"SM"; font-size:30px; color:#A99BB3; }}
      .calc b {{ font-family:"SG"; font-weight:700; font-size:72px; color:#fff; }}
      .li {{ display:flex; align-items:center; gap:24px; margin-top:28px; padding:24px; border-radius:22px; background:rgba(103,7,7,.35); border:1.5px solid rgba(224,88,79,.4); }}
      .li.ok {{ background:rgba(157,20,255,.18); border-color:rgba(200,88,198,.5); }}
      .x {{ width:72px; height:72px; flex:none; border-radius:50%; background:#670707; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:38px; }}
      .li.ok .x {{ background:linear-gradient(135deg,#9D14FF,#C858C6); }}
      .pd {{ margin-top:26px; text-align:center; font-weight:700; font-size:50px; white-space:nowrap; background:linear-gradient(90deg,#E7B6FF,#C858C6,#9D14FF); -webkit-background-clip:text; color:transparent; }}
      .cin {{ display:flex; align-items:center; gap:18px; margin-top:20px; padding:18px; border-radius:20px; background:#120917; }}
      .ctx {{ flex:1; font-weight:600; font-size:40px; }} .ctx i {{ font-style:normal; color:#C858C6; }}
      .cpost {{ font-weight:600; font-size:30px; color:#C858C6; }}
      .reply {{ display:flex; gap:18px; align-items:center; margin-top:22px; padding:20px; border-radius:20px; border:1.5px solid rgba(200,88,198,.5); background:rgba(157,20,255,.12); }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
      <div id="bgc" class="clip" data-start="0" data-duration="{DUR}" data-track-index="0" data-layout-allow-overlap>
        <div id="bg"></div>
        <div class="gb" id="g1" style="left:520px;top:1300px;width:900px;height:900px;background:rgba(200,88,198,.5)"></div>
        <div class="gb" id="g2" style="left:-300px;top:1500px;width:900px;height:700px;background:rgba(157,20,255,.45)"></div>
        <div class="gb" id="g3" style="left:200px;top:700px;width:700px;height:500px;background:rgba(157,20,255,.12)"></div>
        <div id="grid"></div>
        <div id="pts">{parts}</div>
        <svg id="grain" width="1080" height="1920"><filter id="gn"><feTurbulence type="fractalNoise" baseFrequency="1" numOctaves="2" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter><rect width="1080" height="1920" filter="url(#gn)"/></svg>
        <div id="vig"></div>
        <div id="handle">niks<b>.crypto</b></div>
        <div id="stl"><div class="stl-h"><span>CRYPTO STORIES</span><span>EP 01 · PIZZA DAY</span></div>
          <div class="stl-r"><div class="stl-l"></div><div class="stl-f" id="stf"></div>
            {"".join(f'<div class="stl-d" style="left:{x}%"><i id="sd{i}"></i><b>{lab}</b></div>' for i, (x, lab) in enumerate([(0,"18 MAY · POST"),(33,"22 MAY · PIZZA"),(66,"2010 · $40"),(100,"AAJ · ₹ CR")]))}
          </div></div>
      </div>
{props}
{chr(10).join(caps)}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      const D = {DUR};
      const cyc = (id, from, to, per) => {{ const n = Math.ceil(D / per); tl.fromTo(id, from, {{ ...to, duration: per / 2, ease: "sine.inOut", yoyo: true, repeat: n * 2 - 1 }}, 0); }};
      cyc("#g1", {{ x: 0, y: 0 }}, {{ x: -160, y: -120 }}, 14);
      cyc("#g2", {{ x: 0, y: 0 }}, {{ x: 200, y: -80 }}, 18);
      cyc("#g3", {{ x: 0, y: 0, scale: 1 }}, {{ x: 60, y: 40, scale: 1.2 }}, 11);
      tl.fromTo("#pts", {{ y: 0 }}, {{ y: -260, duration: D, ease: "none" }}, 0);
      document.querySelectorAll(".pt").forEach((p, i) => cyc(p, {{ opacity: 0.2 }}, {{ opacity: 1 }}, 2 + (i % 5)));
      // captions: block enter/exit + word reveal
      document.querySelectorAll(".capb").forEach((c) => {{
        const a = parseFloat(c.dataset.start), b = a + parseFloat(c.dataset.duration);
        tl.fromTo(c.querySelector(".cbx"), {{ y: 24, opacity: 0, filter: "blur(8px)" }}, {{ y: 0, opacity: 1, filter: "blur(0px)", duration: 0.3, ease: "power3.out" }}, a + 0.02);
        tl.to(c.querySelector(".cbx"), {{ y: -20, opacity: 0, filter: "blur(8px)", duration: 0.2, ease: "power2.in" }}, b - 0.2);
        c.querySelectorAll(".w").forEach((w) => tl.fromTo(w, {{ opacity: 0.25, y: 6 }}, {{ opacity: 1, y: 0, duration: 0.14 }}, parseFloat(w.dataset.t)));
      }});
      // props: rise + blur, slow push-in, light sweep, exit
      document.querySelectorAll(".prop").forEach((p) => {{
        const a = parseFloat(p.dataset.start), b = a + parseFloat(p.dataset.duration), w = p.querySelector(".pw");
        tl.fromTo(w, {{ y: 90, scale: 0.9, opacity: 0, filter: "blur(12px)" }}, {{ y: 0, scale: 1, opacity: 1, filter: "blur(0px)", duration: 0.45, ease: "power3.out" }}, a + 0.05);
        tl.to(w, {{ scale: 1.05, duration: b - a - 0.7, ease: "none" }}, a + 0.5);
        tl.fromTo(p.querySelector(".sweep"), {{ x: 0 }}, {{ x: 1400, duration: 0.9, ease: "power2.inOut" }}, a + 0.35);
        tl.to(w, {{ y: -50, opacity: 0, filter: "blur(10px)", duration: 0.22, ease: "power2.in" }}, b - 0.22);
      }});
      const pop = (id, t) => tl.fromTo(id, {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.35, ease: "back.out(2.4)" }}, t);
      const slam = (id, t, r) => tl.fromTo(id, {{ scale: 2.3, opacity: 0, rotation: r - 12 }}, {{ scale: 1, opacity: 1, rotation: r, duration: 0.2, ease: "power4.in" }}, t);
      const count = (id, a, b, t, d, fmt) => {{ const o = {{ v: a }}; tl.fromTo(o, {{ v: a }}, {{ v: b, duration: d, ease: "power2.out", onUpdate: () => {{ document.querySelector(id).textContent = fmt(o.v); }} }}, t); }};
      tl.fromTo("#stl", {{ y: 120, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power3.out" }}, 0.4);
      tl.fromTo("#stf", {{ scaleX: 0 }}, {{ scaleX: 1, duration: D - 1, ease: "none" }}, 0.5);
      [13.0, 27.1, 20.1, 34.7].forEach((t, i) => tl.to("#sd" + i, {{ background: "#C858C6", borderColor: "#fff", scale: 1.25, duration: 0.25, ease: "back.out(3)" }}, t));
      // p1
      tl.fromTo("#p1d", {{ y: 60, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "back.out(2)" }}, 0.3);
      tl.fromTo("#p1z svg", {{ scale: 0, rotation: -20 }}, {{ scale: 1, rotation: 0, duration: 0.35, stagger: 0.18, ease: "back.out(2.4)" }}, 4.64);
      // p2 slot-roll count
      count("#p2n", 0, 10000, 7.76, 1.1, (v) => Math.round(v).toLocaleString("en-US")); slam("#p2s", 9.0, -8);
      // p3
      tl.fromTo("#p3w .chips span", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25, stagger: 0.15 }}, 11.4);
      // p4 forum
      tl.fromTo("#p4t", {{ clipPath: "inset(0 100% 0 0)" }}, {{ clipPath: "inset(0 0% 0 0)", duration: 1.6, ease: "none" }}, 13.4);
      pop("#p4a", 15.5); pop("#p4b", 17.5);
      // p5
      pop("#p5c", 24.7);
      // p6
      tl.fromTo("#p6z svg", {{ y: -200, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.45, stagger: 0.2, ease: "bounce.out" }}, 29.3); slam("#p6s", 32.2, -4);
      // p7 chart
      tl.to("#p7l", {{ attr: {{ "stroke-dashoffset": 0 }}, duration: 2.0, ease: "power2.in" }}, 35.4);
      tl.to("#p7t", {{ opacity: 1, duration: 0.3 }}, 37.6);
      // p8
      tl.fromTo("#p8a", {{ x: -80, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.3, ease: "power3.out" }}, 41.1);
      tl.fromTo("#p8b", {{ x: -80, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.3, ease: "power3.out" }}, 44.3);
      // p9
      pop("#p9t", 52.2);
      // p10 comment typing
      const typ = {{ n: 0 }}; const word = "PIZZA";
      tl.fromTo(typ, {{ n: 0 }}, {{ n: word.length, duration: 0.6, ease: "none", onUpdate: () => {{ document.querySelector("#p10t").textContent = word.slice(0, Math.round(typ.n)); }} }}, 57.0);
      cyc("#p10c", {{ opacity: 1 }}, {{ opacity: 0 }}, 1);
      tl.fromTo("#p10r", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "back.out(2)" }}, 58.1);
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''
    open(os.path.join(HERE, "hf", "index.html"), "w").write(html)
    print("blocks:", len(BLOCKS), "props:", len(PROPS))


if __name__ == "__main__":
    build()
