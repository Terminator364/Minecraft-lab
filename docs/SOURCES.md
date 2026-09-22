# Minecraft Lab — Source Registry

This registry records what was inspected, what was integrated, and why.

## INTEGRATED — RMPlaysMCYT Minecraft Bedrock Vehicle Template
- Source: https://github.com/RMPlaysMCYT/Minecraft-Bedrock-Vehicle-Template
- Author: Ronnel "RMPlaysMCYT" Mitra
- License: MIT
- Integrated in v0.3.0: Simple Car geometry, Simple Car texture, wheel/steering animation definitions, movement animation controller.
- Minecraft Lab changes: custom entity identifier, road-only behavior, no horse jump mechanics, no saddle requirement, no horse inventory, no can_climb component, no spawn egg, custom placer item, reduced auto-step.
- Full MIT license retained at licenses/RMPLAYS_VEHICLE_TEMPLATE_MIT.txt.
- The source project's original behavior was NOT copied because it intentionally uses saddle/horse/jump mechanics that conflict with Minecraft Lab's road-car contract.

## OFFICIAL RUNTIME / VERSION REFERENCES
### Mojang bedrock-samples
- Source: https://github.com/Mojang/bedrock-samples
- Role: canonical Bedrock component/model reference.
- Stable samples observed during the run: v1.26.50.4.
- Preview samples observed during the run: v1.26.60.24-preview.

### Bedrock Dedicated Server
- Source: https://www.minecraft.net/en-us/download/server/bedrock
- Role: official runtime smoke-test oracle.
- Stable BDS tested by CI for this candidate: 1.26.51.1.
- This does not replace final Android rendering/touch testing.

### Microsoft minecraft-samples
- Source: https://github.com/microsoft/minecraft-samples
- License: MIT
- Role: official add-on structure/behavior examples.

## REFERENCE ONLY — MinerYuri/myv
- Source: https://github.com/MinerYuri/myv
- License: GPL-3.0
- Useful findings: current 1.26-era entity patterns, @minecraft/server 2.0 input handling, terrain-corner sampling, pitch/roll concepts and multi-seat patterns.
- No GPL source code copied into v0.3.0. Concepts are retained as research input for independent future implementation.

## REFERENCE / OPTIONAL CONTROL RESEARCH — MCA Master Controller Addon
- Source: CurseForge project "MCA | Master Controller Addon" by zaminationru.
- License: MIT.
- Role: alternative touch/mobile control architecture using inventory control items.
- Not required by v0.3.0.

## COMMUNITY COMPARISON SET — not copied
- Simple Vehicles Addon / RMPlaysMCYT public releases and YouTube tutorials.
- MS-100 Car Addon (CC BY-NC 3.0).
- Vanilla Vehicles (MIT), useful as a negative-control example because its own description reports duplicate UUID and extra-inventory issues.
- Current YouTube vehicle roundups were used for discovery and UX comparison.
- All-Rights-Reserved or unclear-license packs are research/reference only.

## FUTURE CC0 ART POOL — not bundled in v0.3.0
- Kenney Car Kit.
- OpenGameArt Low Poly Vehicles Pack.
- OpenGameArt 3D Vehicles Pack.
- OpenGameArt Cartoon Vehicles Pack 1.
These are fallback sources if we later replace the current MIT Bedrock-ready model.
