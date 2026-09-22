# Field findings — Road Car

## F-001 — v0.1 generic mount UX
Observed: prototype looked and behaved too much like a horse/mount.
Status: FIXED structurally by removing horse/taming/jump/inventory components.

## F-002 — road-only requirement
Observed: vehicle must not climb normal Minecraft steps like a horse.
Status: GUARDED by max auto-step <= 0.0625 block.

## F-003 — creative inventory discoverability
Observed on Android v0.3.0: /give succeeds, but searching "voiture" in Creative inventory does not reliably surface the item.
v0.4 response:
- item format 1.21.60;
- explicit Equipment category;
- explicit vanilla Minecart group;
- explicit crafting item catalog entry;
- command visibility explicitly enabled.

## F-004 — hotbar icon readability
Observed on Android v0.3.0: slot is occupied but item icon is effectively unreadable/invisible.
v0.4 response:
- stop depending on the custom item-atlas sprite for this gate;
- use Mojang's existing vanilla minecart_normal icon key as the reliable icon.
This is intentionally conservative: first make the item unmistakably visible, then replace the icon only after a proven render gate exists.

## F-005 — cockpit/camera obstruction
Observed on Android v0.3.0: first-person rider camera is buried inside vehicle geometry and exterior visibility is poor.
v0.4 response:
- script-driven dedicated third-person/follow-orbit camera while riding;
- camera clears automatically on dismount/spawn recovery;
- render-controller fallback hides major cabin bones in first-person rendering;
- horse-health HUD hide is attempted as a cosmetic improvement but is non-critical.

## Runtime truth
These changes can be statically validated and partially loaded in BDS, but final Android camera feel and Creative UI rendering remain device/client gates. They must not be reported as runtime-proven until physically observed.
