"""Mix voice-over + music bed + SFX for Case 01 and mux with the HyperFrames render."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.expanduser("~/explainer-reel/engine"))
import audio as AU

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 40.8
EV = [(t - 0.05, "whoosh", .45) for t in (2.75, 5.45, 9.85, 14.25, 20.05, 25.6, 28.9, 31.3, 38.7)] + [
      (0.3, "pop", .6), (1.5, "thud", .9), (3.55, "hit", .7), (3.6, "riser", .35), (6.6, "riser", .3), (7.8, "pop", .5), (8.3, "pop", .5), (8.8, "pop", .5),
      (10.3, "pop", .6), (11.15, "riser", .35), (13.1, "pop", .6), (16.8, "pop", .6), (17.8, "whoosh", .3), (18.4, "pop", .5),
      (20.4, "tick", .4), (21.9, "riser", .4), (23.4, "pop", .7), (25.8, "hit", .8), (26.5, "thud", .5), (28.15, "pop", .7),
      (29.0, "riser", .8), (29.95, "thud", 1.0), (30.0, "hit", .9), (32.25, "pop", .5), (35.4, "pop", .5), (36.6, "thud", .8),
      (39.62, "tick", 1.0), (39.7, "chime", .9)]

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
                "-ar", "48000", "-shortest", "-movflags", "+faststart", os.path.join(HERE, "pump-dump-niks-style.mp4")], check=True)
print("done")
