# Field findings — Vehicle

## F-004 — icon invisible on Android
Observed on v0.3/v0.4: item registration worked, but the icon was blank.
Cause class: item icon key existed in behavior data without a guaranteed resource-pack texture mapping.
v0.5 correction:
- dedicated 64x64 PNG with transparency;
- explicit resource-pack textures/item_texture.json mapping;
- item uses the mapped key minecraft_lab_4x4_icon;
- CI validates PNG dimensions, alpha/non-empty pixels, mapping and key equality.

## F-005 — driver view obstructed
Observed on v0.3/v0.4: rider remained visually trapped inside the cabin; v0.4 camera strategy did not prove effective on device.
v0.5 correction:
- built-in minecraft:third_person is forced while riding;
- camera is reasserted every 10 ticks instead of only once;
- command fallback exists if Script Camera setCamera fails;
- camera clears on dismount/spawn recovery;
- driver seat raised from 0.55 to 1.10 blocks as a physical fallback.

## F-006 — road car cannot traverse Minecraft terrain
Observed: 0.0625-block auto-step made ordinary terrain unusable.
Requirement changed: this candidate is an OFF-ROAD 4x4.
v0.5 correction:
- controlled auto-step 1.25 blocks;
- one-block ledges and block-by-block mounds are within policy;
- a vertical two-block wall remains out of policy (not treated as a realistic mound).

## F-007 — installation UX
Observed: one-click .mcaddon is the only accepted delivery path.
Status: retained as mandatory release gate.
