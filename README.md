# Minecraft Lab — Road Car

Current candidate: **v0.4.0**

This build is driven directly by Android field findings from v0.3.0.

## v0.4 fixes
- Creative inventory: explicit Items > Minecarts registration plus crafting item catalog.
- Hotbar icon: Mojang's proven vanilla minecart_normal icon replaces the unreliable custom icon path.
- Camera: dedicated follow-orbit driver camera applied automatically while riding and cleared after dismount.
- First-person fallback: large cabin/body bones hidden when the render context reports first-person.
- No-cheat normal path: Creative inventory -> Voiture Minecraft Lab -> place -> drive.
- Two direct install files are produced because Android may treat .mcaddon as an archive.

## Install order on Android
1. 01-MinecraftLab-RoadCar-RP-v0.4.0.mcpack
2. 02-MinecraftLab-RoadCar-BP-v0.4.0.mcpack

Then activate the BP in the world. The RP is the linked dependency.

See docs/FIELD_FINDINGS.md, docs/ANTICIPATIONS.md and docs/SOURCES.md.
