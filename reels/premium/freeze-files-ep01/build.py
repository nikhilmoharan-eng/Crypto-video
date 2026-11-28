"""Freeze Files EP 01 · Freeze ka raasta — v2, built to the reference grammar (thebigaistory-style) in the purple palette.

Grammar copied from the references:
- small handle at the top, sentence captions near the top that grow word by word
  (s = small regular, b = bold, a = accent gradient, h = highlight bar that wipes in)
- one compact, realistic prop mid-screen that PERSISTS and evolves across several sentences
- small sticker cards / stamps pop onto the prop; numbers count up on the prop
- ending: comment being typed + DM reply + glossy spheres
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 83.3

CAPS = [
    (0.0, 8.1, [("s", "Aapka bank account", 0.0, 0.9), ("a", "FREEZE hua.", 0.9, 1.83), ("s", "Lekin kisne kiya?", 2.59, 3.46), ("b", "Police? Bank?", 4.31, 5.92), ("h", "Ya koi aur?", 6.54, 7.33)]),
    (8.1, 14.6, [("s", "Aaj samjhte hain,", 8.64, 9.6), ("h", "freeze ka poora raasta.", 9.6, 10.98), ("s", "Ek shikayat se,", 11.65, 12.48), ("a", "aapke account tak.", 12.8, 13.82)]),
    (14.6, 21.9, [("b", "Step 1.", 15.35, 16.06), ("s", "Koi scam ka shikaar hota hai.", 16.8, 18.6), ("s", "Wo cyber helpline", 19.12, 20.3), ("a", "1930", 20.3, 21.71)]),
    (21.9, 25.0, [("s", "ya cybercrime portal pe", 22.05, 23.2), ("h", "shikayat karta hai.", 23.2, 24.17)]),
    (25.0, 34.6, [("b", "Step 2.", 25.47, 26.05), ("s", "Shikayat seedhe us bank tak,", 26.8, 28.4), ("s", "jisme victim ka paisa gaya.", 28.4, 30.15), ("s", "Bank dekhta hai,", 30.85, 31.63), ("h", "paisa aage kahan gaya.", 32.08, 33.8)]),
    (34.6, 43.3, [("b", "Step 3.", 35.26, 35.9), ("s", "Paisa jin accounts se guzra,", 36.5, 38.41), ("s", "har bank ko alert jaata hai.", 38.62, 40.07), ("s", "Aur wo accounts,", 40.58, 41.37), ("a", "HOLD pe.", 41.87, 42.41)]),
    (43.3, 51.3, [("s", "Aapne P2P pe crypto becha,", 43.69, 45.83), ("s", "aur buyer ne wahi paisa bheja…", 46.07, 47.58), ("s", "toh us chain mein,", 48.22, 49.06), ("h", "aapka account bhi aa gaya.", 49.26, 50.43)]),
    (51.3, 59.2, [("b", "Step 4.", 52.04, 52.76), ("s", "Police jaanch karti hai.", 53.46, 55.06), ("s", "Aur jab tak jaanch chalti hai,", 55.61, 56.89), ("h", "freeze bana rehta hai.", 57.28, 58.34)]),
    (59.2, 64.8, [("s", "Yaani,", 59.83, 60.22), ("s", "freeze karwaati hai", 60.56, 61.6), ("b", "police ki shikayat,", 61.6, 62.8), ("s", "aur lagaata hai", 62.8, 63.5), ("a", "aapka bank.", 63.5, 64.2)]),
    (64.8, 75.7, [("s", "Isliye freeze ho toh pehle", 65.05, 66.77), ("s", "bank se poochho:", 67.03, 67.89), ("s", "kaunsa police station,", 68.44, 69.9), ("h", "kaunsa complaint number?", 69.9, 71.81), ("s", "Yahi jaankari", 72.69, 73.48), ("s", "aage sab kuch kholti hai.", 73.73, 75.11)]),
    (75.7, DUR, [("s", "Agle episode mein:", 75.93, 77.49), ("h", "lien vs full freeze.", 77.71, 79.38), ("s", "Follow karo, comment karo,", 80.06, 81.6), ("a", "FREEZE", 81.7, 82.29)]),
]

STEPS = [("📞", "Victim → 1930 / portal", "scam ki shikayat"), ("🏦", "Victim ka bank", "paisa trace karta hai"),
         ("🔗", "Har account pe alert", "accounts HOLD pe"), ("👮", "Police jaanch", "tab tak freeze jaari")]
ROUTE = '<div class="seed route"><div class="sdh">🔒 FREEZE ROUTE</div>' + "".join(
    f'<div class="stp" id="st{i}"><span class="rn">{i+1}</span><div class="stx"><b>{e} {t}</b><span>{d}</span></div><i class="sck" id="sk{i}">✓</i></div>'
    + (f'<div class="sar" id="sa{i}">↓</div>' if i < 3 else "") for i, (e, t, d) in enumerate(STEPS)) + \
    '<div class="mch" id="mch"><span>Acc 1 🔒</span><span>Acc 2 🔒</span><span>Buyer 🔒</span><span class="me" id="me">🧑 Aap 🔒</span></div></div>'

PROPS = [
    ("pa", 0.0, 8.1, """
      <div style="width:680px;position:relative">
        <div class="win" style="padding-bottom:26px;width:680px"><div class="wbar"><i></i><i></i><i></i><span>bank app</span></div>
          <div class="rw" style="margin-top:22px"><span>BALANCE</span><b>₹84,250</b></div>
          <div class="err" id="fz"><div class="eic">🔒</div><div><div class="et">Account frozen</div><div class="es">DEBIT FREEZE · REASON: ???</div></div></div></div>
        <div class="sus"><span id="q1">👮 Police?</span><span id="q2">🏦 Bank?</span><span id="q3">❓ Koi aur?</span></div></div>"""),
    ("pb", 8.1, 59.2, ROUTE),
    ("pc", 59.2, 64.8, """
      <div style="width:700px"><div class="row2">
        <div class="kc q" id="w1"><div class="ki">👮</div><b>Police shikayat</b><span>freeze KARWAATI</span></div>
        <div class="kc q" id="w2"><div class="ki">🏦</div><b>Aapka bank</b><span>freeze LAGAATA</span></div></div></div>"""),
    ("pd", 64.8, 75.7, """
      <div class="pass" style="position:relative"><div class="ph2" style="font-size:26px">📝 BANK SE POOCHHO</div>
        <div class="fill"><span>🏢 Police station</span><b id="f1">__________</b></div>
        <div class="fill"><span>#️⃣ Complaint / Ack no.</span><b id="f2">__________</b></div>
        <div class="fill"><span>💰 Kitna amount hold?</span><b id="f3">__________</b></div>
        <div class="chip" id="key" style="top:auto;bottom:-40px;right:-10px">🔑 Yahi se raasta khulta hai</div></div>"""),
    ("pe", 75.7, DUR, """
      <div class="cmt"><div class="ct">Comments</div><div class="cin"><span id="ty"></span><i id="cur">|</i><b>Post</b></div></div>
      <div class="dm" id="dm"><div class="ava sm">N</div><div><div class="dn">niks.crypto <span>sent you a message · now</span></div>
        <div class="dt">Freeze Files EP 02: Lien vs Full freeze 🔜</div><div class="dlk">niks.crypto/freeze-files</div></div></div>
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
      #pas > * {{ zoom:1.3; }} #pbs > * {{ zoom:1.18; }} #pcs > * {{ zoom:1.35; }} #pds > * {{ zoom:1.3; }} #pes > * {{ zoom:1.3; }}
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
      .stg {{ position:relative; margin:18px 30px 10px; height:280px; border-radius:20px; background:radial-gradient(circle at 50% 0%,#4A1670,#160E1C 70%); display:flex; flex-direction:column; align-items:center; justify-content:center; overflow:hidden; }}
      .spot {{ position:absolute; left:50%; top:-40px; width:340px; height:420px; margin-left:-170px; background:radial-gradient(ellipse at 50% 0%,rgba(241,210,255,.35),transparent 70%); }}
      .shout {{ font-family:"SG"; font-weight:700; font-size:54px; letter-spacing:-.02em; color:#F1D2FF; text-shadow:0 0 30px rgba(200,88,198,.8); line-height:1.05; }}
      .pyr {{ margin-top:14px; }} .prow {{ display:flex; justify-content:center; gap:8px; font-size:46px; margin-top:6px; }} .prow i {{ font-style:normal; }}
      .flow {{ display:flex; align-items:center; justify-content:center; gap:16px; margin-top:24px; }}
      .fb {{ width:230px; padding:20px; border-radius:20px; background:#ECE3F3; font-size:60px; }} .fb b {{ display:block; font-size:30px; margin-top:6px; }} .fb span {{ font-family:"SM"; font-size:20px; color:#8B7B98; }}
      .far {{ font-size:60px; color:#C858C6; font-weight:700; }}
      .wl {{ font-size:28px; line-height:1.55; color:#E9DDF2; }}
      .crown {{ position:absolute; right:-14px; top:-40px; font-size:70px; transform:rotate(18deg); }}
      .anon {{ font-size:72px; }}
      .ppl {{ display:grid; grid-template-columns:repeat(5,1fr); gap:10px; margin-top:18px; font-size:64px; }} .ppl i {{ font-style:normal; }}
      .bcoin {{ position:absolute; left:-30px; top:-40px; width:110px; height:110px; border-radius:50%; background:radial-gradient(circle at 35% 30%,#F4DCFF,#B44AE0 55%,#5B0E96); color:#fff; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:64px; box-shadow:0 20px 40px rgba(0,0,0,.45); }}
      .flags {{ display:flex; justify-content:center; gap:18px; margin-top:22px; font-size:70px; }}
      #handle {{ color:rgba(255,255,255,.5); }} .hb2 {{ display:inline-block; padding:8px 22px; border-radius:30px; border:1.5px solid rgba(200,88,198,.55); background:rgba(157,20,255,.12); font-family:"SM"; font-weight:700; font-size:24px; letter-spacing:.14em; color:#E7B6FF; }}
      .sus {{ display:flex; justify-content:center; gap:16px; margin-top:26px; }} .sus span {{ padding:14px 22px; border-radius:30px; background:#F6F0FA; color:#1A0F22; font-weight:700; font-size:30px; box-shadow:0 20px 40px rgba(0,0,0,.4); }}
      .route {{ width:680px; }}
      .stp {{ position:relative; display:flex; align-items:center; gap:18px; margin-top:12px; padding:16px 20px; border-radius:20px; background:#ECE3F3; border:3px solid transparent; }}
      .stx b {{ display:block; font-size:32px; transform-origin:0 50%; }} .stx span {{ font-family:"SM"; font-size:20px; color:#8B7B98; }}
      .stp .rn {{ width:56px; height:56px; flex:none; border-radius:50%; background:linear-gradient(135deg,#9D14FF,#C858C6); color:#fff; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:28px; }}
      .sck {{ margin-left:auto; font-style:normal; font-size:34px; color:#2E9E6E; font-weight:700; }}
      .sar {{ text-align:center; font-size:30px; color:#C858C6; font-weight:700; line-height:1; margin-top:8px; }}
      .mch {{ display:flex; flex-wrap:wrap; gap:10px; margin-top:16px; padding:14px; border-radius:18px; background:#FDEDEC; border:2px dashed #E0584F; }}
      .mch span {{ padding:8px 14px; border-radius:14px; background:#fff; font-family:"SM"; font-weight:700; font-size:22px; color:#B3261E; }} .mch .me {{ background:#E0584F; color:#fff; }}
      .fill {{ display:flex; justify-content:space-between; align-items:center; gap:16px; margin-top:20px; padding:16px 20px; border-radius:16px; background:#ECE3F3; font-size:28px; }}
      .fill b {{ font-family:"SM"; font-size:26px; color:#B3A6BE; white-space:nowrap; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
      <div id="bgc" class="clip" data-start="0" data-duration="{DUR}" data-track-index="0"><div id="bg"></div><div id="glow"></div><div id="grid"></div><div id="handle"><span class="hb2">🔒 FREEZE FILES · EP 01</span></div></div>
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
      const lite = (i, t) => {{ tl.to("#st" + i, {{ opacity: 1, background: "#F1E3FF", borderColor: "#C858C6", duration: 0.3 }}, t); pop("#st" + i + " .rn", t, 0); }};
      const done = (i, t) => {{ tl.to("#st" + i, {{ background: "#ECE3F3", borderColor: "transparent", duration: 0.3 }}, t); pop("#sk" + i, t, 0); }};
      // A frozen + who?
      tl.set("#fz", {{ opacity: 0.2, scale: 1, rotation: 0 }}, 0.01); pop("#fz", 0.9, 0); tl.to("#pas .win", {{ x: 10, duration: 0.05, yoyo: true, repeat: 5, ease: "none" }}, 1.0);
      pop("#q1", 4.31, -4); pop("#q2", 5.35, 3); pop("#q3", 6.54, -2);
      // B route builds step by step
      tl.set([".stp", ".sar"], {{ opacity: 0.22 }}, 8.15); tl.set("#mch", {{ opacity: 0.22 }}, 8.15); tl.set("#mch span:not(.me)", {{ opacity: 1, y: 0 }}, 8.16); tl.set(".sck", {{ opacity: 0 }}, 8.15);
      tl.to([".stp", ".sar"], {{ opacity: 0.45, duration: 0.25, stagger: 0.12 }}, 9.6);
      lite(0, 15.35); tl.fromTo("#st0 .stx b", {{ scale: 1 }}, {{ scale: 1.06, duration: 0.2, yoyo: true, repeat: 1 }}, 20.3);
      done(0, 25.3); tl.to("#sa0", {{ opacity: 1, duration: 0.2 }}, 25.3); lite(1, 25.47);
      done(1, 35.1); tl.to("#sa1", {{ opacity: 1, duration: 0.2 }}, 35.1); lite(2, 35.26);
      tl.to("#mch", {{ opacity: 1, duration: 0.3 }}, 38.62); tl.fromTo("#mch span:not(.me)", {{ opacity: 0, y: 10 }}, {{ opacity: 1, y: 0, duration: 0.2, stagger: 0.5 }}, 38.7);
      tl.set("#me", {{ opacity: 0 }}, 38.65); pop("#me", 49.26, 0); tl.to("#me", {{ x: 6, duration: 0.05, yoyo: true, repeat: 7, ease: "none" }}, 49.6);
      done(2, 51.9); tl.to("#sa2", {{ opacity: 1, duration: 0.2 }}, 51.9); lite(3, 52.04);
      // C who does what
      pop("#w1", 61.6, -3); pop("#w2", 63.5, 3);
      // D ask the bank
      typ("#f1", "Cyber PS, ______", 68.44, 0.8); tl.set("#f1", {{ color: "#7A10D8" }}, 68.44);
      typ("#f2", "Ack no. 3XXXXXXXXXXX", 69.9, 1.0); tl.set("#f2", {{ color: "#7A10D8" }}, 69.9);
      typ("#f3", "₹____ (lien?)", 71.3, 0.6); tl.set("#f3", {{ color: "#7A10D8" }}, 71.3);
      tl.set("#key", {{ opacity: 0 }}, 64.8); pop("#key", 73.73, -3);
      // E comment + DM + spheres
      typ("#ty", "FREEZE", 81.7, 0.5);
      tl.fromTo("#cur", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.4, yoyo: true, repeat: 7, ease: "steps(1)" }}, 75.8);
      tl.fromTo("#dm", {{ y: 40, opacity: 0, scale: 0.95 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.4, ease: "back.out(2)" }}, 77.71);
      ["#s1", "#s2"].forEach((s, i) => tl.fromTo(s, {{ y: -900, opacity: 1 }}, {{ y: 0, duration: 0.7, ease: "bounce.out" }}, 76.2 + i * 0.3));
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''
    open(os.path.join(HERE, "hf", "index.html"), "w").write(html)
    print("captions:", len(CAPS), "props:", len(PROPS))


if __name__ == "__main__":
    build()
