"""Overlay the HyperFrames hero clips (alpha MOV) onto the engine render and add their sound effects."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import audio as AU

BASE, MIX = "freeze2_base.mp4", "freeze2_base_work/mix.wav"
HF = sys.argv[1] if len(sys.argv) > 1 else "."
H1, H2, T1, T2 = os.path.join(HF, "heroC.mov"), os.path.join(HF, "heroD.mov"), 0.35, 26.47
OUT = "freeze-part2.mp4"

ev = []
h1 = [(0.0, "whoosh", .5), (0.3, "riser", .4), (0.6, "hit", 1.0), (0.85, "thud", .5), (1.48, "chime", .7), (2.6, "whoosh", .3),
      (3.6, "pop", .6), (3.78, "pop", .6), (3.96, "pop", .6)]
h2 = [(0.0, "hit", .7), (0.95, "whoosh", .4), (1.4, "pop", .4), (2.24, "whoosh", .45), (2.3, "pop", .5), (3.55, "whoosh", .45), (3.6, "pop", .5),
      (4.76, "whoosh", .45), (4.82, "pop", .5), (5.3, "whoosh", .3), (5.6, "thud", .8), (5.62, "chime", .5)]
ev += [(T1 + t, k, g) for t, k, g in h1] + [(T2 + t, k, g) for t, k, g in h2]
y, sr = sf.read(MIX, dtype="float32")
mono = y.mean(1) if y.ndim > 1 else y
fx = np.zeros(len(mono) + sr, np.float32)
rng = np.random.default_rng(9)
for t, k, g in ev:
    AU.place(fx, AU.sfx(k, rng), t, g)
out = mono + fx[:len(mono)] * 0.55
out = out / (np.abs(out).max() + 1e-9) * 0.89
sf.write("freeze2_mix_fx.wav", np.stack([out, out], 1), sr)

subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", BASE, "-i", H1, "-i", H2, "-i", "freeze2_mix_fx.wav",
    "-filter_complex",
    f"[1:v]format=yuva420p,setpts=PTS+{T1}/TB[a];[2:v]format=yuva420p,setpts=PTS+{T2}/TB[b];"
    "[0:v][a]overlay=0:0:eof_action=pass:format=auto[v1];[v1][b]overlay=0:0:eof_action=pass:format=auto,format=yuv420p[v]",
    "-map", "[v]", "-map", "3:a", "-c:v", "libx264", "-preset", "medium", "-crf", "17",
    "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    "-shortest", "-movflags", "+faststart", OUT], check=True)
print("done:", OUT)
