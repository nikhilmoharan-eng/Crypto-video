# EP 3: Seed Phrase Scam (@niks.crypto)

`seed-phrase-scam.mp4`: 1080×1920, 30 fps, 58 s, −14 LUFS. It uses a red and violet palette,
with "CRYPTO.DECODED · EP 3" in the header.

- `voiceover.mp3`: the ElevenLabs voice-over (Shrey).
- `build_seed.py`: cuts the voice-over into one clip per caption beat and writes `episode.json`.
- `cover_1080x1920.png` / `cover_grid_1080x1440.png`: the cover, made from `cover_src/cover.html`
  (run `python3 cover_src/render_cover.py`).

```bash
python3 build_seed.py
python3 <engine>/render.py episode.json -o seed-phrase-scam.mp4   # Explainer Reel Engine (see ../india-crypto-paradox/render_patched.py)
```
