#!/usr/bin/env python3
"""Render a vertical Hinglish explainer reel from an episode JSON.

usage: python3 render.py episode.json -o out.mp4 [--workers 4] [--preview 12.5 30 ...] [--no-tts] [--fps 30]
"""
import argparse, json, os, re, sys, hashlib, subprocess, math, copy, shutil, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import audio as AU

KOKORO_DIR = os.environ.get("KOKORO_DIR", os.path.expanduser("~/.cache/explainer-reel/kokoro"))
TIME_KEYS = {"in", "out", "hl", "dim", "red", "green", "tick", "strike", "sign", "cross", "shake", "at"}
STYLE_MARK = {"*": "acc", "~": "red", "^": "green"}

# ---------------------------------------------------------------- caption parsing

def parse_words(say):
    """'Toh transfer *pakka.*' -> [(word, style)]"""
    words, cur, style = [], "", None
    stack = []
    for ch in say:
        if ch in STYLE_MARK:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
            continue
        if ch == " ":
            if cur:
                words.append((cur, cur_style))
            cur = ""
            continue
        if not cur:
            cur_style = STYLE_MARK[stack[-1]] if stack else None
        cur += ch
    if cur:
        words.append((cur, cur_style))
    return words


def plain(say):
    return re.sub(r"[*~^]", "", say)


def syl(w):
    w = re.sub(r"[^a-zA-Z0-9₹%]", "", w.lower())
    if not w:
        return 0.5
    if re.fullmatch(r"[0-9,.]+", w):
        return 1.2 * len(re.sub(r"\D", "", w)) ** 0.8
    n = len(re.findall(r"[aeiouy]+", w))
    return max(1, n) + (0.3 if len(w) > 6 else 0)

# ---------------------------------------------------------------- TTS

class TTS:
    def __init__(self, voice="hm_omega", speed=1.1, cache=None, enabled=True):
        self.voice, self.speed, self.enabled = voice, speed, enabled
        self.cache = cache or os.path.join(KOKORO_DIR, "cache")
        os.makedirs(self.cache, exist_ok=True)
        self.k = None

    def _load(self):
        if self.k is None:
            from kokoro_onnx import Kokoro
            self.k = Kokoro(os.path.join(KOKORO_DIR, "kokoro-v1.0.onnx"), os.path.join(KOKORO_DIR, "voices-v1.0.bin"))
        return self.k

    def say(self, text, voice=None, speed=None):
        voice = voice or self.voice; speed = speed or self.speed
        key = hashlib.md5(f"{voice}|{speed}|{text}".encode()).hexdigest()
        p = os.path.join(self.cache, key + ".npy")
        if os.path.exists(p):
            return np.load(p)
        lang = "hi" if re.search(r"[ऀ-ॿ]", text) else "en-us"
        if voice.startswith(("hf_", "hm_")) and lang != "hi":
            lang = "en-us"
        samples, sr = self._load().create(text, voice=voice, speed=speed, lang=lang)
        from scipy.signal import resample_poly
        y = resample_poly(samples.astype(np.float64), AU.SR, sr).astype(np.float32)
        np.save(p, y)
        return y


def trim(y, thr_db=-38):
    if len(y) == 0:
        return y, 0.0
    fr = int(0.01 * AU.SR)
    n = len(y) // fr
    if n == 0:
        return y, 0.0
    e = np.sqrt((y[:n * fr].reshape(n, fr) ** 2).mean(1) + 1e-12)
    db = 20 * np.log10(e / (e.max() + 1e-9))
    idx = np.where(db > thr_db)[0]
    if len(idx) == 0:
        return y, 0.0
    a = max(0, idx[0] - 2) * fr; b = min(len(y), (idx[-1] + 4) * fr)
    return y[a:b], 0.0


