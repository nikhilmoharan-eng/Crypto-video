"""EP 4: why Bitcoin is capped at 21 million. Cuts the voice-over into per-beat clips and writes episode JSON."""
import json, os, subprocess
import numpy as np, soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.environ.get("VO", os.path.join(HERE, "voiceover.mp3"))
OUT = os.environ.get("OUT", os.path.join(HERE, "episode.json"))
CLIPS = os.path.join(HERE, "clips_btc")
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
    "series_icon": "coin",
    "episode": 4,
    "tag": "21 MILLION CAP",
    "accent": "orange",
    "disclaimer": "SIRF JAANKARI · FIGURES: 31 OCT 2026 TAK · NOT ADVICE",
    "concept": "BITCOIN 21 MILLION LIMIT",
    "music_mood": "bright",
    "brand": {"wordmark": "niks", "suffix": ".crypto", "handle": "@niks.crypto", "color": "#7C5CFF",
              "outro_log": "Bitcoin basics successfully installed.", "follow": "FOLLOW @NIKS.CRYPTO"},
    "stinger_lines": {"boot": "SYSTEM ONLINE", "detect": "CONCEPT DETECTED:", "run": "RUNNING EXPLANATION…"},

    "hook": [
        {
            "hold": 0.04, "chip": "DOLLAR vs BITCOIN",
            "elements": [
                {"type": "card", "w": 600, "in": 0, "rows": [
                    {"icon": "bank", "iconColor": "mute", "label": "US Dollar", "sub": "SARKAR / CENTRAL BANK", "in": "0:dollar"},
                    {"icon": "doc", "iconColor": "red", "label": "Supply limit?", "sub": "ZAROORAT PADE TOH", "badge": "AUR CHHAP SAKTE", "badgeColor": "red", "in": "1", "red": "1:chhaap"}
                ]},
                {"type": "grid", "shape": "doc", "cols": 16, "count": 32, "cell": 30, "color": "green", "in": "1", "stagger": 0.025, "mt": 12,
                 "label": "$ PRINTER · AUR, AUR, AUR…"},
                {"type": "row", "gap": 22, "in": "2:Bitcoin", "mt": 20, "align": "center", "items": [
                    {"type": "icon", "name": "₿", "size": 104, "color": "#16171a", "bg": "acc", "round": True, "in": "2:Bitcoin"},
                    {"type": "stat", "value": 21, "from": 0, "prefix": "₿ ", "suffix": "M", "size": "l", "color": "acc", "label": "MAX SUPPLY · BAS ITNE HI", "in": "3:million"}
                ]},
                {"type": "stamp", "text": "HARD CAP", "color": "acc", "rot": -6, "size": 46, "in": "4:zyada",
                 "pos": {"x": 430, "y": 470, "center": True}}
            ],
            "beats": [
                B(0.00, 1.44, "Duniya mein *dollar* kitne hain?", mascot="think", mascot_pos=R),
                B(1.95, 4.37, "Zaroorat pade, toh sarkar ~aur chhaap~ sakti hai."),
                B(4.92, 5.60, "Par *Bitcoin?*", mascot="think", mascot_pos=R),
                B(6.09, 7.25, "Sirf *21 million.*", mascot="shock", mascot_pos=R),
                B(7.65, 8.42, "Ek bhi ~zyada nahi.~", mascot="point", mascot_pos=R, pause=0.18)
            ]
        }
    ],

    "body": [
        {
            "hold": 0.04, "chip": "LIMIT KISNE RAKHI?",
            "elements": [
                {"type": "card", "w": 600, "in": 0, "rows": [
                    {"icon": "building", "iconColor": "mute", "label": "Koi company", "badge": "NAHI", "badgeColor": "red", "in": "0:company", "dim": "1"},
                    {"icon": "cpu", "iconColor": "acc", "label": "Bitcoin ka code", "sub": "HAZAARON COMPUTERS CHALATE HAIN", "badge": "HAAN", "badgeColor": "green", "in": "1:code", "hl": "1:code"}
                ]},
                {"type": "paper", "kicker": "BITCOIN RULE", "right": "SINCE 2009", "title": "21,000,000", "sub": "MAX SUPPLY · CODE MEIN FIXED", "in": "1:code", "mt": 20}
            ],
            "beats": [
                B(8.87, 10.30, "Ye limit kisi *company* ne nahi,", mascot="idle", mascot_pos=R),
                B(10.53, 12.09, "*Bitcoin ke code* ne tay ki hai.", mascot="point", mascot_pos=R)
            ]
        },
        {
            "hold": 0.04, "chip": "NAYE BITCOIN KAISE?",
            "elements": [
                {"type": "grid", "shape": "square", "cols": 12, "count": 36, "cell": 38, "color": "dim", "highlight": 1.0,
                 "hl": "1:block", "hlColor": "acc", "in": "0:mining", "stagger": 0.03, "label": "HAR SQUARE = EK BLOCK"},
                {"type": "row", "gap": 30, "in": "1:das", "mt": 18, "items": [
                    {"type": "ring", "text": "10m", "frac": 1, "color": "acc", "r": 62, "label": "LAGBHAG HAR BLOCK", "in": "1:das"},
                    {"type": "icon", "name": "gear", "size": 96, "color": "acc", "label": "MINING", "in": "0:mining"}
                ]}
            ],
            "beats": [
                B(12.52, 14.14, "Naye bitcoin *mining* se bante hain."),
                B(14.56, 16.84, "Lagbhag har *das minute* mein, ek naya *block.*", mascot="happy", mascot_pos=R)
            ]
        },
        {
            "hold": 0.04, "chip": "HALVING",
            "elements": [
                {"type": "bars", "title": "BLOCK REWARD (BTC)", "w": 600, "labelW": 96, "in": 0, "items": [
                    {"label": "2009", "value": 1.0, "color": "acc", "right": "50", "in": "2:pachaas"},
                    {"label": "2012", "value": 0.5, "color": "acc", "right": "25", "in": "0:aadha"},
                    {"label": "2016", "value": 0.25, "color": "acc", "right": "12.5", "in": "0:aadha+0.25"},
                    {"label": "2020", "value": 0.125, "color": "acc", "right": "6.25", "in": "0:aadha+0.5"},
                    {"label": "2024", "value": 0.0625, "color": "green", "right": "3.125", "in": "3:teen"}
                ]},
                {"type": "stamp", "text": "HALVING = ÷2", "color": "acc", "rot": -5, "size": 46, "in": "1:halving",
                 "pos": {"x": 320, "y": 400, "center": True}},
                {"type": "text", "mono": True, "text": "AGLA HALVING: ~2028", "in": "3:teen+0.6", "mt": 16}
            ],
            "beats": [
                B(17.22, 19.93, "Aur har *chaar saal* mein, ye reward ~aadha~ ho jaata hai.", mascot="point", mascot_pos=R),
                B(20.38, 21.71, "Ise kehte hain, *halving.*", mascot="wink", mascot_pos=R),
                B(22.16, 24.51, "Shuru mein ek block pe *50 bitcoin* milte the."),
                B(24.92, 27.01, "Aaj sirf, *3.125.*", mascot="shock", mascot_pos=R)
            ]
        },
        {
            "hold": 0.04, "chip": "AB TAK KITNE NIKLE?",
            "elements": [
                {"type": "stat", "value": 20, "from": 0, "suffix": "M+", "prefix": "₿ ", "size": "xl", "color": "acc", "label": "BITCOIN MINED · OCT 2026", "in": 0},
                {"type": "split", "title": "21 MILLION MEIN SE", "w": 600, "in": "0:million", "mt": 18,
                 "a": {"label": "MINED ~96%", "frac": 0.957, "color": "acc"}, "b": {"label": "BAAKI ~4%", "color": "mute", "in": "1:Lagbhag"}},
                {"type": "grid", "shape": "dot", "cols": 25, "count": 100, "cell": 18, "color": "acc", "highlight": 4,
                 "hl": "1:Lagbhag", "hlColor": "mute", "hlFrom": "end", "in": "0:million", "mt": 16, "label": "HAR DOT = 1%"}
            ],
            "beats": [
                B(27.42, 30.47, "Aur ab tak, *20 million* se zyada bitcoin nikal chuke hain.", mascot="shock", mascot_pos=R),
                B(30.86, 32.10, "Lagbhag *96%.*", mascot="point", mascot_pos=R)
            ]
        },
        {
            "hold": 0.04, "chip": "AAKHRI BITCOIN",
            "elements": [
                {"type": "timeline", "title": "BITCOIN TIMELINE", "icon": "clock", "w": 600, "in": 0,
                 "segments": [{"from": 0, "to": 0.13, "color": "acc", "in": 0, "dur": 0.6},
                              {"from": 0.13, "to": 1, "color": "dim", "in": "1:saal", "dur": 1.6}],
                 "ticks": [{"pos": 0, "label": "2009"}, {"pos": 0.13, "label": "AAJ", "color": "acc"},
                           {"pos": 1, "label": "~2140", "color": "acc", "in": "1:saal"}]},
                {"type": "bigtext", "text": "~*2140*", "size": 150, "in": "1:2140", "mt": 30},
                {"type": "text", "mono": True, "text": "AAKHRI BITCOIN · LAGBHAG", "in": "1:2140", "mt": 4}
            ],
            "beats": [
                B(32.53, 33.44, "*Aakhri bitcoin…*", mascot="think", mascot_pos=R),
                B(33.82, 36.23, "saal *2140* ke aas paas niklega.", mascot="shock", mascot_pos=R)
            ]
        },
        {
            "hold": 0.04, "chip": "KEY BHOOL GAYE?",
            "chip_color": "red",
            "elements": [
                {"type": "row", "gap": 22, "in": 0, "items": [
                    {"type": "object", "kind": "lock", "color": "red", "size": 120, "in": 0},
                    {"type": "card", "w": 440, "in": "0:key", "rows": [
                        {"icon": "key", "iconColor": "red", "label": "Key bhool gaye", "sub": "PASSWORD / SEED PHRASE", "in": "0:key", "compact": True},
                        {"icon": "lock", "iconColor": "red", "label": "Coins", "badge": "LOCK FOREVER", "badgeColor": "red", "in": "1:lock", "compact": True}
                    ]}
                ]},
                {"type": "grid", "shape": "ring", "cols": 10, "count": 40, "cell": 46, "color": "acc", "highlight": 9,
                 "hl": "1:lock", "hlColor": "#3a3d3d", "hlFrom": "end", "in": 0, "mt": 18, "label": "EXAMPLE · KUCH COINS HAMESHA KE LIYE GAYE"},
                {"type": "stamp", "text": "ASLI SUPPLY < 21M", "color": "acc", "rot": -5, "size": 34, "in": "2:supply",
                 "pos": {"x": 320, "y": 330, "center": True}}
            ],
            "beats": [
                B(36.72, 38.25, "Aur jo log apni *key bhool gaye…*", mascot="sad", mascot_pos=R),
                B(38.68, 40.64, "unke coins, ~hamesha ke liye lock~ hain.", mascot="sad", mascot_pos=R),
                B(41.07, 42.98, "Matlab asli supply, *aur bhi kam.*", mascot="point", mascot_pos=R)
            ]
        },
        {
            "hold": 0.04, "chip": "DIGITAL GOLD",
            "chip_color": "yellow",
            "elements": [
                {"type": "row", "gap": 40, "in": 0, "items": [
                    {"type": "icon", "name": "Au", "size": 140, "color": "#16171a", "bg": "gold", "round": True, "label": "GOLD", "in": 0},
                    {"type": "text", "text": "≈", "size": 90, "weight": 900, "color": "mute", "in": "0:digital"},
                    {"type": "icon", "name": "₿", "size": 140, "color": "#16171a", "bg": "acc", "round": True, "label": "BITCOIN", "in": "0:digital"}
                ]},
                {"type": "check", "title": "KYUN?", "in": "1:Kam", "mt": 22, "items": [
                    {"label": "Kam supply", "tick": "1:Kam"},
                    {"label": "Fixed rules", "tick": "1:fixed"}
                ]}
            ],
            "beats": [
                B(43.38, 45.70, "Isliye log Bitcoin ko *digital gold* kehte hain.", mascot="happy", mascot_pos=R),
                B(46.12, 47.63, "*Kam supply,* *fixed rules.*", mascot="point", mascot_pos=R)
            ]
        },
        {
            "hold": 0.04, "chip": "PAR YAAD RAKHO",
            "chip_color": "red",
            "flash": True,
            "elements": [
                {"type": "linechart", "title": "PRICE · EXAMPLE", "tag": "UP & DOWN", "w": 600, "in": 0, "color": "acc", "dur": 2.2,
                 "points": [30, 42, 36, 58, 47, 72, 55, 64, 41, 52, 38, 60], "min": 20, "max": 80},
                {"type": "bigtext", "text": "Supply *≠* Price", "size": 84, "in": "1:matlab", "mt": 22},
                {"type": "stamp", "text": "DEMAND SE CHALTA HAI", "color": "acc", "rot": -4, "size": 30, "in": "2:demand",
                 "pos": {"x": 320, "y": 470, "center": True}}
            ],
            "beats": [
                B(48.05, 48.69, "Par *yaad rakho.*", mascot="point", mascot_pos=R),
                B(49.12, 51.97, "Kam supply ka matlab ye nahi, ki price ~sirf upar~ jaayega.", mascot="think", mascot_pos=R),
                B(52.39, 53.82, "Price, *demand* se chalta hai.", mascot="wink", mascot_pos=R)
            ]
        },
        {
            "hold": 0.04, "chip": "SHARE KARO",
            "elements": [
                {"type": "bigtext", "text": "Share *karo*", "size": 84, "in": 0},
                {"type": "bubble", "quote": "Bitcoin mein aisa kya hai?", "in": "0:poochta", "w": 560, "mt": 18},
                {"type": "tiles", "size": 100, "in": "0:dost", "mt": 24, "items": [
                    {"icon": "users", "color": "acc", "label": "Dost", "in": "0:dost"},
                    {"icon": "link", "color": "brand", "label": "Share"},
                    {"icon": "heart", "color": "red", "label": "Save"},
                    {"icon": "bell", "color": "green", "label": "Follow"}
                ]}
            ],
            "beats": [
                B(54.25, 58.00, "Ye video us *dost* ko bhejo, jo poochta hai, \"Bitcoin mein *aisa kya hai?*\"", mascot="point", mascot_pos=R)
            ]
        }
    ],
    "outro": {"say": "Ab samjhe?", "audio": clip(58.41, 58.97), "dur": 3.0}
}

json.dump(ep, open(OUT, "w"), ensure_ascii=False, indent=1)
print("beats:", sum(len(s["beats"]) for s in ep["hook"] + ep["body"]))
