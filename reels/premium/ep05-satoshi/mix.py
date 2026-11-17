"""Mix voice-over + music bed + SFX for Crypto Stories EP 05 and mux with the HyperFrames render."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.expanduser("~/explainer-reel/engine"))
import audio as AU

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 67.8
EV = [(t - 0.05, "whoosh", .4) for t in (6.7, 13.4, 22.6, 28.2, 34.7, 39.6, 49.9, 54.6, 61.9)] + [
      (0.4, "riser", .3), (4.6, "tick", .5), (7.65, "tick", .5), (11.64, "pop", .6), (17.75, "whoosh", .6), (19.2, "chime", .5),
      (23.04, "pop", .5), (25.27, "pop", .5), (26.74, "pop", .5), (32.3, "tick", .5), (36.6, "riser", .4), (38.0, "thud", 1.0),
      (43.6, "riser", .6), (47.93, "chime", .6), (50.5, "tick", .5), (52.9, "thud", .9), (55.04, "pop", .5), (56.61, "pop", .5),
      (58.03, "pop", .5), (60.27, "hit", .8), (66.24, "tick", .6), (66.9, "chime", .8)]

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
                "-ar", "48000", "-shortest", "-movflags", "+faststart", os.path.join(HERE, "crypto-stories-ep05-satoshi.mp4")], check=True)
print("done")