def speech_pauses(y, min_gap=0.12, thr_db=-34):
    """return list of (start,end) silent gaps inside speech, seconds"""
    fr = int(0.01 * AU.SR); n = len(y) // fr
    if n < 5:
        return []
    e = np.sqrt((y[:n * fr].reshape(n, fr) ** 2).mean(1) + 1e-12)
    db = 20 * np.log10(e / (e.max() + 1e-9))
    sil = db < thr_db
    gaps, s = [], None
    for i, v in enumerate(sil):
        if v and s is None:
            s = i
        if not v and s is not None:
            if (i - s) * 0.01 >= min_gap and s > 3:
                gaps.append((s * 0.01, i * 0.01))
            s = None
    return gaps

# ---------------------------------------------------------------- timeline

def resolve_ref(ref, sc, beats):
    """beat-relative reference -> absolute seconds"""
    sb = sc["_beats"]
    if ref is None:
        return None
    if isinstance(ref, dict):
        if "t" in ref:
            return sc["t0"] + float(ref["t"])
        if "abs" in ref:
            return float(ref["abs"])
    off = 0.0
    if isinstance(ref, str):
        m = re.match(r"^(.*?)([+-]\d*\.?\d+)$", ref.strip())
        if m and m.group(1) not in ("",):
            ref, off = m.group(1), float(m.group(2))
        if ref == "end":
            return sc["t1"] - 0.6 + off
        if ref == "start":
            return sc["t0"] + off
        if ":" in ref:
            bi, word = ref.split(":", 1)
            b = beats[sb[int(bi)]]
            for w in b["words"]:
                if word.lower() in re.sub(r"[^\w₹%]", "", w["text"].lower()) or word.lower() in w["text"].lower():
                    return w["t"] + off
            return b["t0"] + off
        if "." in ref:
            bi, wi = ref.split(".", 1)
            b = beats[sb[int(bi)]]
            wi = min(int(wi), len(b["words"]) - 1)
            return (b["words"][wi]["t"] if b["words"] else b["t0"]) + off
        ref = int(ref)
    if isinstance(ref, float) and not ref.is_integer():
        b = beats[sb[int(ref)]]
        return b["t0"] + (b["t1"] - b["t0"]) * (ref - int(ref)) + off
    b = beats[sb[min(int(ref), len(sb) - 1)]]
    return b["t0"] + off


def resolve_tree(node, sc, beats):
    if isinstance(node, dict):
        for k, v in list(node.items()):
            if k in TIME_KEYS and not isinstance(v, (dict, list)) or (k in TIME_KEYS and isinstance(v, dict) and ("t" in v or "abs" in v)):
                node[k] = resolve_ref(v, sc, beats)
            elif k == "then" and isinstance(v, list):
                for st in v:
                    if "at" in st:
                        st["at"] = resolve_ref(st["at"], sc, beats)
            else:
                resolve_tree(v, sc, beats)
    elif isinstance(node, list):
        for x in node:
            resolve_tree(x, sc, beats)


def default_ins(elements, t0):
    k = 0
    for e in elements:
        if e.get("in") is None:
            e["in"] = t0 + 0.12 + 0.1 * k
            k += 1
        for key in ("items",):
            if e.get("type") in ("row", "stack"):
                default_ins(e.get(key, []), e["in"])


