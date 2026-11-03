"""EP 8: freeze part 3 - 5 red flags. Cuts the voice-over into per-beat clips and writes episode JSON."""
import json, os, subprocess
import numpy as np, soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.environ.get("VO", os.path.join(HERE, "voiceover.mp3"))
OUT = os.environ.get("OUT", os.path.join(HERE, "episode.json"))
CLIPS = os.path.join(HERE, "clips_freeze3")
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

def flag(n, title, sub):
    return {"type": "row", "gap": 20, "in": 0, "items": [
        {"type": "icon", "name": "flag", "size": 110, "color": "#fff", "bg": "red", "round": True, "label": f"RED FLAG {n}", "in": 0},
        {"type": "stack", "gap": 6, "items": [
            {"type": "text", "text": title, "size": 54, "weight": 900, "in": 0},
            {"type": "text", "mono": True, "text": sub, "in": 0}]}]}

ep = {
    "series": "CRYPTO.DECODED", "series_icon": "bank", "episode": 8, "tag": "FREEZE · PART 3",
    "accent": "cyan",
    "disclaimer": "SIRF JAANKARI · EXAMPLE NAMES · NOT ADVICE",
    "concept": "P2P BUYER · 5 RED FLAGS", "music_mood": "tense",
    "brand": {"wordmark": "niks", "suffix": ".crypto", "handle": "@niks.crypto", "color": "#7C5CFF",
              "outro_log": "Red flag scanner installed.", "follow": "FOLLOW @NIKS.CRYPTO"},
    "stinger_lines": {"boot": "SYSTEM ONLINE", "detect": "SCAN STARTED:", "run": "CHECKING BUYER…"},
    "hook": [
        {"hold": 0.04, "chip": "P2P BUYER · SCAN", "elements": [],
         "beats": [
            B(0.00, 2.12, "P2P pe buyer *safe* hai ya ~scammer?~", mascot="think", mascot_pos=R),
            B(2.82, 4.13, "Ye *paanch red flags* dekho.", mascot="point", mascot_pos=R, pause=0.25)]}
    ],
    "body": [
        {"hold": 0.04, "chip": "RED FLAG 1 · NAAM", "chip_color": "red", "elements": [],
         "beats": [
            B(5.16, 6.07, "*Red flag ek:*", dur=0.8),
            B(6.47, 7.61, "~naam match~ nahi karta."),
            B(8.35, 9.51, "Trade *kisi aur naam* se,"),
            B(9.91, 11.52, "aur paisa ~kisi aur ke account~ se.", mascot="shock", mascot_pos=R, pause=0.2)]},
        {"hold": 0.04, "chip": "RED FLAG 2 · NAYA ACCOUNT", "chip_color": "red",
         "elements": [
            flag(2, "Bilkul naya account", "JOINED: 2 DIN PEHLE"),
            {"type": "card", "title": "BUYER PROFILE · EXAMPLE", "w": 600, "in": "1", "mt": 22, "rows": [
                {"icon": "users", "iconColor": "red", "label": "Completed trades", "value": "0", "valueColor": "red", "in": "1:purane", "compact": True},
                {"icon": "check", "iconColor": "red", "label": "Completion rate", "value": "—", "valueColor": "red", "in": "1:completed", "compact": True},
                {"icon": "shield", "iconColor": "red", "label": "Verified", "badge": "NAHI", "badgeColor": "red", "in": "1:orders", "compact": True}]}],
         "beats": [
            B(12.50, 13.26, "*Red flag do:*", mascot="think", mascot_pos=R, dur=0.8),
            B(13.66, 17.46, "~bilkul naya account.~ Na purane trades, na completed orders.", mascot="shock", mascot_pos=R)]},
        {"hold": 0.04, "chip": "RED FLAG 3 · JALDI", "chip_color": "red",
         "elements": [
            flag(3, "Jaldi machana", "URGENCY = DABAAV"),
            {"type": "chat", "title": "P2P ORDER CHAT", "right": "BUYER", "in": "1", "mt": 20, "messages": [
                {"from": "Buyer", "text": "Bhai jaldi release karo!!", "in": "1:jaldi"},
                {"from": "Buyer", "text": "Mujhe urgent hai, 2 min mein", "in": "1:urgent"}]},
            {"type": "ring", "text": "2:00", "frac": 0.3, "color": "red", "r": 56, "label": "TIMER", "in": "1:urgent", "mt": 16}],
         "beats": [
            B(18.54, 19.47, "*Red flag teen:*", dur=0.8),
            B(19.92, 20.78, "~jaldi machana.~", mascot="shock", mascot_pos=R),
            B(21.36, 23.31, "\"Bhai *jaldi release* karo, mujhe *urgent* hai.\"", mascot="think", mascot_pos=R, pause=0.2)]},
        {"hold": 0.04, "chip": "RED FLAG 4 · PLATFORM KE BAHAR", "chip_color": "red",
         "elements": [
            flag(4, "Platform ke bahar", "NO ESCROW · NO PROTECTION"),
            {"type": "row", "gap": 30, "in": "1", "mt": 24, "items": [
                {"type": "icon", "name": "shield", "size": 120, "color": "#0b0d0e", "bg": "acc", "round": True, "label": "EXCHANGE · SAFE", "in": "1"},
                {"type": "text", "text": "→", "size": 90, "weight": 900, "color": "red", "in": "2:WhatsApp"},
                {"type": "icon", "name": "chat", "size": 120, "color": "#fff", "bg": "green", "round": True, "label": "WHATSAPP", "in": "2:WhatsApp", "cross": "2:sasta"}]},
            {"type": "bubble", "quote": "WhatsApp pe aao, sasta de dunga", "in": "2:WhatsApp", "mt": 20, "w": 560}],
         "beats": [
            B(24.46, 25.35, "*Red flag chaar:*", dur=0.8),
            B(25.83, 27.36, "~platform ke bahar~ deal ki baat.", mascot="think", mascot_pos=R),
            B(28.07, 29.70, "\"*WhatsApp* pe aao, ~sasta~ de dunga.\"", mascot="shock", mascot_pos=R, pause=0.2)]},
        {"hold": 0.04, "chip": "RED FLAG 5 · TUKDON MEIN", "chip_color": "red", "elements": [],
         "beats": [
            B(30.80, 31.79, "*Red flag paanch:*", dur=0.8),
            B(32.29, 34.98, "ek trade ka paisa, *kai alag alag accounts* se,"),
            B(35.19, 35.88, "~tukdon~ mein aana.", mascot="shock", mascot_pos=R, pause=0.25)]},
        {"hold": 0.04, "chip": "TOH KYA KAREIN?", "chip_color": "green",
         "elements": [
            {"type": "bigtext", "text": "Ek bhi flag? ~Cancel.~", "size": 74, "in": 0},
            {"type": "compare", "arrow": False, "itemW": 280, "in": "1", "mt": 24, "items": [
                {"top": "THODA MUNAFA", "value": "₹200", "color": "mute", "sub": "CHHOD DO", "in": "2:munafa"},
                {"top": "ACCOUNT FREEZE", "value": "MAHINE", "color": "red", "border": "red", "sub": "BACH GAYE", "in": "3:freeze"}]}],
         "beats": [
            B(37.04, 38.15, "Inme se *ek bhi* dikhe,", mascot="point", mascot_pos=R),
            B(38.52, 39.52, "toh trade ~cancel~ karo.", mascot="point", mascot_pos=R),
            B(39.97, 41.09, "*Thoda munafa* chhodna,"),
            B(41.28, 42.52, "^account freeze se behtar^ hai.", mascot="happy", mascot_pos=R)]},
        {"hold": 0.04, "chip": "SHARE KARO",
         "elements": [
            {"type": "check", "title": "5 RED FLAGS", "in": 0, "items": [
                {"label": "Naam match nahi", "state": "x", "tick": "0:video"},
                {"label": "Naya account", "state": "x", "tick": "0:video+0.2"},
                {"label": "Jaldi machana", "state": "x", "tick": "0:video+0.4"},
                {"label": "Platform ke bahar", "state": "x", "tick": "0:video+0.6"},
                {"label": "Tukdon mein paisa", "state": "x", "tick": "0:video+0.8"}]}],
         "beats": [B(43.31, 46.84, "Ye video us *dost* ko bhejo, jo *roz P2P* pe trade karta hai.", mascot="point", mascot_pos=R)]}
    ],
    "outro": {"say": "Ab samjhe?", "audio": clip(47.30, 47.80), "dur": 3.0}
}

json.dump(ep, open(OUT, "w"), ensure_ascii=False, indent=1)
print("beats:", sum(len(s["beats"]) for s in ep["hook"] + ep["body"]))
