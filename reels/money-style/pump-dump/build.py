"""Pump & Dump in the niks.finance "card" style on the blue gradient background.

Writes hf/index.html (HyperFrames). Captions reveal word by word; {g:word} / {r:word} / {b:word} = coloured keyword pill.
"""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 40.8

PHRASES = [
    (0.00, 0.97, "Scam Files."),
    (1.46, 2.42, "Case number {b:ek.}"),
    (2.79, 5.14, "Ye coin, kal {g:100X} ho jayega!"),
    (5.56, 7.33, "Telegram group mein, {b:hazaaron} log."),
    (7.81, 9.50, "Sab ek hi coin ki baat kar rahe hain."),
    (9.98, 10.71, "Aap {b:kharidte} ho."),
    (11.15, 12.12, "Price {g:upar} jaata hai."),
    (12.50, 13.94, "Aur lagta hai, sab {g:sach} hai."),
    (14.37, 16.32, "Par {r:asli} khel… pehle hi ho chuka hai."),
    (16.79, 19.75, "Group chalane wale, coin pehle hi {g:sasta} kharid chuke the."),
    (20.16, 22.90, "Aapke jaise {b:naye} log aate hain, price upar jaata hai…"),
    (23.34, 25.23, "aur wo sab {r:bech} ke nikal jaate hain."),
    (25.74, 26.61, "Price {r:gir} jaata hai."),
    (27.11, 27.69, "Aur bacha kaun?"),
    (28.19, 28.70, "{r:Aap.}"),
    (28.96, 30.93, "Ise kehte hain, {r:pump and dump.}"),
    (31.43, 33.71, "Yaad rakho: {r:guaranteed} profit bolne wala,"),
    (33.92, 34.97, "aapka dost {r:nahi} hai."),
    (35.37, 38.38, "Aur sirf {b:hype} wale coin se door raho."),
    (38.81, 39.81, "{b:Case} closed."),
]

# card windows
CARDS = [("k1", 0.0, 2.75), ("k2", 2.75, 5.45), ("k3", 5.45, 9.85), ("k4", 9.85, 14.25), ("k5", 14.25, 20.05),
         ("k6", 20.05, 25.6), ("k7", 25.6, 28.9), ("k8", 28.9, 31.3), ("k9", 31.3, 38.7), ("k10", 38.7, DUR)]

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


