# EP 4: Bitcoin Sirf 21 Million Kyun? (@niks.crypto)

`bitcoin-21-million.mp4`: 1080×1920, 30 fps, 59 s, −14 LUFS, Bitcoin-orange palette,
with "CRYPTO.DECODED · EP 4" in the header. Supply figures are as of October 2026 (about 20M+ mined, ~96%).

- `voiceover.mp3`: the ElevenLabs voice-over (Shrey).
- `build_btc.py`: cuts the voice-over into one clip per caption beat and writes `episode.json`.
- `cover_1080x1920.png` / `cover_grid_1080x1440.png`: the cover, made from `cover_src/cover.html`.

```bash
python3 build_btc.py
python3 <engine>/render.py episode.json -o bitcoin-21-million.mp4
```
