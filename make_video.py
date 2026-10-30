#!/usr/bin/env python3
"""Render a kinetic-typography vertical video entirely from code.

Every pixel is drawn here with Pillow (background, petals, text, illustrations)
and piped to ffmpeg, which mixes the voice-over MP3 with sound effects
synthesised in sfx.py.

    python3 make_video.py --audio combined.mp3 --script script.json --out out.mp4
"""
import argparse
import json
import math
import random
import os
import subprocess
import tempfile

import sfx
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

W, H, FPS = 1080, 1920, 30
SS = 2  # supersampling factor for smooth shapes drawn on small layers

BG = (250, 248, 244)
INK = (17, 17, 17)
MUTED = (120, 120, 120)
GRID = (205, 202, 198)

FONT_DIR = "/usr/share/fonts/opentype/inter/"
FONTS = {
    "light": FONT_DIR + "Inter-Light.otf",
    "regular": FONT_DIR + "Inter-Regular.otf",
    "medium": FONT_DIR + "Inter-Medium.otf",
    "bold": FONT_DIR + "InterDisplay-Bold.otf",
    "black": FONT_DIR + "InterDisplay-ExtraBold.otf",
}
_font_cache = {}


def font(kind, size):
    key = (kind, size)
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(FONTS[kind], size)
    return _font_cache[key]


# ---------------------------------------------------------------- easing

def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, x))


def ease_out(x):
    x = clamp(x)
    return 1 - (1 - x) ** 3


def ease_in_out(x):
    x = clamp(x)
    return 4 * x ** 3 if x < 0.5 else 1 - (-2 * x + 2) ** 3 / 2


def back_out(x):
    x = clamp(x)
    c = 1.70158
    return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2


def lerp(a, b, t):
    return a + (b - a) * t


# ---------------------------------------------------------------- static layers