def build(ep, tts, no_tts=False):
    ep = copy.deepcopy(ep)
    hook = ep.get("hook", [])
    body = ep.get("body", [])
    scenes = [dict(s, _part="hook") for s in hook] + [dict(s, _part="body") for s in body]
    beats, voice_events, sfx = [], [], []
    t = 0.35
    stinger = None
    for si, sc in enumerate(scenes):
        if sc["_part"] == "body" and stinger is None and hook and ep.get("stinger", True) is not False:
            st_d = 3.7
            stinger = {"t0": t, "t1": t + st_d, "lines": ep.get("stinger_lines", {})}
            # sfx: type ticks + riser + hit
            for k in range(26):
                sfx.append((t + 0.05 + k * 0.045, "tick", 0.6))
            for k in range(18):
                sfx.append((t + 0.6 + k * 0.035, "tick", 0.5))
            sfx.append((t + st_d - 1.65, "riser", 0.9))
            sfx.append((t + st_d - 0.45, "hit", 1.0))
            t += st_d + 0.15
        sc["t0"] = t
        sc["_beats"] = []
        if sc.get("flash"):
            sfx.append((t - 0.05, "hit", 0.6))
        else:
            sfx.append((t - 0.08, "whoosh", 0.35 if si else 0.0))
        for bi, b in enumerate(sc.get("beats", [])):
            say = b.get("say", "")
            words = parse_words(say)
            if b.get("audio"):
                import soundfile as sf
                y, sr = sf.read(b["audio"], dtype="float32")
                if y.ndim > 1: y = y.mean(1)
                if sr != AU.SR:
                    from scipy.signal import resample_poly
                    y = resample_poly(y, AU.SR, sr).astype(np.float32)
            elif no_tts or not say.strip():
                y = np.zeros(int(AU.SR * max(b.get("dur", 0), 0.30 * sum(syl(w) for w, _ in words) / 1.6 + 0.2)), np.float32)
            else:
                y = tts.say(b.get("tts") or plain(say), b.get("voice"), b.get("speed"))
            y, _ = trim(y)
            d = max(len(y) / AU.SR, b.get("dur", 0))
            # word timing: proportional to syllables, snapped to detected pauses at punctuation
            wts = [syl(w) + (0.9 if re.search(r"[,:;]$", w) else 0) + (1.2 if re.search(r"[.?!]$", w) else 0) for w, _ in words]
            tot = sum(wts) or 1
            speech = len(y) / AU.SR
            starts, acc = [], 0.0
            for w in wts:
                starts.append(acc / tot * speech * 0.97)
                acc += w
            # snap: words after punctuation start at the end of the nearest detected pause
            if not no_tts and words:
                gaps = speech_pauses(y)
                for i in range(1, len(words)):
                    if re.search(r"[,.:;?!…]$", words[i - 1][0]) and gaps:
                        g = min(gaps, key=lambda g: abs(g[1] - starts[i]))
                        if abs(g[1] - starts[i]) < 0.45:
                            shift = g[1] - starts[i]
                            for j in range(i, len(starts)):
                                starts[j] += shift * (1 - (j - i) / max(1, len(starts) - i))
            bt0 = t
            beat = {"t0": bt0, "words": [{"text": w, "style": s, "t": bt0 + st - 0.04} for (w, s), st in zip(words, starts)],
                    "mascot": b.get("mascot"), "mascot_pos": b.get("mascot_pos", "center"), "scene": si}
            prev = beats[-1] if beats else None
            beat["mascot_enter"] = not (prev and prev.get("mascot") and beat["mascot"] and prev.get("mascot_pos") == beat["mascot_pos"])
            if len(y):
                voice_events.append((bt0, y))
            gap = b.get("pause", 0.16 + (0.12 if re.search(r"[.?!]\W*$", say.strip()) else 0))
            t = bt0 + d + gap
            beat["t1"] = t
            sc["_beats"].append(len(beats))
            beats.append(beat)
        t += sc.get("hold", 0.12)
        sc["t1"] = t
    # outro
    outro = ep.get("outro", {"say": "Ab samjhe?", "tts": "अब समझे?"})
    if outro is not False:
        o_t0 = t + 0.1
        if outro.get("audio"):
            import soundfile as sf
            y, sr = sf.read(outro["audio"], dtype="float32")
            if y.ndim > 1: y = y.mean(1)
            if sr != AU.SR:
                from scipy.signal import resample_poly
                y = resample_poly(y, AU.SR, sr).astype(np.float32)
            y, _ = trim(y)
            voice_events.append((o_t0 + 0.25, y))
        elif outro.get("say") and not no_tts:
            y, _ = trim(tts.say(outro.get("tts") or plain(outro["say"])))
            voice_events.append((o_t0 + 0.25, y))
        sfx.append((o_t0, "whoosh", 0.4)); sfx.append((o_t0 + 0.2, "chime", 1.0))
        for k in range(30):
            sfx.append((o_t0 + 0.8 + k * 0.034, "tick", 0.35))
        outro_d = {"t0": o_t0, "big": outro.get("big", plain(outro.get("say", "Ab samjhe?")))}
        t = o_t0 + outro.get("dur", 3.6)
    else:
        outro_d = None
    total = t + 0.2
    # resolve element times
    for sc in scenes:
        resolve_tree(sc.get("elements", []), sc, beats)
        default_ins(sc.get("elements", []), sc["t0"])
        for e in sc.get("elements", []):
            _sfx_for(e, sfx, sc)
    for sc in scenes:
        sc.pop("_beats", None)
    data = {k: v for k, v in ep.items() if k not in ("hook", "body", "outro")}
    data.update({"scenes": scenes, "beats": beats, "stinger": stinger, "outro": outro_d, "duration": total})
    return data, voice_events, sfx


