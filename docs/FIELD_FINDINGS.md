# Field findings — Road Car

## C-008 — steering failure
Observed on Android 1.0.0: vehicle moved but did not truly yaw left/right; lateral input felt like sliding.
1.1.0 response:
- steering now reads Player.inputInfo.getMovementVector();
- left/right input explicitly changes entity yaw via Entity.setRotation();
- reverse steering flips direction like a road car;
- lateral velocity is damped instead of accepted as strafing.

## C-009 — excessive lateral slide
Observed: body direction and motion direction were decoupled.
1.1.0 response:
- ground friction raised to 2.0 using corrected 1.26.20 semantics;
- lateral velocity decomposed from forward velocity and actively damped;
- no sideways movement model is intentionally added.

## C-010 — forced third person rejected
Observed: third person improved visibility but removed the desired in-cabin sensation.
1.1.0 response:
- forced third-person camera removed;
- normal Minecraft perspective is restored on mount;
- driver seat moved forward toward the windscreen to reduce obstruction;
- player remains free to switch perspective normally.

## C-011 — normal car vs 4x4
Decision:
- this product is the ROAD CAR;
- full one-block climbing is removed;
- road car auto-step = 0.5625 block (slabs/small road irregularities);
- a future 4x4 is a separate vehicle class and may use ~1.0-1.25 block auto-step.
