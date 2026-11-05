"""SCAM FILES · Case 01 (Pump & Dump): writes the HyperFrames project (index.html) for the whole reel.

Timings come from the ElevenLabs voice-over (seconds). Captions are 2-3 word chunks; *word* = red keyword box.
"""
import os, re, shutil, json

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.join(HERE, "hf")
DUR = 40.8

# (start, end, text) per spoken phrase; each phrase is split into caption chunks on " / "
PHRASES = [
    (2.79, 5.14, "Ye coin, / kal *100X* / ho jayega!"),
    (5.56, 6.43, "Telegram group mein,"),
    (6.64, 7.33, "*hazaaron* log."),
    (7.81, 9.50, "Sab ek hi coin / ki baat kar rahe hain."),
    (9.98, 10.71, "Aap *kharidte* ho."),
    (11.15, 12.12, "Price *upar* jaata hai."),
    (12.50, 13.94, "Aur lagta hai, / sab *sach* hai."),
    (14.37, 15.19, "Par *asli khel*…"),
    (15.44, 16.32, "pehle hi ho chuka hai."),
    (16.79, 17.70, "Group chalane wale,"),
    (17.91, 19.75, "wo coin pehle hi / *sasta* kharid chuke the."),
    (20.16, 21.57, "Aapke jaise / *naye log* aate hain,"),
    (21.90, 22.90, "price upar jaata hai…"),
    (23.34, 25.23, "aur wo sab *bech ke* / nikal jaate hain."),
    (25.74, 26.61, "Price *gir* jaata hai."),
    (27.11, 27.69, "Aur bacha kaun?"),
    (28.19, 28.70, "*Aap.*"),
    (28.96, 29.69, "Ise kehte hain,"),
    (29.97, 30.93, "*pump and dump.*"),
    (31.43, 31.94, "Yaad rakho:"),
    (32.25, 33.71, "*\"guaranteed profit\"* / bolne wala,"),
    (33.92, 34.97, "aapka *dost nahi* hai."),
    (35.37, 37.18, "Aur jo coin / sirf *hype* pe chal raha hai,"),
    (37.50, 38.38, "usse *door raho.*"),
    (38.81, 39.81, "*Case closed.*"),
]

# scene windows [start, end)
SCENES = [("s1", 0.0, 2.72), ("s2", 2.72, 5.40), ("s3", 5.40, 9.80), ("s4", 9.80, 14.20), ("s5", 14.20, 19.95),
          ("s6", 19.95, 25.55), ("s7", 25.55, 28.85), ("s8", 28.85, 31.25), ("s9", 31.25, 38.60), ("s10", 38.60, DUR)]


def chunks():
    out = []
    for s, e, text in PHRASES:
        parts = [p.strip() for p in text.split(" / ")]
        w = [max(4, len(re.sub(r"[*]", "", p))) for p in parts]
        t = s
        for p, wi in zip(parts, w):
            d = (e - s) * wi / sum(w)
            out.append((round(t, 2), round(t + d, 2), p))
            t += d
    # each chunk stays until the next one starts (or 0.35 s after its phrase ends)
    res = []
    for i, (a, b, p) in enumerate(out):
        nxt = out[i + 1][0] if i + 1 < len(out) else DUR
        res.append((a, round(min(nxt, b + 0.45), 2), p))
    return res


def cap_html(p):
    p = re.sub(r"\*(.+?)\*", r'<span class="k">\1</span>', p)
    return p


