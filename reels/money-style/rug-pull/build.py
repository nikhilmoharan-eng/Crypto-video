"""Case 04 Rug Pull in the niks.finance "card" style on the blue gradient background.

Writes hf/index.html (HyperFrames). Captions reveal word by word; {g:word} / {r:word} / {b:word} = coloured keyword pill.
"""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 46.9

PHRASES = [
    (0.00, 0.96, "Scam Files."),
    (1.51, 2.38, "Case number {b:chaar.}"),
    (2.92, 3.74, "Ek naya {b:token.}"),
    (4.24, 5.23, "Website {g:chamakdaar.}"),
    (5.79, 6.61, "Roadmap {g:bada.}"),
    (7.28, 9.96, "Influencers bol rahe hain, {g:\"Next big thing!\"}"),
    (10.81, 11.84, "Log {b:paisa} daalte hain."),
    (12.77, 13.54, "Price {g:badhta} hai."),
    (14.90, 17.79, "Ek raat… developers saara paisa nikaal ke {r:gayab.}"),
    (18.66, 19.93, "Ise kehte hain, {r:rug pull.}"),
    (20.72, 23.43, "Jaise kisi ke pairon ke neeche se, {r:kaleen} kheench lena."),
    (24.38, 25.54, "Token ki value {r:zero.}"),
    (26.27, 27.04, "Website {r:band.}"),
    (27.66, 28.74, "Twitter {r:delete.}"),
    (29.91, 31.75, "Toh naya token kharidne se pehle, {b:socho:}"),
    (32.54, 34.46, "team {g:asli} hai ya {r:anonymous?}"),
    (35.20, 36.73, "{b:Liquidity lock} hai ya nahi?"),
    (37.50, 40.35, "Aur kya sirf {r:hype} hai, ya koi {g:asli product} bhi hai?"),
    (41.29, 43.83, "Jitna bada promise, utna bada {r:red flag.}"),
    (45.10, 45.87, "{b:Case} closed."),
]

# card windows
CARDS = [("k1", 0.0, 2.7), ("k2", 2.7, 10.4), ("k3", 10.4, 14.4), ("k4", 14.4, 18.4), ("k5", 18.4, 24.0),
         ("k6", 24.0, 29.5), ("k7", 29.5, 40.9), ("k8", 40.9, 44.8), ("k9", 44.8, DUR)]

TRACK = [("🚀", "Launch", 2.7), ("📣", "Hype", 7.28), ("💰", "Pool", 10.4), ("🌙", "3 AM", 14.4), ("🧹", "Rug", 18.4),
         ("💀", "$0", 24.0), ("✅", "Check", 29.5), ("🚩", "Lesson", 40.9)]

COL = {"g": "#22A45D", "r": "#E5484D", "b": "#2F6FD8"}


def words(phr):
    out = []
    for s, e, text in phr:
        toks = re.findall(r"\{[grb]:[^}]+\}|\S+", text)
        w = [max(2, len(re.sub(r"\{[grb]:|\}", "", t))) for t in toks]
        tot, acc = sum(w), 0
        items = []
        for t, wi in zip(toks, w):
            m = re.match(r"\{([grb]):(.+)\}", t)
            items.append({"t": round(s + (e - s) * acc / tot, 2), "text": m.group(2) if m else t, "k": m.group(1) if m else None})
            acc += wi
        out.append((s, e, items))
    return out


def card(cid, inner, top=600, h=620):
    a, b = [(x, y) for k, x, y in CARDS if k == cid][0]
    n = [k for k, _, _ in CARDS].index(cid)
    tag = f'<div class="exh">EXHIBIT #{n:02d}</div>' if 0 < n < len(CARDS) - 1 else ""
    return (f'      <div id="{cid}" class="clip cardwrap" data-start="{a}" data-duration="{round(b-a,2)}" data-track-index="3">'
            f'<div class="card" id="{cid}c" style="top:{top}px;min-height:{min(h, 440)}px">{inner}{tag}</div></div>')


ICON_BANK = '<svg viewBox="0 0 64 64" width="{s}" height="{s}"><path d="M32 6 L60 20 H4 Z" fill="#111"/><g fill="#111"><rect x="9" y="24" width="7" height="24"/><rect x="22" y="24" width="7" height="24"/><rect x="35" y="24" width="7" height="24"/><rect x="48" y="24" width="7" height="24"/></g><rect x="4" y="50" width="56" height="6" fill="#111"/></svg>'
PERSON = '<svg viewBox="0 0 40 52" width="{w}" height="{h}"><circle cx="20" cy="12" r="10" fill="{c}"/><path d="M2 52 Q2 26 20 26 Q38 26 38 52Z" fill="{c}"/></svg>'


