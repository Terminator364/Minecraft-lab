import { world, system, EntityComponentTypes } from "@minecraft/server";

const VEHICLE_ID = "minecraft_lab:vehicle";
const CAMERA_ID = "minecraft_lab:driver";
const activeRiders = new Set();

function isInMinecraftLabCar(player) {
  try {
    const riding = player.getComponent(EntityComponentTypes.Riding);
    return riding?.entityRidingOn?.typeId === VEHICLE_ID;
  } catch {
    return false;
  }
}

function enterDriverView(player) {
  try { player.camera.setCamera(CAMERA_ID); } catch {}
  try { player.runCommand("hud @s hide horse_health"); } catch {}
}

function leaveDriverView(player) {
  try { player.camera.clear(); } catch {}
  try { player.runCommand("hud @s reset horse_health"); } catch {}
}

system.runInterval(() => {
  const currentPlayers = world.getAllPlayers();
  const liveIds = new Set();

  for (const player of currentPlayers) {
    liveIds.add(player.id);
    const ridingCar = isInMinecraftLabCar(player);

    if (ridingCar && !activeRiders.has(player.id)) {
      enterDriverView(player);
      activeRiders.add(player.id);
      continue;
    }

    if (!ridingCar && activeRiders.has(player.id)) {
      leaveDriverView(player);
      activeRiders.delete(player.id);
    }
  }

  for (const id of [...activeRiders]) {
    if (!liveIds.has(id)) activeRiders.delete(id);
  }
}, 4);

world.afterEvents.playerSpawn.subscribe(({ player }) => {
  system.run(() => {
    if (!isInMinecraftLabCar(player)) {
      leaveDriverView(player);
      activeRiders.delete(player.id);
    }
  });
});
