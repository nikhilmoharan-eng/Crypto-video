"""Mix voice-over + music bed + SFX for Crypto Stories EP 08 and mux with the HyperFrames render."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.expanduser("~/explainer-reel/engine"))
import audio as AU

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 79.5
EV = [(t - 0.05, "whoosh", .4) for t in (8.2, 15.4, 21.3, 29.1, 38.1, 43.1, 59.8, 62.4, 69.1, 75.2)] + [
      (0.1, "pop", .5), (5.29, "riser", .6), (7.0, "chime", .5), (15.71, "tick", .4), (16.06, "tick", .4), (16.41, "tick", .4), (20.15, "pop", .6),
      (27.15, "riser", .4), (29.47, "pop", .5), (36.35, "chime", .6), (39.1, "thud", .9), (51.41, "pop", .5), (51.9, "hit", .5),
      (56.88, "pop", .6), (57.6, "whoosh", .6), (60.95, "thud", 1.0), (64.3, "riser", .6), (67.81, "thud", .9),
      (70.46, "pop", .5), (72.3, "pop", .5), (78.06, "tick", .6), (78.6, "chime", .8)]

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
                "-ar", "48000", "-shortest", "-movflags", "+faststart", os.path.join(HERE, "crypto-stories-ep08-silk-road.mp4")], check=True)
print("done")
