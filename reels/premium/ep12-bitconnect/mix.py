"""Mix voice-over + music bed + SFX for Crypto Stories EP 12 and mux with the HyperFrames render."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.expanduser("~/explainer-reel/engine"))
import audio as AU

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 92.2
EV = [(t - 0.05, "whoosh", .4) for t in (11.8, 19.8, 31.8, 41.6, 50.3, 62.2, 72.3, 80.7, 86.2)] + [
      (2.0, "hit", .8), (3.6, "riser", .4), (7.2, "whoosh", .4), (9.81, "thud", 1.0), (15.16, "chime", .5), (17.6, "pop", .5), (24.6, "pop", .5),
      (29.0, "riser", .6), (32.3, "tick", .4), (33.5, "tick", .4), (34.7, "tick", .4), (35.9, "tick", .4), (39.2, "riser", .5), (44.62, "pop", .5),
      (48.4, "hit", .9), (55.9, "whoosh", .4), (56.8, "pop", .5), (57.7, "tick", .5), (58.2, "pop", .5), (60.46, "thud", 1.0),
      (64.35, "pop", .6), (68.95, "riser", .4), (70.3, "thud", 1.0), (74.8, "hit", .6), (79.0, "thud", .9), (82.18, "pop", .5), (83.67, "pop", .5),
      (90.63, "tick", .6), (91.2, "chime", .8)]

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
                "-ar", "48000", "-shortest", "-movflags", "+faststart", os.path.join(HERE, "crypto-stories-ep12-bitconnect.mp4")], check=True)
print("done")
