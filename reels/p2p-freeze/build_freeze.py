"""EP 5: P2P bank account freeze. Cuts the voice-over into per-beat clips and writes episode JSON."""
import json, os, subprocess
import numpy as np, soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.environ.get("VO", os.path.join(HERE, "voiceover.mp3"))
OUT = os.environ.get("OUT", os.path.join(HERE, "episode.json"))
CLIPS = os.path.join(HERE, "clips_freeze")
os.makedirs(CLIPS, exist_ok=True)
wav = os.path.join(CLIPS, "_vo.wav")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", SRC, "-ac", "1", "-ar", "44100", wav], check=True)
y, SR = sf.read(wav, dtype="float32")


def clip(a, b):
    s, e = int(max(0, a - 0.06) * SR), int((b + 0.08) * SR)
    seg = y[s:e].copy()
    n = int(0.01 * SR); seg[:n] *= np.linspace(0, 1, n); seg[-n:] *= np.linspace(1, 0, n)
    p = os.path.join(CLIPS, f"{a:07.2f}.wav"); sf.write(p, seg, SR)
    return p


def B(a, b, say, **kw):
    d = {"say": say, "audio": clip(a, b), "pause": 0.07}
    d.update(kw)
    return d


R, C = "right", "center"

ep = {
    "series": "CRYPTO.DECODED",
    "series_icon": "bank",
    "episode": 5,
    "tag": "P2P FREEZE",
    "accent": "cyan",
    "disclaimer": "SIRF JAANKARI · EXAMPLE AMOUNTS · NOT LEGAL ADVICE",
    "concept": "P2P BANK FREEZE",
    "music_mood": "tense",
    "brand": {"wordmark": "niks", "suffix": ".crypto", "handle": "@niks.crypto", "color": "#7C5CFF",
              "outro_log": "P2P safety successfully installed.", "follow": "FOLLOW @NIKS.CRYPTO"},
    "stinger_lines": {"boot": "SYSTEM ONLINE", "detect": "ALERT DETECTED:", "run": "TRACING MONEY…"},

    "hook": [
        {   # HyperFrames hero 1 plays over this scene's stage
            "hold": 0.04, "chip": "AAPKA P2P TRADE · EXAMPLE", "elements": [],
            "beats": [
                B(0.00, 1.10, "Aapne *crypto becha.*"),
                B(1.60, 2.21, "*Paisa aa gaya.*"),
                B(2.54, 3.09, "^Sab theek.^", mascot="happy", mascot_pos=R),
                B(4.88, 5.77, "*3 din baad…*"),
                B(6.34, 7.50, "aapka *bank account,*"),
                B(7.71, 8.29, "~freeze.~", mascot="shock", mascot_pos=R, pause=0.9)
            ]
        },
        {
            "hold": 0.04, "chip": "KYUN?", "chip_color": "red",
            "elements": [
                {"type": "bigtext", "text": "*Kyun?*", "size": 110, "in": 0},
                {"type": "row", "gap": 20, "in": "1", "mt": 20, "items": [
                    {"type": "icon", "name": "₹", "size": 96, "color": "#16171a", "bg": "acc", "round": True, "in": "1"},
                    {"type": "stat", "value": 50000, "from": 0, "prefix": "₹", "size": "l", "color": "ink", "label": "JO PAISA AAYA · EXAMPLE", "in": "1"}
                ]},
                {"type": "stamp", "text": "SCAM KA PAISA", "color": "red", "rot": -6, "size": 46, "in": "2:scam",
                 "pos": {"x": 320, "y": 300, "center": True}, "shake": "2:scam"}
            ],
            "beats": [
                B(9.39, 9.68, "*Kyun?*", mascot="think", mascot_pos=R, dur=0.9),
                B(10.93, 11.85, "Kyunki wo paisa,"),
                B(12.26, 13.30, "kisi ~scam~ ka tha.", mascot="shock", mascot_pos=R, pause=0.2)
            ]
        }
    ],

    "body": [
        {
            "hold": 0.04, "chip": "P2P TRADE KYA HAI?",
            "elements": [
                {"type": "flow", "w": 640, "h": 330, "in": 0, "nodes": [
                    {"id": "you", "x": 150, "y": 20, "w": 220, "icon": "user", "iconColor": "acc", "label": "Aap", "sub": "CRYPTO BECHTE HO", "in": 0},
                    {"id": "str", "x": 490, "y": 20, "w": 220, "icon": "users", "iconColor": "mute", "label": "Anjaan insaan", "sub": "BUYER", "in": "1:anjaan"},
                    {"id": "upi", "x": 320, "y": 200, "w": 260, "icon": "bank", "iconColor": "acc", "label": "UPI / Bank", "sub": "₹ AAPKE ACCOUNT MEIN", "color": "acc", "in": "2:UPI"}
                ], "edges": [
                    {"from": "you", "to": "str", "fromSide": "right", "toSide": "left", "color": "acc", "in": "1:crypto"},
                    {"from": "str", "to": "upi", "fromSide": "bottom", "toSide": "right", "color": "green", "dashed": True, "in": "2:UPI"},
                    {"from": "upi", "to": "you", "fromSide": "left", "toSide": "bottom", "color": "green", "dashed": True, "in": "2:bank"}
                ]}
            ],
            "beats": [
                B(14.33, 15.97, "Ise kehte hain, *P2P trade.*", mascot="point", mascot_pos=R),
                B(16.65, 19.10, "Aap seedha kisi *anjaan insaan* ko crypto bechte ho,"),
                B(19.38, 22.55, "aur wo aapko *UPI ya bank* se paisa bhejta hai.", mascot="idle", mascot_pos=R)
            ]
        },
        {
            "hold": 0.04, "chip": "TWIST", "chip_color": "red", "flash": True,
            "elements": [
                {"type": "card", "title": "WO PAISA KAHAN SE AAYA?", "w": 600, "in": 0, "rows": [
                    {"icon": "users", "iconColor": "mute", "label": "Buyer ka paisa?", "sub": "AAPKO LAGA", "in": 0, "dim": "1:fraud"},
                    {"icon": "alert", "iconColor": "red", "label": "Fraud victim ka paisa", "sub": "ASAL MEIN", "badge": "CHORI KA", "badgeColor": "red", "in": "1:fraud", "red": "1:victim"}
                ]},
                {"type": "bubble", "quote": "Sir, aapke account mein galti se paise aa gaye…", "in": "1:victim", "mt": 22, "w": 560}
            ],
            "beats": [
                B(23.61, 24.26, "Par *kai baar,*", mascot="think", mascot_pos=R),
                B(24.70, 26.75, "wo paisa kisi ~fraud victim~ ka hota hai.", mascot="shock", mascot_pos=R)
            ]
        },
        {   # HyperFrames hero 2 (money trail + freeze chain) plays over this scene's stage
            "hold": 0.04, "chip": "CYBER COMPLAINT → TRACE", "chip_color": "red", "elements": [],
            "beats": [
                B(27.63, 29.24, "*Victim* cyber complaint karta hai…"),
                B(29.73, 32.93, "aur *police,* paise ka poora raasta ~trace~ karti hai."),
                B(34.03, 35.41, "Aur jahan jahan wo paisa gaya,"),
                B(35.86, 37.22, "wo account ~freeze~ ho sakta hai."),
                B(37.52, 39.17, "Chahe aapki *koi galti na ho.*", mascot="sad", mascot_pos=R, pause=0.2)
            ]
        },
        {
            "hold": 0.04, "chip": "KITNA TIME?",
            "elements": [
                {"type": "timeline", "title": "ACCOUNT FREEZE", "icon": "lock", "w": 600, "in": 0,
                 "segments": [{"from": 0, "to": 1, "color": "red", "in": "1:hafte", "dur": 1.4}],
                 "ticks": [{"pos": 0, "label": "FREEZE"}, {"pos": 0.45, "label": "HAFTE…", "in": "1:hafte"},
                           {"pos": 1, "label": "MAHINE…", "color": "red", "in": "1:mahine"}]},
                {"type": "grid", "shape": "square", "cols": 10, "count": 40, "cell": 40, "color": "dim", "highlight": 1.0,
                 "hl": "1:mahine", "hlColor": "red", "in": 0, "mt": 18, "stagger": 0.015, "label": "HAR SQUARE = EK DIN · ACCOUNT BAND"}
            ],
            "beats": [
                B(40.75, 42.08, "Phir account *khulwane* mein,", mascot="think", mascot_pos=R),
                B(42.56, 44.10, "~hafte ya mahine~ bhi lag sakte hain.", mascot="sad", mascot_pos=R)
            ]
        },
        {
            "hold": 0.04, "chip": "3 RULES YAAD RAKHO", "chip_color": "green",
            "elements": [
                {"type": "bigtext", "text": "*3* rules", "size": 110, "in": 0, "out": "1", "pos": {"x": 320, "y": 200, "center": True}},
                {"type": "list", "w": 600, "in": "1", "items": [
                    {"kicker": "RULE 1", "title": "Sirf *verified, purane* traders", "in": "1:verified"},
                    {"kicker": "RULE 2", "title": "Paisa *usi ke naam* se", "in": "3:naam"},
                    {"kicker": "RULE 3", "title": "Har trade ka *screenshot + record*", "in": "5:screenshot"}
                ]},
                {"type": "check", "title": "PAYMENT CHECK", "in": "2", "mt": 16, "items": [
                    {"label": "Trader ka naam = account ka naam", "tick": "3:naam"},
                    {"label": "Third party payment", "state": "x", "tick": "4:Third"}
                ]}
            ],
            "beats": [
                B(45.34, 46.56, "Toh *teen cheezein* yaad rakho.", mascot="point", mascot_pos=C),
                B(47.04, 50.06, "Ek: sirf *verified, purane traders* se deal karo.", mascot="point", mascot_pos=R),
                B(50.73, 52.84, "Do: jiske naam se trade hai,"),
                B(53.17, 55.16, "paisa *usi ke naam* ke account se aana chahiye."),
                B(56.00, 57.80, "~Third party payment,~ bilkul nahi.", mascot="shock", mascot_pos=R),
                B(58.61, 62.38, "Teen: har trade ka *screenshot aur record,* sambhaal ke rakho.", mascot="wink", mascot_pos=R)
            ]
        },
        {
            "hold": 0.04, "chip": "SHARE KARO",
            "elements": [
                {"type": "bigtext", "text": "Share = *Safe*", "size": 84, "in": 0},
                {"type": "bubble", "quote": "Main toh P2P pe hi bechta hoon.", "in": "0:dost", "w": 560, "mt": 18},
                {"type": "tiles", "size": 100, "in": "0:video", "mt": 24, "items": [
                    {"icon": "users", "color": "acc", "label": "Dost", "in": "0:dost"},
                    {"icon": "link", "color": "brand", "label": "Share"},
                    {"icon": "shield", "color": "green", "label": "Safe"},
                    {"icon": "bell", "color": "yellow", "label": "Follow"}
                ]}
            ],
            "beats": [
                B(63.44, 66.77, "Ye video us *dost* ko bhejo, jo *P2P* pe crypto bechta hai.", mascot="point", mascot_pos=R)
            ]
        }
    ],
    "outro": {"say": "Ab samjhe?", "audio": clip(67.52, 68.13), "dur": 3.0}
}

json.dump(ep, open(OUT, "w"), ensure_ascii=False, indent=1)
print("beats:", sum(len(s["beats"]) for s in ep["hook"] + ep["body"]))
