"""Mix voice-over + music bed + SFX for Crypto Stories EP 14 and mux with the HyperFrames render."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.expanduser("~/explainer-reel/engine"))
import audio as AU

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 92.5
EV = [(t - 0.05, "whoosh", .4) for t in (11.9, 19.8, 31.4, 44.9, 53.2, 62.5, 72.7, 80.5, 87.0)] + [
      (3.6, "chime", .6), (9.6, "thud", 1.0), (12.8, "pop", .5), (18.14, "pop", .5), (20.9, "riser", .5), (25.82, "pop", .5), (30.11, "hit", .8),
      (36.5, "pop", .5), (37.6, "chime", .5), (39.8, "pop", .5), (43.0, "chime", .6), (45.3, "riser", .6), (51.6, "pop", .6),
      (55.62, "hit", .5), (56.6, "hit", .5), (60.08, "hit", .5), (62.89, "pop", .5), (65.92, "pop", .5), (68.38, "pop", .5), (70.6, "thud", .8),
      (74.2, "pop", .5), (76.9, "pop", .5), (78.48, "thud", .8), (82.0, "tick", .4), (82.4, "tick", .4), (82.8, "tick", .4), (83.2, "tick", .4),
      (83.6, "tick", .4), (90.98, "tick", .6), (91.5, "chime", .8)]

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
                "-ar", "48000", "-shortest", "-movflags", "+faststart", os.path.join(HERE, "crypto-stories-ep14-el-salvador.mp4")], check=True)
print("done")