ROBOT = '''
<svg viewBox="0 0 260 260" width="230" height="230">
  <ellipse cx="130" cy="250" rx="80" ry="8" fill="#1A1A00" opacity=".18"/>
  <rect x="58" y="96" width="144" height="126" rx="34" fill="#FFF7D3" stroke="#1A1A00" stroke-width="7"/>
  <rect x="84" y="196" width="22" height="34" rx="8" fill="#1A1A00"/><rect x="154" y="196" width="22" height="34" rx="8" fill="#1A1A00"/>
  <rect x="76" y="114" width="108" height="66" rx="18" fill="#1A1A00"/>
  <g id="eyeN"><circle cx="106" cy="147" r="9" fill="#FFF7D3"/><circle cx="152" cy="147" r="22" fill="#FFBA09" stroke="#FFF7D3" stroke-width="5"/><circle cx="152" cy="147" r="9" fill="#1A1A00"/></g>
  <g id="eyeS" opacity="0"><rect x="94" y="144" width="24" height="6" rx="3" fill="#FFF7D3"/><circle cx="152" cy="147" r="22" fill="#FFBA09" stroke="#FFF7D3" stroke-width="5"/><rect x="138" y="143" width="28" height="8" rx="4" fill="#1A1A00"/></g>
  <g id="eyeX" opacity="0"><circle cx="106" cy="147" r="13" fill="#FFF7D3"/><circle cx="152" cy="147" r="26" fill="#FFBA09" stroke="#FFF7D3" stroke-width="5"/><circle cx="152" cy="147" r="5" fill="#1A1A00"/></g>
  <g id="eyeH" opacity="0"><path d="M96 150 q10 -12 20 0" stroke="#FFF7D3" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M138 152 q14 -16 28 0" stroke="#FFBA09" stroke-width="7" fill="none" stroke-linecap="round"/></g>
  <g id="hat"><path d="M40 98 Q130 74 220 98 Q215 110 130 108 Q45 110 40 98Z" fill="#AB1509" stroke="#1A1A00" stroke-width="6"/>
  <path d="M78 96 Q80 42 130 40 Q180 42 182 96Z" fill="#AB1509" stroke="#1A1A00" stroke-width="6"/><rect x="80" y="78" width="100" height="12" fill="#1A1A00"/></g>
  <g id="armL"><path d="M58 170 Q30 175 26 150" stroke="#1A1A00" stroke-width="7" fill="none" stroke-linecap="round"/>
  <circle cx="22" cy="128" r="20" fill="rgba(255,247,211,.5)" stroke="#1A1A00" stroke-width="7"/></g>
  <path d="M202 170 Q228 176 232 196" stroke="#1A1A00" stroke-width="7" fill="none" stroke-linecap="round"/>
  <g id="bang" opacity="0"><rect x="214" y="30" width="16" height="44" rx="6" fill="#AB1509"/><circle cx="222" cy="88" r="9" fill="#AB1509"/></g>
</svg>'''

PERSON = '<svg viewBox="0 0 40 52" width="{w}" height="{h}"><circle cx="20" cy="12" r="10" fill="{c}"/><path d="M2 52 Q2 26 20 26 Q38 26 38 52Z" fill="{c}"/></svg>'


def people(n, w, c, cls=""):
    return "".join(f'<div class="pp {cls}">{PERSON.format(w=w, h=int(w*1.3), c=c)}</div>' for _ in range(n))


