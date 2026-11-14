"""Mix voice-over + music bed + SFX for Case 01 and mux with the HyperFrames render."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.expanduser("~/explainer-reel/engine"))
import audio as AU

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 61.4
EV = [(t - 0.05, "whoosh", .4) for t in (12.4, 16.3, 27.3, 32.1, 42.0, 49.4, 57.2)] + [
      (6.3, "pop", .5), (10.05, "tick", .5), (10.3, "whoosh", .5), (10.9, "thud", .9), (14.2, "riser", .4), (15.3, "thud", .8),
      (18.7, "tick", .5), (19.6, "tick", .5), (20.5, "tick", .5), (21.6, "tick", .5), (25.4, "pop", .6), (27.5, "thud", .4), (28.6, "pop", .5),
      (30.0, "riser", .4), (34.9, "tick", .3), (36.2, "tick", .3), (37.5, "tick", .3), (41.0, "thud", 1.0), (41.05, "hit", .8),
      (42.3, "riser", .4), (44.3, "chime", .6), (47.4, "pop", .5), (53.4, "tick", .4), (55.4, "thud", .8), (59.6, "tick", .6), (60.4, "chime", .8)]

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
                "-ar", "48000", "-shortest", "-movflags", "+faststart", os.path.join(HERE, "crypto-stories-ep02-hard-drive.mp4")], check=True)
print("done")
