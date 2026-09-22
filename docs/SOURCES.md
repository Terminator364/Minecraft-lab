# Minecraft Lab — Source Registry

This registry records what was inspected, what was integrated, and why.

## INTEGRATED — RMPlaysMCYT Minecraft Bedrock Vehicle Template
- Source: https://github.com/RMPlaysMCYT/Minecraft-Bedrock-Vehicle-Template
- Author: Ronnel "RMPlaysMCYT" Mitra
- License: MIT
- Integrated in v0.3.0: Simple Car geometry, Simple Car texture, wheel/steering animation definitions, movement animation controller.
- Minecraft Lab changes: custom entity identifier, road-only behavior, no horse jump mechanics, no saddle requirement, no horse inventory, no can_climb component, no spawn egg, custom placer item, reduced auto-step.
- Full MIT license retained at licenses/RMPLAYS_VEHICLE_TEMPLATE_MIT.txt.

## REFERENCE — Mojang bedrock-samples
- Source: https://github.com/Mojang/bedrock-samples
- Role: canonical version/component reference for current Bedrock.
- Stable reference observed during this run: v1.26.50.4.
- Preview reference observed: v1.26.60.24-preview.
- Not copied wholesale into this project.

## REFERENCE — Microsoft minecraft-samples
- Source: https://github.com/microsoft/minecraft-samples
- License: MIT
- Role: official add-on structure and behavior reference.

## REFERENCE ONLY — MinerYuri/myv
- Source: https://github.com/MinerYuri/myv
- License: GPL-3.0
- Useful findings: modern @minecraft/server 2.0 input handling, terrain-corner sampling, pitch/roll concepts, multi-seat vehicle patterns.
- Not copied into Minecraft Lab v0.3.0 to avoid mixing GPL code into this candidate. Concepts may be reimplemented independently later.

## REFERENCE / OPTIONAL DEPENDENCY RESEARCH — MCA Master Controller Addon
- Source: CurseForge project "MCA | Master Controller Addon" by zaminationru
- License: MIT
- Role: alternative mobile control architecture using inventory/control items.
- Not required by v0.3.0.

## REFERENCE ONLY — community vehicle packs
Examples inspected during the research run include Simple Vehicles, MS-100 Car Addon, Vanilla Vehicles, and current vehicle-add-on showcases on YouTube.
- If a source is All Rights Reserved or lacks a clear reusable license, it is not copied into Minecraft Lab.
- YouTube is used for discovery/behavior comparison; video content is not copied merely because it is publicly viewable.

## ART ASSET POOL — not integrated in v0.3.0
Potential future CC0 sources inspected: Kenney Car Kit and multiple OpenGameArt CC0 low-poly vehicle packs. They are retained as fallback/reference options, not bundled in v0.3.0.
