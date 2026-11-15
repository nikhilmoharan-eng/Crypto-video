import os
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__))
CSS='''
@font-face{font-family:SG;font-weight:400;src:url(../ep03-mt-gox/cover/fonts/space-grotesk-latin-400-normal.woff2)}
@font-face{font-family:SG;font-weight:500;src:url(../ep03-mt-gox/cover/fonts/space-grotesk-latin-500-normal.woff2)}
@font-face{font-family:SG;font-weight:700;src:url(../ep03-mt-gox/cover/fonts/space-grotesk-latin-700-normal.woff2)}
@font-face{font-family:SM;font-weight:400;src:url(../ep03-mt-gox/cover/fonts/space-mono-latin-400-normal.woff2)}
@font-face{font-family:SM;font-weight:700;src:url(../ep03-mt-gox/cover/fonts/space-mono-latin-700-normal.woff2)}
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
<div class="a top"><div>niks<b>.crypto</b></div><div class="n">Crypto Stories · QuadrigaCX · {i}/6</div></div>
<div class="a cap">{cap}</div>{body}
<div class="a foot"><div class="dots">{dots}</div>{sw}</div></body></html>'''

S=[]
B='<b style="width:60px;height:60px;flex:none;border-radius:50%;background:#E0584F;color:#fff;display:flex;align-items:center;justify-content:center;font-size:38px">!</b>'
S.append(page(1,'<div class="s">CEO ki death hui…</div><div class="b" style="margin-top:8px">aur saath le gaya</div><div class="g">₹1,000 Cr+</div><div class="b" style="font-size:72px">ka password.</div>',
'''<div class="a card" style="left:190px;top:720px;width:700px;padding:32px 36px;transform:rotate(-3deg)">
<div style="display:flex;gap:18px;align-items:center"><div style="width:76px;height:76px;border-radius:20px;background:linear-gradient(135deg,#9D14FF,#C858C6);display:flex;align-items:center;justify-content:center;font-size:40px">🔒</div>
<div><div style="font-weight:700;font-size:40px">QuadrigaCX</div><div class="mono" style="font-size:20px;color:#8B7B98;letter-spacing:.1em">CANADA KA #1 EXCHANGE</div></div></div>
<div class="mono" style="margin-top:24px;padding:18px 22px;border-radius:16px;background:#140A1A;color:#E7B6FF;font-size:34px;letter-spacing:.3em">●●●●●●●●●●</div></div>
<div class="a stamp" style="left:640px;top:990px;transform:rotate(-8deg)">LOCKED</div>'''))
S.append(page(2,'<div class="s">Dec 2018. Honeymoon trip.</div><div class="b">Jaipur, India.</div><div class="s" style="margin-top:6px">30 saal ke CEO ki achanak death.</div>',
'''<div class="a card" style="left:240px;top:600px;width:600px;padding:34px 38px">
<div class="mono" style="font-size:22px;color:#8B7B98;letter-spacing:.12em">CEO · QUADRIGACX</div>
<div style="font-weight:700;font-size:52px;margin-top:10px">Gerald Cotten</div>
<div style="display:flex;justify-content:space-between;margin-top:22px;font-size:32px"><span>Age</span><b class="mono" style="color:#7A10D8">30</b></div>
<div style="display:flex;justify-content:space-between;margin-top:12px;font-size:32px"><span>Location</span><b class="mono" style="color:#7A10D8">📍 Jaipur</b></div>
<div style="display:flex;justify-content:space-between;margin-top:12px;font-size:32px"><span>Date</span><b class="mono" style="color:#7A10D8">9 DEC 2018</b></div></div>
<div class="a" style="left:0;right:0;top:1010px;text-align:center"><div class="h" style="font-size:46px">Problem toh ab shuru hui…</div></div>'''))
S.append(page(3,'<div class="s">Cold wallet ki keys</div><div class="b">sirf ek aadmi</div><div class="g" style="font-size:96px">ke paas thi.</div>',
'''<div class="a" style="left:0;right:0;top:600px;display:flex;justify-content:center;gap:28px">
<div class="card" style="width:300px;padding:30px;text-align:center"><div class="mono" style="font-weight:700;font-size:64px;color:#7A10D8">76,000</div><div style="font-size:30px;margin-top:6px">customers</div></div>
<div class="card" style="width:300px;padding:30px;text-align:center"><div class="mono" style="font-weight:700;font-size:64px;color:#E0584F">0</div><div style="font-size:30px;margin-top:6px">backup keys</div></div></div>
<div class="a card" style="left:240px;top:850px;width:600px;padding:24px 30px;display:flex;gap:18px;align-items:center;border:3px solid #E0584F;background:#FDEDEC">'''+B+'''
<div><div style="font-weight:700;font-size:34px;color:#B3261E">Withdrawals frozen</div><div class="mono" style="font-size:20px;color:#8B7B98">JAN 2019</div></div></div>'''))
S.append(page(4,'<div class="s">Experts ne wallets khole…</div><div class="b">Andar kya mila?</div><div class="g">Kuch nahi.</div>',
'''<div class="a card" style="left:240px;top:640px;width:600px;padding:34px 40px">
<div class="mono" style="font-size:22px;color:#8B7B98;letter-spacing:.12em">COLD WALLET · BALANCE</div>
<div class="mono" style="font-weight:700;font-size:120px;color:#E0584F;margin-top:6px">0.00</div>
<div class="mono" style="font-size:26px;color:#8B7B98">BTC · EMPTY SINCE 2018</div></div>
<div class="a stamp" style="left:610px;top:930px;transform:rotate(-7deg)">KHAALI</div>'''))
S.append(page(5,'<div class="s">Investigation (2020) ka result:</div><div class="b">Ye hack nahi tha.</div><div class="g">Fraud tha.</div>',
'''<div class="a card" style="left:190px;top:640px;width:700px;padding:34px 40px">
<div class="mono" style="font-size:22px;color:#8B7B98;letter-spacing:.12em">CUSTOMER KA PAISA GAYA KAHAN?</div>
<div style="margin-top:20px;font-size:34px;line-height:1.6">✗ Doosre exchanges pe risky trading<br>✗ Fake accounts, fake balance<br>✗ Luxury lifestyle, jet, property</div></div>
<div class="a" style="left:0;right:0;top:1030px;text-align:center"><div class="h" style="font-size:46px">Paisa kabhi tha hi nahi.</div></div>'''))
S.append(page(6,'<div class="s">Lesson:</div><div class="b">Exchange bank</div><div class="g">nahi hai.</div>',
'''<div class="a card" style="left:190px;top:590px;width:700px;padding:34px 40px">
<div style="font-weight:700;font-size:38px">Apne crypto ko safe rakho:</div>
<div style="margin-top:18px;font-size:32px;line-height:1.55">✓ Long term coins → apne wallet mein<br>✓ Exchange pe sirf trading amount<br>✓ Proof of reserves check karo<br>✓ "Too good" returns = red flag</div></div>
<div class="a" style="left:190px;top:1020px;width:700px;display:flex;align-items:center;padding:22px 30px;border-radius:44px;background:rgba(255,255,255,.1);border:1.5px solid rgba(255,255,255,.25);font-size:36px;font-weight:700">
<span>Comment <span style="color:#E7B6FF">"KEYS"</span> 👇</span><span style="margin-left:auto;font-size:28px;color:#C858C6">Follow @niks.crypto</span></div>''',last=True))

with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,h in enumerate(S,1):
        f=f"{D}/slide{i}.html"; open(f,"w").write(h)
        pg.goto('file://'+f); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
        pg.screenshot(path=f'{D}/quadriga-carousel-{i}.png')
    b.close()
