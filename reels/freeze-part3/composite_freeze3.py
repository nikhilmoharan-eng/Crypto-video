"""EP 8: overlay three HyperFrames heroes on the engine render, add their SFX."""
import subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import audio as AU

BASE, MIX, OUT = "freeze3_base.mp4", "freeze3_base_work/mix.wav", "freeze-part3.mp4"
HF = sys.argv[1] if len(sys.argv) > 1 else "."
HEROES = [("heroE.mov", 0.35), ("heroF.mov", 7.96), ("heroG.mov", 27.05)]
SFX = {
    0.35: [(0.0, "whoosh", .5), (0.3, "riser", .5), (1.3, "thud", .6), (2.25, "pop", .6), (2.39, "pop", .6), (2.53, "pop", .6), (2.67, "pop", .6), (2.81, "pop", .6)],
    7.96: [(0.0, "hit", .7), (1.0, "whoosh", .45), (2.3, "whoosh", .45), (3.6, "pop", .7), (4.4, "thud", 1.0), (4.6, "thud", .5)],
    27.05: [(0.0, "hit", .7), (1.0, "whoosh", .4), (2.0, "pop", .4), (2.12, "pop", .4), (2.24, "pop", .4), (2.36, "pop", .4), (2.48, "pop", .4),
            (2.5, "tick", .5), (2.9, "riser", .6), (3.95, "thud", 1.0)],
}
y, sr = sf.read(MIX, dtype="float32")
mono = y.mean(1) if y.ndim > 1 else y
fx = np.zeros(len(mono) + sr, np.float32); rng = np.random.default_rng(11)
for T, evs in SFX.items():
    for t, k, g in evs: AU.place(fx, AU.sfx(k, rng), T + t, g)
out = mono + fx[:len(mono)] * 0.55
out = out / (np.abs(out).max() + 1e-9) * 0.89
sf.write("freeze3_mix_fx.wav", np.stack([out, out], 1), sr)
args = ["ffmpeg", "-v", "error", "-y", "-i", BASE] + sum([["-i", os.path.join(HF, h)] for h, _ in HEROES], []) + ["-i", "freeze3_mix_fx.wav"]
fc, prev = [], "0:v"
for i, (_, t) in enumerate(HEROES, 1):
    fc.append(f"[{i}:v]format=yuva420p,setpts=PTS+{t}/TB[h{i}]")
    fc.append(f"[{prev}][h{i}]overlay=0:0:eof_action=pass:format=auto[v{i}]"); prev = f"v{i}"
fc.append(f"[{prev}]format=yuv420p[v]")
args += ["-filter_complex", ";".join(fc), "-map", "[v]", "-map", f"{len(HEROES)+1}:a", "-c:v", "libx264", "-preset", "medium", "-crf", "17",
         "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-shortest", "-movflags", "+faststart", OUT]
subprocess.run(args, check=True); print("done:", OUT)
