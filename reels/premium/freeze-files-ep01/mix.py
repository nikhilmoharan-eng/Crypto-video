"""Mix voice-over + music bed + SFX for Freeze Files EP 01 and mux with the HyperFrames render."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.expanduser("~/explainer-reel/engine"))
import audio as AU

HERE = os.path.dirname(os.path.abspath(__file__))
DUR = 83.3
EV = [(t - 0.05, "whoosh", .4) for t in (8.1, 59.2, 64.8, 75.7)] + [
      (0.9, "hit", .9), (4.31, "pop", .5), (5.35, "pop", .5), (6.54, "pop", .5), (9.6, "riser", .4), (15.35, "chime", .5), (20.3, "pop", .5),
      (25.47, "chime", .5), (32.08, "tick", .4), (35.26, "chime", .5), (38.7, "tick", .3), (39.2, "tick", .3), (39.7, "tick", .3), (41.87, "thud", .8),
      (49.26, "hit", .9), (52.04, "chime", .5), (57.28, "thud", .6), (61.6, "pop", .5), (63.5, "pop", .5), (68.44, "tick", .4), (69.9, "tick", .4),
      (71.3, "tick", .4), (73.73, "chime", .6), (77.71, "chime", .6), (81.7, "tick", .6)]

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
                "-ar", "48000", "-shortest", "-movflags", "+faststart", os.path.join(HERE, "freeze-files-ep01.mp4")], check=True)
print("done")
