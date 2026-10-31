"""Cut the fixed ElevenLabs voice-over into per-beat clips and write the episode JSON.

Beat times are on the ORIGINAL full.mp3 timeline; `fixed()` maps them onto vo_fixed.wav
(patched "apnaane mein", stage direction 26.55-29.55 and spoken "CTA" 130.85-131.90 removed).
"""
import json, os
import numpy as np, soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
VO = os.path.join(HERE, "voiceover_fixed.flac")
CLIPS = os.path.join(HERE, "clips")
os.makedirs(CLIPS, exist_ok=True)
y, SR = sf.read(VO, dtype="float32")


def fixed(o):
    if o <= 2.69: return o
    if o <= 26.6: return o + 0.078
    if o <= 130.9: return o - 1.922
    return o - 2.972


def clip(a, b):
    name = f"{a:07.2f}.wav"
    s, e = int(max(0, fixed(a) - 0.06) * SR), int((fixed(b) + 0.08) * SR)
    seg = y[s:e].copy()
    n = int(0.01 * SR); seg[:n] *= np.linspace(0, 1, n); seg[-n:] *= np.linspace(1, 0, n)
    p = os.path.join(CLIPS, name); sf.write(p, seg, SR)
    return p


def B(a, b, say, **kw):
    d = {"say": say, "audio": clip(a, b)}
    d.update(kw)
    return d


