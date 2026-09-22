# Minecraft Lab — Sources / decisions

## REUSE — RMPlaysMCYT Minecraft Bedrock Vehicle Template
- MIT.
- Reused geometry, texture, wheel/steering animations.
- Original horse/saddle behavior is NOT reused.

## ADAPT — official Microsoft Bedrock APIs
- InputInfo.getMovementVector(): current touch/controller/keyboard movement vector.
- Entity.setRotation(): explicit body yaw steering.
- Entity.getVelocity()/applyImpulse(): anti-slip correction.
- minecraft:friction_modifier: in format >=1.26.20, higher values correctly increase ground friction.
- minecraft:input_ground_controlled: retained for Bedrock-native propulsion/collision.
- minecraft:variable_max_auto_step: road-car limit 0.5625.

## REFERENCE_ONLY — MinerYuri/myv
- GPL-3.0.
- Inspected for current 1.26-era use of Player.inputInfo and vehicle terrain concepts.
- No GPL source code copied. Minecraft Lab steering implementation is independently written from Microsoft API contracts.

## REFERENCE_ONLY — Defence: Trooper 4x4
- Current 26.x community benchmark for rough-terrain + dedicated vehicle camera.
- No compatible reuse licence established in this run; no files copied.

## BENCHMARK — The Typical Prius by rbmasterchief
- CurseForge lists MIT.
- Current 26.40-era vehicle with modeled interior, animations and four-passenger capacity.
- Used as a functional benchmark; files not imported in this run.

## Product split
- Road Car = current 1.1.0, road/slab behavior.
- 4x4 = separate future vehicle class; do not make normal cars climb full blocks.
