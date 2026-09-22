import { world, system } from "@minecraft/server";

const VEHICLE_ID = "minecraft_lab:vehicle";
const CAMERA_ID = "minecraft_lab:cockpit_drive";
const active = new Set();

function riddenVehicle(player) {
  try {
    const riding = player.getComponent("minecraft:riding");
    const entity = riding?.entityRidingOn;
    return entity?.typeId === VEHICLE_ID ? entity : undefined;
  } catch {
    return undefined;
  }
}

function applyCockpit(player) {
  // Near-zero follow-orbit gives a cockpit-like viewpoint while the
  // player_relative control scheme maps left/right to steering, not strafing.
  try {
    player.camera.setCamera(CAMERA_ID);
  } catch {
    try { player.runCommand("camera @s set minecraft:follow_orbit"); } catch {}
  }

  // Explicit fallback for clients that ignore the camera preset's scheme.
  try { player.runCommand("controlscheme @s set player_relative"); } catch {}
  try { player.runCommand("hud @s hide horse_health"); } catch {}
}

function restorePlayer(player) {
  try { player.camera.clear(); } catch {
    try { player.runCommand("camera @s clear"); } catch {}
  }
  try { player.runCommand("controlscheme @s clear"); } catch {}
  try { player.runCommand("hud @s reset horse_health"); } catch {}
}

system.runInterval(() => {
  const seen = new Set();

  for (const player of world.getAllPlayers()) {
    seen.add(player.id);
    if (riddenVehicle(player)) {
      if (!active.has(player.id)) {
        applyCockpit(player);
        active.add(player.id);
      }
    } else if (active.delete(player.id)) {
      restorePlayer(player);
    }
  }

  for (const id of [...active]) {
    if (!seen.has(id)) active.delete(id);
  }
}, 4);

world.afterEvents.playerSpawn.subscribe(({ player }) => {
  system.run(() => {
    if (!riddenVehicle(player)) {
      restorePlayer(player);
      active.delete(player.id);
    }
  });
});