def _sfx_for(e, sfx, sc):
    typ = e.get("type")
    tin = e.get("in")
    if tin is None:
        return
    if typ == "stamp":
        sfx.append((tin, "thud", 0.9))
    elif typ == "bigtext":
        sfx.append((tin, "hit", 0.55))
    elif typ in ("row", "stack"):
        for k in e.get("items", []):
            _sfx_for(k, sfx, sc)
    else:
        sfx.append((tin, "pop", 0.55))
    if e.get("shake") is not None:
        sfx.append((e["shake"], "thud", 0.6))
    for key in ("rows", "items", "nodes", "messages"):
        for i, r in enumerate(e.get(key, []) or []):
            if isinstance(r, dict) and r.get("in") is not None and abs(r["in"] - tin) > 0.15 and typ not in ("row", "stack"):
                sfx.append((r["in"], "pop", 0.4))
            for kk in ("tick", "hl", "red"):
                if isinstance(r, dict) and r.get(kk) is not None:
                    sfx.append((r[kk], "pop", 0.45))
    if typ == "check" and e.get("tick") is not None:
        sfx.append((e["tick"], "pop", 0.6))

# ---------------------------------------------------------------- frame rendering

def _worker(args):
    data_path, a, b, fps, out, scale = args
    from playwright.sync_api import sync_playwright
    data = json.load(open(data_path))
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(fps), "-c:v", "mjpeg", "-i", "-",
                           "-c:v", "libx264", "-preset", "veryfast", "-crf", "17", "-pix_fmt", "yuv420p", "-r", str(fps), out],
                          stdin=subprocess.PIPE)
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={"width": 720, "height": 1280}, device_scale_factor=scale)
        pg.goto("file://" + os.path.join(HERE, "engine.html"))
        pg.evaluate("d=>window.__init(d)", data)
        pg.evaluate("document.fonts.ready.then(()=>1)")
        pg.wait_for_timeout(150)
        for f in range(a, b):
            pg.evaluate(f"window.__seek({f / fps})")
            ff.stdin.write(pg.screenshot(type="jpeg", quality=93))
        br.close()
    ff.stdin.close(); ff.wait()
    return out


