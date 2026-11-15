"""Mix voice-over + music bed + SFX for Case 01 and mux with the HyperFrames render."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.expanduser("~/explainer-reel/engine"))
import audio as AU

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 74.4
EV = [(t - 0.05, "whoosh", .4) for t in (8.0, 19.8, 28.4, 37.0, 44.6, 50.6, 59.4, 68.6)] + [
      (0.4, "riser", .3), (3.3, "pop", .5), (6.15, "chime", .5), (13.3, "whoosh", .5), (13.85, "tick", .4), (14.35, "tick", .4), (14.85, "tick", .4),
      (15.35, "tick", .4), (15.85, "tick", .4), (18.2, "pop", .7), (23.4, "riser", .5), (31.6, "tick", .3), (32.6, "tick", .3), (34.9, "pop", .4),
      (39.9, "hit", .9), (42.3, "thud", .7), (46.6, "riser", .6), (49.65, "thud", 1.0), (49.7, "hit", .8), (56.6, "tick", .5), (58.0, "chime", .6),
      (61.2, "pop", .5), (63.1, "pop", .5), (66.9, "thud", .8), (72.7, "tick", .6), (73.4, "chime", .8)]

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
                "-ar", "48000", "-shortest", "-movflags", "+faststart", os.path.join(HERE, "crypto-stories-ep03-mt-gox.mp4")], check=True)
print("done")
