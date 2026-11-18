"""Mix voice-over + music bed + SFX for Crypto Stories EP 06 and mux with the HyperFrames render."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.expanduser("~/explainer-reel/engine"))
import audio as AU

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 57.0
EV = [(t - 0.05, "whoosh", .4) for t in (7.6, 21.4, 30.4, 42.4, 47.6, 53.0)] + [
      (0.2, "riser", .4), (1.9, "hit", .8), (3.85, "pop", .6), (5.42, "thud", 1.0), (15.48, "pop", .5), (16.6, "riser", .5), (19.9, "pop", .4),
      (25.3, "whoosh", .5), (28.2, "whoosh", .6), (29.22, "thud", 1.0), (31.9, "riser", .4), (35.63, "hit", .7), (36.5, "pop", .5)] + [
      (38.9 + k * 0.24, "tick", .5) for k in range(8)] + [(41.23, "thud", .9), (43.5, "chime", .5), (45.85, "hit", .6),
      (51.5, "pop", .5), (52.2, "pop", .5), (55.35, "tick", .6), (56.0, "chime", .8)]

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
                "-ar", "48000", "-shortest", "-movflags", "+faststart", os.path.join(HERE, "crypto-stories-ep06-password.mp4")], check=True)
print("done")
