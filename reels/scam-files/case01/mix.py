"""Mix voice-over + music bed + SFX for Case 01 and mux with the HyperFrames render."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.expanduser("~/explainer-reel/engine"))
import audio as AU

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 40.8
EV = [(2.47, "whoosh", .7), (9.55, "whoosh", .7), (19.7, "whoosh", .7), (28.6, "whoosh", .7), (38.35, "whoosh", .7),
      (0.05, "hit", .9), (0.75, "whoosh", .35), (1.45, "thud", 1.0), (2.79, "hit", .5), (3.55, "hit", .8), (4.35, "hit", .5), (3.7, "riser", .4),
      (5.45, "whoosh", .4), (6.6, "riser", .35), (7.8, "pop", .6), (8.22, "pop", .6), (8.64, "pop", .6), (9.06, "pop", .6),
      (9.98, "hit", .5), (10.3, "pop", .7), (11.15, "riser", .4), (13.1, "pop", .7), (14.37, "hit", .6), (15.4, "whoosh", .3), (15.8, "whoosh", .3),
      (16.75, "pop", .5), (16.9, "pop", .5), (18.3, "pop", .6), (19.0, "thud", 1.0), (20.6, "tick", .5), (21.0, "tick", .5), (21.9, "riser", .5),
      (23.4, "pop", .8), (24.2, "whoosh", .4), (25.74, "hit", .8), (26.4, "thud", .5), (27.1, "hit", .5), (28.2, "pop", .7),
      (29.0, "riser", .9), (29.97, "thud", 1.0), (30.0, "hit", 1.0), (31.43, "hit", .5), (31.6, "whoosh", .3), (32.25, "pop", .5),
      (33.95, "thud", .8), (35.4, "pop", .5), (38.62, "whoosh", .3), (38.85, "thud", 1.0), (38.9, "hit", .8), (39.3, "chime", 1.0)]

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
                "-ar", "48000", "-shortest", "-movflags", "+faststart", os.path.join(HERE, "scam-files-case01-pump-and-dump.mp4")], check=True)
print("done")
