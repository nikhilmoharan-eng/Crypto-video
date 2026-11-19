"""Mix voice-over + music bed + SFX for Crypto Stories EP 07 and mux with the HyperFrames render."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.expanduser("~/explainer-reel/engine"))
import audio as AU

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 63.4
EV = [(t - 0.05, "whoosh", .4) for t in (7.6, 19.3, 23.2, 33.8, 44.1, 53.4, 58.8)] + [
      (0.0, "pop", .5), (1.41, "pop", .5), (4.71, "riser", .6), (5.9, "thud", 1.0), (10.5, "hit", .9), (12.3, "riser", .5), (17.51, "pop", .4),
      (20.84, "tick", .5), (21.5, "thud", .8), (25.71, "pop", .4), (26.91, "riser", .5), (31.41, "tick", .4), (32.2, "chime", .5),
      (36.78, "hit", 1.0), (38.62, "pop", .5), (40.03, "pop", .5), (42.4, "pop", .5), (45.5, "riser", .6), (48.12, "chime", .6),
      (51.6, "thud", .9), (54.79, "pop", .5), (56.69, "pop", .5), (62.03, "tick", .6), (62.55, "chime", .8)]

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
                "-ar", "48000", "-shortest", "-movflags", "+faststart", os.path.join(HERE, "crypto-stories-ep07-bitfinex.mp4")], check=True)
print("done")
