"""Crypto Stories EP 11 · Forgot BTC — v2, built to the reference grammar (thebigaistory-style) in the purple palette.

Grammar copied from the references:
- small handle at the top, sentence captions near the top that grow word by word
  (s = small regular, b = bold, a = accent gradient, h = highlight bar that wipes in)
- one compact, realistic prop mid-screen that PERSISTS and evolves across several sentences
- small sticker cards / stamps pop onto the prop; numbers count up on the prop
- ending: comment being typed + DM reply + glossy spheres
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 76.7

CAPS = [
    (0.0, 5.7, [("s", "Ek ladke ne sirf", 0.0, 1.2), ("a", "₹1,200 ka bitcoin", 1.2, 2.6), ("s", "khareeda…", 2.6, 3.4), ("h", "aur bhool gaya.", 4.1, 4.88)]),
    (5.7, 10.1, [("s", "4 saal baad,", 6.03, 7.01), ("s", "usi se usne", 7.27, 8.2), ("b", "ek flat khareeda.", 8.2, 9.49)]),
    (10.1, 17.0, [("s", "2009.", 10.35, 11.09), ("s", "Norway ka ek student,", 11.79, 12.7), ("b", "Kristoffer Koch.", 12.7, 13.83), ("s", "Encryption pe thesis likh raha tha.", 14.49, 16.55)]),
    (17.0, 24.3, [("s", "Research ke dauraan,", 17.24, 18.28), ("s", "use bitcoin ka pata chala.", 18.62, 20.23), ("s", "Maze-maze mein laga diye", 21.15, 22.8), ("a", "₹1,200.", 22.8, 23.83)]),
    (24.3, 27.9, [("s", "Badle mein mile…", 24.49, 25.35), ("a", "5,000 BTC.", 25.82, 27.08)]),
    (27.9, 34.2, [("s", "Thesis khatam hui.", 28.05, 28.88), ("s", "Zindagi aage badh gayi.", 29.18, 30.23), ("s", "Aur bitcoin?", 30.86, 31.42), ("h", "Dimaag se nikal gaye.", 32.0, 33.52)]),
    (34.2, 42.3, [("s", "Phir 2013.", 34.46, 35.4), ("s", "News mein har taraf bitcoin.", 36.18, 38.19), ("s", "Achanak yaad aaya…", 38.95, 39.97), ("h", "“Mere paas bhi toh the!”", 40.66, 41.74)]),
    (42.3, 49.7, [("s", "Lekin wallet ka password?", 42.47, 43.7), ("b", "Yaad hi nahi.", 44.04, 44.68), ("s", "Poori raat dimaag lagaya…", 45.45, 46.65), ("s", "aur aakhirkaar,", 47.25, 47.9), ("h", "password mil gaya.", 48.25, 49.1)]),
    (49.7, 55.5, [("s", "Screen pe dikha,", 49.91, 50.77), ("a", "5,000 BTC.", 51.05, 52.15), ("s", "Keemat, lagbhag", 52.87, 53.9), ("h", "₹5 crore.", 53.9, 54.89)]),
    (55.5, 59.7, [("s", "Kuch coin beche,", 55.79, 56.87), ("s", "aur Oslo mein", 57.12, 57.9), ("b", "flat khareed liya.", 57.9, 58.93)]),
    (59.7, 64.8, [("s", "Aur aaj?", 59.93, 60.39), ("s", "Un 5,000 bitcoin ki keemat…", 61.11, 62.98), ("a", "hazaaron crore.", 63.27, 64.1)]),
    (64.8, 71.5, [("b", "Sabak?", 65.23, 65.62), ("s", "Utna hi lagao,", 66.28, 67.0), ("h", "jitna bhool sako.", 67.0, 68.0), ("s", "Aur password,", 68.49, 69.34), ("s", "hamesha sambhaal ke rakho.", 69.62, 70.8)]),
    (71.5, DUR, [("s", "Aap hote toh bechte,", 71.89, 72.8), ("b", "ya HOLD karte?", 72.8, 73.8), ("s", "Comment", 74.44, 75.02), ("a", "HOLD", 75.24, 75.65)]),
]

PROPS = [
    ("pa", 0.0, 10.1, """
      <div class="win" style="position:relative;padding-bottom:30px"><div class="wbar"><i></i><i></i><i></i><span>bitcoin purchase · <b id="yy">2009</b></span></div>
        <div class="rw" style="margin-top:24px"><span>PAID</span><b>₹1,200</b></div>
        <div class="rw"><span>RECEIVED</span><b>5,000 BTC</b></div>
        <div class="chip" id="zz" style="top:auto;bottom:-44px;right:-10px">😴 Bhool gaya…</div>
        <div class="chip" id="fl" style="top:auto;bottom:-44px;right:auto;left:30px">🏠 + Naya flat!</div></div>"""),
    ("pb", 10.1, 17.0, """
      <div class="seed" style="position:relative"><div class="sdh">UNIVERSITY · STUDENT ID</div>
        <div style="display:flex;gap:26px;margin-top:20px;align-items:center"><div class="pimg" style="width:160px;height:190px">KK</div>
        <div class="pf2"><span>NAAM</span><b>Kristoffer Koch</b><span>DESH</span><b>Norway 🇳🇴</b><span>THESIS</span><b id="th" style="opacity:0">Encryption 🔐</b></div></div></div>"""),
    ("pc", 17.0, 27.9, """
      <div class="term" style="position:relative"><div class="wbar"><i></i><i></i><i></i><span>2009 · research.txt</span></div>
        <div class="cd">reading: <span style="color:#E7B6FF">bitcoin.pdf</span><br>idea: <span style="color:#E7B6FF">"try karte hain 😄"</span></div>
        <div class="tl">SPENT</div><div class="tbig" style="font-size:64px"><b id="sp">₹0</b></div>
        <div class="tl">RECEIVED</div><div class="tbig" style="font-size:80px;padding-bottom:24px"><b id="rc">0</b> BTC</div></div>"""),
    ("pd", 27.9, 34.2, """
      <div class="seed"><div class="sdh">2009 → 2013</div>
        <div class="br"><div class="bl"><span>🎓 Thesis</span><b>DONE ✓</b></div><div class="bt2"><i id="m1" style="background:linear-gradient(90deg,#9D14FF,#C858C6);width:100%"></i></div></div>
        <div class="br"><div class="bl"><span>🧠 Bitcoin yaad?</span><b id="m2t" style="color:#E0584F">100%</b></div><div class="bt2"><i id="m2" style="background:#E0584F;width:100%"></i></div></div></div>"""),
    ("pe", 34.2, 42.3, """
      <div class="win" style="position:relative;padding-bottom:26px"><div class="wbar"><i></i><i></i><i></i><span>news · April 2013</span></div>
        <div class="nd" id="h1"><div class="ava sm">📰</div><div class="ndt">Bitcoin $100 ke paar!<br><span>BREAKING</span></div></div>
        <div class="nd" id="h2"><div class="ava sm">📈</div><div class="ndt">Bitcoin millionaires ki kahani<br><span>TRENDING</span></div></div>
        <div class="chip" id="bulb" style="top:auto;bottom:-44px;right:-10px">💡 Mere paas bhi toh the!</div></div>"""),
    ("pf", 42.3, 55.5, """
      <div class="term" style="position:relative;text-align:center"><div class="wbar"><i></i><i></i><i></i><span>wallet.dat</span></div>
        <div class="tl">ENTER PASSWORD</div><div class="pwi" id="pw" style="text-align:left">●●●●●●</div>
        <div class="tl" id="st2" style="color:#E0584F">✗ wrong password</div>
        <div class="tl">BALANCE</div><div class="tbig" style="font-size:100px"><b id="bl">🔒</b></div>
        <div class="chip" id="cr" style="position:relative;display:inline-block;right:auto;top:auto;margin:14px 0 26px">≈ ₹5 CRORE (2013)</div></div>"""),
    ("pg", 55.5, 64.8, """
      <div style="width:680px">
        <div class="seed" id="hs" style="display:flex;align-items:center;gap:24px"><div style="font-size:110px">🏠</div><div><div class="sdh">OSLO · 2013</div><b style="font-size:44px">Naya flat 🔑</b><div style="font-family:SM;font-size:22px;color:#8B7B98;margin-top:6px">kuch BTC bech ke</div></div></div>
        <div class="term" id="td" style="margin-top:26px;text-align:center"><div class="tl">5,000 BTC · AAJ</div><div class="tbig" style="font-size:72px;padding-bottom:24px">₹ HAZAARON CR</div></div></div>"""),
    ("ph", 64.8, 71.5, """
      <div class="seed"><div class="sdh">SABAK</div>
        <div class="row2"><div class="kc" id="k1"><div class="ki">💸</div><b>Utna hi lagao</b><span>jitna bhool sako</span></div><div class="kc" id="k2"><div class="ki">🔑</div><b>Password</b><span>backup rakho</span></div></div></div>"""),
    ("pi", 71.5, DUR, """
      <div class="cmt"><div class="ct">Comments</div><div class="cin"><span id="ty"></span><i id="cur">|</i><b>Post</b></div></div>
      <div class="dm" id="dm"><div class="ava sm">N</div><div><div class="dn">niks.crypto <span>sent you a message · now</span></div>
        <div class="dt">Agli crypto kahani ready hai 🙌</div><div class="dlk">niks.crypto/stories</div></div></div>
      <div class="sph" id="s1" style="left:70px"></div><div class="sph" id="s2" style="left:670px"></div>"""),
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
    CW = {"s": 27, "b": 49, "a": 51, "h": 36}
    import math
    def lh(st, txt): return LH[st] * max(1, math.ceil(len(txt) * CW[st] / 990))
    def top_for(a, b):
        hs = [sum(lh(l[0], l[1]) for l in lines) for ca, cb, lines in CAPS if ca < b - 0.01 and cb > a + 0.01]
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
      #pas > * {{ zoom:1.35; }} #pbs > * {{ zoom:1.3; }} #pcs > * {{ zoom:1.25; }} #pds > * {{ zoom:1.35; }} #pes > * {{ zoom:1.3; }} #pfs > * {{ zoom:1.22; }} #pgs > * {{ zoom:1.32; }} #phs > * {{ zoom:1.35; }} #pis > * {{ zoom:1.3; }}
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
      .room {{ position:relative; width:640px; height:620px; }}
      .shelf {{ position:absolute; left:40px; right:40px; top:150px; height:18px; border-radius:9px; background:#3A2846; }}
      .hdd {{ position:absolute; left:150px; top:-40px; width:340px; height:190px; border-radius:18px; background:linear-gradient(180deg,#C9CBD3,#8D909B); box-shadow:0 30px 50px rgba(0,0,0,.55); padding:14px 18px; color:#1A0F22; }}
      .hl1 {{ font-family:"SM"; font-weight:700; font-size:18px; letter-spacing:.06em; }}
      .platter {{ position:absolute; right:18px; top:30px; width:110px; height:110px; border-radius:50%; background:radial-gradient(circle,#E8E9EE 0 18%,#A4A7B2 19% 60%,#6F7280 61%); }}
      .platter i {{ position:absolute; left:50%; top:50%; width:60px; height:8px; margin:-4px 0 0 -6px; border-radius:4px; background:#2B2F3A; transform-origin:6px 4px; transform:rotate(-30deg); }}
      .hlab {{ position:absolute; left:18px; bottom:16px; background:#F6F0FA; border-radius:6px; padding:6px 12px; font-family:"SM"; font-size:18px; }}
      .bin {{ position:absolute; left:180px; top:300px; width:280px; height:300px; }}
      .blid {{ position:absolute; left:-20px; right:-20px; top:0; height:34px; border-radius:12px; background:#5B4A68; transform-origin:0 100%; }}
      .bbody {{ position:absolute; left:0; right:0; top:34px; bottom:0; border-radius:0 0 30px 30px; background:linear-gradient(180deg,#4A3A57,#2E2238); display:flex; align-items:center; justify-content:center; }}
      .bbody span {{ font-family:"SM"; font-weight:700; font-size:30px; color:#A99BB3; letter-spacing:.2em; }}
      .term {{ width:660px; border-radius:26px; background:#0E0812; border:1.5px solid rgba(200,88,198,.4); padding:0 0 30px; box-shadow:0 50px 100px rgba(0,0,0,.55); font-family:"SM"; }}
      .term .wbar {{ border-color:rgba(255,255,255,.08); }} .term .wbar i {{ background:#3A2846; }}
      .tl {{ padding:18px 30px 0; font-size:28px; color:#A99BB3; }} .tl.ok {{ color:#C858C6; }}
      .tbig {{ padding:20px 30px 0; font-weight:700; font-size:92px; color:#E7B6FF; text-shadow:0 0 34px rgba(200,88,198,.6); white-space:nowrap; }}
      .lap {{ position:relative; width:640px; }}
      .lap .scr {{ height:400px; border-radius:22px 22px 0 0; background:#0E0812; border:14px solid #2C2236; padding:22px 26px; font-family:"SM"; }}
      .sh {{ font-size:22px; color:#A99BB3; }} .ml {{ font-size:26px; color:#E9DDF2; margin-top:22px; opacity:0; }} .ml b {{ color:#C858C6; }}
      .lap .base {{ height:34px; margin:0 -40px; border-radius:0 0 22px 22px; background:linear-gradient(180deg,#3A2E46,#251B2E); }}
      .chip {{ position:absolute; right:-30px; top:-36px; padding:16px 26px; border-radius:40px; background:#F6F0FA; color:#7A10D8; font-family:"SM"; font-weight:700; font-size:34px; transform:rotate(5deg); box-shadow:0 20px 40px rgba(0,0,0,.45); }}
      .pit {{ position:relative; width:660px; border-radius:26px; overflow:hidden; box-shadow:0 50px 100px rgba(0,0,0,.55); }}
      .sky {{ height:90px; background:linear-gradient(180deg,#2A1838,#3A2148); display:flex; align-items:center; padding:0 26px; font-family:"SM"; font-size:22px; color:#A99BB3; letter-spacing:.14em; }}
      .lay {{ height:96px; border-top:2px dashed rgba(255,255,255,.08); }}
      .dd {{ position:absolute; left:0; right:0; bottom:20px; height:170px; }} .dd .hdd {{ left:180px; top:0; transform:scale(.7) rotate(-14deg); }}
      .tons {{ position:absolute; right:20px; top:110px; padding:16px 22px; border-radius:18px; background:#F6F0FA; color:#1A0F22; text-align:center; box-shadow:0 20px 40px rgba(0,0,0,.45); }}
      .tons b {{ display:block; font-weight:700; font-size:48px; color:#7A10D8; }} .tons span {{ font-family:"SM"; font-size:16px; color:#8B7B98; }}
      .dh {{ font-family:"SM"; font-size:22px; color:#8B7B98; margin-bottom:12px; }}
      .pin {{ position:absolute; left:150px; top:600px; padding:14px 24px; border-radius:40px; background:#F6F0FA; color:#1A0F22; font-weight:700; font-size:32px; transform:rotate(-4deg); box-shadow:0 20px 40px rgba(0,0,0,.45); white-space:nowrap; }}
      .seed {{ width:640px; border-radius:26px; padding:34px; background:#F6F0FA; color:#1A0F22; box-shadow:0 50px 100px rgba(0,0,0,.55); }}
      .sdh {{ font-family:"SM"; font-weight:700; font-size:24px; letter-spacing:.12em; color:#7A10D8; }}
      .sg {{ display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin-top:20px; }}
      .sw {{ display:flex; align-items:center; gap:10px; padding:14px; border-radius:14px; background:#ECE3F3; }}
      .sw i {{ font-style:normal; font-family:"SM"; font-size:20px; color:#8B7B98; width:30px; }} .sw span {{ flex:1; height:12px; border-radius:6px; background:#CDBDDC; }}
      .badge {{ display:inline-block; margin-top:20px; padding:12px 22px; border-radius:30px; background:linear-gradient(90deg,#9D14FF,#C858C6); color:#fff; font-family:"SM"; font-weight:700; font-size:24px; letter-spacing:.08em; }}
      .cardf {{ width:440px; height:620px; perspective:1600px; }}
      .cin2 {{ position:relative; width:100%; height:100%; transform-style:preserve-3d; }}
      .face {{ position:absolute; inset:0; border-radius:30px; backface-visibility:hidden; box-shadow:0 50px 100px rgba(0,0,0,.55); padding:34px; }}
      .front {{ background:linear-gradient(160deg,#3A1F4D,#1E1028); border:8px solid #C9A86A; text-align:center; }}
      .cft {{ font-family:"SM"; font-weight:700; font-size:36px; letter-spacing:.3em; color:#C9A86A; }}
      .art {{ margin:40px auto; width:300px; height:300px; border-radius:20px; background:radial-gradient(circle,#C858C6,#4A1670); display:flex; align-items:center; justify-content:center; font-size:150px; color:#F1D2FF; }}
      .cfb {{ font-family:"SM"; font-size:22px; color:#C9A86A; letter-spacing:.14em; }}
      .back {{ background:#F6F0FA; color:#1A0F22; transform:rotateY(180deg); display:flex; flex-direction:column; justify-content:center; }}
      .acr {{ font-size:46px; line-height:1.3; font-weight:600; color:#B3A6BE; }} .acr b {{ color:#7A10D8; font-weight:700; }}
      .acr span {{ display:block; opacity:.35; }}
      .gx {{ margin-top:30px; font-weight:700; font-size:80px; color:#7A10D8; opacity:0; }}
      .donut {{ position:relative; width:520px; height:520px; }}
      .dc {{ position:absolute; inset:0; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; }}
      .dc b {{ font-family:"SM"; font-weight:700; font-size:110px; color:#E7B6FF; }} .dc span {{ font-family:"SM"; font-size:20px; color:#A99BB3; letter-spacing:.1em; width:260px; }}
      .leak {{ position:relative; height:90px; margin:10px 30px 0; }}
      .leak i {{ position:absolute; top:0; width:30px; height:30px; border-radius:50%; background:radial-gradient(circle at 35% 30%,#F4DCFF,#B44AE0 55%,#5B0E96); opacity:0; }}
      .err {{ display:flex; gap:20px; align-items:center; margin:30px 40px 0; padding:26px; border-radius:20px; background:#FDEDEC; border:3px solid #E0584F; }}
      .eic {{ width:70px; height:70px; flex:none; border-radius:50%; background:#E0584F; color:#fff; font-weight:700; font-size:44px; display:flex; align-items:center; justify-content:center; }}
      .et {{ font-weight:700; font-size:38px; color:#B3261E; }} .es {{ font-family:"SM"; font-size:20px; color:#8B7B98; margin-top:4px; }}
      .off {{ margin:24px 40px 0; padding:30px; border-radius:20px; background:#ECE3F3; text-align:center; opacity:0; }}
      .ot {{ font-weight:700; font-size:36px; }} .os {{ font-family:"SM"; font-size:20px; color:#8B7B98; margin-top:6px; }}
      .row2 {{ display:flex; gap:20px; margin-top:22px; }}
      .kc {{ flex:1; padding:26px 20px; border-radius:22px; background:#EFFAF3; text-align:center; border:3px solid #3FBF8A; }}
      .kc.bad {{ background:#FDEDEC; border-color:#E0584F; }}
      .ki {{ font-size:70px; }} .kc b {{ display:block; font-size:32px; margin-top:8px; }} .kc span {{ font-family:"SM"; font-size:20px; color:#8B7B98; }}
      .sph {{ position:absolute; top:560px; width:90px; height:90px; border-radius:50%; background:radial-gradient(circle at 35% 30%,#F8E6FF,#C858C6 45%,#6E0FB4); box-shadow:0 20px 40px rgba(0,0,0,.5); }}
      .br {{ margin-top:26px; }} .bl {{ display:flex; justify-content:space-between; align-items:baseline; font-size:30px; }} .bl b {{ font-family:"SM"; font-size:32px; color:#7A10D8; }}
      .bt2 {{ margin-top:10px; height:44px; border-radius:22px; background:#ECE3F3; overflow:hidden; }} .bt2 i {{ display:block; height:100%; min-width:0; border-radius:22px; }}
      .mx {{ margin-top:28px; text-align:center; }} .mx b {{ display:block; font-family:"SM"; font-weight:700; font-size:110px; color:#E0584F; }} .mx span {{ font-family:"SM"; font-size:22px; color:#8B7B98; letter-spacing:.14em; }}
      .cd {{ padding:22px 30px 6px; font-size:28px; line-height:1.6; color:#E9DDF2; }} .cm2 {{ color:#8B7B98; }}
      .odo {{ margin:12px 30px 0; padding:14px 20px; border-radius:16px; background:#1E1426; font-weight:700; font-size:96px; letter-spacing:.18em; color:#E7B6FF; text-align:center; }}
      .nd {{ display:flex; align-items:center; gap:20px; margin:22px 40px 0; padding:18px 22px; border-radius:20px; background:#ECE3F3; }}
      .ndt {{ font-weight:700; font-size:32px; }} .ndt span {{ font-family:"SM"; font-weight:400; font-size:20px; color:#8B7B98; }} .nd b {{ margin-left:auto; font-size:30px; color:#2E9E6E; }}
      .dlb {{ margin:0 40px; padding:22px; border-radius:20px; background:#7A10D8; color:#fff; text-align:center; font-weight:700; font-size:36px; }}
      .chain {{ position:relative; display:flex; align-items:center; width:760px; height:300px; }}
      .blk {{ width:200px; height:200px; border-radius:26px; background:#F6F0FA; color:#1A0F22; display:flex; flex-direction:column; align-items:center; justify-content:center; font-family:"SM"; font-weight:700; font-size:34px; box-shadow:0 30px 60px rgba(0,0,0,.5); }}
      .blk span {{ font-family:"SG"; font-size:28px; color:#2E9E6E; margin-top:10px; }}
      .blk.bad {{ background:#FDEDEC; border:4px solid #E0584F; }} .blk.bad span {{ color:#E0584F; }}
      .blk.good {{ border:4px solid #C858C6; }} .blk.good span {{ color:#7A10D8; }}
      .slot2 {{ position:relative; width:200px; height:200px; }} .slot2 .blk {{ position:absolute; inset:0; }}
      .lnk {{ flex:1; height:10px; border-radius:5px; background:#C858C6; margin:0 8px; }}
      .pdh {{ font-family:"SM"; font-size:20px; color:#8B7B98; letter-spacing:.12em; }}
      .fl {{ height:16px; border-radius:8px; background:#E3D8EC; margin-top:18px; }}
      .pgc {{ margin-top:26px; font-family:"SM"; font-size:26px; color:#8B7B98; letter-spacing:.12em; }} .pgc b {{ color:#7A10D8; font-size:40px; }}
      .anon {{ margin:0 auto; width:170px; height:170px; border-radius:50%; background:linear-gradient(135deg,#9D14FF,#C858C6); color:#fff; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:100px; }}
      .pr {{ display:flex; justify-content:space-between; margin-top:16px; padding:16px 22px; border-radius:16px; background:#ECE3F3; font-size:30px; }} .pr b {{ font-family:"SM"; color:#7A10D8; }}
      .news {{ position:absolute; left:120px; top:330px; width:520px; padding:28px 32px; background:#F3EEE4; color:#1A1A1A; border-radius:6px; box-shadow:0 40px 80px rgba(0,0,0,.6); font-family:Georgia,serif; }}
      .nh {{ font-weight:700; font-size:46px; text-align:center; border-bottom:3px solid #1A1A1A; padding-bottom:8px; letter-spacing:.04em; }}
      .nd2 {{ font-family:"SM"; font-size:18px; text-align:center; margin-top:8px; color:#555; }}
      .nt {{ font-weight:700; font-size:40px; line-height:1.2; margin-top:16px; background:linear-gradient(90deg,rgba(200,88,198,.45),rgba(200,88,198,.45)) no-repeat 0 0 / 0% 100%; }}
      .kc span {{ display:block; }}
      .kc.q {{ background:#F6F0FA; border-color:#C858C6; color:#1A0F22; }} .kc.q b {{ font-size:28px; }}
      .pwi {{ margin:14px 30px 0; padding:18px 24px; border-radius:16px; background:#1E1426; font-size:44px; letter-spacing:.2em; color:#E7B6FF; }} .pwi i {{ font-style:normal; color:#C858C6; }}
      .dots {{ display:grid; grid-template-columns:repeat(5,1fr); gap:12px; margin:22px 30px 6px; }}
      .dots i {{ height:62px; border-radius:14px; background:#2C1E36; color:#A99BB3; font-style:normal; font-family:"SM"; font-weight:700; font-size:26px; display:flex; align-items:center; justify-content:center; }}
      .dots.big {{ margin:22px 0 0; }} .dots.big i {{ height:86px; font-size:32px; }}
      .rl2 {{ margin-top:22px; font-size:34px; }}
      .gl {{ font-weight:700; font-size:150px; color:#E0584F; line-height:1; text-shadow:0 0 40px rgba(224,88,79,.5); }}
      .vid {{ position:relative; margin:24px 30px 0; height:300px; border-radius:20px; background:linear-gradient(135deg,#2C1E36,#4A1670); display:flex; flex-direction:column; align-items:center; justify-content:center; }}
      .play {{ width:110px; height:110px; border-radius:50%; background:#fff; color:#7A10D8; display:flex; align-items:center; justify-content:center; font-size:50px; padding-left:8px; }}
      .vt {{ margin-top:16px; color:#fff; font-weight:700; font-size:40px; }}
      .rw {{ display:flex; justify-content:space-between; align-items:center; margin:22px 40px 0; padding:18px 24px; border-radius:18px; background:#ECE3F3; font-family:"SM"; }} .rw span {{ font-size:22px; color:#8B7B98; }} .rw b {{ font-size:44px; color:#7A10D8; }}
      .usb {{ position:absolute; left:60px; top:120px; width:520px; height:200px; transform:rotate(-8deg); display:flex; align-items:center; filter:drop-shadow(0 40px 50px rgba(0,0,0,.6)); }}
      .usbc {{ width:90px; height:90px; border-radius:10px 0 0 10px; background:linear-gradient(180deg,#D3D5DD,#8D909B); }}
      .usbb {{ flex:1; height:200px; border-radius:30px; background:linear-gradient(180deg,#2E2238,#160E1C); border:3px solid #C858C6; display:flex; flex-direction:column; justify-content:center; padding-left:40px; }}
      .usbb b {{ font-family:"SM"; font-size:52px; letter-spacing:.14em; color:#E7B6FF; }} .usbb span {{ font-family:"SM"; font-size:26px; color:#A99BB3; margin-top:6px; }}
      .note {{ position:absolute; left:360px; top:250px; width:280px; padding:22px; background:#FFF3B8; color:#3A2E00; border-radius:6px; box-shadow:0 30px 50px rgba(0,0,0,.5); }}
      .nh2 {{ font-family:"SM"; font-size:22px; }} .nv {{ font-family:"SM"; font-weight:700; font-size:36px; margin-top:6px; }}
      .lb {{ margin-top:70px; text-align:center; font-family:"SM"; font-size:40px; color:#A99BB3; }} .lb b {{ display:block; font-size:110px; color:#E7B6FF; text-shadow:0 0 34px rgba(200,88,198,.6); }}
      .srl {{ padding:22px 30px 6px; font-weight:700; font-size:54px; color:#E7B6FF; font-family:"SG"; }} .srl span {{ display:block; font-family:"SM"; font-weight:400; font-size:22px; color:#8B7B98; letter-spacing:.1em; }}
      .it {{ display:flex; align-items:center; gap:18px; margin:14px 30px 0; padding:16px 20px; border-radius:16px; background:#1E1426; font-size:28px; }}
      .it i {{ width:56px; height:56px; border-radius:12px; background:#3A2846; }} .bl2 {{ flex:1; color:#6D5F78; filter:blur(3px); }} .it b {{ color:#E7B6FF; }}
      .scene {{ position:relative; width:760px; height:680px; text-align:center; }}
      .lpw {{ position:absolute; left:60px; top:110px; }} .lpw .lap {{ transform:scale(.82); transform-origin:0 0; }}
      .cp {{ position:absolute; left:0; top:470px; display:flex; align-items:center; gap:16px; padding:16px 24px; border-radius:22px; background:#F6F0FA; color:#1A0F22; box-shadow:0 20px 40px rgba(0,0,0,.45); text-align:left; }}
      .cp b {{ display:block; font-size:32px; }} .cp span {{ font-family:"SM"; font-size:22px; color:#E0584F; }}
      .ag {{ position:absolute; right:50px; top:420px; padding:18px 26px; border-radius:40px; background:#7A10D8; color:#fff; font-weight:700; font-size:34px; box-shadow:0 20px 40px rgba(0,0,0,.45); }}
      .ucoin {{ margin:20px auto 10px; width:240px; height:240px; border-radius:50%; background:radial-gradient(circle at 35% 30%,#F4DCFF,#B44AE0 55%,#5B0E96); color:#fff; display:flex; flex-direction:column; align-items:center; justify-content:center; font-weight:700; font-size:64px; box-shadow:0 20px 40px rgba(0,0,0,.4); }}
      .ucoin span {{ font-family:"SM"; font-size:34px; }}
      .crowd {{ display:flex; justify-content:center; gap:8px; font-size:48px; margin-top:6px; }} .crowd i {{ font-style:normal; }}
      .sells {{ display:flex; gap:16px; justify-content:center; padding:10px 0 24px; }} .sells span {{ padding:10px 26px; border-radius:30px; background:#E0584F; color:#fff; font-weight:700; font-size:30px; }}
      .prt {{ margin:20px auto 28px; display:inline-block; padding:14px 30px; border-radius:20px; background:#1E1426; font-size:40px; color:#E7B6FF; }}
      .pass {{ width:680px; padding:34px; border-radius:24px; background:#F3EEE4; color:#1A1A1A; box-shadow:0 50px 100px rgba(0,0,0,.55); }}
      .ph2 {{ font-family:"SM"; font-weight:700; font-size:34px; letter-spacing:.3em; color:#7A10D8; border-bottom:3px solid #CBBFD6; padding-bottom:12px; }}
      .pimg {{ width:180px; height:220px; flex:none; border-radius:14px; background:linear-gradient(135deg,#9D14FF,#C858C6); color:#fff; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:64px; }}
      .pf2 span {{ display:block; font-family:"SM"; font-size:18px; color:#8B7B98; letter-spacing:.1em; margin-top:8px; }} .pf2 b {{ display:block; font-size:36px; }}
      .ugrid {{ display:grid; grid-template-columns:repeat(6,1fr); gap:10px; margin-top:20px; font-size:58px; }} .ugrid i {{ font-style:normal; }}
      .chainv {{ width:660px; }}
      .cn2 {{ position:relative; display:flex; align-items:center; gap:18px; padding:14px 22px; border-radius:20px; background:#F6F0FA; color:#1A0F22; border:3px solid transparent; box-shadow:0 20px 40px rgba(0,0,0,.4); }}
      .cn2.me {{ border-color:#C858C6; }}
      .ce {{ font-size:50px; }} .ct2 b {{ display:block; font-size:32px; }} .ct2 span {{ font-family:"SM"; font-size:18px; color:#8B7B98; letter-spacing:.08em; text-transform:uppercase; }}
      .cam {{ margin-left:auto; font-family:"SM"; font-size:30px; color:#7A10D8; }}
      .lk {{ position:absolute; right:-22px; top:-18px; font-style:normal; font-size:44px; opacity:0; }}
      .arw {{ text-align:center; font-size:34px; color:#C858C6; line-height:1.1; font-weight:700; }}
      .rl3 {{ display:flex; gap:20px; align-items:center; margin-top:18px; padding:18px 22px; border-radius:20px; background:#ECE3F3; }}
      .rl3 span.rn {{ font-family:"SG"; font-size:32px; color:#fff; }}
      .rl3.bad {{ background:#FDEDEC; margin-left:60px; }} .rl3.bad .rn {{ background:#E0584F; }}
      .rn {{ width:60px; height:60px; flex:none; border-radius:50%; background:linear-gradient(135deg,#9D14FF,#C858C6); color:#fff; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:32px; }}
      .rl3 b {{ display:block; font-size:33px; }} .rl3 span {{ font-family:"SM"; font-size:20px; color:#8B7B98; }}
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
      const typ = (id, word, t, d) => {{ const o = {{ n: 0 }}; tl.fromTo(o, {{ n: 0 }}, {{ n: word.length, duration: d, ease: "none", onUpdate: () => {{ document.querySelector(id).textContent = word.slice(0, Math.round(o.n)); }} }}, t); }};
      const IN = (v) => Math.round(v).toLocaleString("en-IN");
      // A purchase -> forgot -> flat
      pop("#zz", 4.1, 4); tl.to("#pas .rw", {{ opacity: 0.35, filter: "blur(2px)", duration: 0.5 }}, 4.3);
      num("#yy", 2009, 2013, 6.03, 1.2, (v) => String(Math.round(v)));
      tl.to("#pas .rw", {{ opacity: 1, filter: "blur(0px)", duration: 0.3 }}, 7.3); pop("#fl", 8.2, -3);
      // B student id
      tl.to("#th", {{ opacity: 1, duration: 0.3 }}, 14.49); pop("#th", 14.49, 0);
      // C spent + received
      num("#sp", 0, 1200, 22.8, 1.0, (v) => "₹" + IN(v));
      num("#rc", 0, 5000, 25.82, 1.3, IN);
      // D memory fades
      tl.to("#m2", {{ width: "0%", duration: 1.5, ease: "power2.in" }}, 32.0);
      num("#m2t", 100, 0, 32.0, 1.5, (v) => Math.round(v) + "%");
      // E news + bulb
      pop("#h1", 36.18, 0); pop("#h2", 37.2, 0); pop("#bulb", 40.66, -3);
      // F password hunt
      tl.set("#st2", {{ opacity: 0 }}, 42.3);
      ["koch2009", "oslo123", "thesis!", "kristoffer"].forEach((g, i) => {{ tl.set("#pw", {{ textContent: g }}, 45.45 + i * 0.45); tl.set("#st2", {{ opacity: 1 }}, 45.6 + i * 0.45); }});
      tl.set("#pw", {{ textContent: "●●●●●●●●●" }}, 48.25); tl.set("#st2", {{ textContent: "✓ unlocked", color: "#3FBF8A" }}, 48.25);
      tl.set("#bl", {{ textContent: "🔒" }}, 42.35); tl.set("#bl", {{ textContent: "0" }}, 49.9); num("#bl", 0, 5000, 51.05, 1.1, (v) => IN(v));
      pop("#cr", 53.9, -3);
      // G flat + today
      pop("#hs", 55.79, 0); tl.set("#td", {{ opacity: 0 }}, 55.5); pop("#td", 61.11, 0);
      tl.fromTo("#td .tbig", {{ scale: 0.8 }}, {{ scale: 1, duration: 0.4, ease: "back.out(2)" }}, 63.27);
      // H lesson
      pop("#k1", 66.28, -2); pop("#k2", 68.49, 2);
      // I comment + DM + spheres
      typ("#ty", "HOLD", 75.24, 0.4);
      tl.fromTo("#cur", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.4, yoyo: true, repeat: 7, ease: "steps(1)" }}, 71.6);
      tl.fromTo("#dm", {{ y: 40, opacity: 0, scale: 0.95 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.4, ease: "back.out(2)" }}, 75.7);
      ["#s1", "#s2"].forEach((s, i) => tl.fromTo(s, {{ y: -900, opacity: 1 }}, {{ y: 0, duration: 0.7, ease: "bounce.out" }}, 72.0 + i * 0.3));
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''
    open(os.path.join(HERE, "hf", "index.html"), "w").write(html)
    print("captions:", len(CAPS), "props:", len(PROPS))


if __name__ == "__main__":
    build()
