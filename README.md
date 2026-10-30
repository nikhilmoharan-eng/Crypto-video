# Crypto-video

A 1080×1920 kinetic-typography video ("What is FOMO in Crypto?") made entirely with code.
It is styled after the reference: cream background, dashed grid, black petal shapes in the corners, and bold black and grey headlines.
Every frame is drawn with Pillow and piped to ffmpeg, which mixes the voice-over MP3 with sound effects synthesised in `sfx.py` (whooshes, pops, ticks, booms, riser and crash, all made from sine waves and noise).

```bash
pip install pillow numpy         # also needs ffmpeg and the Inter font (fonts-inter)
python3 make_video.py --audio combined.mp3 --script script.json --out output.mp4
python3 make_video.py --audio x --script script.json --preview 3 12 25   # PNG stills
```

- `script.json` lists each scene's start and end time, its text lines (style plus when each word appears), and an optional visual (`bars`, `hourglass`, `crowd`, `pumpdump`, `dots`). The word times match the Hindi voice-over.
- Effects are timed from the same `script.json`. Set their level under the voice with `--sfx-volume` (default 0.35).
- `output.mp4` is the rendered result (37.6 s, 30 fps).
