# Minecraft Lab — Road Car

Current candidate: **v0.3.0**

This version replaces the hand-built block prototype with a proven Bedrock-ready car model/animation base from RMPlaysMCYT's MIT-licensed Vehicle Template, while deliberately replacing its horse/saddle behavior with Minecraft Lab's road-focused behavior.

## Design goals
- Looks like a car, not a generic rideable mob.
- Dedicated placement item, no generic spawn egg.
- No horse jump, saddle, taming, breeding, climbing or horse inventory mechanics.
- Maximum automatic step: 0.0625 block (one Minecraft pixel).
- Driver + one passenger.
- Moving wheels / steering animation definitions.
- French/English drive prompt.

## Install
Use only the candidate placed in Google Drive:
`Minecraft / À installer / MinecraftLab-RoadCar-v0.3.0.mcaddon`

## Test on phone
Physical Android test is intentionally small:
1. import;
2. activate the pack;
3. place the car;
4. mount it;
5. drive on flat ground;
6. attempt a slab/full-block obstacle;
7. report visual/touch/camera issues.

See `docs/SOURCES.md`, `docs/ANTICIPATIONS.md` and `THIRD_PARTY_NOTICES.md`.
