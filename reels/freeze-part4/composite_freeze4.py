"""EP 9: overlay three HyperFrames heroes on the engine render, add their SFX."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import audio as AU

BASE, MIX, OUT = "freeze4_base.mp4", "freeze4_base_work/mix.wav", "freeze-part4.mp4"
HF = sys.argv[1] if len(sys.argv) > 1 else "."
HEROES = [("heroH.mov", 0.35), ("heroI.mov", 8.5), ("heroJ.mov", 32.78)]
SFX = {
    0.35: [(0.0, "pop", .6), (0.35, "pop", .6), (1.0, "whoosh", .4), (1.15, "whoosh", .4), (1.55, "whoosh", .4), (2.7, "riser", .4), (2.9, "pop", .7), (3.1, "chime", .7)],
    8.5: [(0.0, "hit", .6), (1.0, "pop", .6), (3.15, "whoosh", .4), (3.9, "tick", .5), (4.8, "whoosh", .4), (5.55, "tick", .5), (6.1, "chime", .6),
          (7.35, "whoosh", .4), (7.75, "thud", .7), (8.2, "pop", .7)],
    32.78: [(0.0, "hit", .6), (0.85, "whoosh", .4), (1.75, "whoosh", .4), (2.1, "pop", .5), (3.4, "riser", .4), (3.6, "thud", .9), (4.45, "chime", .7)],
}
y, sr = sf.read(MIX, dtype="float32")
mono = y.mean(1) if y.ndim > 1 else y
fx = np.zeros(len(mono) + sr, np.float32); rng = np.random.default_rng(11)
for T, evs in SFX.items():
    for t, k, g in evs: AU.place(fx, AU.sfx(k, rng), T + t, g)
out = mono + fx[:len(mono)] * 0.55
out = out / (np.abs(out).max() + 1e-9) * 0.89
sf.write("freeze4_mix_fx.wav", np.stack([out, out], 1), sr)
args = ["ffmpeg", "-v", "error", "-y", "-i", BASE] + sum([["-i", os.path.join(HF, h)] for h, _ in HEROES], []) + ["-i", "freeze4_mix_fx.wav"]
fc, prev = [], "0:v"
for i, (_, t) in enumerate(HEROES, 1):
    fc.append(f"[{i}:v]format=yuva420p,setpts=PTS+{t}/TB[h{i}]")
    fc.append(f"[{prev}][h{i}]overlay=0:0:eof_action=pass:format=auto[v{i}]"); prev = f"v{i}"
fc.append(f"[{prev}]format=yuv420p[v]")
args += ["-filter_complex", ";".join(fc), "-map", "[v]", "-map", f"{len(HEROES)+1}:a", "-c:v", "libx264", "-preset", "medium", "-crf", "17",
         "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-shortest", "-movflags", "+faststart", OUT]
subprocess.run(args, check=True); print("done:", OUT)
