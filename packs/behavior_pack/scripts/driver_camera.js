import { world, system } from "@minecraft/server";

const VEHICLE_ID = "minecraft_lab:vehicle";
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

function applyDrivingView(player) {
  // Use the stable built-in third-person preset. This keeps the camera outside
  // the cabin and avoids requiring experimental custom-camera toggles.
  try {
    player.camera.setCamera("minecraft:third_person");
  } catch {
    try { player.runCommand("camera @s set minecraft:third_person"); } catch {}
  }
  try { player.runCommand("hud @s hide horse_health"); } catch {}
}

function restoreNormalView(player) {
  try {
    player.camera.clear();
  } catch {
    try { player.runCommand("camera @s clear"); } catch {}
  }
  try { player.runCommand("hud @s reset horse_health"); } catch {}
}

system.runInterval(() => {
  const seen = new Set();
  for (const player of world.getAllPlayers()) {
    seen.add(player.id);
    if (riddenVehicle(player)) {
      // Reassert periodically: Android clients can reset perspective during
      // mount/chunk transitions.
      applyDrivingView(player);
      active.add(player.id);
    } else if (active.delete(player.id)) {
      restoreNormalView(player);
    }
  }
  for (const id of [...active]) {
    if (!seen.has(id)) active.delete(id);
  }
}, 10);

world.afterEvents.playerSpawn.subscribe(({ player }) => {
  system.run(() => {
    if (!riddenVehicle(player)) {
      restoreNormalView(player);
      active.delete(player.id);
    }
  });
});
