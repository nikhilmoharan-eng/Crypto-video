"""Mix voice-over + music bed + SFX for Crypto Stories EP 09 and mux with the HyperFrames render."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.expanduser("~/explainer-reel/engine"))
import audio as AU

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 78.2
EV = [(t - 0.05, "whoosh", .4) for t in (6.9, 11.6, 17.7, 21.6, 29.9, 35.9, 44.8, 52.5, 61.3, 67.9, 73.4)] + [
      (0.2, "riser", .4), (3.58, "hit", .8), (5.4, "thud", 1.0), (17.87, "tick", .5), (20.11, "pop", .6), (23.6, "riser", .5),
      (26.5, "tick", .3), (27.86, "chime", .5), (33.4, "tick", .4), (38.1, "pop", .4), (38.7, "pop", .4), (39.3, "pop", .4),
      (41.4, "riser", .4), (43.33, "hit", .8), (45.23, "hit", .7), (47.9, "riser", .6), (53.9, "riser", .6), (56.8, "hit", .8),
      (58.5, "thud", 1.0), (63.63, "tick", .5), (64.8, "pop", .5), (66.01, "thud", .9), (69.81, "pop", .4), (71.1, "hit", .6),
      (76.7, "tick", .6), (77.25, "chime", .8)]

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
                "-ar", "48000", "-shortest", "-movflags", "+faststart", os.path.join(HERE, "crypto-stories-ep09-luna.mp4")], check=True)
print("done")
