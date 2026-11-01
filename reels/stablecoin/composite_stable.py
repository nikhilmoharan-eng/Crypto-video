"""Overlay the HyperFrames hero clips (alpha MOV) onto the engine render and add their sound effects."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import audio as AU

BASE, MIX = "stable_base.mp4", "stable_base_work/mix.wav"
HF = sys.argv[1] if len(sys.argv) > 1 else "."
H1, H2, T1, T2 = os.path.join(HF, "heroA.mov"), os.path.join(HF, "heroB.mov"), 0.35, 29.72
OUT = "stablecoin.mp4"

ev = []
h1 = [(0.0, "whoosh", .5), (0.15, "riser", .35), (1.2, "pop", .6), (2.15, "whoosh", .4), (2.35, "tick", .5), (3.95, "pop", .8),
      (4.6, "pop", .7), (4.95, "tick", .5), (5.2, "tick", .5)]
h2 = [(0.0, "whoosh", .5), (1.6, "riser", .7), (2.05, "thud", .7), (2.15, "hit", .9), (2.85, "whoosh", .4), (3.05, "tick", .4),
      (4.65, "pop", .4), (5.2, "riser", .8), (6.35, "hit", 1.0), (6.42, "thud", .6), (6.8, "chime", .35)]
ev += [(T1 + t, k, g) for t, k, g in h1] + [(T2 + t, k, g) for t, k, g in h2]
y, sr = sf.read(MIX, dtype="float32")
mono = y.mean(1) if y.ndim > 1 else y
fx = np.zeros(len(mono) + sr, np.float32)
rng = np.random.default_rng(9)
for t, k, g in ev:
    AU.place(fx, AU.sfx(k, rng), t, g)
out = mono + fx[:len(mono)] * 0.55
out = out / (np.abs(out).max() + 1e-9) * 0.89
sf.write("stable_mix_fx.wav", np.stack([out, out], 1), sr)

subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", BASE, "-i", H1, "-i", H2, "-i", "stable_mix_fx.wav",
    "-filter_complex",
    f"[1:v]format=yuva420p,setpts=PTS+{T1}/TB[a];[2:v]format=yuva420p,setpts=PTS+{T2}/TB[b];"
    "[0:v][a]overlay=0:0:eof_action=pass:format=auto[v1];[v1][b]overlay=0:0:eof_action=pass:format=auto,format=yuv420p[v]",
    "-map", "[v]", "-map", "3:a", "-c:v", "libx264", "-preset", "medium", "-crf", "17",
    "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    "-shortest", "-movflags", "+faststart", OUT], check=True)
print("done:", OUT)
