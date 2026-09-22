# Minecraft Lab — ANTICIPATIONS

## Canonical definition
An anticipation is one concrete, traceable pre-delivery scenario/test intended to catch a real user-visible failure before the installable reaches the phone.
It is not a repeated counter and not a marketing number.

## v0.4 mandatory gates
- BP/RP versions and dependency match.
- package structure valid.
- placement item command-visible.
- item explicitly registered in Creative Equipment > Minecarts.
- crafting item catalog independently includes the item.
- item points to the correct vehicle entity.
- no custom atlas dependency is required for the v0.4 item icon.
- Mojang vanilla minecart_normal icon key used.
- localized name exists FR/EN.
- no spawn egg exposed.
- no horse/taming/breeding/jump/inventory components.
- max auto-step <= 0.0625.
- custom driver camera preset exists.
- script module depends on @minecraft/server 2.0.0.
- riding detection uses minecraft:riding.
- camera set on entering and cleared on exit.
- first-person render fallback hides cabin bones that blocked Android view.

## Evidence classes
STATIC_PASS: file/schema/semantic gates passed.
BDS_PASS: official Bedrock Dedicated Server loaded candidate without relevant content errors.
DEVICE_PENDING: visual/touch/camera behavior still requires the real Android client.
