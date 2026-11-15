import os
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__))
CSS='''
@font-face{font-family:SG;font-weight:400;src:url(../cover/fonts/space-grotesk-latin-400-normal.woff2)}
@font-face{font-family:SG;font-weight:500;src:url(../cover/fonts/space-grotesk-latin-500-normal.woff2)}
@font-face{font-family:SG;font-weight:700;src:url(../cover/fonts/space-grotesk-latin-700-normal.woff2)}
@font-face{font-family:SM;font-weight:400;src:url(../cover/fonts/space-mono-latin-400-normal.woff2)}
@font-face{font-family:SM;font-weight:700;src:url(../cover/fonts/space-mono-latin-700-normal.woff2)}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden;background:#120917}
body{position:relative;font-family:SG,sans-serif;color:#fff}
.a{position:absolute}
.bg{inset:0;background:radial-gradient(1000px 800px at 50% 70%,#24113A 0%,#170B20 55%,#120917 100%)}
.glow{left:140px;top:980px;width:800px;height:500px;border-radius:50%;background:rgba(157,20,255,.24);filter:blur(90px)}
.grid{left:60px;right:60px;top:420px;height:860px;background-image:linear-gradient(rgba(231,182,255,.07) 1.5px,transparent 1.5px),linear-gradient(90deg,rgba(231,182,255,.07) 1.5px,transparent 1.5px);background-size:64px 64px;
 -webkit-mask-image:radial-gradient(ellipse at center,#000 35%,transparent 72%)}
.top{left:70px;right:70px;top:60px;display:flex;justify-content:space-between;align-items:center;font-size:28px;font-weight:500;color:rgba(255,255,255,.45)}
.top b{color:#C858C6;font-weight:700}
.top .n{font-family:SM;font-size:24px;padding:8px 18px;border-radius:30px;border:1.5px solid rgba(255,255,255,.2)}
.cap{left:70px;right:70px;top:150px;text-align:center}
.s{font-size:50px;color:rgba(255,255,255,.88);line-height:1.15}
.b{font-weight:700;font-size:92px;letter-spacing:-.04em;line-height:1.02}
.g{font-weight:700;font-size:104px;letter-spacing:-.04em;line-height:1.02;background:linear-gradient(90deg,#F1D2FF,#C858C6 55%,#A63BFF);-webkit-background-clip:text;color:transparent}
.h{display:inline-block;margin-top:16px;background:#fff;color:#120917;font-weight:700;font-size:56px;padding:2px 22px 8px;letter-spacing:-.02em}
.card{background:#F6F0FA;color:#1A0F22;border-radius:30px;box-shadow:0 50px 100px rgba(0,0,0,.6)}
.mono{font-family:SM}
.foot{left:70px;right:70px;bottom:56px;display:flex;justify-content:space-between;align-items:center}
.dots{display:flex;gap:10px}.dots i{width:12px;height:12px;border-radius:6px;background:rgba(255,255,255,.22)}.dots i.on{width:40px;background:linear-gradient(90deg,#9D14FF,#C858C6)}
.sw{font-weight:700;font-size:30px;color:#fff}.sw span{color:#C858C6}
.stamp{border:6px solid #E0584F;color:#E0584F;border-radius:16px;padding:8px 24px;font-family:SM;font-weight:700;font-size:44px;letter-spacing:.06em;background:rgba(18,9,23,.85);white-space:nowrap}
'''
def page(i,cap,body,last=False):
    dots=''.join(f'<i class="{"on" if k==i else ""}"></i>' for k in range(1,7))
    sw='<div class="sw">Save karo <span>🔖</span></div>' if last else '<div class="sw">Swipe <span>→</span></div>'
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="a bg"></div><div class="a glow"></div><div class="a grid"></div>
<div class="a top"><div>niks<b>.crypto</b></div><div class="n">Crypto Stories · EP 03 · {i}/6</div></div>
<div class="a cap">{cap}</div>{body}
<div class="a foot"><div class="dots">{dots}</div>{sw}</div></body></html>'''

S=[]
# 1 hook
S.append(page(1,'<div class="s">Duniya ka #1 bitcoin exchange.</div><div class="b" style="margin-top:8px">Ek din band.</div><div class="g">8,50,000 BTC</div><div class="b" style="font-size:72px">gayab.</div>',
'''<div class="a card" style="left:170px;top:700px;width:740px;transform:rotate(-3deg);padding-bottom:30px">
<div style="display:flex;gap:12px;align-items:center;padding:22px 28px;border-bottom:2px solid #E6DDEE"><i style="width:16px;height:16px;border-radius:50%;background:#D5C8E0"></i><i style="width:16px;height:16px;border-radius:50%;background:#D5C8E0"></i><i style="width:16px;height:16px;border-radius:50%;background:#D5C8E0"></i><span class="mono" style="margin-left:14px;font-size:24px;color:#8B7B98">mtgox.com</span></div>
<div style="padding:24px 34px 0;font-weight:700;font-size:54px;color:#7A10D8">Mt. Gox</div>
<div style="display:flex;gap:18px;align-items:center;margin:18px 34px 0;padding:20px;border-radius:20px;background:#FDEDEC;border:3px solid #E0584F">
<b style="width:60px;height:60px;flex:none;border-radius:50%;background:#E0584F;color:#fff;display:flex;align-items:center;justify-content:center;font-size:38px">!</b>
<div><div style="font-weight:700;font-size:36px;color:#B3261E">Withdrawals suspended</div><div class="mono" style="font-size:20px;color:#8B7B98;margin-top:4px">FEB 2014 · UNTIL FURTHER NOTICE</div></div></div></div>
<div class="a stamp" style="left:650px;top:1030px;transform:rotate(-8deg)">GAYAB</div>'''))
# 2 origin
S.append(page(2,'<div class="s">Shuruaat hui ek</div><div class="b">card game site</div><div class="s" style="margin-top:6px">se. Naam ka matlab tha:</div>',
'''<div class="a" style="left:0;right:0;top:560px;display:flex;justify-content:center;gap:16px">'''+''.join(f'<div class="card" style="width:150px;height:190px;border-radius:24px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:110px;color:#7A10D8">{c}</div>' for c in 'MTGOX')+'''</div>
<div class="a" style="left:0;right:0;top:800px;text-align:center;font-size:46px;line-height:1.35"><b style="color:#E7B6FF">M</b>agic: <b style="color:#E7B6FF">T</b>he <b style="color:#E7B6FF">G</b>athering<br><b style="color:#E7B6FF">O</b>nline e<b style="color:#E7B6FF">X</b>change</div>
<div class="a" style="left:0;right:0;top:960px;text-align:center"><div class="h" style="font-size:46px">2010 → Bitcoin exchange ban gaya</div></div>'''))
# 3 70%
S.append(page(3,'<div class="s">2013 tak duniya ke</div><div class="g">~70%</div><div class="s">bitcoin trades yahin hote the.</div>',
'''<div class="a" style="left:340px;top:520px;width:400px;height:400px">
<svg width="400" height="400" viewBox="0 0 400 400"><defs><linearGradient id="gr" x1="0" x2="1"><stop offset="0" stop-color="#9D14FF"/><stop offset="1" stop-color="#C858C6"/></linearGradient></defs>
<circle cx="200" cy="200" r="160" fill="none" stroke="rgba(255,255,255,.1)" stroke-width="56"/>
<circle cx="200" cy="200" r="160" fill="none" stroke="url(#gr)" stroke-width="56" stroke-linecap="round" stroke-dasharray="703.7 1005.3" transform="rotate(-90 200 200)"/></svg>
<div class="a" style="inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center"><div class="mono" style="font-weight:700;font-size:96px;color:#E7B6FF">70%</div><div class="mono" style="font-size:20px;color:#A99BB3;letter-spacing:.1em;text-align:center;line-height:1.4">OF ALL<br>BTC TRADES</div></div></div>
<div class="a" style="left:0;right:0;top:980px;text-align:center"><div class="h" style="font-size:48px">Sabse bada. Sabse "safe"?</div></div>'''))
# 4 hack
S.append(page(4,'<div class="s">Saalon tak hot wallet se</div><div class="b">chupke se BTC</div><div class="g" style="font-size:96px">leak hote rahe.</div>',
'''<div class="a card" style="left:190px;top:560px;width:700px;padding:36px 40px">
<div class="mono" style="font-size:22px;color:#8B7B98;letter-spacing:.12em">MT. GOX · FEB 2014</div>
<div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:22px"><span style="font-size:36px">Customers ka BTC</span><b class="mono" style="font-size:40px;color:#7A10D8">7,50,000</b></div>
<div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:16px"><span style="font-size:36px">Company ka BTC</span><b class="mono" style="font-size:40px;color:#7A10D8">1,00,000</b></div>
<div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:22px;padding-top:22px;border-top:3px dashed #CBBFD6"><span style="font-weight:700;font-size:40px">Total missing</span><b class="mono" style="font-size:52px;color:#E0584F">8,50,000</b></div>
<div style="margin-top:20px;font-size:28px;color:#5D4E68">7 Feb: withdrawals band · 28 Feb: bankruptcy</div></div>
<div class="a stamp" style="left:600px;top:1000px;transform:rotate(-7deg);font-size:38px">BANKRUPT</div>'''))
# 5 refund
S.append(page(5,'<div class="s">Baad mein ~2,00,000 BTC mile.</div><div class="b">Refund shuru hua</div><div class="g">10 saal baad.</div>',
'''<div class="a" style="left:0;right:0;top:620px;display:flex;justify-content:center;align-items:center;gap:40px">
<div class="card" style="width:330px;text-align:center;opacity:.55;transform:rotate(-5deg)"><div class="mono" style="border-radius:30px 30px 0 0;background:#3A2846;color:#fff;font-weight:700;font-size:32px;letter-spacing:.2em;padding:22px 0">FEB</div><div style="font-weight:700;font-size:130px;letter-spacing:-.04em;line-height:1.1">2014</div><div class="mono" style="font-size:22px;color:#8B7B98;padding-bottom:22px">BAND HUA</div></div>
<div style="font-size:80px;color:#C858C6;font-weight:700">→</div>
<div class="card" style="width:330px;text-align:center;transform:rotate(4deg)"><div class="mono" style="border-radius:30px 30px 0 0;background:linear-gradient(90deg,#9D14FF,#C858C6);color:#fff;font-weight:700;font-size:32px;letter-spacing:.2em;padding:22px 0">JUL</div><div style="font-weight:700;font-size:130px;letter-spacing:-.04em;line-height:1.1;color:#7A10D8">2024</div><div class="mono" style="font-size:22px;color:#8B7B98;padding-bottom:22px">REFUND SHURU</div></div></div>
<div class="a" style="left:0;right:0;top:1010px;text-align:center"><div class="h" style="font-size:46px">10 saal ka intezaar ⏳</div></div>'''))
# 6 lesson + CTA
S.append(page(6,'<div class="s">Lesson simple hai:</div><div class="b">Not your keys,</div><div class="g">not your coins.</div>',
'''<div class="a card" style="left:190px;top:560px;width:700px;padding:34px 40px">
<div style="display:flex;gap:20px;align-items:center"><div style="width:84px;height:84px;border-radius:22px;background:linear-gradient(135deg,#9D14FF,#C858C6);display:flex;align-items:center;justify-content:center;font-size:46px">🔑</div>
<div><div style="font-weight:700;font-size:38px">Lambe time ka BTC?</div><div style="font-size:30px;color:#5D4E68;margin-top:4px">Apne wallet mein rakho.</div></div></div>
<div style="margin-top:24px;font-size:32px;line-height:1.5">✓ Exchange sirf trading ke liye<br>✓ Seed phrase offline, safe jagah<br>✓ Kisi ko keys mat do</div></div>
<div class="a" style="left:190px;top:1010px;width:700px;display:flex;align-items:center;padding:22px 30px;border-radius:44px;background:rgba(255,255,255,.1);border:1.5px solid rgba(255,255,255,.25);font-size:36px;font-weight:700">
<span>Comment <span style="color:#E7B6FF">"GOX"</span> 👇</span><span style="margin-left:auto;font-size:28px;color:#C858C6">Follow @niks.crypto</span></div>''',last=True))

with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,h in enumerate(S,1):
        f=f"{D}/slide{i}.html"; open(f,"w").write(h)
        pg.goto('file://'+f); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
        pg.screenshot(path=f'{D}/mt-gox-carousel-{i}.png')
    b.close()
