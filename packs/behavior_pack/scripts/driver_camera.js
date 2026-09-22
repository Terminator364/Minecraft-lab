import { world, system } from "@minecraft/server";

const VEHICLE_ID = "minecraft_lab:vehicle";
const active = new Set();

function vehicleFor(player) {
  try {
    const riding = player.getComponent("minecraft:riding");
    const entity = riding?.entityRidingOn;
    return entity?.typeId === VEHICLE_ID ? entity : undefined;
  } catch {
    return undefined;
  }
}

function forceDriverCamera(player) {
  try {
    player.camera.setCamera("minecraft:third_person");
  } catch {
    try { player.runCommand("camera @s set minecraft:third_person"); } catch {}
  }
  try { player.runCommand("hud @s hide horse_health"); } catch {}
}

function restoreCamera(player) {
  try { player.camera.clear(); } catch {
    try { player.runCommand("camera @s clear"); } catch {}
  }
  try { player.runCommand("hud @s reset horse_health"); } catch {}
}

system.runInterval(() => {
  const seen = new Set();
  for (const player of world.getAllPlayers()) {
    seen.add(player.id);
    if (vehicleFor(player)) {
      forceDriverCamera(player); // reassert; do not rely on one transition event
      active.add(player.id);
    } else if (active.delete(player.id)) {
      restoreCamera(player);
    }
  }
  for (const id of [...active]) {
    if (!seen.has(id)) active.delete(id);
  }
}, 10);

world.afterEvents.playerSpawn.subscribe(({player}) => {
  system.run(() => {
    if (!vehicleFor(player)) restoreCamera(player);
  });
});
