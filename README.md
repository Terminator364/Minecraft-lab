# Minecraft Lab

Prototype 0.2.0: road-focused vehicle for Minecraft Bedrock/mobile.

## What changed
- Replaced the blocky v0.1 body with a car-shaped model with four wheels, glass, lights, bumpers and roof.
- Removed the automatic spawn egg from Creative inventory.
- Added a dedicated **Véhicule Minecraft Lab** item that places the vehicle.
- Reduced automatic step height to 0.05 blocks so the vehicle no longer climbs half-block terrain like a mount.
- Slower turning and road-oriented movement.
- Uses Minecraft's built-in localized mount prompt.

## Test
1. Import `MinecraftLab-Vehicle-v0.2.0.mcaddon`.
2. Activate **Minecraft Lab Vehicle BP** in a Creative world.
3. Search Creative inventory for **Véhicule Minecraft Lab**.
4. Use the item on a flat surface.
5. Mount it and test it on a flat road, slabs/steps, grass and a full block obstacle.

Fallback command:
`/summon minecraft_lab:vehicle`