def card(cid, inner, top=640, h=620):
    a, b = [(x, y) for k, x, y in CARDS if k == cid][0]
    return (f'      <div id="{cid}" class="clip cardwrap" data-start="{a}" data-duration="{round(b-a,2)}" data-track-index="3">'
            f'<div class="card" id="{cid}c" style="top:{top}px;height:{h}px">{inner}</div></div>')


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
          <div class="stampc" id="k1s">CASE #01</div>'''),
        card("k2", '''<div class="lab">TELEGRAM · VIP SIGNALS</div>
          <div class="hugeg" id="k2n">100X</div>
          <svg id="k2r" viewBox="0 0 64 64" width="170" height="170" style="position:absolute;right:70px;top:90px"><path d="M40 6 C54 8 58 22 52 34 L38 48 L22 32 L36 18 C38 14 38 10 40 6Z" fill="#E5484D" stroke="#111" stroke-width="3"/><circle cx="42" cy="22" r="5" fill="#fff" stroke="#111" stroke-width="2.5"/><path d="M24 40 L12 52 M30 46 L22 56 M18 34 L8 42" stroke="#F4A100" stroke-width="4" stroke-linecap="round"/></svg>
          <div class="sub" id="k2t">"Kal ho jayega!" 🚀</div>'''),
        card("k3", f'''<div class="row1"><div class="av" style="background:#2AABEE">✈</div><div><div class="t1">VIP Crypto Signals</div><div class="t2"><span id="k3n">1,240</span> members</div></div></div>
          <div class="msg" id="m1">BUY NOW!! 100X loading 🚀</div><div class="msg" id="m2">Kal moon pe jayega</div><div class="msg" id="m3">Last chance, jaldi karo!</div>
          <div class="crowd" id="k3c">{ppl(10, 46, "#9aa3b2")}</div>'''),
        card("k4", '<div class="lab">PRICE · EXAMPLE</div>' + chart("k4l", "20,330 120,315 220,300 320,260 420,210 520,160 620,110 720,70 800,40", "#22A45D",
             extra='<g id="k4m"><circle cx="220" cy="300" r="16" fill="#2F6FD8" stroke="#fff" stroke-width="4"/><rect x="160" y="226" width="120" height="48" rx="10" fill="#2F6FD8"/><text x="220" y="258" text-anchor="middle" font-family="IN" font-weight="800" font-size="26" fill="#fff">AAP: BUY</text></g>') +
             '<div class="chipq" id="k4q">Sab sach?</div>'),
        card("k5", f'''<div class="lab">PEHLE SE KHAREEDA</div>
          <div class="adm" id="k5a"><div class="admbox">{ppl(3, 70, "#111")}</div><div class="t1" style="margin-top:12px">Group admins</div></div>
          <svg id="k5arr" width="120" height="60" viewBox="0 0 120 60" style="position:absolute;left:390px;top:200px"><path d="M6 30 H100 M80 12 L104 30 L80 48" stroke="#2F6FD8" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <div id="k5c" style="position:absolute;right:50px;top:110px">{chart("k5l", "10,250 80,240 150,232 220,200 290,150 360,90", "#22A45D", w=370, h=280,
            extra='<g id="k5d"><circle cx="80" cy="240" r="14" fill="#22A45D" stroke="#fff" stroke-width="4"/><text x="100" y="222" font-family="IN" font-weight="800" font-size="26" fill="#22A45D">SASTA</text></g>')}</div>'''),
        card("k6", f'''<div class="lab">PEAK · EXAMPLE</div>{chart("k6l", "20,320 160,290 300,220 440,140 540,70 600,40", "#22A45D", h=340,
             extra='<g id="k6s"><rect x="560" y="60" width="200" height="54" rx="10" fill="#E5484D"/><text x="660" y="97" text-anchor="middle" font-family="IN" font-weight="800" font-size="28" fill="#fff">ADMINS: SELL</text></g>')}
          <div class="crowd" id="k6c">{ppl(10, 46, "#2F6FD8")}</div><div class="t2" id="k6t" style="margin-top:6px">naye log aate hain →</div>''', h=640),
        card("k7", f'''<div class="lab">CRASH</div>{chart("k7a", "20,300 160,260 300,190 440,110 540,40", "#22A45D", h=330,
             extra='<polyline id="k7b" points="540,40 600,180 660,270 740,305 820,315" fill="none" stroke="#E5484D" stroke-width="11" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="500" stroke-dashoffset="500"/>')}
          <div id="k7y" style="display:flex;align-items:center;gap:16px;justify-content:center">{PERSON.format(w=70, h=91, c="#E5484D")}<div class="t1" style="color:#E5484D;font-size:52px">Aap</div></div>'''),
        card("k8", '''<div class="stampbig" id="k8s">PUMP<br>&amp; DUMP</div>'''),
        card("k9", '''<div class="lesson">LESSON</div>
          <div class="li" id="k9a"><span class="x">✕</span><div><div class="t1">"Guaranteed profit"</div><div class="t2">bolne wala dost nahi hai</div></div></div>
          <div class="li" id="k9b"><span class="x">✕</span><div><div class="t1">Sirf hype wala coin</div><div class="t2">usse door raho</div></div></div>
          <div class="flag" id="k9f">RED FLAG</div>''', h=640),
        card("k10", '''<div class="prof"><div class="pav">₿</div><div><div class="t1">niks.crypto</div><div class="t2">Crypto · Scams · Money</div></div></div>
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
      .pills {{ position:absolute; left:0; right:0; top:250px; display:flex; justify-content:center; gap:14px; }}
      .pill {{ padding:14px 26px; border-radius:40px; font-weight:800; font-size:30px; }}
      .pd {{ background:#0B1F4A; color:#fff; }} .pd i {{ display:inline-block; width:14px; height:14px; border-radius:4px; background:#22D37A; margin-right:12px; vertical-align:2px; }}
      .pw {{ background:#fff; color:#111; }}
      .cap {{ position:absolute; left:70px; right:70px; top:350px; text-align:center; }}
      .cl {{ font-weight:800; font-size:66px; line-height:1.2; letter-spacing:-.02em; color:#fff; text-shadow:0 4px 20px rgba(4,14,38,.35); }}
      .w {{ display:inline-block; opacity:.35; }}
      .kw {{ color:#fff; padding:0 16px 4px; border-radius:14px; transform:rotate(-2deg); text-shadow:none; box-shadow:0 8px 20px rgba(4,14,38,.25); }}
      .cardwrap {{ position:absolute; inset:0; }}
      .card {{ position:absolute; left:90px; width:900px; border-radius:36px; background:#fff; box-shadow:0 30px 70px rgba(4,14,38,.35);
        padding:44px 40px; display:flex; flex-direction:column; align-items:center; overflow:hidden; }}
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
      .handle {{ position:absolute; left:0; right:0; top:1330px; text-align:center; font-weight:800; font-size:32px; color:rgba(255,255,255,.85); }}
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
        <div class="pills"><div class="pill pd"><i></i>Scam Files</div><div class="pill pw">Case 01 · Pump &amp; Dump</div></div>
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
      // k1
      pop("#fold", 0.3); slam("#k1s", 1.5, -6);
      // k2
      tl.fromTo("#k2n", {{ scale: 2.2, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.22, ease: "power4.in" }}, 3.55);
      tl.fromTo("#k2r", {{ x: -300, y: 200, opacity: 0 }}, {{ x: 0, y: 0, opacity: 1, duration: 1.0, ease: "power2.out" }}, 3.6);
      tl.fromTo("#k2t", {{ y: 30, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.3 }}, 4.4);
      // k3
      const cnt = {{ n: 1240 }};
      tl.fromTo(cnt, {{ n: 1240 }}, {{ n: 52000, duration: 0.9, ease: "power1.in", onUpdate: () => {{ document.querySelector("#k3n").textContent = Math.round(cnt.n).toLocaleString("en-IN"); }} }}, 6.6);
      ["#m1", "#m2", "#m3"].forEach((m, i) => tl.fromTo(m, {{ x: -60, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.22, ease: "back.out(2)" }}, 7.8 + i * 0.5));
      tl.fromTo("#k3c .pp", {{ y: 50, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.2, stagger: 0.05 }}, 6.7);
      // k4
      pop("#k4m", 10.3); draw("#k4l", 11.15, 1.4); slam("#k4q", 13.1, 5);
      // k5
      pop("#k5a", 16.8); tl.fromTo("#k5arr", {{ x: -40, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.3 }}, 17.6);
      tl.fromTo("#k5c", {{ x: 200, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.35, ease: "power3.out" }}, 17.8); draw("#k5l", 18.0, 1.0); pop("#k5d", 18.4);
      // k6
      tl.fromTo("#k6c .pp", {{ y: -120, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.3, stagger: 0.07, ease: "bounce.out" }}, 20.4);
      tl.fromTo("#k6t", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2 }}, 21.0); draw("#k6l", 21.9, 1.1); pop("#k6s", 23.4);
      tl.to("#k6c", {{ opacity: 0.3, duration: 0.3 }}, 24.3);
      // k7
      draw("#k7a", 25.65, 0.01); draw("#k7b", 25.8, 0.7); tl.to("#k7c", {{ x: 0 }}, 25.6);
      tl.to("#k7c", {{ x: 12, duration: 0.05, yoyo: true, repeat: 7, ease: "none" }}, 26.5); pop("#k7y", 28.15);
      // k8
      slam("#k8s", 29.95, -7); tl.to("#k8c", {{ x: 14, duration: 0.04, yoyo: true, repeat: 7, ease: "none" }}, 30.17);
      // k9
      tl.fromTo("#k9a", {{ x: -80, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.3, ease: "power3.out" }}, 32.25);
      tl.fromTo("#k9b", {{ x: -80, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.3, ease: "power3.out" }}, 35.4);
      slam("#k9f", 36.6, -5);
      // k10 follow
      tl.fromTo("#cur", {{ x: 760, y: 420, opacity: 0 }}, {{ x: 760, y: 420, opacity: 1, duration: 0.1 }}, 39.0);
      tl.to("#cur", {{ x: 300, y: 270, duration: 0.5, ease: "power2.inOut" }}, 39.1);
      tl.to("#cur", {{ scale: 0.85, duration: 0.08, yoyo: true, repeat: 1 }}, 39.62);
      tl.to("#fb", {{ scale: 0.96, duration: 0.08, yoyo: true, repeat: 1 }}, 39.62);
      tl.fromTo("#fb2", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.15 }}, 39.7);
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''
    open(os.path.join(HERE, "hf", "index.html"), "w").write(html)
    print("captions:", len(caps), "cards:", len(cards))


if __name__ == "__main__":
    build()
