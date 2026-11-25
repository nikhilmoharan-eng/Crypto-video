"""Mix voice-over + music bed + SFX for Crypto Stories EP 13 and mux with the HyperFrames render."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.expanduser("~/explainer-reel/engine"))
import audio as AU

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 81.0
EV = [(t - 0.05, "whoosh", .4) for t in (6.8, 12.0, 18.5, 29.5, 44.2, 53.2, 60.8, 67.6, 71.5, 75.7)] + [
      (0.1, "pop", .4), (0.5, "pop", .4), (2.48, "hit", .9), (4.19, "chime", .4), (10.98, "chime", .5), (13.6, "pop", .5), (16.7, "pop", .5),
      (21.6, "riser", .6), (25.2, "tick", .5), (27.9, "hit", .7), (33.0, "tick", .4), (33.7, "tick", .4), (34.4, "tick", .4), (35.1, "tick", .4),
      (35.8, "tick", .4), (37.78, "hit", .7), (41.4, "riser", .6), (42.9, "thud", .9), (47.13, "pop", .5), (49.96, "pop", .5), (51.66, "thud", .7),
      (54.8, "riser", .5), (57.75, "thud", 1.0), (65.98, "pop", .6), (69.0, "chime", .6), (72.39, "pop", .5), (73.9, "pop", .5),
      (79.5, "tick", .6), (80.0, "chime", .8)]

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
                "-ar", "48000", "-shortest", "-movflags", "+faststart", os.path.join(HERE, "crypto-stories-ep13-dao.mp4")], check=True)
print("done")
