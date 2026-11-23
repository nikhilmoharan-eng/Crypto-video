"""Mix voice-over + music bed + SFX for Crypto Stories EP 11 and mux with the HyperFrames render."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.expanduser("~/explainer-reel/engine"))
import audio as AU

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 76.7
EV = [(t - 0.05, "whoosh", .4) for t in (10.1, 17.0, 27.9, 34.2, 42.3, 55.5, 64.8, 71.5)] + [
      (0.2, "riser", .3), (4.1, "pop", .5), (6.03, "tick", .5), (8.2, "chime", .6), (14.49, "pop", .5), (22.8, "tick", .5), (25.82, "riser", .6),
      (32.0, "whoosh", .4), (36.18, "pop", .4), (37.2, "pop", .4), (40.66, "chime", .6), (45.45, "tick", .4), (45.9, "tick", .4), (46.35, "tick", .4),
      (46.8, "tick", .4), (48.25, "chime", .7), (51.05, "riser", .6), (53.9, "hit", .7), (55.79, "pop", .5), (61.11, "riser", .5), (63.27, "thud", .9),
      (66.28, "pop", .5), (68.49, "pop", .5), (75.24, "tick", .6), (75.7, "chime", .8)]

vo, sr = sf.read(os.path.join(HERE, "voiceover.wav"), dtype="float32")
if vo.ndim > 1: vo = vo.mean(1)
n = int(DUR * AU.SR)
v = np.zeros(n, np.float32); v[:min(n, len(vo))] = vo[:n]
fx = np.zeros(n + AU.SR, np.float32)
rng = np.random.default_rng(4)
for t, k, g in EV:
    AU.place(fx, AU.sfx(k, rng), t, g)
mb = AU.music_bed(DUR + 0.5, bpm=96, mood="tense")[:n]
from scipy.ndimage import maximum_filter1d, uniform_filter1d
env = uniform_filter1d(maximum_filter1d(np.abs(v), int(0.05 * AU.SR)), int(0.2 * AU.SR))
duck = 1 - 0.45 * np.clip(env / (env.max() + 1e-9) * 4, 0, 1)
out = v * 1.0 + fx[:n] * 0.5 + mb * duck * 0.6
out = out / (np.abs(out).max() + 1e-9) * 0.89
sf.write(os.path.join(HERE, "mix.wav"), np.stack([out, out], 1), AU.SR)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(HERE, "video_silent.mp4"), "-i", os.path.join(HERE, "mix.wav"),
                "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "192k",
                "-ar", "48000", "-shortest", "-movflags", "+faststart", os.path.join(HERE, "crypto-stories-ep11-forgot-btc.mp4")], check=True)
print("done")
