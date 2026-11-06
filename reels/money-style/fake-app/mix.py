"""Mix voice-over + music bed + SFX for Case 01 and mux with the HyperFrames render."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.expanduser("~/explainer-reel/engine"))
import audio as AU

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 44.3
EV = [(t - 0.05, "whoosh", .45) for t in (3.0, 9.35, 15.0, 23.3, 29.5, 37.05, 42.35)] + [
      (0.3, "pop", .6), (1.5, "thud", .9), (4.9, "pop", .5), (6.5, "tick", .6), (7.3, "tick", .6), (8.0, "riser", .35), (8.6, "chime", .6),
      (10.8, "pop", .6), (12.3, "tick", .9), (13.5, "hit", .8), (13.6, "thud", .7), (15.9, "pop", .5), (18.3, "pop", .5), (21.0, "pop", .6),
      (24.6, "riser", .5), (25.0, "whoosh", .4), (27.6, "thud", 1.0), (31.5, "pop", .5), (34.4, "pop", .5), (35.9, "pop", .5),
      (38.3, "pop", .5), (40.6, "thud", .9), (43.22, "tick", 1.0), (43.3, "chime", .9)]

vo, sr = sf.read(os.path.join(HERE, "voiceover.wav"), dtype="float32")
if vo.ndim > 1: vo = vo.mean(1)
n = int(DUR * AU.SR)
v = np.zeros(n, np.float32); v[:min(n, len(vo))] = vo[:n]
fx = np.zeros(n + AU.SR, np.float32)
rng = np.random.default_rng(4)
for t, k, g in EV:
    AU.place(fx, AU.sfx(k, rng), t, g)
mb = AU.music_bed(DUR + 0.5, bpm=96, mood="bright")[:n]
from scipy.ndimage import maximum_filter1d, uniform_filter1d
env = uniform_filter1d(maximum_filter1d(np.abs(v), int(0.05 * AU.SR)), int(0.2 * AU.SR))
duck = 1 - 0.45 * np.clip(env / (env.max() + 1e-9) * 4, 0, 1)
out = v * 1.0 + fx[:n] * 0.5 + mb * duck * 0.6
out = out / (np.abs(out).max() + 1e-9) * 0.89
sf.write(os.path.join(HERE, "mix.wav"), np.stack([out, out], 1), AU.SR)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(HERE, "video_silent.mp4"), "-i", os.path.join(HERE, "mix.wav"),
                "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "192k",
                "-ar", "48000", "-shortest", "-movflags", "+faststart", os.path.join(HERE, "fake-trading-app-niks-style.mp4")], check=True)
print("done")
