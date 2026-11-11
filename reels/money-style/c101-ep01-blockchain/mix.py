"""Mix voice-over + music bed + SFX for Case 01 and mux with the HyperFrames render."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.expanduser("~/explainer-reel/engine"))
import audio as AU

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 56.0
EV = [(t - 0.05, "whoosh", .45) for t in (7.0, 12.1, 20.5, 27.9, 37.3, 41.1, 50.3, 54.3)] + [
      (0.3, "pop", .5), (0.42, "pop", .4), (0.54, "pop", .4), (3.4, "pop", .6), (5.0, "thud", .8), (8.8, "tick", .5), (9.7, "tick", .5), (10.6, "tick", .5),
      (12.4, "pop", .5), (13.0, "pop", .5), (13.6, "pop", .5), (15.6, "chime", .4), (16.0, "chime", .4), (24.6, "riser", .4), (26.6, "chime", .5),
      (29.0, "pop", .6), (31.5, "thud", .5), (34.6, "thud", 1.0), (34.65, "hit", .8), (37.7, "pop", .6), (39.6, "thud", .9),
      (42.6, "pop", .5), (45.6, "pop", .5), (48.0, "pop", .5), (50.7, "pop", .6), (55.12, "tick", 1.0), (55.2, "chime", .9)]

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
                "-ar", "48000", "-shortest", "-movflags", "+faststart", os.path.join(HERE, "crypto101-ep01-blockchain.mp4")], check=True)
print("done")