def make_background():
    img = Image.new("RGB", (W, H), BG)
    # soft diagonal light bands
    bands = Image.new("L", (W * 2, H * 2), 0)
    d = ImageDraw.Draw(bands)
    for i in range(-4, 14):
        x = i * 360
        d.polygon([(x, 0), (x + 140, 0), (x + 140 - H * 2, H * 2), (x - H * 2, H * 2)], fill=10)
    bands = bands.resize((W, H)).filter(ImageFilter.GaussianBlur(40))
    img.paste((255, 255, 255), mask=bands)

    # dashed grid fading out radially from the centre
    grid = Image.new("L", (W, H), 0)
    g = ImageDraw.Draw(grid)
    step, cx, cy = 135, W // 2, int(H * 0.47)
    for x in range(cx % step, W, step):
        for y in range(0, H, 16):
            g.line([(x, y), (x, y + 8)], fill=255, width=2)
    for y in range(cy % step, H, step):
        for x in range(0, W, 16):
            g.line([(x, y), (x + 8, y)], fill=255, width=2)
    fade = Image.radial_gradient("L").resize((int(W * 1.1), int(W * 1.25)))
    fade = fade.point(lambda v: int(clamp(1 - v / 200) ** 1.5 * 170))
    mask = Image.new("L", (W, H), 0)
    mask.paste(fade, (cx - fade.width // 2, cy - fade.height // 2))
    grid = ImageChops.multiply(grid, mask)
    img.paste(GRID, mask=grid)

    # subtle warm glow behind the text area
    glow = Image.radial_gradient("L").resize((W, W)).point(lambda v: int(clamp(1 - v / 255) * 60))
    gl = Image.new("L", (W, H), 0)
    gl.paste(glow, (0, cy - W // 2))
    img.paste((255, 253, 250), mask=gl)
    return img


def petal_cluster(size):
    """Four teardrop petals radiating from a point (drawn in a size x size box)."""
    s = size * SS
    im = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(im)
    c = s / 2
    for k in range(4):
        a0 = k * math.pi / 2 + math.pi / 4
        pts = []
        for i in range(60):
            t = i / 59 * math.pi
            r = math.sin(t) ** 0.8 * s * 0.13
            along = (1 - math.cos(t)) / 2 * s * 0.48
            px = along * math.cos(a0) - r * math.sin(a0)
            py = along * math.sin(a0) + r * math.cos(a0)
            pts.append((c + px, c + py))
        for i in range(59, -1, -1):
            t = i / 59 * math.pi
            r = math.sin(t) ** 0.8 * s * 0.13
            along = (1 - math.cos(t)) / 2 * s * 0.48
            px = along * math.cos(a0) + r * math.sin(a0)
            py = along * math.sin(a0) - r * math.cos(a0)
            pts.append((c + px, c + py))
        d.polygon(pts, fill=255)
    return im.resize((size, size), Image.LANCZOS)


PETALS = None


def draw_petals(img, t):
    global PETALS
    if PETALS is None:
        PETALS = petal_cluster(560)
    for (cx, cy, base) in ((0, 0, 0), (W, H, 45)):
        ang = base + 6 * math.sin(t * 0.6) + t * 4
        p = PETALS.rotate(ang, resample=Image.BICUBIC)
        img.paste(INK, (int(cx - p.width / 2), int(cy - p.height / 2)), p)



# ---------------------------------------------------------------- text

STYLE = {
    # kind, size, colour ("grad" = vertical grey gradient)
    "small": ("regular", 44, MUTED),
    "label": ("medium", 50, INK),
    "big": ("black", 120, INK),
    "huge": ("black", 160, INK),
    "grad": ("black", 120, "grad"),
    "hugegrad": ("black", 160, "grad"),
}


def gradient_fill(mask):
    w, h = mask.size
    grad = Image.linear_gradient("L").resize((w, h))
    grad = grad.point(lambda v: int(lerp(95, 185, v / 255)))
    layer = Image.merge("RGB", (grad, grad, grad))
    return layer


def render_word(text, style):
    kind, size, colour = STYLE[style]
    f = font(kind, size)
    l, tp, r, b = f.getbbox(text)
    w, h = r + 4, b + int(size * 0.25)
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).text((0, 0), text, font=f, fill=255)
    if colour == "grad":
        fill = gradient_fill(mask)
    else:
        fill = Image.new("RGB", (w, h), colour)
    return fill, mask, f


_word_cache = {}


def word_image(text, style):
    key = (text, style)
    if key not in _word_cache:
        _word_cache[key] = render_word(text, style)
    return _word_cache[key]


def expand_line(line):
    """Accept {"style", "text", "at": t0 | [t per word]} and fill in per-word timings."""
    if "words" not in line:
        words = line["text"].split()
        at = line["at"]
        times = at if isinstance(at, list) else [at + i * 0.14 for i in range(len(words))]
        line["words"] = [{"text": w, "at": t} for w, t in zip(words, times)]
    return line


def layout_line(line):
    """Returns list of (word, style, width) and total width / ascent."""
    out, total = [], 0
    for wd in line["words"]:
        fill, mask, f = word_image(wd["text"], line["style"])
        out.append((wd, fill, mask, f))
        total += mask.width
    space = font(STYLE[line["style"]][0], STYLE[line["style"]][1]).getlength(" ")
    total += space * (len(out) - 1)
    return out, total, space


def draw_text_block(img, block, t):
    """block = {"y": centre y, "lines": [{style, words:[{text, at}], dx}] ,"start","end"}"""
    y = block.get("y", H * 0.42)
    lines = [expand_line(l) for l in block["lines"]]
    heights = [STYLE[l["style"]][1] * (1.35 if STYLE[l["style"]][1] < 60 else 1.05) for l in lines]
    total_h = sum(heights)
    cy = y - total_h / 2
    out_t = clamp((t - (block["end"] - 0.35)) / 0.35)
    for line, lh in zip(lines, heights):
        items, total, space = layout_line(line)
        align = line.get("align", "center")
        x = W / 2 - total / 2 if align == "center" else 90
        x += line.get("dx", 0)
        for wd, fill, mask, f in items:
            k = ease_out((t - wd["at"]) / 0.45)
            if k <= 0:
                x += mask.width + space
                continue
            alpha = k * (1 - out_t)
            if alpha <= 0.01:
                x += mask.width + space
                continue
            dy = (1 - k) * 60 - out_t * 40
            m = mask
            if k < 1:
                blur = (1 - k) * 10
                m = m.filter(ImageFilter.GaussianBlur(blur))
            m = m.point(lambda v, a=alpha: int(v * a))
            img.paste(fill, (int(x), int(cy + dy)), m)
            x += mask.width + space
        cy += lh


# ---------------------------------------------------------------- illustrations
# Each visual takes (img, t_local, dur, params) and draws itself; t_local is
# seconds since the scene started.


def fade_mul(t, dur, fin=0.4, fout=0.35):
    return clamp(t / fin) * clamp((dur - t) / fout)


def person(d, x, y, h, fill):
    """Simple standing silhouette with feet at (x, y)."""
    hr = h * 0.11
    d.ellipse([x - hr, y - h, x + hr, y - h + 2 * hr], fill=fill)
    bw = h * 0.17
    d.rounded_rectangle([x - bw, y - h + 2.3 * hr, x + bw, y - h * 0.45], radius=bw * 0.6, fill=fill)
    lw = h * 0.07
    d.rounded_rectangle([x - bw + 2, y - h * 0.5, x - bw + 2 + lw * 2, y], radius=lw, fill=fill)
    d.rounded_rectangle([x + bw - 2 - lw * 2, y - h * 0.5, x + bw - 2, y], radius=lw, fill=fill)


def layer_paste(img, layer, alpha):
    if alpha <= 0:
        return
    a = layer.getchannel("A").point(lambda v: int(v * alpha))
    img.paste(layer.convert("RGB"), (0, 0), a)



def vis_crowd(img, t, dur, p):
    """Scattered figures popping in (an audience)."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    rnd = random.Random(p.get("seed", 3))
    n = p.get("n", 14)
    base = p.get("y", 1250)
    for i in range(n):
        x = rnd.uniform(120, W - 120)
        yy = base + rnd.uniform(-180, 300)
        h = rnd.uniform(120, 220) * (0.75 + (yy - base + 180) / 1200)
        g = rnd.choice([30, 60, 110, 150])
        k = back_out((t - i * 0.08) / 0.5)
        if k <= 0:
            continue
        person(d, x, yy + (1 - k) * 80, h * clamp(k, 0, 1.2), (g, g, g, 255))
    layer_paste(img, layer, fade_mul(t, dur))




def vis_hourglass(img, t, dur, p):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    cx, top, bot = W / 2 + 200, 820, 1720
    mid = (top + bot) / 2
    wdt = 300
    d.rounded_rectangle([cx - wdt - 30, top - 40, cx + wdt + 30, top], radius=16, fill=(60, 60, 60, 255))
    d.rounded_rectangle([cx - wdt - 30, bot, cx + wdt + 30, bot + 40], radius=16, fill=(60, 60, 60, 255))
    glass = [(cx - wdt, top), (cx + wdt, top), (cx + 30, mid), (cx + wdt, bot), (cx - wdt, bot), (cx - 30, mid)]
    d.polygon(glass, outline=(150, 150, 150, 255), fill=(235, 235, 235, 160), width=6)
    k = clamp(t / dur)
    # sand: top triangle shrinks, bottom mound grows
    st = lerp(top + 80, mid - 10, k)
    sw = wdt * (mid - st) / (mid - top)
    d.polygon([(cx - sw, st), (cx + sw, st), (cx, mid)], fill=(110, 110, 110, 255))
    mh = lerp(20, 300, k)
    d.polygon([(cx - wdt + 10, bot), (cx + wdt - 10, bot), (cx, bot - mh)], fill=(110, 110, 110, 255))
    d.line([(cx, mid), (cx, bot - mh)], fill=(110, 110, 110, 255), width=6)
    layer_paste(img, layer, fade_mul(t, dur))



def vis_bars(img, t, dur, p):
    """Rising bar chart with an arrow (growth / conversions)."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    vals = p.get("vals", [0.2, 0.35, 0.3, 0.55, 0.7, 1.0])
    base, maxh, bw = 1700, 620, 110
    x0 = W / 2 - len(vals) * (bw + 30) / 2
    pts = []
    for i, v in enumerate(vals):
        k = ease_out((t - i * 0.12) / 0.6)
        h = maxh * v * k
        g = 70 + i * 15
        d.rounded_rectangle([x0 + i * (bw + 30), base - h, x0 + i * (bw + 30) + bw, base], radius=14, fill=(g, g, g, 255))
        pts.append((x0 + i * (bw + 30) + bw / 2, base - h - 50))
    if t > 0.8:
        d.line(pts, fill=(20, 20, 20, 255), width=10, joint="curve")
        ex, ey = pts[-1]
        d.polygon([(ex + 10, ey - 40), (ex + 40, ey + 20), (ex - 25, ey + 15)], fill=(20, 20, 20, 255))
    layer_paste(img, layer, fade_mul(t, dur))



def vis_dots(img, t, dur, p):
    """Three separate pulsing circles (no sequence / no warm-up / no moment)."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for i in range(3):
        k = back_out((t - i * 0.25) / 0.5)
        r = 70 * clamp(k, 0, 1.3) * (1 + 0.05 * math.sin(t * 4 + i))
        cx = W / 2 + (i - 1) * 260
        d.ellipse([cx - r, 1300 - r, cx + r, 1300 + r], outline=(40, 40, 40, 255), width=10)
        if i < 2 and t > 0.8:
            d.line([(cx + 90, 1300), (cx + 170, 1300)], fill=(160, 160, 160, 255), width=8)
    layer_paste(img, layer, fade_mul(t, dur))


def vis_pumpdump(img, t, dur, p):
    """Price line that pumps up, then crashes at `crash_at` seconds."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    rnd = random.Random(11)
    n, x0, x1, base = 48, 110, W - 110, 1700
    crash = p.get("crash_at", dur * 0.6)
    pts = []
    for i in range(n):
        u = i / (n - 1)
        up = (u / 0.62) ** 2 if u < 0.62 else 1 - ((u - 0.62) / 0.38) ** 0.7 * 0.9
        pts.append((lerp(x0, x1, u), base - 80 - up * 560 + rnd.uniform(-22, 22)))
    # reveal: up-leg during [0, crash], down-leg during [crash, crash + 1.2]
    if t < crash:
        shown = 0.62 * ease_out(t / max(0.3, crash))
    else:
        shown = 0.62 + 0.38 * ease_out((t - crash) / 1.2)
    m = max(2, int(shown * (n - 1)) + 1)
    seg = pts[:m]
    poly = seg + [(seg[-1][0], base), (seg[0][0], base)]
    d.polygon(poly, fill=(0, 0, 0, 22))
    for i in range(len(seg) - 1):
        falling = seg[i + 1][1] > seg[i][1] and i >= 0.62 * (n - 1) - 1
        d.line([seg[i], seg[i + 1]], fill=(150, 150, 150, 255) if falling else (20, 20, 20, 255), width=12)
    hx, hy = seg[-1]
    d.ellipse([hx - 18, hy - 18, hx + 18, hy + 18], fill=(20, 20, 20, 255))
    d.line([(x0, base), (x1, base)], fill=(180, 180, 180, 255), width=4)
    layer_paste(img, layer, fade_mul(t, dur))


VISUALS = {
    "pumpdump": vis_pumpdump,
    "crowd": vis_crowd,
    "hourglass": vis_hourglass,
    "bars": vis_bars,
    "dots": vis_dots,
}


# ---------------------------------------------------------------- main loop

def render(script, audio, out, duration, sfx_volume):
    bg = make_background()
    scenes = script["scenes"]
    for sc in scenes:
        for line in sc["lines"]:
            expand_line(line)
    sfx_path = os.path.join(tempfile.mkdtemp(), "sfx.wav")
    sfx.build(script, duration, sfx_path)
    n = int(math.ceil(duration * FPS))
    ff = subprocess.Popen([
        "ffmpeg", "-v", "error", "-y",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
        "-i", audio, "-i", sfx_path,
        "-filter_complex",
        f"[1:a]aresample=44100[vo];[2:a]volume={sfx_volume}[fx];"
        "[vo][fx]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]",
        "-map", "0:v", "-map", "[a]",
        "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out,
    ], stdin=subprocess.PIPE)
    for i in range(n):
        t = i / FPS
        img = bg.copy()
        for sc in scenes:
            if sc["start"] - 0.05 <= t <= sc["end"]:
                v = sc.get("visual")
                if v:
                    VISUALS[v["type"]](img, t - sc["start"], sc["end"] - sc["start"], v)
                draw_text_block(img, sc, t)
        draw_petals(img, t)
        ff.stdin.write(img.tobytes())
        if i % (FPS * 5) == 0:
            print(f"  frame {i}/{n}", flush=True)
    ff.stdin.close()
    ff.wait()


def audio_duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", path], capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audio", required=True)
    ap.add_argument("--script", default="script.json")
    ap.add_argument("--out", default="output.mp4")
    ap.add_argument("--sfx-volume", type=float, default=0.35, help="sound-effect level under the voice")
    ap.add_argument("--preview", type=float, nargs="*", help="render still PNGs at these times instead")
    a = ap.parse_args()
    script = json.load(open(a.script))
    if a.preview:
        bg = make_background()
        for t in a.preview:
            img = bg.copy()
            for sc in script["scenes"]:
                if sc["start"] <= t <= sc["end"]:
                    v = sc.get("visual")
                    if v:
                        VISUALS[v["type"]](img, t - sc["start"], sc["end"] - sc["start"], v)
                    draw_text_block(img, sc, t)
            draw_petals(img, t)
            img.save(f"preview_{t:05.2f}.png")
        return
    render(script, a.audio, a.out, audio_duration(a.audio), a.sfx_volume)


if __name__ == "__main__":
    main()