R = "right"
ep = {
    "series": "CRYPTO.DECODED",
    "series_icon": "coin",
    "episode": 1,
    "tag": "CRYPTO PARADOX",
    "accent": "yellow",
    "disclaimer": "SIRF JAANKARI · FIGURES: 31 OCT 2026 TAK · NOT ADVICE",
    "concept": "INDIA KA CRYPTO PARADOX",
    "music_mood": "tense",
    "brand": {"wordmark": "niks", "suffix": ".crypto", "handle": "@niks.crypto", "color": "#7C5CFF",
              "outro_log": "Crypto gyaan successfully installed.", "follow": "FOLLOW @NIKS.CRYPTO"},
    "stinger_lines": {"boot": "SYSTEM ONLINE", "detect": "TOPIC LOCKED:", "run": "LOADING EXPLANATION…"},

    "hook": [
        {
            "chip": "CRYPTO ADOPTION · DUNIYA MEIN",
            "elements": [
                {"type": "stat", "value": "#1", "count": False, "size": "xl", "color": "acc", "in": 0,
                 "label": "CRYPTO APNAANE MEIN", "sub": "CHAINALYSIS GLOBAL ADOPTION INDEX"},
                {"type": "card", "title": "CHAINALYSIS RANKING", "right": "INDIA", "w": 600, "in": "3:Chainalysis", "mt": 14, "rows": [
                    {"icon": "flag", "iconColor": "acc", "label": "2024", "sub": "GLOBAL INDEX", "value": "#1", "valueColor": "acc", "in": "4:2024", "compact": True},
                    {"icon": "flag", "iconColor": "acc", "label": "2025", "sub": "GLOBAL INDEX", "value": "#1", "valueColor": "acc", "in": "5:2025", "compact": True},
                    {"icon": "users", "label": "America", "badge": "PEECHHE", "badgeColor": "mute", "in": "6:America", "compact": True},
                    {"icon": "users", "label": "Nigeria", "badge": "PEECHHE", "badgeColor": "mute", "in": "7:Nigeria", "compact": True}
                ]}
            ],
            "beats": [
                B(0.00, 1.10, "Do saal tak…"),
                B(1.75, 4.94, "duniya mein *crypto apnaane* mein *number one* desh kaun tha?", mascot="think", mascot_pos=R),
                B(5.86, 6.29, "*India.*", mascot="happy", mascot_pos=R, pause=0.3),
                B(6.81, 8.07, "*Chainalysis* ki ranking mein —"),
                B(8.37, 9.56, "*2024* mein bhi,"),
                B(9.77, 10.95, "*2025* mein bhi —"),
                B(11.29, 12.14, "*America* se aage,"),
                B(12.43, 13.42, "*Nigeria* se aage.", mascot="happy", mascot_pos=R)
            ]
        },
        {
            "chip": "SEPTEMBER 2026",
            "elements": [
                {"type": "card", "title": "GOVT OF INDIA", "right": "REPORTS", "w": 600, "in": 0, "rows": [
                    {"icon": "bank", "iconColor": "acc", "label": "Finance Ministry", "sub": "PARLIAMENT COMMITTEE KO", "in": "1:sarkar", "compact": True}
                ]},
                {"type": "bubble", "quote": "Crypto ke liye alag kanoon?", "in": "2:alag", "mt": 26, "w": 560},
                {"type": "stamp", "text": "NAHI CHAHIYE", "color": "red", "rot": -6, "size": 44, "in": "3:Nahi+0.1",
                 "pos": {"x": 320, "y": 300, "center": True}}
            ],
            "beats": [
                B(14.06, 16.06, "Aur *September 2026* mein…"),
                B(16.29, 17.18, "*sarkar* ne kya kaha?", mascot="think", mascot_pos=R),
                B(17.72, 18.98, "\"Crypto ke liye *alag kanoon?*\""),
                B(19.51, 20.02, "\"~Nahi chahiye.~\"", mascot="shock", mascot_pos=R, pause=0.35)
            ]
        },
        {
            "align": "center",
            "elements": [
                {"type": "bigtext", "text": "*#1* in use", "size": 92, "in": 0},
                {"type": "text", "mono": True, "text": "— PHIR BHI —", "in": "1:rules", "mt": 10},
                {"type": "bigtext", "text": "~0~ naye rules?", "size": 92, "in": "1:mana", "mt": 6}
            ],
            "beats": [
                B(20.69, 23.21, "Toh jo desh *sabse zyada* crypto use karta hai…"),
                B(23.70, 26.32, "wahi *rules banane* se ~mana kyun~ kar raha hai?", mascot="think", mascot_pos="center")
            ]
        }
    ],

    "body": [
        {
            "chip": "NUMBER ONE KAISE?",
            "elements": [
                {"type": "bigtext", "text": "*Number one* kaise?", "size": 64, "in": 0, "out": "1", "pos": {"x": 320, "y": 190, "center": True}},
                {"type": "card", "title": "CHAINALYSIS KYA GINTA HAI?", "w": 600, "in": "1", "rows": [
                    {"icon": "building", "label": "Sirf bade investors", "sub": "NAHI", "in": "2:bade", "dim": "3", "compact": True},
                    {"icon": "users", "iconColor": "green", "label": "Aam log", "sub": "KHAREEDNA · BHEJNA", "in": "3:aam", "hl": "3:aam", "compact": True},
                    {"icon": "building", "iconColor": "acc", "label": "Chhote shehar", "sub": "TIER 2 · TIER 3", "in": "4:shehron", "compact": True},
                    {"icon": "coin", "iconColor": "acc", "label": "Chhoti amounts", "sub": "RETAIL TRANSFERS", "in": "5:amounts", "compact": True}
                ]},
                {"type": "grid", "shape": "person", "cols": 14, "count": 42, "cell": 30, "color": "dim", "highlight": 1.0,
                 "hl": "7:crores", "hlColor": "acc", "in": "6:India", "mt": 16, "label": "CRORES MEIN USERS"}
            ],
            "beats": [
                B(29.80, 30.78, "*Number one* kaise?", mascot="think", mascot_pos="center"),
                B(31.33, 33.68, "Pehle samjho, ye *number one* aaya kahan se."),
                B(34.19, 36.41, "*Chainalysis* sirf bade investors ko nahi ginta."),
                B(36.88, 40.59, "Wo dekhta hai ki *aam log* kitna crypto kharid rahe hain, bhej rahe hain —"),
                B(40.92, 41.74, "*chhote shehron* se,"),
                B(41.98, 42.73, "*chhoti amounts* mein."),
                B(43.22, 44.35, "Aur India mein aise log…"),
                B(44.68, 45.32, "*crores* mein hain.", mascot="happy", mascot_pos=R)
            ]
        },
        {
            "chip": "ABHI RULES KYA HAIN?",
            "elements": [
                {"type": "bigtext", "text": "*Abhi rules* kya hain?", "size": 64, "in": 0, "out": "1", "pos": {"x": 320, "y": 190, "center": True}},
                {"type": "card", "title": "CRYPTO IN INDIA", "right": "STATUS", "w": 600, "in": "1", "rows": [
                    {"icon": "check", "iconColor": "green", "label": "Ban?", "sub": "TRADING LEGAL HAI", "badge": "NAHI", "badgeColor": "green", "in": "2:ban"},
                    {"icon": "rupee", "iconColor": "red", "label": "Legal tender?", "sub": "RUPEE JAISA PAISA NAHI", "badge": "NAHI", "badgeColor": "red", "in": "3:legal"},
                    {"icon": "doc", "iconColor": "acc", "label": "Tax?", "sub": "POORA LAGTA HAI", "badge": "POORA", "badgeColor": "acc", "in": "4:tax", "hl": "4:Poora"}
                ]}
            ],
            "beats": [
                B(45.97, 46.94, "*Abhi rules* kya hain?", mascot="think", mascot_pos="center"),
                B(47.49, 48.47, "Ab *ajeeb baat* suno.", mascot="wink", mascot_pos="center"),
                B(48.99, 50.55, "Crypto India mein ^ban nahi^ hai."),
                B(50.96, 52.15, "Par *legal tender* bhi ~nahi~ hai."),
                B(52.55, 53.85, "Lekin *tax?* Poora hai.", mascot="shock", mascot_pos="center")
            ]
        },
        {
            "chip": "TAX KA HISAAB",
            "elements": [
                {"type": "row", "gap": 16, "in": 0, "items": [
                    {"type": "stat", "value": 30, "suffix": "%", "size": "l", "color": "acc", "label": "MUNAFE PE TAX", "in": "0:tees"},
                    {"type": "stat", "value": 1, "suffix": "%", "size": "l", "color": "acc", "label": "TDS · HAR SALE PE", "in": "1:TDS"}
                ]},
                {"type": "card", "title": "AUR NUKSAAN?", "w": 600, "in": "2:nuksaan", "mt": 18, "rows": [
                    {"icon": "down", "iconColor": "red", "label": "Loss set-off", "sub": "DOOSRE MUNAFE SE", "badge": "ALLOWED NAHI", "badgeColor": "red",
                     "in": "3:Usse", "red": "3:adjust"}
                ]},
                {"type": "stamp", "text": "NO SET-OFF", "color": "red", "rot": -7, "size": 38, "in": "3:sakte",
                 "pos": {"x": 430, "y": 330, "center": True}}
            ],
            "beats": [
                B(54.19, 55.95, "Munafe pe seedha *tees percent.*"),
                B(56.34, 58.13, "Har sale pe *ek percent TDS.*"),
                B(58.48, 59.11, "Aur ~nuksaan~ hua?", mascot="think", mascot_pos=R),
                B(59.49, 61.64, "Usse kisi munafe mein ~adjust bhi nahi~ kar sakte.", mascot="sad", mascot_pos=R)
            ]
        },
        {
            "chip": "SARKAR KI NAZAR",
            "elements": [
                {"type": "check", "title": "CONTROL CHECKLIST", "in": 0, "items": [
                    {"label": "FIU-IND registration", "tick": "0:FIU"},
                    {"label": "Anti-money laundering rules", "tick": "1:laundering"},
                    {"label": "Tax: 30% + 1% TDS", "tick": "2:tax"},
                    {"label": "Reporting · nazar", "tick": "3:nazar"},
                    {"label": "Crypto ka alag kanoon", "state": "x", "tick": "4:kanoon"}
                ]},
                {"type": "stamp", "text": "NO LAW", "color": "red", "rot": -8, "size": 46, "in": "4:banati",
                 "pos": {"x": 320, "y": 345, "center": True}}
            ],
            "beats": [
                B(62.13, 65.36, "*Exchanges* ko *FIU-IND* mein register hona padta hai,"),
                B(65.65, 67.42, "*money laundering* ke rules maanne padte hain."),
                B(67.88, 69.51, "Matlab sarkar *tax leti hai…*", mascot="point", mascot_pos=R),
                B(69.77, 70.56, "*nazar rakhti hai…*", mascot="point", mascot_pos=R),
                B(70.94, 71.94, "par ~kanoon nahi banati.~", mascot="shock", mascot_pos=R, pause=0.3)
            ]
        },
        {
            "chip": "MANA KYUN?",
            "elements": [
                {"type": "bigtext", "text": "*Mana* kyun?", "size": 64, "in": 0, "out": "1", "pos": {"x": 320, "y": 190, "center": True}},
                {"type": "card", "w": 600, "in": "1:Reports", "rows": [
                    {"icon": "bank", "iconColor": "acc", "label": "Finance Ministry", "sub": "→ PARLIAMENT COMMITTEE", "badge": "REPORTS", "badgeColor": "mute", "compact": True, "in": "1:Finance"}
                ]},
                {"type": "flow", "w": 640, "h": 380, "in": "2:alag", "mt": 12, "nodes": [
                    {"id": "law", "x": 170, "y": 0, "w": 250, "icon": "doc", "label": "Alag kanoon", "sub": "AGAR BANA", "in": "2:alag"},
                    {"id": "ok", "x": 470, "y": 95, "w": 250, "icon": "check", "iconColor": "green", "label": "\"Manzoori\"", "sub": "LOGON KO LAGEGA", "in": "3:manzoori"},
                    {"id": "money", "x": 170, "y": 190, "w": 250, "icon": "rupee", "iconColor": "acc", "label": "Zyada paisa", "sub": "LOG LAGAYENGE", "in": "4:paisa"},
                    {"id": "risk", "x": 470, "y": 285, "w": 250, "icon": "alert", "iconColor": "red", "label": "Zyada risk", "color": "red", "in": "5:risk"}
                ], "edges": [
                    {"from": "law", "to": "ok", "fromSide": "right", "toSide": "top", "color": "acc", "dashed": True, "in": "3:manzoori"},
                    {"from": "ok", "to": "money", "fromSide": "left", "toSide": "top", "color": "acc", "dashed": True, "in": "4:paisa"},
                    {"from": "money", "to": "risk", "fromSide": "right", "toSide": "top", "color": "red", "dashed": True, "in": "5:risk"}
                ]}
            ],
            "beats": [
                B(72.46, 72.92, "*Mana* kyun?", mascot="think", mascot_pos="center"),
                B(73.47, 77.10, "*Reports* ke mutabik, *Finance Ministry* ne Parliament ki committee ko bataya —"),
                B(77.67, 79.83, "agar crypto ke liye *alag kanoon* bana diya,"),
                B(80.16, 82.19, "toh lagega sarkar ne isse *manzoori* de di."),
                B(82.73, 84.66, "Aur phir log aur *zyada paisa* lagayenge —"),
                B(84.93, 85.92, "~zyada risk~ ke saath.", mascot="sad", mascot_pos=R)
            ]
        },
        {
            "chip": "SARKAR KA PLAN: e-RUPEE",
            "elements": [
                {"type": "object", "kind": "coin", "color": "gold", "symbol": "₹", "size": 230, "label": "e-RUPEE · RBI KI DIGITAL CURRENCY", "in": "0:digital"},
                {"type": "card", "title": "SARKAR KI PASAND", "w": 600, "in": "1:Rupee", "mt": 16, "rows": [
                    {"icon": "coin", "iconColor": "red", "label": "Crypto", "sub": "PRIVATE · VOLATILE", "badge": "ALAG KANOON NAHI", "badgeColor": "red", "compact": True, "in": "1:Rupee"},
                    {"icon": "rupee", "iconColor": "acc", "label": "e-Rupee", "sub": "RBI JAARI KARTA HAI", "badge": "FOCUS", "badgeColor": "acc", "compact": True, "in": "1:Rupee+0.2", "hl": "1:Rupee+0.2"}
                ]},
                {"type": "card", "w": 600, "in": "2:RBI", "mt": 12, "rows": [
                    {"icon": "bank", "iconColor": "acc", "label": "RBI", "sub": "CRYPTO PE STANCE", "badge": "KHILAAF", "badgeColor": "red", "in": "2:RBI", "red": "3:khilaaf"}
                ]}
            ],
            "beats": [
                B(86.36, 89.37, "Sarkar ka *focus* hai *RBI* ka apna *digital rupaya* —"),
                B(89.69, 90.09, "*e-Rupee.*", mascot="happy", mascot_pos="center"),
                B(90.48, 91.05, "Aur *RBI?*", mascot="think", mascot_pos="center"),
                B(91.44, 92.96, "Wo toh pehle se crypto ke ~khilaaf~ hai.", mascot="point", mascot_pos="center")
            ]
        },
        {
            "chip": "AAPKE LIYE MATLAB?",
            "chip_color": "red",
            "flash": True,
            "elements": [
                {"type": "bigtext", "text": "~Aapke liye~ matlab?", "size": 64, "in": 0, "out": "1", "pos": {"x": 320, "y": 190, "center": True}},
                {"type": "card", "title": "AGAR EXCHANGE…", "w": 600, "in": "1", "rows": [
                    {"icon": "building", "iconColor": "red", "label": "Doob jaaye", "sub": "BAND / DIWALIYA", "badge": "RISK", "badgeColor": "red", "in": "2:doob", "red": "2:doob"},
                    {"icon": "unlock", "iconColor": "red", "label": "Hack ho jaaye", "sub": "WALLET KHALI", "badge": "RISK", "badgeColor": "red", "in": "3:hack", "red": "3:hack"},
                    {"icon": "shield", "label": "Crypto-specific kanoon", "sub": "AAPKO BACHAANE KE LIYE", "badge": "NAHI", "badgeColor": "red", "in": "4:kanoon"}
                ]},
                {"type": "stamp", "text": "NO SAFETY NET", "color": "red", "rot": -6, "size": 40, "in": "4:bachaane",
                 "pos": {"x": 320, "y": 420, "center": True}}
            ],
            "beats": [
                B(93.63, 94.34, "*Aapke liye* matlab?", mascot="think", mascot_pos="center"),
                B(94.80, 96.90, "Toh aapke liye iska *matlab* kya hai?"),
                B(97.51, 98.88, "Agar koi exchange ~doob jaaye…~"),
                B(99.20, 99.96, "ya ~hack~ ho jaaye…", mascot="shock", mascot_pos=R),
                B(100.48, 102.97, "koi khaas crypto kanoon aapko ~bachaane nahi~ aayega.", mascot="sad", mascot_pos=R)
            ]
        },
        {
            "chip": "YAAD HAI WAZIRX?",
            "chip_color": "red",
            "elements": [
                {"type": "card", "title": "WAZIRX · JULY 2024", "right": "HACK", "w": 600, "in": 0, "rows": [
                    {"icon": "alert", "iconColor": "red", "label": "Indian exchange hack", "sub": "JULY 2024", "in": 0},
                    {"icon": "lock", "iconColor": "red", "label": "Users ka paisa", "sub": "WITHDRAWALS BAND", "badge": "ATKA", "badgeColor": "red", "in": "1:paisa", "red": "1:atka"}
                ]},
                {"type": "timeline", "title": "PAISA ATKA RAHA", "icon": "clock", "w": 600, "in": "1:mahino", "mt": 18,
                 "segments": [{"from": 0, "to": 1, "color": "red", "in": "1:mahino", "dur": 1.6}],
                 "ticks": [{"pos": 0, "label": "JUL '24"}, {"pos": 0.5, "label": "MAHINE"}, {"pos": 1, "label": "AUR MAHINE…", "color": "red"}]}
            ],
            "beats": [
                B(103.53, 104.38, "Yaad hai *WazirX?*", mascot="think", mascot_pos=R),
                B(104.77, 106.73, "Users ka paisa ~mahino tak atka~ raha.", mascot="sad", mascot_pos=R)
            ]
        },
        {
            "chip": "TWIST · 2026 INDEX",
            "flash": True,
            "elements": [
                {"type": "stat", "value": 1, "prefix": "#", "count": False, "size": "xl", "color": "acc", "label": "INDIA · 2025", "in": 0,
                 "then": [{"at": "2:chhathe", "value": 6, "color": "red", "label": "INDIA · 2026"}]},
                {"type": "card", "title": "CHAINALYSIS 2026", "right": "TOP 6", "w": 600, "in": "1:ranking", "mt": 12, "rows": [
                    {"label": "Brazil", "value": "#1", "compact": True, "in": "1:ranking"},
                    {"label": "United States", "value": "#2", "compact": True, "in": "1:ranking+0.15"},
                    {"label": "Nigeria", "value": "#3", "compact": True, "in": "1:ranking+0.3"},
                    {"label": "India", "value": "#6", "valueColor": "red", "compact": True, "in": "2:chhathe", "red": "2:chhathe"}
                ]},
                {"type": "text", "mono": True, "text": "30% TAX + ADHOORE RULES = ASAR?", "in": "3:Tees", "mt": 12}
            ],
            "beats": [
                B(107.41, 108.06, "Aur ek *twist* —", mascot="shock", mascot_pos=R),
                B(108.44, 112.07, "*2026* ki nayi ranking mein India number one se ~phisal kar…~"),
                B(112.40, 113.43, "~chhathe number~ par aa gaya.", mascot="sad", mascot_pos=R),
                B(114.04, 116.27, "*Tees percent tax* aur *adhoore rules* ka asar?", mascot="think", mascot_pos=R),
                B(116.87, 117.36, "Ho sakta hai.", mascot="think", mascot_pos=R)
            ]
        },
        {
            "chip": "KYA KAREIN? · 3 TIPS",
            "chip_color": "green",
            "elements": [
                {"type": "bigtext", "text": "*Kya* karein?", "size": 64, "in": 0, "out": "2", "pos": {"x": 320, "y": 190, "center": True}},
                {"type": "list", "w": 600, "in": "2", "items": [
                    {"kicker": "TIP 1", "title": "Sirf *FIU-registered* exchange", "in": "2:FIU"},
                    {"kicker": "TIP 2", "title": "Saara paisa exchange pe *mat chhodo*", "in": "3:saara"},
                    {"kicker": "TIP 3", "title": "Har trade ka *hisaab* rakho", "in": "4:hisaab"}
                ]},
                {"type": "stamp", "text": "TAX WAALE DEKH RAHE HAIN", "color": "acc", "rot": -4, "size": 26, "in": "5:tax",
                 "pos": {"x": 320, "y": 470, "center": True}}
            ],
            "beats": [
                B(117.92, 118.31, "*Kya* karein?", mascot="point", mascot_pos="center"),
                B(118.88, 120.16, "Toh agar aap crypto *rakhte* ho —", mascot="point", mascot_pos=R),
                B(120.54, 123.52, "Ek: sirf *FIU-registered exchange* use karo."),
                B(123.92, 126.42, "Do: saara paisa exchange pe ~mat chhodo.~"),
                B(126.89, 128.78, "Teen: har trade ka *hisaab* rakho…"),
                B(129.12, 130.65, "kyunki *tax waale* nahi chhodenge.", mascot="wink", mascot_pos=R)
            ]
        },
        {
            "chip": "SHARE KARO",
            "elements": [
                {"type": "bubble", "quote": "Crypto mein sab chalta hai.", "strike": "1:chalta+0.6", "in": "1:kehta", "w": 560},
                {"type": "tiles", "size": 92, "in": "0:video", "mt": 24, "items": [
                    {"icon": "users", "color": "acc", "label": "Dost", "in": "0:dost"},
                    {"icon": "link", "color": "brand", "label": "Share"},
                    {"icon": "heart", "color": "red", "label": "Save"},
                    {"icon": "bell", "color": "green", "label": "Follow"}
                ]}
            ],
            "beats": [
                B(132.13, 134.49, "Ye video us *dost* ko bhejo", mascot="point", mascot_pos=R),
                B(134.78, 136.25, "jo kehta hai, \"*crypto mein sab chalta hai.*\"", mascot="wink", mascot_pos=R)
            ]
        }
    ],
    "outro": {"say": "Ab samjhe?", "audio": clip(136.71, 137.64)}
}

json.dump(ep, open(os.path.join(HERE, "episode.json"), "w"), ensure_ascii=False, indent=1)
print("beats:", sum(len(s["beats"]) for s in ep["hook"] + ep["body"]))
