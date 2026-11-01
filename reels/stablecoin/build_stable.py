"""EP 6: stablecoins. Cuts the voice-over into per-beat clips and writes episode JSON."""
import json, os, subprocess
import numpy as np, soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.environ.get("VO", os.path.join(HERE, "voiceover.mp3"))
OUT = os.environ.get("OUT", os.path.join(HERE, "episode.json"))
CLIPS = os.path.join(HERE, "clips_stable")
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
    "series": "CRYPTO.DECODED", "series_icon": "coin", "episode": 6, "tag": "STABLECOIN",
    "accent": "green",
    "disclaimer": "SIRF JAANKARI · FIGURES: 1 NOV 2026 TAK · NOT ADVICE",
    "concept": "STABLECOIN · $1 PEG", "music_mood": "tense",
    "brand": {"wordmark": "niks", "suffix": ".crypto", "handle": "@niks.crypto", "color": "#7C5CFF",
              "outro_log": "Stablecoin basics successfully installed.", "follow": "FOLLOW @NIKS.CRYPTO"},
    "stinger_lines": {"boot": "SYSTEM ONLINE", "detect": "CONCEPT DETECTED:", "run": "CHECKING PEG…"},
    "hook": [
        {"hold": 0.04, "chip": "BTC vs USDT", "elements": [],
         "beats": [
            B(0.00, 1.90, "*Bitcoin* roz ~upar neeche~ hota hai."),
            B(2.49, 3.49, "Par *USDT?*", mascot="think", mascot_pos=R),
            B(4.05, 5.47, "Hamesha lagbhag *$1.*", mascot="point", mascot_pos=R),
            B(5.99, 6.31, "*Kaise?*", mascot="think", mascot_pos=R, dur=0.8, pause=0.25)]}
    ],
    "body": [
        {"hold": 0.04, "chip": "STABLECOIN KYA HAI?",
         "elements": [
            {"type": "row", "gap": 24, "in": 0, "items": [
                {"type": "icon", "name": "₮", "size": 120, "color": "#0b0d0e", "bg": "acc", "round": True, "label": "STABLECOIN", "in": 0},
                {"type": "text", "text": "=", "size": 96, "weight": 900, "color": "mute", "in": "1:currency"},
                {"type": "icon", "name": "$", "size": 120, "color": "#0b0d0e", "bg": "#e9e5da", "round": True, "label": "DOLLAR", "in": "2:dollar"}]},
            {"type": "card", "title": "PEG · 1 = 1", "w": 600, "in": "1", "mt": 22, "rows": [
                {"icon": "₮", "iconColor": "acc", "label": "1 USDT", "value": "≈ $1.00", "valueColor": "acc", "in": "1:crypto", "compact": True},
                {"icon": "$", "iconColor": "acc", "label": "1 USDC", "value": "≈ $1.00", "valueColor": "acc", "in": "1:currency", "compact": True}]}],
         "beats": [
            B(6.78, 8.41, "Ise kehte hain, *stablecoin.*", mascot="point", mascot_pos=R),
            B(8.88, 11.64, "Ek crypto, jo kisi *asli currency* se juda rehta hai."),
            B(12.06, 13.29, "Zyadatar, *dollar* se.", mascot="happy", mascot_pos=R)]},
        {"hold": 0.04, "chip": "PEECHE KYA HAI?",
         "elements": [
            {"type": "row", "gap": 26, "in": 0, "items": [
                {"type": "object", "kind": "safe", "color": "silver", "size": 170, "in": 0},
                {"type": "stack", "gap": 10, "items": [
                    {"type": "stat", "value": 1, "prefix": "$", "size": "l", "color": "acc", "label": "HAR 1 USDT KE PEECHE", "in": "1:dollar"},
                    {"type": "text", "mono": True, "text": "COMPANY KA DAAVA", "in": "1:reserve"}]}]},
            {"type": "card", "title": "RESERVE", "w": 600, "in": "1:reserve", "mt": 20, "rows": [
                {"icon": "$", "iconColor": "acc", "label": "Cash", "sub": "BANK MEIN", "in": "2:Cash", "compact": True},
                {"icon": "doc", "iconColor": "acc", "label": "US govt bonds", "sub": "TREASURY BILLS", "in": "2:bonds", "compact": True}]}],
         "beats": [
            B(13.84, 16.46, "Company kehti hai, har ek *USDT* ke peeche,", mascot="idle", mascot_pos=R),
            B(16.69, 18.70, "*ek dollar* jitna paisa *reserve* mein rakha hai."),
            B(19.18, 21.33, "*Cash,* aur American sarkar ke *bonds.*", mascot="point", mascot_pos=R)]},
        {"hold": 0.04, "chip": "USE KAHAN HOTA HAI?",
         "elements": [
            {"type": "bigtext", "text": "*$1* = Stable", "size": 92, "in": 0},
            {"type": "tiles", "size": 104, "in": "0:trading", "mt": 26, "items": [
                {"icon": "chart", "color": "acc", "label": "Trading", "in": "0:trading"},
                {"icon": "arrow", "color": "cyan", "label": "Transfer", "in": "1:bhejne"},
                {"icon": "globe", "color": "blue", "label": "Duniya bhar", "in": "1:udhar"},
                {"icon": "users", "color": "brand", "label": "P2P", "in": "1:use"}]}],
         "beats": [
            B(21.79, 23.16, "Isliye log isse *trading* mein,", mascot="happy", mascot_pos=R),
            B(23.34, 25.43, "aur paisa *idhar udhar bhejne* mein use karte hain.")]},
        {"hold": 0.04, "chip": "PAR YAAD RAKHO", "chip_color": "red", "flash": True,
         "elements": [
            {"type": "paper", "kicker": "STABLECOIN", "right": "TERMS", "title": "1 = $1", "sub": "COMPANY KA PROMISE", "sign": "1:promise", "in": 0},
            {"type": "stamp", "text": "SIRF PROMISE", "color": "red", "rot": -7, "size": 46, "in": "1:promise+0.3", "pos": {"x": 320, "y": 250, "center": True}}],
         "beats": [
            B(26.00, 26.65, "Par *yaad rakho.*", mascot="point", mascot_pos=R),
            B(27.07, 28.51, "Ye ek ~promise~ pe chalta hai.", mascot="think", mascot_pos=R, pause=0.2)]},
        {"hold": 0.04, "chip": "2023 · DEPEG", "chip_color": "red", "elements": [],
         "beats": [
            B(29.07, 31.73, "*2023* mein, ek American bank ~doob~ gaya."),
            B(32.15, 33.91, "Aur *USDC* naam ka stablecoin,"),
            B(34.14, 34.97, "kuch ghanton ke liye,"),
            B(35.26, 37.05, "lagbhag ~88 cent~ tak gir gaya.", mascot="shock", mascot_pos=R, pause=0.2)]},
        {"hold": 0.04, "chip": "FREEZE POWER",
         "elements": [
            {"type": "grid", "shape": "square", "cols": 8, "count": 24, "cell": 54, "color": "acc", "highlight": 7, "hl": "1:freeze", "hlColor": "red",
             "in": 0, "stagger": 0.02, "label": "HAR SQUARE = EK WALLET · EXAMPLE"},
            {"type": "card", "w": 600, "in": "2:Binance", "mt": 18, "rows": [
                {"icon": "lock", "iconColor": "red", "label": "Binance hack · Oct 2026", "sub": "HACKER KE STABLECOINS", "badge": "FROZEN", "badgeColor": "red", "in": "2:Binance"}]},
            {"type": "stamp", "text": "FREEZE", "color": "red", "rot": -8, "size": 60, "in": "1:freeze+0.2", "pos": {"x": 320, "y": 120, "center": True}, "shake": "1:freeze+0.2"}],
         "beats": [
            B(37.49, 38.14, "Aur *ek baat.*", mascot="point", mascot_pos=R),
            B(38.63, 42.17, "Company chahe toh, kisi bhi wallet ke stablecoin ~freeze~ kar sakti hai.", mascot="shock", mascot_pos=R),
            B(42.65, 44.29, "*Binance hack* mein, yahi hua tha.", mascot="wink", mascot_pos=R)]},
        {"hold": 0.04, "chip": "TOH MATLAB?",
         "elements": [
            {"type": "bigtext", "text": "Stable *≠* Safe", "size": 96, "in": 0},
            {"type": "check", "title": "STABLECOIN", "in": "1", "mt": 24, "items": [
                {"label": "Zero risk", "state": "x", "tick": "1:risk"},
                {"label": "Kam utaar chadhaav", "tick": "2:utaar"}]}],
         "beats": [
            B(44.74, 45.94, "Toh stablecoin ka *matlab,*", mascot="think", mascot_pos=R),
            B(46.21, 47.06, "~zero risk~ nahi.", mascot="shock", mascot_pos=R),
            B(47.43, 48.71, "Bas, *kam utaar chadhaav.*", mascot="happy", mascot_pos=R)]},
        {"hold": 0.04, "chip": "SHARE KARO",
         "elements": [
            {"type": "bigtext", "text": "Share *karo*", "size": 84, "in": 0},
            {"type": "bubble", "quote": "USDT toh bilkul safe hai.", "strike": "0:safe+0.5", "in": "0:sochta", "w": 560, "mt": 18},
            {"type": "tiles", "size": 100, "in": "0:dost", "mt": 24, "items": [
                {"icon": "users", "color": "acc", "label": "Dost", "in": "0:dost"},
                {"icon": "link", "color": "brand", "label": "Share"},
                {"icon": "heart", "color": "red", "label": "Save"},
                {"icon": "bell", "color": "yellow", "label": "Follow"}]}],
         "beats": [B(49.17, 53.16, "Ye video us *dost* ko bhejo, jo sochta hai, *USDT bilkul safe* hai.", mascot="point", mascot_pos=R)]}
    ],
    "outro": {"say": "Ab samjhe?", "audio": clip(53.67, 54.36), "dur": 3.0}
}

json.dump(ep, open(OUT, "w"), ensure_ascii=False, indent=1)
print("beats:", sum(len(s["beats"]) for s in ep["hook"] + ep["body"]))
