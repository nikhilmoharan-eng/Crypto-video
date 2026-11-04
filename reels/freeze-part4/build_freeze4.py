"""EP 9: freeze part 4 - safe crypto to INR. Cuts the voice-over into per-beat clips and writes episode JSON."""
import json, os, subprocess
import numpy as np, soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.environ.get("VO", os.path.join(HERE, "voiceover.mp3"))
OUT = os.environ.get("OUT", os.path.join(HERE, "episode.json"))
CLIPS = os.path.join(HERE, "clips_freeze4")
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
    "series": "CRYPTO.DECODED", "series_icon": "bank", "episode": 9, "tag": "FREEZE · PART 4",
    "accent": "cyan",
    "disclaimer": "SIRF JAANKARI · TAX: 30% + 1% TDS · NOT ADVICE",
    "concept": "CRYPTO → ₹ · SAFE TAREEKA", "music_mood": "bright",
    "brand": {"wordmark": "niks", "suffix": ".crypto", "handle": "@niks.crypto", "color": "#7C5CFF",
              "outro_log": "Safe cash-out installed.", "follow": "FOLLOW @NIKS.CRYPTO"},
    "stinger_lines": {"boot": "SYSTEM ONLINE", "detect": "ROUTE DETECTED:", "run": "FINDING SAFE PATH…"},
    "hook": [
        {"hold": 0.04, "chip": "CRYPTO → ₹", "elements": [],
         "beats": [
            B(0.00, 0.96, "~Freeze~ ka darr hai?", mascot="think", mascot_pos=R),
            B(1.73, 4.66, "Toh crypto ko rupaye mein badalne ka, *safe tareeka* samjho.", mascot="point", mascot_pos=R, pause=0.25)]}
    ],
    "body": [
        {"hold": 0.04, "chip": "SABSE SAFE · INR WITHDRAWAL", "chip_color": "green", "elements": [],
         "beats": [
            B(5.74, 6.39, "^Sabse safe:^", dur=0.8),
            B(7.14, 9.30, "exchange ka apna *INR withdrawal.*"),
            B(10.01, 11.54, "Aap exchange pe *crypto becho,*"),
            B(11.85, 14.50, "aur paisa *seedha exchange se* aapke bank mein aata hai."),
            B(15.27, 16.63, "~Kisi anjaan insaan~ se nahi.", mascot="happy", mascot_pos=R)]},
        {"hold": 0.04, "chip": "CHECK KARO",
         "elements": [
            {"type": "card", "title": "EXCHANGE CHECK", "w": 600, "in": 0, "rows": [
                {"icon": "shield", "iconColor": "green", "label": "FIU-IND registered", "sub": "INDIA MEIN REPORTING ENTITY", "badge": "ZAROORI", "badgeColor": "green", "in": "1:FIU", "hl": "1:registered"},
                {"icon": "bank", "iconColor": "acc", "label": "INR withdrawal", "sub": "APNE NAAM KE BANK MEIN", "in": "1:registered+0.3"}]},
            {"type": "stamp", "text": "VERIFIED", "color": "green", "rot": -6, "size": 48, "in": "1:registered+0.5", "pos": {"x": 400, "y": 300, "center": True}}],
         "beats": [
            B(17.21, 18.03, "Bas *dhyan rakho,*", mascot="point", mascot_pos=R),
            B(18.50, 20.89, "exchange *FIU-IND* mein ^registered^ ho.", mascot="happy", mascot_pos=R)]},
        {"hold": 0.04, "chip": "P2P KARNA HI HAI?",
         "elements": [
            {"type": "check", "title": "P2P SAFETY", "in": 0, "items": [
                {"label": "Sirf verified, purane traders", "tick": "1:verified"},
                {"label": "Paisa usi ke naam se", "tick": "3:naam"},
                {"label": "Third party payment", "state": "x", "tick": "3:account"}]}],
         "beats": [
            B(22.03, 23.01, "*P2P karna hi hai?*", mascot="think", mascot_pos=R),
            B(23.74, 24.67, "Toh sirf *verified,*"),
            B(25.00, 25.98, "*purane traders* se."),
            B(26.58, 28.86, "Aur paisa sirf *usi ke naam* ke account se.", mascot="point", mascot_pos=R)]},
        {"hold": 0.04, "chip": "RECORD + TAX",
         "elements": [
            {"type": "row", "gap": 16, "in": "2:tees", "items": [
                {"type": "stat", "value": 30, "suffix": "%", "size": "l", "color": "acc", "label": "MUNAFE PE TAX", "in": "2:tees"},
                {"type": "stat", "value": 1, "suffix": "%", "size": "l", "color": "acc", "label": "TDS · HAR SALE", "in": "3:TDS"}]},
            {"type": "card", "title": "TRADE LOG · EXAMPLE", "w": 600, "in": 0, "mt": 18, "rows": [
                {"icon": "doc", "iconColor": "acc", "label": "03 Nov · Sell 200 USDT", "value": "₹18,400", "in": "0:record", "compact": True},
                {"icon": "doc", "iconColor": "acc", "label": "28 Oct · Sell 0.01 BTC", "value": "₹62,100", "in": "0:record+0.2", "compact": True}]}],
         "beats": [
            B(29.72, 30.95, "Har trade ka *record* rakho.", mascot="point", mascot_pos=R),
            B(31.66, 32.95, "*Tax ke time* bhi kaam aayega."),
            B(33.57, 34.49, "*Tees percent tax,*"),
            B(34.68, 36.13, "aur *ek percent TDS,*"),
            B(36.37, 36.88, "yaad hai na?", mascot="wink", mascot_pos=R, dur=0.8)]},
        {"hold": 0.04, "chip": "PRO TIP · ALAG ACCOUNT", "chip_color": "green", "elements": [],
         "beats": [
            B(37.96, 38.40, "Aur *ek tip:*", dur=0.8),
            B(39.34, 41.26, "trading ke liye *alag bank account* rakho."),
            B(41.96, 43.23, "Agar kabhi ~freeze~ hua bhi,"),
            B(43.59, 45.47, "toh aapka ^salary account^ bacha rahega.", mascot="happy", mascot_pos=R, pause=0.2)]},
        {"hold": 0.04, "chip": "SAVE + SHARE",
         "elements": [
            {"type": "list", "w": 600, "in": 0, "items": [
                {"kicker": "1", "title": "Exchange ka *INR withdrawal*"},
                {"kicker": "2", "title": "P2P: *verified + same naam*"},
                {"kicker": "3", "title": "*Record* + alag account"}]},
            {"type": "tiles", "size": 92, "in": "1:dost", "mt": 22, "items": [
                {"icon": "star", "color": "acc", "label": "Save"},
                {"icon": "users", "color": "brand", "label": "Dost"},
                {"icon": "bell", "color": "green", "label": "Follow"}]}],
         "beats": [
            B(46.58, 47.66, "Ye video *save* karo,", mascot="point", mascot_pos=R),
            B(47.84, 50.57, "aur us *dost* ko bhejo, jo crypto se paisa nikaalta hai.", mascot="wink", mascot_pos=R)]}
    ],
    "outro": {"say": "Ab samjhe?", "audio": clip(51.52, 52.11), "dur": 3.0}
}

json.dump(ep, open(OUT, "w"), ensure_ascii=False, indent=1)
print("beats:", sum(len(s["beats"]) for s in ep["hook"] + ep["body"]))
