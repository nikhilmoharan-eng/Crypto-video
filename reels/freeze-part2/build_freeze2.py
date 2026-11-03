"""EP 7: account freeze part 2 - what to do. Cuts the voice-over into per-beat clips and writes episode JSON."""
import json, os, subprocess
import numpy as np, soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.environ.get("VO", os.path.join(HERE, "voiceover.mp3"))
OUT = os.environ.get("OUT", os.path.join(HERE, "episode.json"))
CLIPS = os.path.join(HERE, "clips_freeze2")
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
    "series": "CRYPTO.DECODED", "series_icon": "bank", "episode": 7, "tag": "FREEZE · PART 2",
    "accent": "cyan",
    "disclaimer": "SIRF JAANKARI · GENERAL STEPS · NOT LEGAL ADVICE",
    "concept": "ACCOUNT FREEZE · AB KYA?", "music_mood": "tense",
    "brand": {"wordmark": "niks", "suffix": ".crypto", "handle": "@niks.crypto", "color": "#7C5CFF",
              "outro_log": "Freeze recovery steps installed.", "follow": "FOLLOW @NIKS.CRYPTO"},
    "stinger_lines": {"boot": "SYSTEM ONLINE", "detect": "CASE DETECTED:", "run": "LOADING STEPS…"},
    "hook": [
        {"hold": 0.04, "chip": "ACCOUNT FROZEN", "chip_color": "red", "elements": [],
         "beats": [
            B(0.00, 1.46, "Aapka account ~freeze~ ho gaya.", mascot="shock", mascot_pos=R),
            B(2.04, 2.63, "^Ghabraiye mat.^", mascot="happy", mascot_pos=R, dur=0.9),
            B(3.13, 5.24, "Pehle ye samjho, ki freeze *kisne kiya.*", mascot="think", mascot_pos=R, pause=0.25)]}
    ],
    "body": [
        {"hold": 0.04, "chip": "FREEZE KISNE KIYA?",
         "elements": [
            {"type": "flow", "w": 640, "h": 420, "in": 0, "nodes": [
                {"id": "pol", "x": 320, "y": 0, "w": 300, "icon": "shield", "iconColor": "acc", "label": "Police / Cyber cell", "sub": "REQUEST BHEJTE HAIN", "in": "1:Police"},
                {"id": "bank", "x": 320, "y": 150, "w": 300, "icon": "bank", "iconColor": "mute", "label": "Bank", "sub": "KHUD NAHI KARTA", "in": "0:bank"},
                {"id": "ac", "x": 320, "y": 300, "w": 300, "icon": "lock", "iconColor": "red", "label": "Aapka account", "sub": "HOLD / LIEN", "color": "red", "in": "2:hold"}],
             "edges": [
                {"from": "pol", "to": "bank", "fromSide": "bottom", "toSide": "top", "color": "acc", "in": "1:kehne"},
                {"from": "bank", "to": "ac", "fromSide": "bottom", "toSide": "top", "color": "red", "in": "2:hold"}]}],
         "beats": [
            B(5.77, 7.56, "Zyadatar, *bank khud* nahi karta.", mascot="point", mascot_pos=R),
            B(8.02, 9.65, "*Police ya cyber cell* ke kehne pe,"),
            B(9.91, 11.49, "bank account pe *hold* lagata hai.", mascot="idle", mascot_pos=R)]},
        {"hold": 0.04, "chip": "STEP 1 · BANK BRANCH", "chip_color": "green",
         "elements": [
            {"type": "bigtext", "text": "Step *1*", "size": 110, "in": 0, "out": "1", "pos": {"x": 320, "y": 200, "center": True}},
            {"type": "paper", "kicker": "APPLICATION · BRANCH MANAGER", "right": "LIKHIT MEIN", "title": "Freeze kyun hua?", "sub": "KAUNSI COMPLAINT · KAUNSA POLICE STATION", "sign": "1:likhit", "in": "1"},
            {"type": "card", "w": 600, "in": "2", "mt": 16, "rows": [
                {"icon": "doc", "iconColor": "acc", "label": "Complaint / FIR no.", "sub": "KISNE REPORT KIYA", "in": "2:complaint", "compact": True},
                {"icon": "shield", "iconColor": "acc", "label": "Police station", "sub": "KAHAN SE REQUEST AAYI", "in": "2:police", "compact": True},
                {"icon": "rupee", "iconColor": "red", "label": "Hold amount", "sub": "KITNA ROKA GAYA", "in": "2:request", "compact": True}]}],
         "beats": [
            B(11.89, 12.64, "Toh *step ek:*", mascot="point", mascot_pos=C),
            B(13.01, 15.00, "*bank branch* jao, aur *likhit mein* poocho,", mascot="point", mascot_pos=R),
            B(15.29, 18.38, "freeze kis *complaint* ya kis *police station* ki request pe hua.")]},
        {"hold": 0.04, "chip": "STEP 2 · POLICE / CYBER CELL", "chip_color": "green",
         "elements": [
            {"type": "bigtext", "text": "Step *2*", "size": 110, "in": 0, "out": "1", "pos": {"x": 320, "y": 200, "center": True}},
            {"type": "row", "gap": 22, "in": "1", "items": [
                {"type": "phone", "w": 200, "in": "1", "screen": "#14161a", "time": "11:20",
                 "app": {"title": "Calling…", "price": "Cyber Cell", "sub": "Officer", "button": "CONNECTED", "buttonColor": "green", "in": "1:contact"}},
                {"type": "card", "w": 380, "in": "1:police", "rows": [
                    {"icon": "user", "iconColor": "acc", "label": "Investigating officer", "sub": "AAPKA CASE ISI KE PAAS", "in": "2:officer"},
                    {"icon": "shield", "iconColor": "acc", "label": "Police station", "sub": "JAHAN COMPLAINT HAI", "in": "1:police"}]}]}],
         "beats": [
            B(18.73, 19.33, "*Step do:*", mascot="point", mascot_pos=C, dur=0.8),
            B(19.73, 22.09, "us *police station ya cyber cell* se contact karo.", mascot="idle", mascot_pos=R),
            B(22.49, 24.47, "*Wahi officer,* aapka case dekh raha hai.", mascot="point", mascot_pos=R)]},
        {"hold": 0.04, "chip": "STEP 3 · SABOOT", "chip_color": "green", "elements": [],
         "beats": [
            B(24.82, 25.55, "*Step teen:*", dur=0.8),
            B(25.94, 27.19, "apna *saboot* taiyaar rakho."),
            B(27.57, 28.74, "Exchange ka *trade record,*"),
            B(28.97, 29.87, "*buyer ki details,*"),
            B(30.14, 31.39, "aur *payment ke screenshots.*", mascot="happy", mascot_pos=R, pause=0.2)]},
        {"hold": 0.04, "chip": "KITNA HOLD HOTA HAI?",
         "elements": [
            {"type": "split", "title": "AAPKA BALANCE · EXAMPLE", "w": 600, "in": 0,
             "a": {"label": "HOLD · COMPLAINT AMOUNT", "frac": 0.3, "color": "red"}, "b": {"label": "BAAKI CHALTA HAI", "color": "green", "in": "1:complaint"}},
            {"type": "card", "w": 600, "in": "0:utna", "mt": 18, "rows": [
                {"icon": "rupee", "iconColor": "red", "label": "Kabhi: sirf disputed amount", "sub": "JITNA COMPLAINT MEIN", "in": "0:utna", "compact": True},
                {"icon": "lock", "iconColor": "red", "label": "Kabhi: poora account", "sub": "DEBIT FREEZE", "badge": "FULL", "badgeColor": "red", "in": "2:poora", "red": "2:poora", "compact": True}]},
            {"type": "stamp", "text": "POORA FROZEN", "color": "red", "rot": -7, "size": 40, "in": "2:account", "pos": {"x": 320, "y": 120, "center": True}}],
         "beats": [
            B(31.72, 33.71, "Kai baar sirf *utna amount* hold hota hai,", mascot="think", mascot_pos=R),
            B(33.90, 34.91, "jitna *complaint* mein hai."),
            B(35.41, 36.76, "Kai baar, ~poora account.~", mascot="shock", mascot_pos=R)]},
        {"hold": 0.04, "chip": "AGLA RASTA",
         "elements": [
            {"type": "list", "w": 600, "in": 0, "items": [
                {"kicker": "OPTION 1", "title": "*Lawyer* se salah lo", "in": "1:lawyer"},
                {"kicker": "OPTION 2", "title": "Court mein *release ki arzi*", "in": "2:Court"}]},
            {"type": "icon", "name": "⚖", "size": 120, "color": "#0b0d0e", "bg": "acc", "round": True, "label": "LEGAL ROUTE", "in": "2:arzi", "mt": 22}],
         "beats": [
            B(37.14, 38.22, "Aur agar *baat na bane,*", mascot="think", mascot_pos=R),
            B(38.43, 39.60, "toh kisi *lawyer* se salah lo.", mascot="point", mascot_pos=R),
            B(40.03, 42.74, "*Court* se bhi, account khulwane ki *arzi* di ja sakti hai.")]},
        {"hold": 0.04, "chip": "SAVE KARO",
         "elements": [
            {"type": "check", "title": "FREEZE CHECKLIST", "in": 0, "items": [
                {"label": "Bank se likhit reason", "tick": "0:save"},
                {"label": "Police / cyber cell contact", "tick": "0:save+0.25"},
                {"label": "Saboot ka folder", "tick": "0:save+0.5"},
                {"label": "Zaroorat ho toh lawyer", "tick": "1:zaroorat"}]},
            {"type": "tiles", "size": 92, "in": "1:kaam", "mt": 22, "items": [
                {"icon": "star", "color": "acc", "label": "Save"},
                {"icon": "link", "color": "brand", "label": "Share"},
                {"icon": "bell", "color": "green", "label": "Follow"}]}],
         "beats": [
            B(43.14, 44.05, "Ye video *save* karo.", mascot="point", mascot_pos=R),
            B(44.41, 46.05, "Kabhi zaroorat pade, toh *kaam aayega.*", mascot="wink", mascot_pos=R)]}
    ],
    "outro": {"say": "Ab samjhe?", "audio": clip(46.49, 47.08), "dur": 3.0}
}

json.dump(ep, open(OUT, "w"), ensure_ascii=False, indent=1)
print("beats:", sum(len(s["beats"]) for s in ep["hook"] + ep["body"]))
