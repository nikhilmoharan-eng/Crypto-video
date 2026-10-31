# India's Crypto Paradox — @niks.crypto reel

`india-crypto-paradox.mp4`: 1080×1920, 30 fps, 133 s, −14 LUFS.

The voice-over is the ElevenLabs recording, with three fixes (`voiceover_fixed.flac`):
- the "apnaane mein" phrase is replaced with the re-recorded patch clip, sped up 1.2× to match the sentence pace and level-matched;
- the read-aloud stage direction "Concept detected. Crypto paradox." (about 27–29 s) is removed;
- the read-aloud heading "CTA" before the share line is removed.

`build_paradox.py` cuts the voice-over into one clip per caption beat and writes `episode.json`.
That file is rendered with the Explainer Reel Engine (`render.py`). `render_patched.py` is the engine's
render script with one addition: the outro can use a recorded clip (`"outro": {"audio": ...}`).

```bash
python3 build_paradox.py
python3 <engine>/render.py episode.json -o india-crypto-paradox.mp4
```
