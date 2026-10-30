"""Synthesised sound effects, timed from the same script.json as the visuals.

Nothing is sampled: every sound is built from sine waves and noise with numpy,
then written to a mono WAV that make_video.py mixes under the voice-over.
"""
import math
import wave

import numpy as np

SR = 44100
rng = np.random.default_rng(5)

BIG_STYLES = {"big", "huge", "grad", "hugegrad"}


def env(n, attack, decay):
    """Fast attack, exponential decay envelope (times in seconds)."""
    t = np.arange(n) / SR
    a = np.clip(t / max(attack, 1e-4), 0, 1)
    return a * np.exp(-t / decay)


def lowpass(x, cutoffs):
    """One-pole low-pass with a per-sample cutoff (Hz)."""
    out = np.empty_like(x)
    k = 1 - np.exp(-2 * math.pi * np.asarray(cutoffs) / SR)
    y = 0.0
    for i in range(len(x)):
        y += k[i] * (x[i] - y)
        out[i] = y
    return out


def whoosh(dur=0.55):
    n = int(dur * SR)
    t = np.linspace(0, 1, n)
    shape = np.sin(math.pi * t) ** 2
    cut = 300 + 3500 * np.sin(math.pi * t) ** 1.5
    return lowpass(rng.standard_normal(n), cut) * shape * 0.9


def pop(freq=520, dur=0.18):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = freq * (1 + 0.8 * np.exp(-t / 0.015))
    return np.sin(2 * math.pi * np.cumsum(f) / SR) * env(n, 0.002, 0.045) * 0.7


def tick(freq=2400, dur=0.05):
    n = int(dur * SR)
    t = np.arange(n) / SR
    click = np.sin(2 * math.pi * freq * t) + 0.4 * rng.standard_normal(n)
    return click * env(n, 0.0005, 0.008) * 0.35


def boom(dur=0.9):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = 45 + 90 * np.exp(-t / 0.06)
    body = np.sin(2 * math.pi * np.cumsum(f) / SR) * env(n, 0.003, 0.25)
    hit = lowpass(rng.standard_normal(n), np.full(n, 1800)) * env(n, 0.001, 0.03)
    return body * 0.9 + hit * 0.6


def blip(freq, dur=0.12):
    n = int(dur * SR)
    t = np.arange(n) / SR
    tone = np.sin(2 * math.pi * freq * t) + 0.3 * np.sin(4 * math.pi * freq * t)
    return tone * env(n, 0.003, 0.04) * 0.3


def riser(dur):
    n = int(dur * SR)
    t = np.linspace(0, 1, n)
    f = 180 + 700 * t ** 2
    tone = np.sin(2 * math.pi * np.cumsum(f) / SR)
    air = lowpass(rng.standard_normal(n), 400 + 4000 * t)
    return (tone * 0.12 + air * 0.25) * t ** 2


def fall(dur=1.2):
    n = int(dur * SR)
    t = np.linspace(0, 1, n)
    f = 900 * (1 - t) ** 2 + 70
    tone = np.sin(2 * math.pi * np.cumsum(f) / SR)
    return tone * np.sin(math.pi * np.minimum(t * 3, 1) / 2) * (1 - t) * 0.35


def add(track, sound, at, gain=1.0):
    i = int(at * SR)
    if i < 0 or i >= len(track):
        return
    j = min(len(track), i + len(sound))
    track[i:j] += sound[: j - i] * gain


def build(script, duration, path, master=1.0):
    track = np.zeros(int(duration * SR) + SR)
    for k, sc in enumerate(script["scenes"]):
        start, end = sc["start"], sc["end"]
        if k > 0:
            add(track, whoosh(), start - 0.25, 0.55)
        for line in sc["lines"]:
            for w in line["words"]:
                if line["style"] in ("huge", "hugegrad"):
                    add(track, boom(), w["at"], 0.6)
                elif line["style"] in BIG_STYLES:
                    add(track, pop(rng.uniform(440, 620)), w["at"], 0.45)
                else:
                    add(track, tick(rng.uniform(2000, 2800)), w["at"], 0.35)
        v = sc.get("visual") or {}
        kind = v.get("type")
        if kind == "bars":
            for i in range(len(v.get("vals", [0] * 6))):
                add(track, blip(440 * 2 ** (i * 2 / 12)), start + i * 0.12, 0.8)
        elif kind == "hourglass":
            t = start + 0.4
            while t < end - 0.3:
                add(track, tick(3200 if int((t - start) * 2) % 2 else 2600, 0.04), t, 0.5)
                t += 0.5
        elif kind == "crowd":
            for i in range(v.get("n", 14)):
                add(track, pop(rng.uniform(700, 1000), 0.08), start + i * 0.08, 0.15)
        elif kind == "pumpdump":
            crash = start + v.get("crash_at", (end - start) * 0.6)
            add(track, riser(crash - start - 0.2), start + 0.2, 0.8)
            add(track, boom(), crash, 0.5)
            add(track, fall(), crash, 0.9)
        elif kind == "dots":
            for i in range(3):
                add(track, pop(330 + i * 110, 0.2), start + i * 0.25, 0.4)
    peak = np.abs(track).max() or 1.0
    track = np.clip(track / peak * 0.8 * master, -1, 1)
    with wave.open(path, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SR)
        wf.writeframes((track * 32767).astype(np.int16).tobytes())
