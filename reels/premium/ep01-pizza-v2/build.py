"""Crypto Stories EP 01 · Pizza Day — v2, built to the reference grammar (thebigaistory-style) in the purple palette.

Grammar copied from the references:
- small handle at the top, sentence captions near the top that grow word by word
  (s = small regular, b = bold, a = accent gradient, h = highlight bar that wipes in)
- one compact, realistic prop mid-screen that PERSISTS and evolves across several sentences
- small sticker cards / stamps pop onto the prop; numbers count up on the prop
- ending: comment being typed + DM reply + glossy spheres
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 59.2

# (start, end, [(style, text, t0, t1)])
CAPS = [
    (0.0, 6.2, [("s", "22 May 2010.", 0.0, 1.7), ("s", "Florida mein ek programmer ne", 2.8, 4.3), ("b", "2 pizza order kiye.", 4.64, 5.8)]),
    (6.2, 9.9, [("s", "Aur payment kiya…", 6.49, 7.33), ("a", "10,000 BTC mein.", 7.76, 9.25)]),
    (9.9, 12.9, [("s", "Uska naam tha,", 10.11, 10.88), ("b", "Laszlo Hanyecz.", 11.11, 12.34)]),
    (12.9, 20.1, [("s", "Online forum pe likha:", 13.09, 14.69), ("h", "“2 pizza bhejo, 10,000 BTC lo.”", 15.39, 19.53)]),
    (20.1, 27.1, [("s", "Us waqt bitcoin ki", 20.33, 21.5), ("b", "keemat hi nahi thi.", 21.5, 22.73), ("s", "10,000 BTC ≈", 23.32, 24.48), ("a", "sirf $40.", 24.73, 26.36)]),
    (27.1, 34.7, [("s", "4 din baad, deal hui.", 27.2, 28.61), ("b", "Pizza aaye.", 29.29, 29.9), ("s", "Pehli baar bitcoin se", 30.27, 31.61), ("h", "asli khareedari.", 31.92, 34.05)]),
    (34.7, 40.0, [("b", "Aaj?", 35.01, 35.34), ("s", "Wahi 10,000 BTC", 35.93, 37.26), ("a", "hazaaron crore ke.", 37.58, 39.15)]),
    (40.0, 47.5, [("s", "Par Laszlo ko", 40.38, 41.1), ("b", "afsos nahi.", 41.1, 41.8), ("s", "Pizza ne dikhaya, bitcoin", 42.52, 45.58), ("h", "paisa ban sakta hai.", 46.0, 46.99)]),
    (47.5, 54.1, [("s", "Har saal 22 May ko", 47.87, 49.86), ("s", "crypto duniya manaati hai", 50.44, 51.85), ("a", "Bitcoin Pizza Day.", 52.2, 53.49)]),
    (54.1, DUR, [("s", "Aur crypto kahaniyan chahiye?", 54.54, 56.14), ("s", "Comment", 56.71, 57.27), ("a", "PIZZA", 57.77, 58.2)]),
]

PIZZA = '''<svg viewBox="0 0 200 200" width="{s}" height="{s}"><circle cx="100" cy="100" r="92" fill="#E3A24A"/><circle cx="100" cy="100" r="80" fill="#C2402C"/>
<g fill="#FFE3A8"><circle cx="70" cy="74" r="12"/><circle cx="128" cy="66" r="12"/><circle cx="116" cy="124" r="12"/><circle cx="66" cy="128" r="10"/><circle cx="100" cy="98" r="9"/></g>
<g fill="#6E1A12"><circle cx="96" cy="58" r="8"/><circle cx="142" cy="104" r="8"/><circle cx="88" cy="146" r="8"/><circle cx="52" cy="98" r="8"/></g>
<g stroke="#E3A24A" stroke-width="3" opacity=".7"><line x1="100" y1="20" x2="100" y2="180"/><line x1="20" y1="100" x2="180" y2="100"/><line x1="43" y1="43" x2="157" y2="157"/><line x1="157" y1="43" x2="43" y2="157"/></g></svg>'''

# props: (id, start, end, html)
PROPS = [
    ("pa", 0.0, 9.9, f'''
      <div class="printer"><div class="slot"><i></i></div>
        <div class="rcw"><div class="rc" id="rc">
          <div class="rlogo">{PIZZA.format(s=70)}</div>
          <div class="rh">PAPA JOHN'S · FLORIDA</div><div class="rs">22 MAY 2010 · ORDER #0001</div>
          <div class="rl"><span>2 × LARGE PIZZA</span><span id="rq">—</span></div>
          <div class="rl dash"></div>
          <div class="rl tot"><span>PAID IN</span><span><b id="rbtc">0</b> BTC</span></div>
          <div class="stampo" id="rst">PAID IN BITCOIN</div>
        </div></div></div>'''),
    ("pb", 9.9, 20.1, f'''
      <div class="win"><div class="wbar"><i></i><i></i><i></i><span>bitcointalk.org</span></div>
        <div class="wt">Pizza for bitcoins?</div>
        <div class="usr"><div class="ava">L</div><div><div class="un"><span id="un">laszlo</span></div><div class="ud">May 18, 2010 · Full Member</div></div></div>
        <div class="body"><span id="bd"></span></div>
        <div class="stk" id="stk"><div class="sk-l">THE OFFER</div><div class="sk-r">{PIZZA.format(s=64)}{PIZZA.format(s=64)}<em>⇄</em><b>10,000 ₿</b></div></div>
      </div>'''),
    ("pc", 20.1, 27.1, '''
      <div class="calc"><div class="ch"><div class="cico">₿</div><div><div class="cn">BTC / USD</div><div class="cs">MAY 2010 · PRICE</div></div><div class="clive"><i></i>LIVE</div></div>
        <div class="disp"><div class="dl" id="dl">1 BTC</div><div class="dv" id="dv">$0.000</div></div>
        <div class="keys">''' + "".join(f'<div class="k" id="k{i}">{c}</div>' for i, c in enumerate("789456123×0=")) + '''</div></div>'''),
    ("pd", 27.1, 34.7, f'''
      <div class="boxes"><div class="box b2" id="bx2"><div class="lid"></div>{PIZZA.format(s=300)}</div>
        <div class="box b1" id="bx1"><div class="lid"></div>{PIZZA.format(s=300)}</div>
        <div class="tag" id="tag"><b>DELIVERED</b><span>4 DIN BAAD · 22 MAY</span></div>
        <div class="stampo big" id="fst">FIRST BTC PURCHASE</div></div>'''),
    ("pe", 34.7, 40.0, '''
      <div class="orbit">''' + "".join(f'<div class="oc" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px;font-size:{s//2}px">₿</div>'
                                        for x, y, s in [(30, 120, 78), (110, 20, 64), (250, -20, 72), (420, 10, 66), (520, 110, 80), (560, 260, 64), (500, 400, 76), (360, 480, 66), (200, 470, 74), (60, 380, 66), (0, 250, 60), (330, 560, 52)]) + '''
        <div class="core"><div class="cv" id="cv">$40</div><div class="cl" id="cl">10,000 BTC · 2010</div></div></div>'''),
    ("pf", 40.0, 47.5, '''
      <div class="doc"><div class="dq">Kya Laszlo ko afsos hai?</div>
        <div class="da" id="da">Nahi.</div>
        <div class="dp">Unke hisaab se, pizza ne <span class="hl" id="hl">dikhaya ki bitcoin asli paisa ban sakta hai.</span></div>
        <div class="stampo" id="nr" style="position:absolute;right:34px;bottom:26px">NO REGRETS</div></div>'''),
    ("pg", 47.5, 54.1, f'''
      <div class="calp"><div class="rings"><i></i><i></i><i></i><i></i></div><div class="cm">MAY</div><div class="cdd">22</div><div class="cy">HAR SAAL</div>
        <div class="stk" id="pdy" style="left:-70px;right:auto;bottom:-120px;white-space:nowrap"><div class="sk-r">{PIZZA.format(s=56)}<b style="font-size:40px">Bitcoin Pizza Day</b></div></div></div>'''),
    ("ph", 54.1, DUR, '''
      <div class="cmt"><div class="ct">Comments</div><div class="cin"><span id="ty"></span><i id="cur">|</i><b>Post</b></div></div>
      <div class="dm" id="dm"><div class="ava sm">N</div><div><div class="dn">niks.crypto <span>sent you a message · now</span></div>
        <div class="dt">Agli crypto kahani ready hai 🙌</div><div class="dlk">niks.crypto/stories</div></div></div>
      <div class="sph" id="s1" style="left:70px"></div><div class="sph" id="s2" style="left:670px"></div>'''),
]


def caption_html(i, a, b, lines):
    out = []
    for j, (st, text, t0, t1) in enumerate(lines):
        ws = text.split()
        w = [max(2, len(x)) for x in ws]
        tot, acc, spans = sum(w), 0, []
        for x, wi in zip(ws, w):
            spans.append(f'<span class="w" data-t="{round(t0 + (t1 - t0) * acc / tot, 2)}">{x}</span>')
            acc += wi
        inner = " ".join(spans)
        if st == "h":
            inner = f'<span class="bar" data-t="{t0}"></span><span class="bt">{inner}</span>'
        out.append(f'<div class="ln {st}">{inner}</div>')
    return f'      <div id="cap{i}" class="clip cap" data-start="{a}" data-duration="{round(b - a, 2)}" data-track-index="5"><div class="cb">{"".join(out)}</div></div>'


def build():
    caps = "\n".join(caption_html(i, *c) for i, c in enumerate(CAPS))
    LH = {"s": 63, "b": 105, "a": 110, "h": 96}
    def top_for(a, b):
        hs = [sum(LH[l[0]] for l in lines) for ca, cb, lines in CAPS if ca < b - 0.01 and cb > a + 0.01]
        return 330 + max(hs or [200]) + 70
    props = "\n".join(f'      <div id="{k}" class="clip prop" data-start="{a}" data-duration="{round(b - a, 2)}" data-track-index="3"><div class="stage" id="{k}s" style="top:{top_for(a, b)}px">{h}</div></div>'
                      for k, a, b, h in PROPS)
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
      html, body {{ width:1080px; height:1920px; overflow:hidden; background:#120917; }}
      #root {{ position:absolute; inset:0; font-family:"SG",sans-serif; color:#fff; overflow:hidden; }}
      #bg {{ position:absolute; inset:0; background:radial-gradient(1100px 900px at 50% 62%,#24113A 0%,#170B20 55%,#120917 100%); }}
      #glow {{ position:absolute; left:140px; top:1500px; width:800px; height:600px; border-radius:50%; background:rgba(157,20,255,.22); filter:blur(90px); }}
      #grid {{ position:absolute; left:60px; right:60px; top:640px; height:1100px;
        background-image:linear-gradient(rgba(231,182,255,.07) 1.5px,transparent 1.5px),linear-gradient(90deg,rgba(231,182,255,.07) 1.5px,transparent 1.5px); background-size:64px 64px;
        -webkit-mask-image:radial-gradient(ellipse at center,#000 35%,transparent 72%); mask-image:radial-gradient(ellipse at center,#000 35%,transparent 72%); }}
      #handle {{ position:absolute; left:0; right:0; top:250px; text-align:center; font-weight:600; font-size:30px; color:rgba(255,255,255,.28); }}
      /* captions */
      .cap {{ position:absolute; left:40px; right:40px; top:330px; text-align:center; }}
      .ln {{ line-height:1.12; }}
      .ln.s {{ font-weight:400; font-size:56px; color:rgba(255,255,255,.9); }}
      .ln.b {{ font-weight:700; font-size:94px; letter-spacing:-.035em; }}
      .ln.a {{ font-weight:700; font-size:98px; letter-spacing:-.035em; }}
      .ln.a .w {{ background:linear-gradient(90deg,#F1D2FF,#C858C6 55%,#A63BFF); -webkit-background-clip:text; color:transparent; }}
      .ln.h {{ position:relative; display:inline-block; margin-top:10px; font-weight:700; font-size:66px; letter-spacing:-.02em; padding:2px 20px 8px; }}
      .bar {{ position:absolute; inset:0; background:#fff; transform-origin:0 50%; }}
      .bt {{ position:relative; color:#120917; }}
      .w {{ display:inline-block; opacity:0; }}
      /* prop stage */
      .prop {{ position:absolute; inset:0; }}
      .stage {{ position:absolute; left:0; right:0; top:690px; height:1050px; display:flex; align-items:flex-start; justify-content:center; }}
      .stage > * {{ zoom:1.28; }}
      #pas > *, #pds > * {{ zoom:1.12; }} #pcs > * {{ zoom:1.18; }} #pbs > *, #pfs > * {{ zoom:1.42; }} #phs > * {{ zoom:1.3; }} #pgs > * {{ zoom:1.4; }} #pes > * {{ zoom:1.38; }}
      .glass {{ background:linear-gradient(180deg,#24162E,#1A1022); border:1.5px solid rgba(255,255,255,.12); box-shadow:0 50px 100px rgba(0,0,0,.55), inset 0 1px 0 rgba(255,255,255,.07); }}
      /* A printer + receipt */
      .printer {{ position:relative; width:700px; height:820px; }}
      .slot {{ position:absolute; left:0; right:0; top:0; height:120px; border-radius:30px; background:linear-gradient(180deg,#2E1F38,#1B1122); border:1.5px solid rgba(255,255,255,.12); box-shadow:0 30px 60px rgba(0,0,0,.6); z-index:3; }}
      .slot i {{ position:absolute; left:90px; right:90px; top:66px; height:14px; border-radius:7px; background:#07040A; }}
      .rcw {{ position:absolute; left:110px; right:110px; top:72px; height:740px; overflow:hidden; z-index:2; }}
      .rc {{ position:relative; background:#F6F0FA; color:#1A0F22; padding:60px 38px 40px; font-family:"SM"; font-size:28px; height:740px;
        background-image:radial-gradient(circle at 10px 100%, transparent 9px, #F6F0FA 10px); }}
      .rlogo {{ text-align:center; }} .rh {{ text-align:center; font-weight:700; font-size:28px; margin-top:12px; }} .rs {{ text-align:center; font-size:20px; color:#6D5F78; margin-top:6px; letter-spacing:.06em; }}
      .rl {{ display:flex; justify-content:space-between; margin-top:34px; }} .rl.dash {{ border-top:3px dashed #CBBFD6; margin-top:28px; }}
      .rl.tot {{ font-weight:700; font-size:34px; color:#7A10D8; margin-top:24px; }}
      .stampo {{ display:inline-block; border:5px solid #C858C6; color:#C858C6; border-radius:14px; padding:8px 20px; font-family:"SM"; font-weight:700; font-size:30px; letter-spacing:.06em; transform:rotate(-7deg); }}
      .rc .stampo {{ margin-top:44px; margin-left:60px; color:#9D14FF; border-color:#9D14FF; }}
      .stampo.big {{ position:absolute; left:150px; bottom:40px; font-size:36px; background:rgba(18,9,23,.85); }}
      /* B forum window */
      .win {{ position:relative; width:670px; border-radius:30px; padding:0 0 40px; background:#F6F0FA; color:#1A0F22; box-shadow:0 50px 100px rgba(0,0,0,.55); }}
      .wbar {{ display:flex; align-items:center; gap:12px; padding:22px 28px; border-bottom:2px solid #E6DDEE; }}
      .wbar i {{ width:16px; height:16px; border-radius:50%; background:#D5C8E0; }} .wbar span {{ margin-left:16px; font-family:"SM"; font-size:22px; color:#8B7B98; }}
      .wt {{ padding:30px 40px 0; font-weight:700; font-size:46px; }}
      .usr {{ display:flex; align-items:center; gap:20px; padding:26px 40px 0; }}
      .ava {{ width:84px; height:84px; border-radius:50%; background:linear-gradient(135deg,#9D14FF,#C858C6); color:#fff; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:40px; flex:none; }}
      .ava.sm {{ width:64px; height:64px; font-size:28px; }}
      .un {{ font-weight:700; font-size:36px; color:#7A10D8; }} .ud {{ font-family:"SM"; font-size:20px; color:#8B7B98; margin-top:2px; }}
      .body {{ padding:24px 40px 40px; font-size:38px; line-height:1.35; min-height:180px; }}
      .stk {{ position:absolute; right:-20px; bottom:-90px; border-radius:24px; padding:20px 26px; background:#1A1022; border:3px solid #C858C6; box-shadow:0 30px 60px rgba(0,0,0,.5); transform:rotate(-4deg); }}
      .sk-l {{ font-family:"SM"; font-size:20px; color:#C858C6; letter-spacing:.12em; }}
      .sk-r {{ display:flex; align-items:center; gap:14px; margin-top:8px; }} .sk-r em {{ font-style:normal; font-size:44px; color:#C858C6; }} .sk-r b {{ font-family:"SM"; font-size:44px; color:#fff; }}
      /* C calculator */
      .calc {{ width:660px; border-radius:40px; padding:34px; background:#F6F0FA; color:#1A0F22; box-shadow:0 50px 100px rgba(0,0,0,.55); }}
      .ch {{ display:flex; align-items:center; gap:18px; }}
      .cico {{ width:70px; height:70px; border-radius:18px; background:linear-gradient(135deg,#9D14FF,#C858C6); color:#fff; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:40px; }}
      .cn {{ font-weight:700; font-size:36px; }} .cs {{ font-family:"SM"; font-size:18px; color:#8B7B98; letter-spacing:.1em; }}
      .clive {{ margin-left:auto; font-family:"SM"; font-size:20px; color:#8B7B98; }} .clive i {{ display:inline-block; width:14px; height:14px; border-radius:50%; background:#C858C6; margin-right:8px; vertical-align:0; }}
      .disp {{ margin-top:26px; border-radius:22px; background:#140A1A; padding:22px 30px; text-align:right; }}
      .dl {{ font-family:"SM"; font-size:22px; color:#8B7B98; letter-spacing:.1em; }}
      .dv {{ font-family:"SM"; font-weight:700; font-size:96px; color:#E7B6FF; text-shadow:0 0 30px rgba(200,88,198,.5); white-space:nowrap; }}
      .keys {{ display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-top:24px; }}
      .k {{ height:86px; border-radius:18px; background:#ECE3F3; box-shadow:0 6px 0 #D5C8E0; display:flex; align-items:center; justify-content:center; font-weight:600; font-size:38px; }}
      /* D boxes */
      .boxes {{ position:relative; width:860px; height:740px; }}
      .box {{ position:absolute; width:440px; height:440px; border-radius:22px; background:linear-gradient(135deg,#F3EBD9,#DCCBA8); box-shadow:0 40px 80px rgba(0,0,0,.55); display:flex; align-items:center; justify-content:center; }}
      .box .lid {{ position:absolute; left:0; right:0; top:-90px; height:110px; border-radius:22px 22px 6px 6px; background:linear-gradient(180deg,#E8DCC2,#CDB98E); transform-origin:50% 100%; transform:perspective(600px) rotateX(55deg); }}
      .b1 {{ left:60px; top:200px; }} .b2 {{ left:360px; top:110px; }}
      .tag {{ position:absolute; right:0; top:40px; border-radius:20px; padding:18px 24px; background:#fff; color:#1A0F22; box-shadow:0 20px 40px rgba(0,0,0,.4); transform:rotate(5deg); }}
      .tag b {{ display:block; font-size:34px; color:#7A10D8; }} .tag span {{ font-family:"SM"; font-size:20px; color:#8B7B98; }}
      /* E orbit */
      .orbit {{ position:relative; width:640px; height:620px; }}
      .oc {{ position:absolute; border-radius:50%; background:radial-gradient(circle at 35% 30%,#F4DCFF,#B44AE0 55%,#5B0E96); color:#fff; display:flex; align-items:center; justify-content:center; font-weight:700; box-shadow:0 14px 30px rgba(0,0,0,.45); }}
      .core {{ position:absolute; left:150px; top:140px; width:340px; height:340px; border-radius:50%; background:radial-gradient(circle at 40% 30%,#FFFFFF,#F1E6F8 60%,#D9C6E8); color:#1A0F22;
        display:flex; flex-direction:column; align-items:center; justify-content:center; box-shadow:0 40px 90px rgba(0,0,0,.6), 0 0 0 10px rgba(200,88,198,.25); }}
      .cv {{ font-family:"SM"; font-weight:700; font-size:68px; color:#7A10D8; white-space:nowrap; }} .cl {{ font-family:"SM"; font-size:20px; color:#8B7B98; letter-spacing:.08em; margin-top:6px; }}
      /* F doc */
      .doc {{ position:relative; width:670px; border-radius:28px; padding:44px 46px 110px; background:#F6F0FA; color:#1A0F22; box-shadow:0 50px 100px rgba(0,0,0,.55); }}
      .dq {{ font-weight:700; font-size:46px; }} .da {{ font-size:42px; margin-top:20px; color:#5D4E68; }}
      .dp {{ font-size:40px; line-height:1.35; margin-top:20px; }}
      .hl {{ background:linear-gradient(90deg,rgba(200,88,198,.38),rgba(200,88,198,.38)) no-repeat 0 0 / 0% 100%; padding:0 4px; }}
      /* G calendar */
      .calp {{ position:relative; width:480px; height:540px; border-radius:36px; background:#F6F0FA; color:#1A0F22; box-shadow:0 50px 100px rgba(0,0,0,.55); text-align:center; overflow:visible; }}
      .rings {{ position:absolute; left:70px; right:70px; top:-26px; display:flex; justify-content:space-between; }} .rings i {{ width:22px; height:56px; border-radius:11px; background:#3A2846; }}
      .cm {{ border-radius:36px 36px 0 0; background:linear-gradient(90deg,#9D14FF,#C858C6); color:#fff; font-family:"SM"; font-weight:700; font-size:44px; letter-spacing:.2em; padding:34px 0 24px; }}
      .cdd {{ font-weight:700; font-size:250px; line-height:1.05; letter-spacing:-.04em; }} .cy {{ font-family:"SM"; font-size:28px; color:#8B7B98; letter-spacing:.16em; }}
      /* H comments */
      .cmt {{ position:absolute; left:70px; top:40px; width:690px; border-radius:28px; padding:30px; background:#F6F0FA; color:#1A0F22; box-shadow:0 40px 80px rgba(0,0,0,.5); }}
      .ct {{ font-weight:700; font-size:34px; }} .cin {{ display:flex; align-items:center; margin-top:20px; padding:22px 26px; border-radius:40px; background:#ECE3F3; font-size:38px; font-weight:600; }}
      .cin i {{ font-style:normal; color:#9D14FF; }} .cin b {{ margin-left:auto; color:#9D14FF; font-size:32px; }}
      .dm {{ position:absolute; left:70px; top:300px; width:690px; display:flex; gap:20px; border-radius:28px; padding:28px; background:#F6F0FA; color:#1A0F22; border:4px solid #C858C6; box-shadow:0 40px 80px rgba(0,0,0,.5); }}
      .dn {{ font-weight:700; font-size:30px; }} .dn span {{ font-weight:400; font-size:22px; color:#8B7B98; }}
      .dt {{ font-size:32px; margin-top:6px; }} .dlk {{ font-size:30px; color:#9D14FF; font-weight:600; margin-top:4px; }}
      .sph {{ position:absolute; top:560px; width:90px; height:90px; border-radius:50%; background:radial-gradient(circle at 35% 30%,#F8E6FF,#C858C6 45%,#6E0FB4); box-shadow:0 20px 40px rgba(0,0,0,.5); }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
      <div id="bgc" class="clip" data-start="0" data-duration="{DUR}" data-track-index="0"><div id="bg"></div><div id="glow"></div><div id="grid"></div><div id="handle">niks.crypto</div></div>
{props}
{caps}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      const D = {DUR};
      tl.fromTo("#glow", {{ x: 0, scale: 1 }}, {{ x: 80, scale: 1.15, duration: D / 2, ease: "sine.inOut", yoyo: true, repeat: 1 }}, 0);
      // captions: whole block in/out, words appear one by one from blur (reference behaviour)
      document.querySelectorAll(".cap").forEach((c) => {{
        const a = parseFloat(c.dataset.start), b = a + parseFloat(c.dataset.duration);
        tl.to(c.querySelector(".cb"), {{ opacity: 0, filter: "blur(10px)", duration: 0.18, ease: "power2.in" }}, b - 0.18);
        c.querySelectorAll(".bar").forEach((r) => tl.fromTo(r, {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.35, ease: "power3.out" }}, parseFloat(r.dataset.t) - 0.05));
        c.querySelectorAll(".w").forEach((w) => tl.fromTo(w, {{ opacity: 0, filter: "blur(8px)", y: 8 }}, {{ opacity: 1, filter: "blur(0px)", y: 0, duration: 0.22, ease: "power2.out" }}, parseFloat(w.dataset.t)));
      }});
      // props: soft blur-in, gentle settle, blur-out
      document.querySelectorAll(".prop").forEach((p) => {{
        const a = parseFloat(p.dataset.start), b = a + parseFloat(p.dataset.duration), s = p.querySelector(".stage");
        tl.fromTo(s, {{ opacity: 0, y: 40, scale: 0.96, filter: "blur(14px)" }}, {{ opacity: 1, y: 0, scale: 1, filter: "blur(0px)", duration: 0.5, ease: "power3.out" }}, a + 0.02);
        tl.to(s, {{ scale: 1.03, duration: Math.max(0.5, b - a - 0.8), ease: "sine.inOut" }}, a + 0.52);
        if (b < D) tl.to(s, {{ opacity: 0, scale: 0.98, filter: "blur(14px)", duration: 0.25, ease: "power2.in" }}, b - 0.25);
      }});
      const num = (id, a, b, t, d, f) => {{ const o = {{ v: a }}; tl.fromTo(o, {{ v: a }}, {{ v: b, duration: d, ease: "power2.out", onUpdate: () => {{ document.querySelector(id).textContent = f(o.v); }} }}, t); }};
      const pop = (id, t, r = 0) => tl.fromTo(id, {{ scale: 0.4, opacity: 0, rotation: r - 10 }}, {{ scale: 1, opacity: 1, rotation: r, duration: 0.4, ease: "back.out(2.2)" }}, t);
      const slam = (id, t, r) => tl.fromTo(id, {{ scale: 2.2, opacity: 0, rotation: r - 10 }}, {{ scale: 1, opacity: 1, rotation: r, duration: 0.22, ease: "power4.in" }}, t);
      const press = (id, t) => tl.fromTo(id, {{ background: "#ECE3F3", y: 0 }}, {{ background: "#E7B6FF", y: 4, duration: 0.08, yoyo: true, repeat: 1 }}, t);
      // A receipt prints out of the slot in steps
      tl.fromTo("#rc", {{ clipPath: "inset(0 0 100% 0)" }}, {{ clipPath: "inset(0 0 66% 0)", duration: 0.8, ease: "power2.out" }}, 0.3);
      tl.to("#rc", {{ clipPath: "inset(0 0 52% 0)", duration: 0.6, ease: "power2.out" }}, 4.6);
      tl.fromTo("#rq", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.1 }}, 4.9); tl.set("#rq", {{ textContent: "×2" }}, 4.9);
      tl.to("#rc", {{ clipPath: "inset(0 0 30% 0)", duration: 0.6, ease: "power2.out" }}, 7.6);
      num("#rbtc", 0, 10000, 7.8, 1.2, (v) => Math.round(v).toLocaleString("en-US"));
      tl.to("#rc", {{ clipPath: "inset(0 0 0% 0)", duration: 0.5, ease: "power2.out" }}, 8.8);
      slam("#rst", 9.1, -7);
      // B forum post: username types, body types, sticker pops
      tl.fromTo("#un", {{ clipPath: "inset(0 100% 0 0)" }}, {{ clipPath: "inset(0 0% 0 0)", duration: 0.6, ease: "none" }}, 11.1);
      const BD = "I'll pay 10,000 bitcoins for a couple of pizzas.. like maybe 2 large ones", bo = {{ n: 0 }};
      tl.fromTo(bo, {{ n: 0 }}, {{ n: BD.length, duration: 3.2, ease: "none", onUpdate: () => {{ document.querySelector("#bd").textContent = BD.slice(0, Math.round(bo.n)); }} }}, 15.2);
      pop("#stk", 17.5, -4);
      // C calculator: price counts, keys pressed, result
      num("#dv", 0, 0.004, 21.4, 1.0, (v) => "$" + v.toFixed(3));
      ["#k6", "#k10", "#k10", "#k10", "#k10", "#k9"].forEach((k, i) => press(k, 23.3 + i * 0.16));
      tl.set("#dl", {{ textContent: "10,000 × $0.004" }}, 23.4);
      press("#k11", 24.6); tl.set("#dl", {{ textContent: "10,000 BTC =" }}, 24.7);
      num("#dv", 0, 40, 24.7, 0.8, (v) => "$" + v.toFixed(v < 39.95 ? 2 : 0));
      // D pizza boxes
      tl.fromTo("#bx1", {{ y: 300, opacity: 0, rotation: -6 }}, {{ y: 0, opacity: 1, rotation: -3, duration: 0.5, ease: "back.out(1.6)" }}, 27.3);
      tl.fromTo("#bx2", {{ y: 300, opacity: 0, rotation: 6 }}, {{ y: 0, opacity: 1, rotation: 4, duration: 0.5, ease: "back.out(1.6)" }}, 29.3);
      pop("#tag", 27.8, 5); slam("#fst", 32.0, -6);
      // E value orbit: coins fill in, counter flips
      tl.fromTo(".oc", {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, stagger: 0.18, ease: "back.out(2.5)" }}, 35.2);
      tl.to("#cv", {{ rotationX: 90, duration: 0.18, ease: "power2.in" }}, 37.45);
      tl.set("#cv", {{ textContent: "₹ ? ? ? CR" }}, 37.63); tl.set("#cl", {{ textContent: "10,000 BTC · AAJ" }}, 37.63);
      tl.to("#cv", {{ rotationX: 0, duration: 0.18, ease: "power2.out" }}, 37.63);
      tl.set("#cv", {{ textContent: "HAZAARON CR" }}, 38.6); tl.to("#cv", {{ fontSize: 48, duration: 0.01 }}, 38.6);
      tl.to(".oc", {{ y: -8, duration: 0.4, stagger: 0.05, yoyo: true, repeat: 3, ease: "sine.inOut" }}, 36.8);
      // F doc: answer + highlight sweep + stamp
      tl.fromTo("#da", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2 }}, 41.1);
      tl.to("#hl", {{ backgroundSize: "100% 100%", duration: 1.6, ease: "none" }}, 43.0);
      slam("#nr", 46.0, -7);
      // G calendar
      pop("#pdy", 52.2, -5);
      // H comment typing + DM + spheres
      const word = "PIZZA", o = {{ n: 0 }};
      tl.fromTo(o, {{ n: 0 }}, {{ n: word.length, duration: 0.7, ease: "none", onUpdate: () => {{ document.querySelector("#ty").textContent = word.slice(0, Math.round(o.n)); }} }}, 57.0);
      tl.fromTo("#cur", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.4, yoyo: true, repeat: 9, ease: "steps(1)" }}, 54.2);
      tl.fromTo("#dm", {{ y: 40, opacity: 0, scale: 0.95 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.4, ease: "back.out(2)" }}, 58.0);
      ["#s1", "#s2"].forEach((s, i) => {{
        tl.fromTo(s, {{ y: -900, opacity: 1 }}, {{ y: 0, duration: 0.7, ease: "bounce.out" }}, 55.0 + i * 0.3);
      }});
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''
    open(os.path.join(HERE, "hf", "index.html"), "w").write(html)
    print("captions:", len(CAPS), "props:", len(PROPS))


if __name__ == "__main__":
    build()
