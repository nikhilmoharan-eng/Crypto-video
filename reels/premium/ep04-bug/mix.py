"""Mix voice-over + music bed + SFX for Crypto Stories EP 04 and mux with the HyperFrames render."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.expanduser("~/explainer-reel/engine"))
import audio as AU

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 66.4
EV = [(t - 0.05, "whoosh", .4) for t in (11.7, 21.7, 34.2, 38.3, 47.0, 53.3, 61.2)] + [
      (0.4, "riser", .3), (6.9, "hit", .7), (8.67, "riser", .6), (10.4, "thud", 1.0), (11.9, "whoosh", .4), (14.4, "pop", .4), (18.6, "riser", .5),
      (23.75, "pop", .7), (25.95, "riser", .5), (29.98, "hit", .9), (32.97, "thud", 1.0), (34.5, "tick", .5), (35.0, "tick", .5), (35.5, "tick", .5),
      (36.7, "thud", .8), (39.5, "pop", .5), (45.4, "tick", .6), (48.6, "hit", .8), (50.2, "thud", .7), (51.55, "pop", .5),
      (54.7, "pop", .5), (57.0, "pop", .5), (59.6, "thud", .8), (64.75, "tick", .6), (65.4, "chime", .8)]

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
                "-ar", "48000", "-shortest", "-movflags", "+faststart", os.path.join(HERE, "crypto-stories-ep04-bug.mp4")], check=True)
print("done")
