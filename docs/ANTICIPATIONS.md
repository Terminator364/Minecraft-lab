# Minecraft Lab — ANTICIPATIONS

An anticipation is one concrete, traceable pre-delivery scenario/test intended to catch a real user-visible failure.

## v0.5 gates
### Icon
- custom icon key exists in item definition;
- same key exists in item_texture.json;
- mapped PNG exists;
- PNG is exactly 64x64 RGBA;
- meaningful opaque pixel count > 10%;
- transparent background exists;
- mutated missing/wrong icon key must fail.

### Camera
- riding detection uses minecraft:riding;
- third-person camera is applied while riding;
- camera is reasserted periodically;
- command fallback exists;
- camera clears on dismount;
- driver seat Y >= 1.0 as a physical visibility fallback.

### 4x4
- controlled auto-step between 1.0 and 1.25 blocks;
- one-block ledge is policy PASS;
- slabs/snow/rough block-by-block mound are PASS;
- vertical 2-block wall is policy FAIL;
- no horse/taming/jump mechanics are introduced.

### Delivery
- one-click mcaddon exists and contains BP+RP;
- old versions do not remain in À installer.
