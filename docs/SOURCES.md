# Minecraft Lab — Source Registry

## Integrated
- RMPlaysMCYT Minecraft Bedrock Vehicle Template — MIT. Geometry/texture/animations reused with attribution.

## Official decisions used in 1.1.0
### Microsoft Control Schemes
- player_relative: left/right rotates; forward/back moves relative to facing.
- player_relative_strafe / locked_player_relative_strafe: left/right strafes.
- built-in camera presets default to locked player relative strafe.
Decision: use custom minecraft:follow_orbit preset with control_scheme=player_relative.

### Microsoft Third Person Camera Preset
- follow_orbit supports radius down to 0.1 and entity/view offsets.
Decision: use radius 0.12 and forward entity offset to approximate cockpit perspective without forcing the ordinary chase camera.

### Microsoft input_ground_controlled
- official rideable WASD/touch ground control component retained.

## Community references
- MinerYuri/myv (GPL-3.0): modern 1.26 car entity also uses minecraft:input_ground_controlled and 1-block auto-step. No GPL code copied.
- Defence: Trooper 4x4: reference-only for specialized off-road class.
- The Typical Prius (MIT): feature benchmark only; no files imported in this run.