def stills(data, times, outdir, scale=1.0):
    from playwright.sync_api import sync_playwright
    os.makedirs(outdir, exist_ok=True)
    paths = []
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={"width": 720, "height": 1280}, device_scale_factor=scale)
        msgs = []
        pg.on("console", lambda m: msgs.append(m.text))
        pg.on("pageerror", lambda e: msgs.append("PAGEERROR " + str(e)))
        pg.goto("file://" + os.path.join(HERE, "engine.html"))
        pg.evaluate("d=>window.__init(d)", data)
        pg.evaluate("document.fonts.ready.then(()=>1)")
        pg.wait_for_timeout(150)
        for t in times:
            pg.evaluate(f"window.__seek({t})")
            pth = os.path.join(outdir, f"still_{t:07.2f}.png")
            pg.screenshot(path=pth); paths.append(pth)
        br.close()
    for m in msgs:
        print("[page]", m)
    return paths


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode")
    ap.add_argument("-o", "--out", default="reel.mp4")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--workers", type=int, default=max(1, min(6, (os.cpu_count() or 2))))
    ap.add_argument("--scale", type=float, default=1.5, help="1.5 => 1080x1920")
    ap.add_argument("--no-tts", action="store_true")
    ap.add_argument("--no-music", action="store_true")
    ap.add_argument("--preview", nargs="*", type=float, help="only render still PNGs at these times (or every scene start if empty)")
    ap.add_argument("--contact", action="store_true", help="render a contact sheet of every beat")
    a = ap.parse_args()

    ep = json.load(open(a.episode))
    tts = TTS(ep.get("voice", "hm_omega"), ep.get("speed", 1.1), enabled=not a.no_tts)
    print("building timeline + voiceover…", flush=True)
    data, vev, sev = build(ep, tts, no_tts=a.no_tts)
    work = os.path.splitext(a.out)[0] + "_work"
    os.makedirs(work, exist_ok=True)
    dpath = os.path.join(work, "timeline.json")
    json.dump(data, open(dpath, "w"), ensure_ascii=False)
    print(f"duration {data['duration']:.1f}s, {len(data['beats'])} beats, {len(data['scenes'])} scenes", flush=True)

    if a.preview is not None or a.contact:
        times = a.preview or []
        if a.contact or not times:
            times = [round(b["t0"] + min(1.2, (b["t1"] - b["t0"]) * 0.8), 2) for b in data["beats"]]
            if data.get("stinger"): times.append(round(data["stinger"]["t0"] + 2.4, 2))
            if data.get("outro"): times.append(round(data["outro"]["t0"] + 2.6, 2))
            times.sort()
        ps = stills(data, times, os.path.join(work, "stills"))
        if a.contact:
            from PIL import Image
            cols = 8; th = [Image.open(p).resize((180, 320)) for p in ps]
            rows = math.ceil(len(th) / cols)
            sheet = Image.new("RGB", (cols * 180, rows * 320))
            for i, im in enumerate(th):
                sheet.paste(im, ((i % cols) * 180, (i // cols) * 320))
            sp = os.path.splitext(a.out)[0] + "_contact.png"; sheet.save(sp); print("contact sheet:", sp)
        else:
            print("\n".join(ps))
        return

    print("mixing audio…", flush=True)
    import soundfile as sf
    mix = AU.mix(data["duration"], vev, sev, music=not a.no_music, mood=ep.get("music_mood", "tense"))
    wav = os.path.join(work, "mix.wav"); sf.write(wav, np.stack([mix, mix], 1), AU.SR)

    nfr = int(math.ceil(data["duration"] * a.fps))
    W = a.workers
    chunk = math.ceil(nfr / W)
    jobs = [(dpath, i * chunk, min(nfr, (i + 1) * chunk), a.fps, os.path.join(work, f"seg{i:02d}.mp4"), a.scale) for i in range(W) if i * chunk < nfr]
    print(f"rendering {nfr} frames on {len(jobs)} workers…", flush=True)
    t0 = time.time()
    from multiprocessing import Pool
    with Pool(len(jobs)) as pool:
        segs = pool.map(_worker, jobs)
    print(f"frames done in {time.time() - t0:.0f}s", flush=True)
    lst = os.path.join(work, "segs.txt")
    open(lst, "w").write("".join(f"file '{os.path.abspath(s)}'\n" for s in segs))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", wav,
                    "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-shortest", "-movflags", "+faststart", a.out], check=True)
    print("done:", a.out)


if __name__ == "__main__":
    main()
