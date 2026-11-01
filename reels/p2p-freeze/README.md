# EP 5: Crypto Becha… Account Freeze! (@niks.crypto)

`p2p-freeze.mp4`: 1080×1920, 30 fps, 59 s, −14 LUFS, cyan palette, with "CRYPTO.DECODED · EP 5" in the header.

Two tools build this episode:

1. **Hinglish explainer engine.** `build_freeze.py` cuts `voiceover.mp3` into one clip per caption beat and writes `episode.json`.
   The engine renders the base video: captions, chips, header, mascot, cards, music bed and SFX. The two hero scenes are left with an empty stage.
2. **HyperFrames** (`hyperframes/hero1`, `hyperframes/hero2`). Two GSAP compositions render as transparent ProRes 4444:
   - hero1 (0.35 s): P2P sell → UPI credit → "3 din baad" → frosted ACCOUNT FROZEN;
   - hero2 (24.51 s): victim → cyber complaint → police trace → money trail → freeze chain.
3. `composite_freeze.py` overlays both onto the base render and adds SFX for their actions.

```bash
python3 build_freeze.py
python3 <engine>/render.py episode.json -o p2p-freeze_base.mp4
(cd hyperframes/hero1 && npx hyperframes render --format mov -o ../../hero1.mov)
(cd hyperframes/hero2 && npx hyperframes render --format mov -o ../../hero2.mov)
python3 composite_freeze.py .
```
The hero times are tied to the engine timeline. If the beats change, update the offsets in `composite_freeze.py` and the local times in the hero `index.html` files.
