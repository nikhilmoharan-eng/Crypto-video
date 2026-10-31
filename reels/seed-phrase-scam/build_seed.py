"""EP 3 — seed phrase scam. Cuts the ElevenLabs voice-over into per-beat clips and writes episode JSON."""
import json, os, subprocess
import numpy as np, soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.environ.get("VO", os.path.join(HERE, "voiceover.mp3"))
CLIPS = os.path.join(HERE, "clips_seed")
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
WORDS = ["river", "candle", "orbit", "maple", "tiger", "lunar", "ocean", "silver", "frozen", "punch", "gravity", "wisdom"]


def word_cols(t0):
    cols = []
    for c in range(2):
        items = []
        for r in range(6):
            i = c * 6 + r
            items.append({"tag": f"{i + 1:02d}", "tagColor": "acc", "text": WORDS[i], "in": f"{t0}+{0.07 * i:.2f}"})
        cols.append({"title": f"WORD {c * 6 + 1}–{c * 6 + 6}", "color": "mute", "items": items})
    return cols


ep = {
    "series": "CRYPTO.DECODED",
    "series_icon": "shield",
    "episode": 3,
    "tag": "SEED PHRASE SCAM",
    "accent": "red",
    "disclaimer": "SIRF JAANKARI · EXAMPLE WORDS · NOT ADVICE",
    "concept": "SEED PHRASE SCAM",
    "music_mood": "tense",
    "brand": {"wordmark": "niks", "suffix": ".crypto", "handle": "@niks.crypto", "color": "#7C5CFF",
              "outro_log": "Scam alert successfully installed.", "follow": "FOLLOW @NIKS.CRYPTO"},
    "stinger_lines": {"boot": "SYSTEM ONLINE", "detect": "THREAT DETECTED:", "run": "SCANNING SCAM…"},

    "hook": [
        {
            "hold": 0.04, "chip": "AAPKA WALLET · EXAMPLE",
            "elements": [
                {"type": "row", "gap": 18, "in": 0, "items": [
                    {"type": "object", "kind": "lock", "color": "red", "size": 120, "in": 0},
                    {"type": "stat", "value": 12, "from": 0, "size": "l", "color": "acc", "label": "WORDS", "sub": "= AAPKA POORA CRYPTO", "in": "1:baarah"}
                ]},
                {"type": "columns", "title": "SEED PHRASE", "in": "0.1", "mt": 12, "cols": word_cols("1:baarah")},
                {"type": "stamp", "text": "SEED PHRASE", "color": "acc", "rot": -6, "size": 40, "in": "2:seed",
                 "pos": {"x": 320, "y": 330, "center": True}}
            ],
            "beats": [
                B(0.00, 1.36, "Aapka *poora crypto…*", mascot="think", mascot_pos=R),
                B(1.75, 3.33, "sirf *baarah words* mein band hai.", mascot="shock", mascot_pos=R),
                B(3.74, 5.23, "Inhe kehte hain *seed phrase.*", mascot="point", mascot_pos=R, pause=0.18)
            ]
        }
    ],

    "body": [
        {
            "hold": 0.04, "chip": "WALLET BANATE HI",
            "elements": [
                {"type": "row", "gap": 24, "in": 0, "items": [
                    {"type": "phone", "w": 250, "in": 0, "screen": "#14161a", "time": "9:41",
                     "app": {"title": "Create wallet", "price": "Recovery phrase", "sub": "Likh lo · kisi ko mat dikhao", "button": "SHOW WORDS", "buttonColor": "acc", "in": "0:wallet"}},
                    {"type": "stack", "gap": 16, "items": [
                        {"type": "stat", "value": 12, "size": "l", "color": "acc", "label": "WORDS", "in": "1:baarah"},
                        {"type": "text", "mono": True, "text": "— YA —", "in": "1:ya"},
                        {"type": "stat", "value": 24, "size": "l", "color": "acc", "label": "WORDS", "in": "1:chaubees"}
                    ]}
                ]}
            ],
            "beats": [
                B(5.62, 6.81, "Jab aap *wallet banate* ho,", mascot="idle", mascot_pos=R),
                B(7.12, 9.77, "wallet aapko *baarah ya chaubees* English words deta hai.", mascot="point", mascot_pos=R)
            ]
        },
        {
            "hold": 0.04, "chip": "2048 WORDS KI LIST",
            "elements": [
                {"type": "stat", "value": 2048, "from": 0, "size": "l", "color": "acc", "label": "WORDS KI FIXED LIST", "in": "0:hazaar"},
                {"type": "grid", "shape": "dot", "cols": 32, "count": 192, "cell": 15, "color": "dim", "highlight": 12,
                 "hl": "0:list", "hlColor": "acc", "in": 0, "mt": 6, "label": "12 WORDS ISI LIST SE"},
                {"type": "stat", "value": "≈ 5 × 10³⁹", "count": False, "size": "m", "color": "ink", "label": "COMBINATIONS", "in": "1:combinations", "mt": 10},
                {"type": "stamp", "text": "GUESS = IMPOSSIBLE", "color": "green", "rot": -5, "size": 32, "in": "2:guess",
                 "pos": {"x": 320, "y": 250, "center": True}}
            ],
            "beats": [
                B(10.24, 13.93, "Ye words, *do hazaar adtaalees* words ki ek fixed list se aate hain."),
                B(14.37, 16.34, "Aur inke *combinations* itne zyada hain,", mascot="think", mascot_pos=R),
                B(16.63, 18.56, "ki koi computer inhe ^guess nahi^ kar sakta.", mascot="happy", mascot_pos=R)
            ]
        },
        {
            "hold": 0.04, "chip": "TOH HACKER KYA KARTA HAI?",
            "flash": True,
            "elements": [
                {"type": "card", "w": 600, "in": 0, "rows": [
                    {"icon": "cpu", "iconColor": "mute", "label": "Guess karna", "sub": "COMPUTER SE", "badge": "NAMUMKIN", "badgeColor": "mute", "in": 0, "dim": "1"},
                    {"icon": "user", "iconColor": "red", "label": "Aapse maangna", "sub": "BAATON MEIN PHASA KE", "badge": "ASAAN", "badgeColor": "red", "in": "1:maangta", "red": "1:maangta"}
                ]},
                {"type": "bigtext", "text": "Wo ~maangta~ hai.", "size": 86, "in": "1:maangta", "mt": 30}
            ],
            "beats": [
                B(19.26, 20.59, "Toh hacker *guess nahi karta…*", mascot="think", mascot_pos=R),
                B(21.11, 22.13, "wo aapse ~maangta~ hai.", mascot="shock", mascot_pos=R, pause=0.18)
            ]
        },
        {
            "hold": 0.04, "chip": "FAKE SUPPORT · SCAM",
            "elements": [
                {"type": "chat", "title": "Wallet Support ✓", "right": "ONLINE", "in": 0, "messages": [
                    {"from": "Wallet Support", "text": "Sir, main wallet support se bol raha hoon.", "in": "0:Sir"},
                    {"from": "Wallet Support", "text": "Verify karne ke liye apne 12 words bhejiye.", "in": "1:Verify"}
                ]},
                {"type": "card", "title": "RED FLAGS", "w": 600, "in": "0:support", "mt": 14, "rows": [
                    {"icon": "check", "iconColor": "red", "label": "Fake blue tick", "sub": "DM · TELEGRAM · CALL", "in": "0:support", "compact": True},
                    {"icon": "clock", "iconColor": "red", "label": "Jaldi verify karo", "sub": "URGENCY = DABAAV", "in": "1:Verify", "compact": True},
                    {"icon": "key", "iconColor": "red", "label": "12 words maange", "sub": "SABSE BADA RED FLAG", "in": "1:words", "red": "2:scam", "compact": True}
                ]},
                {"type": "stamp", "text": "SCAM", "color": "red", "rot": -9, "size": 92, "in": "2:scam",
                 "pos": {"x": 330, "y": 120, "center": True}, "shake": "2:scam"}
            ],
            "beats": [
                B(22.62, 24.72, "\"Sir, main *wallet support* se bol raha hoon.\"", mascot="wink", mascot_pos=R),
                B(25.08, 27.45, "\"Verify karne ke liye, apne *baarah words* bhejiye.\"", mascot="think", mascot_pos=R),
                B(27.86, 28.68, "~Yahi scam hai.~", mascot="shock", mascot_pos=R, pause=0.18)
            ]
        },
        {
            "hold": 0.04, "chip": "WALLET KISKA?",
            "elements": [
                {"type": "object", "kind": "key", "color": "gold", "size": 150, "in": 0, "label": "12 WORDS = MASTER KEY"},
                {"type": "card", "w": 600, "in": 0, "mt": 12, "rows": [
                    {"icon": "key", "iconColor": "acc", "label": "12 words", "sub": "JISKE PAAS", "badge": "WALLET USKA", "badgeColor": "red", "in": "0:baarah", "hl": "1:uska"},
                    {"icon": "lock", "iconColor": "mute", "label": "Password", "badge": "ZAROORI NAHI", "badgeColor": "mute", "in": "2:password"},
                    {"icon": "phone", "iconColor": "mute", "label": "OTP", "badge": "ZAROORI NAHI", "badgeColor": "mute", "in": "2:OTP"}
                ]}
            ],
            "beats": [
                B(29.09, 30.56, "Jiske paas ye *baarah words* hain…", mascot="point", mascot_pos=R),
                B(30.87, 31.84, "wallet ~uska~ hai.", mascot="shock", mascot_pos=R),
                B(32.26, 34.05, "Na *password* chahiye, na *OTP.*", mascot="sad", mascot_pos=R)
            ]
        },
        {
            "hold": 0.04, "chip": "PAISA GAYA TOH?",
            "elements": [
                {"type": "card", "title": "WALLET BALANCE · EXAMPLE", "w": 600, "in": 0, "rows": [
                    {"icon": "wallet", "iconColor": "red", "label": "Transfer: 12 words se", "sub": "BLOCKCHAIN PE CONFIRMED", "badge": "IRREVERSIBLE", "badgeColor": "red", "in": "0:paisa"}
                ]},
                {"type": "stat", "value": 0, "from": 250000, "prefix": "₹", "size": "xl", "color": "red", "label": "AB BALANCE", "in": "0:paisa", "mt": 16},
                {"type": "stamp", "text": "NO REFUND", "color": "red", "rot": -7, "size": 48, "in": "1:wapas",
                 "pos": {"x": 320, "y": 330, "center": True}}
            ],
            "beats": [
                B(34.48, 35.44, "Aur ~paisa gaya…~", mascot="shock", mascot_pos=R),
                B(35.81, 36.75, "toh ~wapas nahi aata.~", mascot="sad", mascot_pos=R, pause=0.18)
            ]
        },
        {
            "hold": 0.04, "chip": "3 RULES YAAD RAKHO",
            "chip_color": "green",
            "elements": [
                {"type": "bigtext", "text": "*3* rules", "size": 110, "in": 0, "out": "1", "pos": {"x": 320, "y": 200, "center": True}},
                {"type": "list", "w": 600, "in": "1", "items": [
                    {"kicker": "RULE 1", "title": "Seed phrase *kabhi share nahi*", "in": "1:kabhi"},
                    {"kicker": "RULE 2", "title": "Screenshot / cloud nahi — *kaagaz pe*", "in": "3:screenshot"},
                    {"kicker": "RULE 3", "title": "Website maange? *Turant band*", "in": "5:website"}
                ]},
                {"type": "stamp", "text": "ASLI SUPPORT KABHI NAHI MAANGTA", "color": "green", "rot": -3, "size": 24, "in": "2:asli",
                 "pos": {"x": 320, "y": 470, "center": True}}
            ],
            "beats": [
                B(37.24, 38.44, "Toh *teen rules* yaad rakho.", mascot="point", mascot_pos=C),
                B(38.85, 41.20, "Ek: seed phrase ~kabhi kisi ko mat do.~", mascot="point", mascot_pos=R),
                B(41.59, 43.38, "Koi bhi *asli support* ye nahi maangta."),
                B(43.79, 46.90, "Do: iska *screenshot,* ya *cloud* mein copy mat rakho."),
                B(47.27, 49.10, "*Kaagaz* pe likho, aur *safe jagah* rakho.", mascot="happy", mascot_pos=R),
                B(49.48, 52.29, "Teen: koi bhi *website ya app* ye words maange…"),
                B(52.60, 53.52, "toh ~turant band~ karo.", mascot="wink", mascot_pos=R)
            ]
        },
        {
            "hold": 0.04, "chip": "SHARE KARO",
            "elements": [
                {"type": "bigtext", "text": "Share = *Protect*", "size": 84, "in": 0},
                {"type": "bubble", "quote": "Mere paas bhi crypto hai.", "in": "0:dost", "w": 560, "mt": 18},
                {"type": "tiles", "size": 100, "in": "0:video", "mt": 24, "items": [
                    {"icon": "users", "color": "acc", "label": "Dost", "in": "0:dost"},
                    {"icon": "link", "color": "brand", "label": "Share"},
                    {"icon": "shield", "color": "green", "label": "Safe"},
                    {"icon": "bell", "color": "yellow", "label": "Follow"}
                ]}
            ],
            "beats": [
                B(53.94, 56.50, "Ye video us *dost* ko bhejo, jiske paas *crypto* hai.", mascot="point", mascot_pos=R)
            ]
        }
    ],
    "outro": {"say": "Ab samjhe?", "audio": clip(56.93, 57.50), "dur": 3.0}
}

json.dump(ep, open(os.path.join(HERE, "episode.json"), "w"), ensure_ascii=False, indent=1)
print("beats:", sum(len(s["beats"]) for s in ep["hook"] + ep["body"]))
