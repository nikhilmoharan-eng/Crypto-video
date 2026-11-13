"""Mix voice-over + music bed + SFX for Case 01 and mux with the HyperFrames render."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.expanduser("~/explainer-reel/engine"))
import audio as AU

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 59.2
EV = [(t - 0.05, "whoosh", .4) for t in (6.2, 9.9, 12.9, 20.1, 27.1, 34.7, 40.0, 47.5, 54.1)] + [
      (0.3, "pop", .5), (4.64, "pop", .5), (4.82, "pop", .5), (7.76, "riser", .35), (8.9, "chime", .5), (9.0, "thud", .7), (11.4, "tick", .4),
      (13.4, "tick", .4), (15.5, "pop", .5), (17.5, "pop", .5), (24.7, "pop", .6), (29.3, "pop", .5), (29.5, "pop", .5), (32.2, "thud", .8),
      (35.4, "riser", .5), (37.6, "chime", .6), (41.1, "pop", .4), (44.3, "pop", .5), (52.2, "chime", .7), (57.0, "tick", .5), (57.3, "tick", .5),
      (57.6, "tick", .5), (58.1, "pop", .6)]

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
                "-ar", "48000", "-shortest", "-movflags", "+faststart", os.path.join(HERE, "crypto-stories-ep01-pizza-v2.mp4")], check=True)
print("done")
