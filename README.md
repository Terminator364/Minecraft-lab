# Minecraft Lab — Road Car 1.1.0

This build directly addresses the Android field failure where the car moved but did not actually steer.

## Driving model
- Bedrock-native ground propulsion/collision remains active.
- Touch left/right explicitly changes vehicle body yaw.
- Sideways velocity is damped so steering is not strafing.
- Reverse steering flips naturally.
- Ground friction = 2.0 using corrected 1.26.20 semantics.

## View
- Forced third-person has been removed.
- Mounting restores normal Minecraft camera behavior.
- Driver seat is moved toward the windscreen to improve the in-cabin view.
- The player may use normal perspective switching.

## Terrain
This is now explicitly a ROAD CAR:
- slabs/small road irregularities: target;
- full one-block climbing: not target.
A 4x4 will be a separate vehicle class.

User-facing installable:
MinecraftLab-RoadCar-1.1.0.mcaddon
