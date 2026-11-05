"""Blue gradient restyle of Case 01: rewrites hf/index.html produced by build.py.

Palette (sampled from the background): navy #0B1F4A · deep #073974 · royal #2F6FD8 · sky #7CC0FF · mist #8FA4BF · ice #EAF3FF
"""
import os, re
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hf", "index.html")
s = open(p).read()
for a, b in [("#1A1A00", "#0B1F4A"), ("#FFF7D3", "#EAF3FF"), ("#AB1509", "#2F6FD8"), ("#FFBA09", "#7CC0FF"), ("#E9DCA8", "rgba(11,31,74,.72)"),
             ("rgba(171,21,9,", "rgba(124,192,255,"), ("rgba(26,26,0,", "rgba(4,14,38,"), ("rgba(255,186,9,.78)", "rgba(124,192,255,.55)"),
             ("rgba(255,247,211,.5)", "rgba(234,243,255,.35)"), ("rgba(255,247,211,.6)", "rgba(11,31,74,.55)"), ("rgba(120,80,0,.2)", "rgba(4,14,38,.45)"),
             ("#2b2b14", "#143a7a")]:
    s = s.replace(a, b)
s = s.replace("--paper:#EAF3FF; --red:#2F6FD8; --ink:#0B1F4A; --amber:#7CC0FF;", "--paper:#EAF3FF; --red:#9FD3FF; --ink:#FFFFFF; --amber:#7CC0FF; --navy:#0B1F4A; --royal:#2F6FD8;")
css = '''
      .bg { background:#0B1F4A url("assets/bg.jpg") center/cover no-repeat; transform-origin:30% 60%; }
      .grid { opacity:0; }
      .lg.ink, .ink { color:#FFFFFF; text-shadow:0 6px 28px rgba(4,14,38,.45); }
      .red { color:#9FD3FF; text-shadow:0 5px 0 #0B1F4A, 0 10px 30px rgba(4,14,38,.4); }
      .mono { color:#EAF3FF; }
      .stamp { color:#EAF3FF; border-color:#EAF3FF; background:rgba(11,31,74,.55); text-shadow:none; }
      .tapebar { background:#0B1F4A; color:#9FD3FF; }
      .pol { background:rgba(234,243,255,.14); box-shadow:0 30px 60px rgba(4,14,38,.45), 0 0 0 2px rgba(234,243,255,.55); backdrop-filter:blur(14px); border-radius:22px; }
      .pol .cap2 { color:#EAF3FF; }
      .dark { background:#0B1F4A; border-radius:14px; }
      .note { background:#EAF3FF; color:#0B1F4A; box-shadow:0 16px 40px rgba(4,14,38,.45); border-radius:12px; }
      .pad { background-color:rgba(11,31,74,.62); background-image:linear-gradient(transparent 118px, rgba(124,192,255,.25) 118px, rgba(124,192,255,.25) 121px, transparent 121px);
        box-shadow:0 30px 60px rgba(4,14,38,.45), 0 0 0 2px rgba(234,243,255,.45); backdrop-filter:blur(12px); border-radius:22px; color:#FFFFFF; }
      .num { background:#7CC0FF; color:#0B1F4A; }
      .hl { background:#EAF3FF; color:#0B1F4A; }
      #topbar { background:#0B1F4A; color:#9FD3FF; }
      #topbar b { color:#FFFFFF; }
      #brand { color:#FFFFFF; } #brand i { color:#9FD3FF; }
      #handle { color:#EAF3FF; }
      .ci { color:#FFFFFF; text-shadow:0 6px 24px rgba(4,14,38,.55); }
      .ci .k { background:#EAF3FF; color:#0B1F4A; text-shadow:none; }
      #swipe { background:#0B1F4A; } #swipe2 { background:linear-gradient(90deg,#2F6FD8,#7CC0FF); }
      #s10f { border-color:rgba(234,243,255,.6) !important; backdrop-filter:blur(12px); }
    </style>'''
s = s.replace("    </style>", css, 1)
# slow drift of the background for motion
s = s.replace('tl.fromTo("#grid", ', 'tl.fromTo("#bgwrap .bg", { scale: 1.08, x: 0 }, { scale: 1.0, x: -30, duration: DURV, ease: "none" }, 0);\n      tl.fromTo("#grid", ')
dur = re.search(r'data-duration="([0-9.]+)" data-width', s).group(1)
s = s.replace("DURV", dur)
s = s.replace("SCAM FILES · CASE #01", "SCAM FILES · CASE #01")
s = s.replace('<polyline id="s7l" points="600,60 650,250 700,420 760,520 836,550" fill="none" stroke="#2F6FD8"', '<polyline id="s7l" points="600,60 650,250 700,420 760,520 836,550" fill="none" stroke="#EAF3FF"')
s = s.replace('id="s7you" style="left:380px;top:1230px;', 'id="s7you" style="left:380px;top:1160px;').replace('id="s7spot" style="left:300px;top:1230px;', 'id="s7spot" style="left:300px;top:1160px;')
open(p, "w").write(s)
print("restyled", dur)