def build():
    caps = chunks()
    cap_divs = "\n".join(
        f'      <div id="c{i}" class="clip cap" data-start="{a}" data-duration="{round(b-a,2)}" data-track-index="9"><div class="ci">{cap_html(p)}</div></div>'
        for i, (a, b, p) in enumerate(caps))
    sc = {k: (a, b) for k, a, b in SCENES}

    def scn(k, inner, extra=""):
        a, b = sc[k]
        return f'      <div id="{k}" class="clip scene" data-start="{a}" data-duration="{round(b-a,2)}" data-track-index="2" {extra}><div class="cam" id="{k}cam">{inner}</div></div>'

    scenes = [
        scn("s1", '''
        <div class="a" id="s1t" style="left:0;right:0;top:600px;text-align:center"><div class="lg red" style="font-size:330px;line-height:.85">SCAM<br>FILES</div></div>
        <div class="a stamp" id="s1st" style="left:300px;top:1290px;font-size:110px;transform:rotate(-8deg)">CASE #01</div>
        <div class="a tapebar" id="s1tape" style="left:150px;top:470px;width:780px;transform:rotate(-2deg)">PUMP &amp; DUMP · PUMP &amp; DUMP</div>'''),
        scn("s2", '''
        <div class="a lg ink" id="s2a" style="left:70px;top:300px;font-size:230px">YE COIN</div>
        <div class="a lg red" id="s2b" style="left:60px;top:500px;font-size:520px;line-height:.86">100X</div>
        <div class="a lg ink" id="s2c" style="left:70px;top:960px;font-size:230px">JAYEGA?!</div>
        <svg class="a" id="s2r" style="left:760px;top:520px" width="260" height="260" viewBox="0 0 64 64"><path d="M40 6 C54 8 58 22 52 34 L38 48 L22 32 L36 18 C38 14 38 10 40 6Z" fill="#AB1509" stroke="#1A1A00" stroke-width="3"/><circle cx="42" cy="22" r="5" fill="#FFF7D3" stroke="#1A1A00" stroke-width="2.5"/><path d="M24 40 L12 52 M30 46 L22 56 M18 34 L8 42" stroke="#FFBA09" stroke-width="4" stroke-linecap="round"/></svg>'''),
        scn("s3", f'''
        <div class="a pol" id="s3p" style="left:150px;top:330px;width:780px;height:960px;transform:rotate(-3deg)">
          <div class="dark" style="height:820px;padding:36px">
            <div class="mono amber" style="font-size:34px">VIP CRYPTO SIGNALS</div>
            <div class="row" style="margin-top:10px"><div class="mono" style="font-size:30px;opacity:.75">MEMBERS:</div><div class="lg" id="s3n" style="font-size:96px;color:#FFF7D3">1,240</div></div>
            <div class="msg" id="m1">BUY NOW!! 100X LOADING</div>
            <div class="msg" id="m2">Kal moon pe jayega</div>
            <div class="msg" id="m3">Last chance, jaldi karo!</div>
            <div class="msg" id="m4">Sab isi coin mein daalo</div>
          </div>
          <div class="cap2">EXHIBIT A · TELEGRAM GROUP</div><div class="tp" style="left:-30px;top:-18px;transform:rotate(-28deg)"></div>
        </div>
        <div class="a crowd" id="s3c" style="left:120px;top:1290px">{people(9, 56, "#1A1A00", "pc")}</div>'''),
        scn("s4", '''
        <div class="a lg ink" id="s4h" style="left:70px;top:270px;font-size:170px">AAP <span class="red">KHAREEDTE</span> HO</div>
        <div class="a pol" id="s4p" style="left:90px;top:520px;width:900px;height:760px;transform:rotate(2deg)">
          <svg width="856" height="640" viewBox="0 0 856 640"><rect width="856" height="640" fill="#1A1A00"/>
            <g stroke="#FFF7D3" stroke-opacity=".1"><line x1="0" y1="160" x2="856" y2="160"/><line x1="0" y1="320" x2="856" y2="320"/><line x1="0" y1="480" x2="856" y2="480"/></g>
            <polyline id="s4l" points="20,560 120,540 220,520 320,470 420,400 520,320 620,240 720,170 830,110" fill="none" stroke="#FFBA09" stroke-width="12" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="1100" stroke-dashoffset="1100"/>
            <g id="s4m"><circle cx="220" cy="520" r="18" fill="#AB1509" stroke="#FFF7D3" stroke-width="4"/><rect x="150" y="430" width="150" height="56" rx="10" fill="#AB1509"/><text x="225" y="470" text-anchor="middle" font-family="SFM" font-weight="700" font-size="30" fill="#FFF7D3">AAP: BUY</text></g>
          </svg>
          <div class="cap2">EXHIBIT B · PRICE</div><div class="tp" style="right:-30px;top:-18px;transform:rotate(25deg)"></div>
        </div>
        <div class="a note" id="s4n" style="left:560px;top:580px;transform:rotate(6deg)">SAB SACH HAI?</div>'''),
        scn("s5", f'''
        <div class="a lg red" id="s5h" style="left:70px;top:250px;font-size:200px">ASLI KHEL</div>
        <div class="a pol" id="s5a" style="left:70px;top:520px;width:430px;height:470px;transform:rotate(-5deg)">
          <div class="dark" style="height:360px;display:flex;align-items:flex-end;justify-content:center;gap:12px;padding-bottom:30px">{people(3, 96, "#FFF7D3")}</div>
          <div class="cap2">GROUP ADMINS</div><div class="tp" style="left:-26px;top:-16px;transform:rotate(-30deg)"></div></div>
        <div class="a pol" id="s5b" style="left:540px;top:600px;width:470px;height:470px;transform:rotate(4deg)">
          <svg width="426" height="360" viewBox="0 0 426 360"><rect width="426" height="360" fill="#1A1A00"/>
            <polyline points="10,330 80,320 150,310 220,270 290,200 360,120 416,60" fill="none" stroke="#FFBA09" stroke-width="8" stroke-linejoin="round" opacity=".55"/>
            <g id="s5lo"><circle cx="80" cy="320" r="16" fill="#3BE58F" stroke="#FFF7D3" stroke-width="3"/><text x="104" y="300" font-family="SFM" font-weight="700" font-size="24" fill="#3BE58F">SASTA</text></g>
          </svg><div class="cap2">PEHLE HI KHAREEDA</div><div class="tp" style="right:-26px;top:-16px;transform:rotate(28deg)"></div></div>
        <svg class="a" style="left:0;top:0" width="1080" height="1920"><path id="s5s" d="M420 560 C 560 470, 700 520, 800 640" stroke="#AB1509" stroke-width="6" fill="none" stroke-dasharray="520" stroke-dashoffset="520"/>
          <circle id="s5p1" cx="420" cy="560" r="16" fill="#AB1509" stroke="#1A1A00" stroke-width="3"/><circle id="s5p2" cx="800" cy="640" r="16" fill="#AB1509" stroke="#1A1A00" stroke-width="3"/></svg>
        <div class="a stamp" id="s5st" style="left:240px;top:1110px;font-size:120px;transform:rotate(-7deg)">INSIDER</div>'''),
        scn("s6", f'''
        <div class="a pol" id="s6p" style="left:90px;top:300px;width:900px;height:760px;transform:rotate(-2deg)">
          <svg width="856" height="640" viewBox="0 0 856 640"><rect width="856" height="640" fill="#1A1A00"/>
            <polyline points="20,560 160,520 300,430 440,300 540,160 600,90" fill="none" stroke="#FFBA09" stroke-width="12" stroke-linejoin="round" stroke-linecap="round" id="s6l" stroke-dasharray="900" stroke-dashoffset="900"/>
            <g id="s6sell"><rect x="560" y="20" width="220" height="60" rx="10" fill="#AB1509"/><text x="670" y="62" text-anchor="middle" font-family="SFM" font-weight="700" font-size="32" fill="#FFF7D3">ADMINS: SELL</text>
            <circle cx="600" cy="90" r="18" fill="#AB1509" stroke="#FFF7D3" stroke-width="4"/></g>
          </svg><div class="cap2">EXHIBIT C · PEAK</div><div class="tp" style="left:-30px;top:-18px;transform:rotate(-26deg)"></div></div>
        <div class="a crowd" id="s6c" style="left:110px;top:1110px">{people(10, 60, "#AB1509", "pc6")}</div>
        <div class="a mono red" id="s6cl" style="left:110px;top:1210px;font-size:30px">NAYE LOG AATE HAIN →</div>
        <div class="a lg ink" id="s6x" style="left:620px;top:1180px;font-size:150px;transform:rotate(-4deg)">EXIT <span class="red">→</span></div>'''),
        scn("s7", f'''
        <div class="a pol" id="s7p" style="left:90px;top:280px;width:900px;height:700px;transform:rotate(1.5deg)">
          <svg width="856" height="580" viewBox="0 0 856 580"><rect width="856" height="580" fill="#1A1A00"/>
            <polyline points="20,500 160,460 300,380 440,260 540,130 600,60" fill="none" stroke="#FFBA09" stroke-width="10" stroke-linejoin="round" opacity=".5"/>
            <polyline id="s7l" points="600,60 650,250 700,420 760,520 836,550" fill="none" stroke="#AB1509" stroke-width="14" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="620" stroke-dashoffset="620"/>
          </svg><div class="cap2">EXHIBIT D · CRASH</div></div>
        <div class="a lg ink" id="s7q" style="left:70px;top:1020px;font-size:190px">BACHA KAUN?</div>
        <div class="a" id="s7spot" style="left:300px;top:1230px;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle,rgba(255,186,9,.55),transparent 70%)"></div>
        <div class="a" id="s7you" style="left:380px;top:1230px;text-align:center">{PERSON.format(w=140, h=182, c="#AB1509")}<div class="lg red" style="font-size:90px;margin-top:-6px">AAP</div></div>'''),
        scn("s8", '''
        <div class="a" id="s8w" style="left:0;right:0;top:520px;text-align:center"><div class="stamp" id="s8st" style="display:inline-block;font-size:260px;line-height:.9;padding:20px 50px 6px;transform:rotate(-8deg)">PUMP<br>&amp; DUMP</div></div>'''),
        scn("s9", '''
        <div class="a lg red" id="s9h" style="left:70px;top:250px;font-size:200px">YAAD RAKHO</div>
        <div class="a pad" id="s9pad" style="left:80px;top:500px;width:920px;height:780px;transform:rotate(-1.5deg)">
          <div class="item" id="s9i1"><div class="num">1</div><div><div class="it">"GUARANTEED PROFIT"</div><div class="is">bolne wala <span class="hl">dost nahi</span> hai</div></div></div>
          <div class="item" id="s9i2"><div class="num">2</div><div><div class="it">SIRF HYPE WALA COIN</div><div class="is">usse <span class="hl">door raho</span></div></div></div>
          <div class="a stamp" id="s9x" style="right:50px;top:560px;font-size:80px;transform:rotate(8deg)">RED FLAG</div>
        </div>'''),
        scn("s10", '''
        <div class="a" id="s10f" style="left:120px;top:420px;width:840px;height:900px;border-radius:18px;background:#E9DCA8;border:5px solid #1A1A00;transform:rotate(-2deg)">
          <div style="position:absolute;left:40px;top:-60px;width:300px;height:70px;background:#E9DCA8;border:5px solid #1A1A00;border-bottom:none;border-radius:16px 16px 0 0"></div>
          <div class="mono" style="position:absolute;left:50px;top:50px;font-size:34px">SCAM FILES · CASE #01</div>
          <div class="lg ink" style="position:absolute;left:50px;top:110px;font-size:150px">PUMP &amp; DUMP</div>
          <div class="mono red" style="position:absolute;left:50px;top:300px;font-size:30px">NEXT: CASE #02 · FAKE TRADING APP</div>
        </div>
        <div class="a stamp" id="s10st" style="left:160px;top:820px;font-size:210px;line-height:.9;transform:rotate(-10deg);background:rgba(255,247,211,.6)">CASE<br>CLOSED</div>
        <div class="a mono red" id="s10h" style="left:0;right:0;top:1370px;text-align:center;font-size:36px">FOLLOW @NIKS.CRYPTO</div>'''),
    ]

    html = f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="assets/gsap.min.js"></script>
    <style>
      @font-face {{ font-family: "SFL"; src: url("assets/fonts/league-gothic-latin-400-normal.woff2"); }}
      @font-face {{ font-family: "SFA"; src: url("assets/fonts/archivo-black-latin-400-normal.woff2"); }}
      @font-face {{ font-family: "SFM"; font-weight: 400; src: url("assets/fonts/space-mono-latin-400-normal.woff2"); }}
      @font-face {{ font-family: "SFM"; font-weight: 700; src: url("assets/fonts/space-mono-latin-700-normal.woff2"); }}
      @font-face {{ font-family: "SFI"; font-weight: 800; src: url("assets/fonts/inter-latin-800-normal.woff2"); }}
      :root {{ --paper:#FFF7D3; --red:#AB1509; --ink:#1A1A00; --amber:#FFBA09; }}
      * {{ margin:0; padding:0; box-sizing:border-box; }}
      html, body {{ width:1080px; height:1920px; overflow:hidden; background:var(--paper); }}
      #root {{ position:absolute; inset:0; font-family:"SFI",sans-serif; color:var(--ink); overflow:hidden; }}
      .bg {{ position:absolute; inset:0; background:var(--paper); }}
      .grid {{ position:absolute; inset:-200px; background-image:linear-gradient(rgba(171,21,9,.07) 2px,transparent 2px),linear-gradient(90deg,rgba(171,21,9,.07) 2px,transparent 2px); background-size:90px 90px; }}
      .vig {{ position:absolute; inset:0; background:radial-gradient(ellipse at 50% 45%,transparent 55%,rgba(120,80,0,.2)); }}
      .scene {{ position:absolute; inset:0; }}
      .cam {{ position:absolute; inset:0; transform-origin:50% 45%; }}
      .a {{ position:absolute; }}
      .lg {{ font-family:"SFL"; text-transform:uppercase; line-height:.9; letter-spacing:.005em; white-space:nowrap; }}
      .mono {{ font-family:"SFM"; font-weight:700; letter-spacing:.08em; }}
      .red {{ color:var(--red); }} .ink {{ color:var(--ink); }} .amber {{ color:var(--amber); }}
      .stamp {{ font-family:"SFL"; color:var(--red); border:12px solid var(--red); padding:10px 34px 0; border-radius:16px; letter-spacing:.04em; text-transform:uppercase; white-space:nowrap; line-height:1; }}
      .tapebar {{ background:var(--ink); color:var(--paper); font-family:"SFM"; font-weight:700; font-size:36px; letter-spacing:.2em; padding:16px 30px; text-align:center; white-space:nowrap; overflow:hidden; }}
      .pol {{ background:#fff; padding:22px 22px 80px; box-shadow:10px 16px 0 rgba(26,26,0,.18),0 0 0 4px var(--ink); }}
      .pol .cap2 {{ position:absolute; left:0; right:0; bottom:22px; text-align:center; font-family:"SFM"; font-weight:700; font-size:30px; letter-spacing:.06em; }}
      .dark {{ background:var(--ink); color:var(--paper); }}
      .tp {{ position:absolute; width:170px; height:50px; background:rgba(255,186,9,.78); }}
      .row {{ display:flex; align-items:baseline; gap:18px; }}
      .msg {{ margin-top:26px; background:#2b2b14; border-left:8px solid var(--amber); border-radius:14px; padding:20px 24px; font-family:"SFI"; font-size:40px; color:var(--paper); }}
      .crowd {{ display:flex; gap:14px; }}
      .note {{ background:var(--amber); padding:22px 30px; font-family:"SFA"; font-size:60px; box-shadow:8px 10px 0 rgba(26,26,0,.2); }}
      .pad {{ background:#fff; box-shadow:10px 16px 0 rgba(26,26,0,.18),0 0 0 4px var(--ink);
        background-image:linear-gradient(transparent 118px, rgba(171,21,9,.18) 118px, rgba(171,21,9,.18) 121px, transparent 121px); background-size:100% 122px; padding:60px 50px; }}
      .item {{ display:flex; gap:30px; align-items:flex-start; margin-bottom:70px; }}
      .num {{ width:110px; height:110px; flex:none; border-radius:50%; background:var(--red); color:var(--paper); font-family:"SFL"; font-size:90px; text-align:center; line-height:118px; }}
      .it {{ font-family:"SFL"; font-size:110px; line-height:.95; }}
      .is {{ font-family:"SFA"; font-size:48px; margin-top:8px; }}
      .hl {{ background:var(--red); color:var(--paper); padding:0 12px; }}
      #topbar {{ position:absolute; left:-40px; top:84px; width:1160px; height:80px; background:var(--red); transform:rotate(-2.5deg); display:flex; align-items:center; gap:36px; padding-left:80px;
        font-family:"SFM"; font-weight:700; font-size:28px; letter-spacing:.18em; color:var(--paper); white-space:nowrap; overflow:hidden; }}
      #topbar b {{ font-family:"SFL"; font-weight:400; font-size:56px; letter-spacing:.04em; }}
      #brand {{ position:absolute; right:50px; top:196px; font-family:"SFM"; font-weight:700; font-size:26px; letter-spacing:.06em; }}
      #brand i {{ font-style:normal; color:var(--red); }}
      #robot {{ position:absolute; left:820px; top:1190px; }}
      .cap {{ position:absolute; left:40px; right:40px; top:1480px; text-align:center; }}
      .ci {{ display:inline-block; font-family:"SFA"; font-size:84px; line-height:1.05; text-transform:uppercase; letter-spacing:-.01em; }}
      .ci .k {{ display:inline-block; background:var(--red); color:var(--paper); padding:0 16px; transform:rotate(-2deg); }}
      #handle {{ position:absolute; left:0; right:0; top:1700px; text-align:center; font-family:"SFM"; font-weight:700; font-size:28px; letter-spacing:.08em; color:var(--red); }}
      #swipe {{ position:absolute; top:-100px; left:0; width:1900px; height:2120px; background:var(--ink); }}
      #swipe2 {{ position:absolute; top:-100px; left:0; width:1900px; height:2120px; background:var(--red); }}
      .pp {{ display:inline-block; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
      <div id="bgwrap" class="clip" data-start="0" data-duration="{DUR}" data-track-index="0"><div class="bg"></div><div class="grid" id="grid"></div><div class="vig"></div></div>
{chr(10).join(scenes)}
      <div id="chrome" class="clip" data-start="2.72" data-duration="{round(DUR-2.72,2)}" data-track-index="7" data-layout-allow-overlap>
        <div id="topbar"><b>SCAM FILES</b> CASE #01 · PUMP &amp; DUMP · CASE #01 · PUMP &amp; DUMP</div>
        <div id="brand">niks<i>.crypto</i></div>
        <div id="handle">● @NIKS.CRYPTO · SCAM FILES</div>
      </div>
      <div id="robotclip" class="clip" data-start="2.72" data-duration="{round(DUR-2.72,2)}" data-track-index="8"><div id="robot">{ROBOT}</div></div>
{cap_divs}
      <div id="swipeclip" class="clip" data-start="0" data-duration="{DUR}" data-track-index="10" data-layout-allow-occlusion><div id="swipe"></div><div id="swipe2"></div></div>
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      const S = {json.dumps({k: [a, b] for k, a, b in SCENES})};
      // camera drift on every scene
      for (const k in S) {{ const [a, b] = S[k]; tl.fromTo("#" + k + "cam", {{ scale: 1.0 }}, {{ scale: 1.045, duration: b - a, ease: "none" }}, a); }}
      tl.fromTo("#grid", {{ x: 0, y: 0 }}, {{ x: -90, y: -180, duration: {DUR}, ease: "none" }}, 0);
      // paper swipes at scene cuts (cover the cut at its midpoint)
      const cuts = [2.72, 9.80, 19.95, 28.85, 38.60];
      cuts.forEach((c, i) => {{
        const el = i % 2 ? "#swipe2" : "#swipe";
        tl.fromTo(el, {{ x: -2300, skewX: -12 }}, {{ x: 1700, skewX: -12, duration: 0.5, ease: "power2.inOut", immediateRender: i < 2 }}, c - 0.25);
      }});
      // punch-in cuts (hard cut + zoom settle)
      [5.40, 14.20, 25.55, 31.25].forEach((c) => {{
        const k = Object.keys(S).find((s) => Math.abs(S[s][0] - c) < 0.01);
        tl.fromTo("#" + k, {{ scale: 1.18 }}, {{ scale: 1, duration: 0.35, ease: "power3.out" }}, c);
      }});
      const slam = {{ scale: 1, opacity: 1, duration: 0.22, ease: "power4.in" }};
      // s1 title
      tl.fromTo("#s1t", {{ scale: 2.6, opacity: 0 }}, slam, 0.05);
      tl.fromTo("#s1tape", {{ scaleX: 0, transformOrigin: "0% 50%" }}, {{ scaleX: 1, duration: 0.35, ease: "power3.out" }}, 0.75);
      tl.fromTo("#s1st", {{ scale: 2.4, opacity: 0, rotation: -20 }}, {{ scale: 1, opacity: 1, rotation: -8, duration: 0.2, ease: "power4.in" }}, 1.45);
      // s2 hype words
      tl.fromTo("#s2a", {{ scale: 2, opacity: 0 }}, slam, 2.79);
      tl.fromTo("#s2b", {{ scale: 2.4, opacity: 0 }}, slam, 3.55);
      tl.fromTo("#s2c", {{ scale: 2, opacity: 0 }}, slam, 4.35);
      tl.fromTo("#s2r", {{ x: -200, y: 300, opacity: 0 }}, {{ x: 40, y: -120, opacity: 1, duration: 1.4, ease: "power2.out" }}, 3.7);
      // s3 telegram
      tl.fromTo("#s3p", {{ y: 900, rotation: 8 }}, {{ y: 0, rotation: -3, duration: 0.5, ease: "power3.out" }}, 5.45);
      const cnt = {{ n: 1240 }};
      tl.fromTo(cnt, {{ n: 1240 }}, {{ n: 52000, duration: 0.9, ease: "power1.in",
        onUpdate: () => {{ document.querySelector("#s3n").textContent = Math.round(cnt.n).toLocaleString("en-IN"); }} }}, 6.6);
      ["#m1", "#m2", "#m3", "#m4"].forEach((m, i) => tl.fromTo(m, {{ x: -60, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.22, ease: "back.out(2)" }}, 7.8 + i * 0.42));
      tl.fromTo("#s3c .pc", {{ y: 80, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25, stagger: 0.05, ease: "back.out(2)" }}, 6.64);
      // s4 you buy, price up
      tl.fromTo("#s4h", {{ scale: 2, opacity: 0 }}, slam, 9.98);
      tl.fromTo("#s4p", {{ y: 700 }}, {{ y: 0, duration: 0.45, ease: "power3.out" }}, 9.85);
      tl.fromTo("#s4m", {{ scale: 0, transformOrigin: "225px 520px" }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)" }}, 10.3);
      tl.to("#s4l", {{ attr: {{ "stroke-dashoffset": 0 }}, duration: 1.4, ease: "power1.in" }}, 11.15);
      tl.fromTo("#s4n", {{ scale: 0, rotation: -20 }}, {{ scale: 1, rotation: 6, duration: 0.3, ease: "back.out(2.2)" }}, 13.1);
      // s5 asli khel
      tl.fromTo("#s5h", {{ scale: 2.2, opacity: 0 }}, slam, 14.37);
      tl.fromTo("#s5a", {{ x: -700 }}, {{ x: 0, duration: 0.4, ease: "power3.out" }}, 15.4);
      tl.fromTo("#s5b", {{ x: 700 }}, {{ x: 0, duration: 0.4, ease: "power3.out" }}, 15.8);
      tl.fromTo(["#s5p1", "#s5p2"], {{ scale: 0, transformOrigin: "50% 50%" }}, {{ scale: 1, duration: 0.2, stagger: 0.15 }}, 16.75);
      tl.to("#s5s", {{ attr: {{ "stroke-dashoffset": 0 }}, duration: 0.6, ease: "power2.out" }}, 16.85);
      tl.fromTo("#s5lo", {{ scale: 0, transformOrigin: "80px 320px" }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)" }}, 18.3);
      tl.fromTo("#s5st", {{ scale: 2.4, opacity: 0, rotation: -20 }}, {{ scale: 1, opacity: 1, rotation: -7, duration: 0.2, ease: "power4.in" }}, 19.0);
      // s6 new people, peak, admins sell
      tl.fromTo("#s6p", {{ y: 700 }}, {{ y: 0, duration: 0.45, ease: "power3.out" }}, 20.0);
      tl.fromTo("#s6c .pc6", {{ y: -200, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.3, stagger: 0.07, ease: "bounce.out" }}, 20.6);
      tl.fromTo("#s6cl", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2 }}, 21.0);
      tl.to("#s6l", {{ attr: {{ "stroke-dashoffset": 0 }}, duration: 1.1, ease: "power1.in" }}, 21.9);
      tl.fromTo("#s6sell", {{ scale: 0, transformOrigin: "670px 60px" }}, {{ scale: 1, duration: 0.25, ease: "back.out(2.5)" }}, 23.4);
      tl.fromTo("#s6x", {{ x: -300, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.35, ease: "power3.out" }}, 24.2);
      tl.to("#s6c", {{ opacity: 0.35, duration: 0.3 }}, 24.4);
      // s7 crash
      tl.to("#s7l", {{ attr: {{ "stroke-dashoffset": 0 }}, duration: 0.7, ease: "power2.in" }}, 25.74);
      tl.to("#s7p", {{ x: 14, duration: 0.05, yoyo: true, repeat: 7, ease: "none" }}, 26.4);
      tl.fromTo("#s7q", {{ scale: 2, opacity: 0 }}, slam, 27.1);
      tl.fromTo("#s7spot", {{ scale: 0, opacity: 0 }}, {{ scale: 1.6, opacity: 1, duration: 0.3 }}, 28.15);
      tl.fromTo("#s7you", {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.25, ease: "back.out(2.5)" }}, 28.2);
      // s8 stamp
      tl.fromTo("#s8st", {{ scale: 3, opacity: 0, rotation: -25 }}, {{ scale: 1, opacity: 1, rotation: -8, duration: 0.2, ease: "power4.in" }}, 29.97);
      tl.to("#s8w", {{ x: 18, duration: 0.04, yoyo: true, repeat: 7, ease: "none" }}, 30.18);
      // s9 tips
      tl.fromTo("#s9h", {{ scale: 2, opacity: 0 }}, slam, 31.43);
      tl.fromTo("#s9pad", {{ y: 900 }}, {{ y: 0, duration: 0.45, ease: "power3.out" }}, 31.6);
      tl.fromTo("#s9i1", {{ x: -80, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.3, ease: "power3.out" }}, 32.25);
      tl.fromTo("#s9x", {{ scale: 2.4, opacity: 0, rotation: -10 }}, {{ scale: 1, opacity: 1, rotation: 8, duration: 0.2, ease: "power4.in" }}, 33.95);
      tl.fromTo("#s9i2", {{ x: -80, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.3, ease: "power3.out" }}, 35.4);
      // s10 case closed
      tl.fromTo("#s10f", {{ y: 900, rotation: 6 }}, {{ y: 0, rotation: -2, duration: 0.45, ease: "power3.out" }}, 38.62);
      tl.fromTo("#s10st", {{ scale: 3, opacity: 0, rotation: -30 }}, {{ scale: 1, opacity: 1, rotation: -10, duration: 0.2, ease: "power4.in" }}, 38.85);
      tl.to("#s10f", {{ x: 14, duration: 0.04, yoyo: true, repeat: 5, ease: "none" }}, 39.05);
      tl.fromTo("#s10h", {{ opacity: 0, y: 20 }}, {{ opacity: 1, y: 0, duration: 0.3 }}, 39.4);
      // chrome + robot
      tl.fromTo("#topbar", {{ x: -1200 }}, {{ x: 0, duration: 0.45, ease: "power3.out" }}, 2.75);
      tl.fromTo("#robot", {{ y: 400 }}, {{ y: 0, duration: 0.5, ease: "back.out(1.6)" }}, 2.8);
      tl.fromTo("#robot", {{ rotation: -3 }}, {{ rotation: 3, duration: 0.6, yoyo: true, repeat: 60, ease: "sine.inOut", transformOrigin: "50% 100%", immediateRender: false }}, 3.3);
      const pose = (id, a, b) => {{ tl.fromTo(id, {{ opacity: 0 }}, {{ opacity: 1, duration: 0.05, immediateRender: false }}, a); tl.to(id, {{ opacity: 0, duration: 0.05 }}, b); }};
      tl.to("#eyeN", {{ opacity: 0, duration: 0.05 }}, 14.3); pose("#eyeS", 14.3, 25.6);
      pose("#eyeX", 25.6, 31.2); pose("#bang", 25.6, 31.2);
      tl.to("#eyeN", {{ opacity: 1, duration: 0.05 }}, 31.2);
      tl.to("#eyeN", {{ opacity: 0, duration: 0.05 }}, 38.6); pose("#eyeH", 38.6, {DUR + 1});
      tl.to("#hat", {{ y: -26, rotation: -12, transformOrigin: "130px 100px", duration: 0.25, yoyo: true, repeat: 1 }}, 39.3);
      tl.to("#armL", {{ rotation: -18, transformOrigin: "58px 170px", duration: 0.25, yoyo: true, repeat: 1 }}, 10.0);
      tl.to("#armL", {{ rotation: -18, transformOrigin: "58px 170px", duration: 0.25, yoyo: true, repeat: 1 }}, 32.3);
      // captions pop
      document.querySelectorAll(".cap").forEach((c) => {{
        const st = parseFloat(c.dataset.start);
        tl.fromTo(c.querySelector(".ci"), {{ scale: 0.7, y: 24, opacity: 0 }}, {{ scale: 1, y: 0, opacity: 1, duration: 0.16, ease: "back.out(2.4)" }}, st);
      }});
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''
    os.makedirs(os.path.join(PROJ, "assets", "fonts"), exist_ok=True)
    open(os.path.join(PROJ, "index.html"), "w").write(html)
    json.dump({"caps": caps, "scenes": SCENES}, open(os.path.join(HERE, "timing.json"), "w"), indent=1)
    print("captions:", len(caps))


if __name__ == "__main__":
    build()