def ppl(n, w, c):
    return "".join(f'<span class="pp">{PERSON.format(w=w, h=int(w*1.3), c=c)}</span>' for _ in range(n))


def chart(pid, pts, color, w=820, h=360, extra=""):
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}"><g stroke="#e6e9ef" stroke-width="2"><line x1="0" y1="{h*0.33:.0f}" x2="{w}" y2="{h*0.33:.0f}"/>'
            f'<line x1="0" y1="{h*0.66:.0f}" x2="{w}" y2="{h*0.66:.0f}"/></g>'
            f'<polyline id="{pid}" points="{pts}" fill="none" stroke="{color}" stroke-width="10" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="2000" stroke-dashoffset="2000"/>{extra}</svg>')


def build():
    W = words(PHRASES)
    caps = []
    for i, (s, e, items) in enumerate(W):
        nxt = W[i + 1][0] if i + 1 < len(W) else DUR
        end = round(min(nxt, e + 0.6), 2)
        spans = "".join((f'<span class="w kw" style="background:{COL[it["k"]]}" data-t="{it["t"]}">{it["text"]}</span> ' if it["k"]
                         else f'<span class="w" data-t="{it["t"]}">{it["text"]}</span> ') for it in items)
        caps.append(f'      <div id="cap{i}" class="clip cap" data-start="{s}" data-duration="{round(end-s,2)}" data-track-index="5"><div class="cl">{spans}</div></div>')

    cards = [
        card("k1", '''<div class="lab">SCAM FILES</div>
          <svg id="fold" viewBox="0 0 120 90" width="300" height="225" style="margin-top:20px"><path d="M6 14 h40 l8 10 h60 v60 h-108z" fill="#F4C84A" stroke="#111" stroke-width="4"/><rect x="6" y="30" width="108" height="54" fill="#FFD866" stroke="#111" stroke-width="4"/></svg>
          <div class="stampc" id="k1s">CASE #04</div>'''),
        card("k2", '''<div class="row1"><div class="av" style="background:linear-gradient(135deg,#7CC0FF,#B98CFF)">🌙</div><div><div class="t1">$MOON token</div><div class="t2">moontoken.xyz · EXAMPLE</div></div></div>
          <div class="hero" id="k2h">Next big thing 🚀</div>
          <div class="rm" id="k2r"><span>Q1 Launch ✓</span><span>Q2 Exchange</span><span>Q3 Moon 🌕</span></div>
          <div class="msg" id="m1">@influencer: "100x gem, abhi lo!" 🔥</div>''', h=660),
        card("k3", '''<div class="lab">LIQUIDITY POOL</div>
          <div class="hugeg" id="k3n" style="font-size:150px;margin-top:40px">$0</div>
          <div class="crowd" id="k3c">''' + ppl(10, 46, "#2F6FD8") + '''</div>
          <div class="sub" id="k3t" style="color:#22A45D">Price ▲</div>'''),
        card("k4", '''<div class="lab">EK RAAT · 3:12 AM</div>
          <div class="pool"><div class="pf" id="k4p"></div><div class="pl" id="k4n">$2,400,000</div></div>
          <div class="msg" id="m2" style="background:#FFF1F1;color:#E5484D">Dev wallet: removed ALL liquidity</div>
          <div class="stampc" id="k4x" style="margin-top:26px">RUG PULLED</div>'''),
        card("k5", '''<div class="lab">RUG PULL = KALEEN KHEENCH</div>
          <div class="rugw"><div class="figs" id="k5f">''' + ppl(4, 70, "#111") + '''</div><div class="rug" id="k5r"></div></div>'''),
        card("k6", '''<div class="lab">AB?</div>
          <div class="hugeg" id="k6v" style="font-size:180px;color:#E5484D;margin-top:20px">$0.00</div>
          <div class="dead" id="k6a">🌐 moontoken.xyz — <b>site can't be reached</b></div>
          <div class="dead" id="k6b">🐦 @moontoken — <b>account deleted</b></div>''', h=640),
        card("k7", '''<div class="lab">KHARIDNE SE PEHLE · SOCHO</div>
          <div class="ck" id="c1"><span class="ok">?</span><div><div class="t1">Team asli ya anonymous?</div><div class="t2">naam, chehra, history</div></div></div>
          <div class="ck" id="c2"><span class="ok">?</span><div><div class="t1">Liquidity locked?</div><div class="t2">lock hai toh nikal nahi sakte</div></div></div>
          <div class="ck" id="c3"><span class="ok">?</span><div><div class="t1">Asli product ya sirf hype?</div><div class="t2">kaam karta hai kuch?</div></div></div>''', h=660),
        card("k8", '''<div class="lesson">LESSON</div>
          <div class="scale"><div class="sc1" id="k8a">Bada promise 🚀</div><div class="eq">=</div><div class="sc2" id="k8b">Bada red flag 🚩</div></div>''', h=520),
        card("k9", '''<div class="prof"><div class="pav">₿</div><div><div class="t1">niks.crypto</div><div class="t2">Crypto · Scams · Money</div></div></div>
          <div class="btns"><div class="fbtn" id="fb"><span id="fb1">Follow</span><span id="fb2">Following ✓</span></div><div class="mbtn">Message</div></div>
          <svg id="cur" viewBox="0 0 24 24" width="64" height="64" style="position:absolute;left:0;top:0"><path d="M4 2 L4 20 L9 15 L12 22 L15 21 L12 14 L19 14 Z" fill="#111" stroke="#fff" stroke-width="1.5"/></svg>''', top=700, h=380),
    ]

    html = f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="assets/gsap.min.js"></script>
    <style>
      @font-face {{ font-family:"IN"; font-weight:400; src:url("assets/fonts/inter-latin-400-normal.woff2"); }}
      @font-face {{ font-family:"IN"; font-weight:700; src:url("assets/fonts/inter-latin-700-normal.woff2"); }}
      @font-face {{ font-family:"IN"; font-weight:800; src:url("assets/fonts/inter-latin-800-normal.woff2"); }}
      @font-face {{ font-family:"IN"; font-weight:900; src:url("assets/fonts/inter-latin-900-normal.woff2"); }}
      * {{ margin:0; padding:0; box-sizing:border-box; }}
      html, body {{ width:1080px; height:1920px; overflow:hidden; background:#0B1F4A; }}
      #root {{ position:absolute; inset:0; font-family:"IN",sans-serif; color:#111; overflow:hidden; }}
      #bg {{ position:absolute; inset:0; background:linear-gradient(160deg,#8EA6C6 0%,#8FA4BF 30%,#3A6CC6 55%,#0F2C58 80%,#0A2350 100%); overflow:hidden; }}
      .blob {{ position:absolute; border-radius:50%; filter:blur(40px); }}
      #lines {{ position:absolute; left:0; top:0; }}
      #grain {{ position:absolute; left:0; top:0; mix-blend-mode:overlay; opacity:.22; }}
      #dots {{ position:absolute; inset:-68px 0 0 0; background-image:radial-gradient(rgba(255,255,255,.16) 1.6px, transparent 1.8px); background-size:34px 34px; }}
      .pills {{ position:absolute; left:0; right:0; top:230px; display:flex; justify-content:center; gap:14px; }}
      .pill {{ padding:14px 26px; border-radius:40px; font-weight:800; font-size:30px; }}
      .pd {{ background:#0B1F4A; color:#fff; }} .pd i {{ display:inline-block; width:14px; height:14px; border-radius:4px; background:#22D37A; margin-right:12px; vertical-align:2px; }}
      .pw {{ background:#fff; color:#111; }}
      .cap {{ position:absolute; left:70px; right:70px; top:330px; text-align:center; }}
      .cl {{ font-weight:800; font-size:66px; line-height:1.2; letter-spacing:-.02em; color:#fff; text-shadow:0 4px 20px rgba(4,14,38,.35); }}
      .w {{ display:inline-block; opacity:.35; }}
      .kw {{ color:#fff; padding:0 16px 4px; border-radius:14px; transform:rotate(-2deg); text-shadow:none; box-shadow:0 8px 20px rgba(4,14,38,.25); }}
      .cardwrap {{ position:absolute; inset:0; }}
      .card {{ position:absolute; left:90px; width:900px; border-radius:36px; background:#fff; box-shadow:0 30px 70px rgba(4,14,38,.35);
        padding:44px 40px 50px; display:flex; flex-direction:column; align-items:center; overflow:visible; }}
      .exh {{ position:absolute; right:-18px; top:-26px; transform:rotate(6deg); background:#F4C84A; color:#111; font-weight:900; font-size:26px; letter-spacing:.1em; padding:10px 20px; border-radius:10px; box-shadow:0 10px 24px rgba(4,14,38,.3); }}
      .lab {{ align-self:flex-start; font-weight:800; font-size:26px; letter-spacing:.12em; color:#6b7280; }}
      .t1 {{ font-weight:800; font-size:44px; letter-spacing:-.02em; }}
      .t2 {{ font-weight:400; font-size:32px; color:#6b7280; }}
      .sub {{ font-weight:800; font-size:48px; margin-top:6px; }}
      .hugeg {{ font-weight:900; font-size:260px; letter-spacing:-.05em; color:#22A45D; line-height:1; margin-top:40px; }}
      .stampc {{ margin-top:20px; font-weight:900; font-size:72px; color:#E5484D; border:8px solid #E5484D; border-radius:18px; padding:4px 30px; transform:rotate(-6deg); }}
      .stampbig {{ margin-top:70px; font-weight:900; font-size:150px; line-height:.95; text-align:center; color:#E5484D; border:14px solid #E5484D; border-radius:26px; padding:24px 50px; transform:rotate(-7deg); }}
      .row1 {{ align-self:stretch; display:flex; gap:24px; align-items:center; }}
      .av {{ width:100px; height:100px; border-radius:50%; color:#fff; display:flex; align-items:center; justify-content:center; font-size:52px; }}
      .msg {{ align-self:stretch; margin-top:22px; background:#EEF4FF; border-radius:22px; padding:20px 26px; font-weight:700; font-size:38px; }}
      .crowd {{ display:flex; gap:12px; margin-top:26px; }}
      .chipq {{ position:absolute; right:50px; top:120px; background:#F4C84A; padding:16px 26px; border-radius:16px; font-weight:800; font-size:40px; transform:rotate(5deg); }}
      .adm {{ position:absolute; left:60px; top:130px; text-align:center; }}
      .admbox {{ background:#F3F4F6; border-radius:24px; padding:30px 26px 10px; display:flex; gap:10px; }}
      .lesson {{ background:#111; color:#fff; font-weight:900; font-size:30px; letter-spacing:.2em; padding:10px 26px; border-radius:30px; }}
      .li {{ align-self:stretch; display:flex; gap:26px; align-items:center; margin-top:40px; background:#FFF1F1; border-radius:24px; padding:26px; }}
      .x {{ width:76px; height:76px; flex:none; border-radius:50%; background:#E5484D; color:#fff; font-weight:900; font-size:40px; display:flex; align-items:center; justify-content:center; }}
      .flag {{ margin-top:34px; font-weight:900; font-size:56px; color:#E5484D; border:7px solid #E5484D; border-radius:14px; padding:2px 26px; transform:rotate(-5deg); }}
      .prof {{ align-self:stretch; display:flex; gap:26px; align-items:center; }}
      .pav {{ width:120px; height:120px; border-radius:50%; background:#0B1F4A; color:#7CC0FF; font-weight:900; font-size:64px; display:flex; align-items:center; justify-content:center; border:6px solid #7CC0FF; }}
      .btns {{ align-self:stretch; display:flex; gap:20px; margin-top:40px; }}
      .fbtn {{ position:relative; flex:1; height:96px; border-radius:20px; background:#2F6FD8; color:#fff; font-weight:800; font-size:40px; overflow:hidden; }}
      .fbtn span {{ position:absolute; inset:0; display:flex; align-items:center; justify-content:center; }}
      #fb2 {{ background:#EEF1F5; color:#111; opacity:0; }}
      .mbtn {{ flex:1; height:96px; border-radius:20px; background:#EEF1F5; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:40px; }}
      .wbtn {{ margin-top:60px; width:640px; height:120px; border-radius:26px; background:#2F6FD8; color:#fff; font-weight:900; font-size:48px; display:flex; align-items:center; justify-content:center; }}
      .err {{ margin-top:40px; padding:22px 34px; border-radius:20px; background:#FFF1F1; color:#E5484D; font-weight:900; font-size:46px; border:4px solid #E5484D; }}
      .tot {{ align-self:flex-end; margin-top:26px; font-weight:900; font-size:48px; color:#E5484D; }}
      .phone {{ position:relative; margin-top:30px; width:420px; height:430px; border-radius:40px; background:#0B1F4A; border:8px solid #1c2c52; overflow:hidden; }}
      .pscr {{ position:absolute; inset:0; background:#fff; display:flex; flex-direction:column; align-items:center; justify-content:center; }}
      .pcode {{ position:absolute; inset:0; padding:40px 30px; font-family:monospace; font-size:30px; line-height:1.6; color:#7CC0FF; }}
      .ck {{ align-self:stretch; display:flex; gap:24px; align-items:center; margin-top:30px; background:#EFFAF3; border-radius:22px; padding:22px 26px; }}
      .ok {{ width:76px; height:76px; flex:none; border-radius:50%; background:#22A45D; color:#fff; font-weight:900; font-size:40px; display:flex; align-items:center; justify-content:center; }}
      .yt {{ position:relative; align-self:stretch; margin-top:22px; height:170px; border-radius:22px; background:#111; display:flex; align-items:center; gap:24px; padding:0 30px; }}
      .ytp {{ width:96px; height:68px; border-radius:16px; background:#FF0033; color:#fff; font-size:40px; display:flex; align-items:center; justify-content:center; }}
      .ytl {{ color:#fff; font-weight:800; font-size:40px; }}
      .like {{ position:absolute; right:30px; font-size:70px; color:#9aa3b2; }}
      .notif {{ align-self:stretch; margin-top:40px; display:flex; gap:24px; align-items:center; background:#EFFAF3; border-radius:24px; padding:28px; }}
      .flow {{ display:flex; align-items:center; gap:22px; margin-top:30px; }}
      .fb {{ width:280px; padding:26px; border-radius:22px; text-align:center; font-weight:700; font-size:32px; }}
      .fb b {{ font-weight:900; font-size:56px; }} .fb.r {{ background:#FFF1F1; color:#E5484D; }} .fb.g {{ background:#EFFAF3; color:#22A45D; }}
      .arr {{ font-weight:900; font-size:70px; color:#2F6FD8; }}
      .meter {{ align-self:stretch; margin-top:40px; height:44px; border-radius:22px; background:#EEF1F5; overflow:hidden; }}
      .mf {{ height:100%; width:100%; background:linear-gradient(90deg,#7CC0FF,#22A45D); transform-origin:0 50%; }}
      .gone {{ align-self:stretch; margin-top:40px; padding:40px; border-radius:24px; background:#F3F4F6; color:#6b7280; text-align:center; font-weight:800; font-size:38px; }}
      .bait {{ margin-top:-60px; padding:16px 34px; border-radius:12px; background:linear-gradient(135deg,#e6efe0,#cfdcc8); border:4px solid #6b8a66; font-weight:900; font-size:56px; color:#2f4f2c; }}
      .call {{ margin-top:40px; display:flex; align-items:center; gap:30px; padding:30px 50px; border-radius:30px; background:#2F6FD8; }}
      .cic {{ font-size:90px; }} .num {{ font-weight:900; font-size:150px; color:#fff; letter-spacing:-.03em; }}
      .hero {{ margin-top:30px; align-self:stretch; padding:40px; border-radius:26px; background:linear-gradient(135deg,#1E5BD8,#8A5CF6); color:#fff; font-weight:900; font-size:62px; text-align:center; }}
      .rm {{ align-self:stretch; display:flex; justify-content:space-between; margin-top:22px; font-weight:800; font-size:30px; color:#2F6FD8; }}
      .pool {{ position:relative; margin-top:40px; width:700px; height:200px; border-radius:30px; border:6px solid #2F6FD8; overflow:hidden; background:#EEF4FF; }}
      .pf {{ position:absolute; left:0; right:0; bottom:0; height:100%; background:linear-gradient(180deg,#7CC0FF,#2F6FD8); transform-origin:50% 100%; }}
      .pl {{ position:absolute; inset:0; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:66px; color:#0B1F4A; }}
      .rugw {{ position:relative; margin-top:60px; width:760px; height:300px; }}
      .figs {{ position:absolute; left:120px; bottom:62px; display:flex; gap:30px; }}
      .rug {{ position:absolute; left:40px; bottom:20px; width:680px; height:46px; border-radius:10px; background:repeating-linear-gradient(90deg,#E5484D 0 40px,#F4C84A 40px 80px); }}
      .dead {{ align-self:stretch; margin-top:22px; padding:22px 26px; border-radius:20px; background:#F3F4F6; color:#6b7280; font-size:32px; }}
      .dead b {{ color:#E5484D; }}
      .scale {{ display:flex; align-items:center; gap:18px; margin-top:60px; }}
      .sc1 {{ white-space:nowrap; padding:30px 28px; border-radius:22px; background:#EFFAF3; color:#22A45D; font-weight:900; font-size:40px; }}
      .sc2 {{ white-space:nowrap; padding:30px 28px; border-radius:22px; background:#FFF1F1; color:#E5484D; font-weight:900; font-size:40px; }}
      .eq {{ font-weight:900; font-size:80px; color:#111; }}
      #trk {{ position:absolute; left:60px; right:60px; top:1350px; padding:26px 26px 30px; border-radius:30px; background:rgba(234,243,255,.16);
        border:2px solid rgba(234,243,255,.4); backdrop-filter:blur(12px); box-shadow:0 20px 50px rgba(4,14,38,.3); }}
      #trk .tl {{ font-weight:800; font-size:22px; letter-spacing:.16em; color:rgba(255,255,255,.8); margin-bottom:16px; }}
      #trk .row {{ display:flex; justify-content:space-between; }}
      .st {{ width:104px; text-align:center; opacity:.35; }}
      .st .e {{ width:84px; height:84px; margin:0 auto; border-radius:50%; background:rgba(11,31,74,.55); display:flex; align-items:center; justify-content:center; font-size:42px; border:3px solid transparent; }}
      .st .n {{ margin-top:8px; font-weight:800; font-size:20px; color:#fff; white-space:nowrap; }}
      .bar {{ margin-top:22px; height:12px; border-radius:6px; background:rgba(11,31,74,.45); overflow:hidden; }}
      .bf {{ height:100%; width:100%; background:linear-gradient(90deg,#7CC0FF,#22D37A); transform-origin:0 50%; }}
      .handle {{ position:absolute; left:0; right:0; top:1640px; text-align:center; font-weight:800; font-size:32px; color:rgba(255,255,255,.85); }}
      .pp {{ display:inline-block; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
      <div id="bgc" class="clip" data-start="0" data-duration="{DUR}" data-track-index="0" data-layout-allow-overlap><div id="bg">
          <div class="blob" id="b1" style="left:-420px;top:-380px;width:1100px;height:1100px;background:radial-gradient(closest-side,#7FB1EE,rgba(127,177,238,0))"></div>
          <div class="blob" id="b2" style="left:-300px;top:380px;width:1300px;height:1300px;background:radial-gradient(closest-side,#2E63C9,rgba(46,99,201,0))"></div>
          <div class="blob" id="b3" style="left:-520px;top:1100px;width:1300px;height:1300px;background:radial-gradient(closest-side,#0C2A57,rgba(12,42,87,0))"></div>
          <div class="blob" id="b4" style="left:420px;top:1240px;width:1100px;height:1100px;background:radial-gradient(closest-side,#5AA8E8,rgba(90,168,232,0))"></div>
          <div class="blob" id="b5" style="left:380px;top:620px;width:900px;height:900px;background:radial-gradient(closest-side,rgba(110,120,200,.55),rgba(110,120,200,0))"></div>
        </div>
        <svg id="lines" width="1080" height="1920" viewBox="0 0 1080 1920">
          <g stroke="rgba(234,243,255,.22)" stroke-width="2"><line x1="398" y1="0" x2="398" y2="1920"/><line x1="682" y1="0" x2="682" y2="1920"/>
            <line x1="0" y1="484" x2="1080" y2="484"/><line x1="0" y1="1430" x2="1080" y2="1430"/><line x1="0" y1="1452" x2="1080" y2="1452"/><line x1="0" y1="1584" x2="1080" y2="1584"/></g>
          <g fill="none" stroke="rgba(234,243,255,.28)" stroke-width="2.2"><circle id="c1" cx="540" cy="716" r="489"/><circle id="c2" cx="540" cy="1203" r="489"/></g>
          <g id="o1" style="transform-origin:540px 716px"><circle cx="540" cy="227" r="9" fill="#EAF3FF"/><circle cx="540" cy="227" r="24" fill="rgba(234,243,255,.25)"/></g>
          <g id="o2" style="transform-origin:540px 1203px"><circle cx="540" cy="1692" r="9" fill="#9FD3FF"/><circle cx="540" cy="1692" r="24" fill="rgba(159,211,255,.25)"/></g>
          <g id="o3" style="transform-origin:540px 716px"><circle cx="1029" cy="716" r="6" fill="#EAF3FF" opacity=".8"/></g>
          <g id="o4" style="transform-origin:540px 1203px"><circle cx="51" cy="1203" r="6" fill="#EAF3FF" opacity=".8"/></g>
        </svg>
        <svg id="grain" width="1080" height="1920"><filter id="gn"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter><rect width="1080" height="1920" filter="url(#gn)"/></svg><div id="dots"></div></div>
      <div id="hdr" class="clip" data-start="0" data-duration="{DUR}" data-track-index="1">
        <div class="pills"><div class="pill pd"><i></i>Scam Files</div><div class="pill pw">Case 04 · Rug Pull</div></div>
        <div id="trk"><div class="tl">CASE TRACKER</div><div class="row">{"".join(f'<div class="st" id="st{i}"><div class="e">{e}</div><div class="n">{n}</div></div>' for i, (e, n, _) in enumerate(TRACK))}</div><div class="bar"><div class="bf" id="bf"></div></div></div>
        <div class="handle">@niks.crypto</div>
      </div>
{chr(10).join(cards)}
{chr(10).join(caps)}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      const C = {json.dumps({k: [a, b] for k, a, b in CARDS})};
      // animated background: drifting blobs, floating circles, orbiting dots, scrolling dot grid
      const D = {DUR}, cyc = (id, from, to, per) => {{ const n = Math.ceil(D / per); tl.fromTo(id, from, {{ ...to, duration: per / 2, ease: "sine.inOut", yoyo: true, repeat: n * 2 - 1 }}, 0); }};
      cyc("#b1", {{ x: 0, y: 0 }}, {{ x: 140, y: 90 }}, 14);
      cyc("#b2", {{ x: 0, y: 0, scale: 1 }}, {{ x: 180, y: -120, scale: 1.12 }}, 18);
      cyc("#b3", {{ x: 0, y: 0 }}, {{ x: 120, y: -80 }}, 16);
      cyc("#b4", {{ x: 0, y: 0, scale: 1 }}, {{ x: -160, y: -110, scale: 1.15 }}, 13);
      cyc("#b5", {{ x: 0, y: 0 }}, {{ x: -120, y: 140 }}, 20);
      cyc("#c1", {{ attr: {{ cy: 716, r: 489 }} }}, {{ attr: {{ cy: 690, r: 500 }} }}, 9);
      cyc("#c2", {{ attr: {{ cy: 1203, r: 489 }} }}, {{ attr: {{ cy: 1228, r: 478 }} }}, 11);
      tl.fromTo("#o1", {{ rotation: 0 }}, {{ rotation: 360 * D / 16, duration: D, ease: "none" }}, 0);
      tl.fromTo("#o2", {{ rotation: 0 }}, {{ rotation: -360 * D / 20, duration: D, ease: "none" }}, 0);
      tl.fromTo("#o3", {{ rotation: 0 }}, {{ rotation: -360 * D / 26, duration: D, ease: "none" }}, 0);
      tl.fromTo("#o4", {{ rotation: 0 }}, {{ rotation: 360 * D / 30, duration: D, ease: "none" }}, 0);
      tl.fromTo("#dots", {{ y: 0 }}, {{ y: 68 * Math.round(D / 3), duration: D, ease: "none" }}, 0);
      for (const k in C) {{
        const [a, b] = C[k];
        tl.fromTo("#" + k + "c", {{ y: 80, scale: 0.92, opacity: 0, filter: "blur(10px)" }}, {{ y: 0, scale: 1, opacity: 1, filter: "blur(0px)", duration: 0.4, ease: "power3.out" }}, a + 0.02);
        tl.to("#" + k + "c", {{ y: -40, scale: 0.97, opacity: 0, filter: "blur(8px)", duration: 0.22, ease: "power2.in" }}, b - 0.22);
      }}
      // word-by-word captions
      document.querySelectorAll(".cap").forEach((c) => {{
        const s = parseFloat(c.dataset.start);
        tl.fromTo(c, {{ y: 16, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.18, ease: "power2.out" }}, s);
        c.querySelectorAll(".w").forEach((w) => {{
          const t = parseFloat(w.dataset.t);
          if (w.classList.contains("kw")) tl.fromTo(w, {{ opacity: 0.35, scale: 0.6 }}, {{ opacity: 1, scale: 1, duration: 0.22, ease: "back.out(3)" }}, t);
          else tl.fromTo(w, {{ opacity: 0.35 }}, {{ opacity: 1, duration: 0.12 }}, t);
        }});
      }});
      const draw = (id, t, d) => tl.to(id, {{ attr: {{ "stroke-dashoffset": 0 }}, duration: d, ease: "power1.inOut" }}, t);
      const pop = (id, t) => tl.fromTo(id, {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2.5)" }}, t);
      const slam = (id, t, r) => tl.fromTo(id, {{ scale: 2.4, opacity: 0, rotation: r - 12 }}, {{ scale: 1, opacity: 1, rotation: r, duration: 0.2, ease: "power4.in" }}, t);
      // tracker
      tl.fromTo("#trk", {{ y: 200, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power3.out" }}, 2.4);
      tl.fromTo("#bf", {{ scaleX: 0 }}, {{ scaleX: 1, duration: {DUR} - 2.6, ease: "none" }}, 2.6);
      {"".join(f'tl.fromTo("#st{i}", {{ opacity: 0.35, scale: 1 }}, {{ opacity: 1, scale: 1.12, duration: 0.25, ease: "back.out(3)" }}, {t});tl.to("#st{i} .e", {{ borderColor: "#22D37A", background: "#0B1F4A", duration: 0.2 }}, {t});tl.to("#st{i}", {{ scale: 1, duration: 0.2 }}, {t + 0.3});' for i, (_, _, t) in enumerate(TRACK))}
      // k1
      pop("#fold", 0.3); slam("#k1s", 1.5, -6);
      // k2 shiny launch
      pop("#k2h", 4.3); tl.fromTo("#k2r span", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.2, stagger: 0.15 }}, 5.8);
      tl.fromTo("#m1", {{ x: -60, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.22, ease: "back.out(2)" }}, 7.4);
      // k3 money in
      tl.fromTo("#k3c .pp", {{ y: -120, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.3, stagger: 0.06, ease: "bounce.out" }}, 10.8);
      const pv = {{ v: 0 }};
      tl.fromTo(pv, {{ v: 0 }}, {{ v: 2400000, duration: 2.2, ease: "power1.in", onUpdate: () => {{ document.querySelector("#k3n").textContent = "$" + Math.round(pv.v).toLocaleString("en-US"); }} }}, 10.9);
      pop("#k3t", 12.8);
      // k4 drain
      const dv = {{ v: 2400000 }};
      tl.fromTo("#k4p", {{ scaleY: 1 }}, {{ scaleY: 0, duration: 1.0, ease: "power2.in" }}, 15.9);
      tl.fromTo(dv, {{ v: 2400000 }}, {{ v: 0, duration: 1.0, ease: "power2.in", onUpdate: () => {{ document.querySelector("#k4n").textContent = "$" + Math.round(dv.v).toLocaleString("en-US"); }} }}, 15.9);
      tl.fromTo("#m2", {{ x: -60, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.22, ease: "back.out(2)" }}, 15.2);
      slam("#k4x", 17.2, -8);
      // k5 rug yank
      tl.fromTo("#k5r", {{ x: 0 }}, {{ x: 900, duration: 0.45, ease: "power3.in" }}, 21.6);
      tl.fromTo("#k5f", {{ y: 0, rotation: 0 }}, {{ y: 60, rotation: -12, duration: 0.4, ease: "power2.in" }}, 21.9);
      // k6 zero
      tl.fromTo("#k6v", {{ scale: 2, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.22, ease: "power4.in" }}, 24.4);
      tl.fromTo("#k6a", {{ x: -60, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.25 }}, 26.3);
      tl.fromTo("#k6b", {{ x: -60, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.25 }}, 27.7);
      // k7 checks
      ["#c1", "#c2", "#c3"].forEach((c, i) => tl.fromTo(c, {{ x: -80, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.3, ease: "power3.out" }}, [32.5, 35.2, 37.5][i]));
      // k8 lesson
      pop("#k8a", 41.3); slam("#k8b", 42.9, 0);
      // k9 follow
      tl.fromTo("#cur", {{ x: 760, y: 420, opacity: 0 }}, {{ x: 760, y: 420, opacity: 1, duration: 0.1 }}, 45.1);
      tl.to("#cur", {{ x: 300, y: 270, duration: 0.5, ease: "power2.inOut" }}, 45.2);
      tl.to("#cur", {{ scale: 0.85, duration: 0.08, yoyo: true, repeat: 1 }}, 45.72);
      tl.to("#fb", {{ scale: 0.96, duration: 0.08, yoyo: true, repeat: 1 }}, 45.72);
      tl.fromTo("#fb2", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.15 }}, 45.8);
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''
    open(os.path.join(HERE, "hf", "index.html"), "w").write(html)
    print("captions:", len(caps), "cards:", len(cards))


if __name__ == "__main__":
    build()
