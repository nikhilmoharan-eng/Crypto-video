"""Mix voice-over + music bed + SFX for Crypto Stories EP 10 and mux with the HyperFrames render."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.expanduser("~/explainer-reel/engine"))
import audio as AU

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 87.7
EV = [(t - 0.05, "whoosh", .4) for t in (8.2, 13.3, 26.5, 44.8, 59.8, 82.5)] + [
      (4.31, "hit", .9), (7.08, "thud", 1.0), (8.4, "riser", .4), (9.8, "tick", .4), (14.2, "pop", .4), (17.49, "pop", .5), (19.11, "pop", .5),
      (24.6, "pop", .5), (27.7, "pop", .5), (31.0, "hit", .5), (34.1, "tick", .4), (35.7, "tick", .4), (37.2, "tick", .4), (38.31, "whoosh", .4),
      (41.18, "pop", .5), (43.51, "hit", .7), (45.53, "chime", .6), (49.6, "thud", .5), (50.5, "thud", .5), (51.4, "thud", .5), (52.3, "thud", .5),
      (53.2, "thud", .5), (55.27, "thud", 1.0), (62.93, "pop", .5), (67.3, "pop", .5), (71.76, "hit", .6), (75.04, "pop", .5),
      (86.0, "tick", .6), (86.7, "chime", .8)]

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
                "-ar", "48000", "-shortest", "-movflags", "+faststart", os.path.join(HERE, "crypto-stories-ep10-freeze-chain.mp4")], check=True)
print("done")
