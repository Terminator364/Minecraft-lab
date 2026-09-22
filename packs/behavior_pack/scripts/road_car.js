import { world, system } from "@minecraft/server";

const VEHICLE_ID = "minecraft_lab:vehicle";
const DEADZONE = 0.12;
const TURN_DEGREES = 3.25;
const LATERAL_DAMPING = 0.78;
const COAST_BRAKE = 0.10;

const activeDrivers = new Set();

function clamp(value, min, max) {
  return Math.max(min, Math.min(max, value));
}

function normalizeYaw(yaw) {
  let y = yaw % 360;
  if (y > 180) y -= 360;
  if (y < -180) y += 360;
  return y;
}

function drivenVehicle(player) {
  try {
    const riding = player.getComponent("minecraft:riding");
    const vehicle = riding?.entityRidingOn;
    return vehicle?.typeId === VEHICLE_ID ? vehicle : undefined;
  } catch {
    return undefined;
  }
}

function enterDriverView(player) {
  // Remove the old forced third-person camera. The normal Minecraft perspective
  // is restored so the player can drive from first person and switch perspective
  // normally if desired.
  try { player.camera.clear(); } catch {}
  try { player.runCommand("hud @s hide horse_health"); } catch {}
}

function leaveDriverView(player) {
  try { player.camera.clear(); } catch {}
  try { player.runCommand("hud @s reset horse_health"); } catch {}
}

function steerVehicle(player, vehicle) {
  let input;
  try {
    input = player.inputInfo.getMovementVector();
  } catch {
    return;
  }

  const steer = Math.abs(input.x) >= DEADZONE ? clamp(input.x, -1, 1) : 0;
  const throttle = Math.abs(input.y) >= DEADZONE ? clamp(input.y, -1, 1) : 0;

  let rotation;
  let velocity;
  try {
    rotation = vehicle.getRotation();
    velocity = vehicle.getVelocity();
  } catch {
    return;
  }

  const horizontalSpeed = Math.hypot(velocity.x, velocity.z);

  // Steering changes vehicle yaw. Reverse steering naturally flips like a car.
  if (steer !== 0 && (Math.abs(throttle) >= DEADZONE || horizontalSpeed > 0.015)) {
    const reverseFactor = throttle < -DEADZONE ? -1 : 1;
    const speedFactor = clamp(0.35 + horizontalSpeed * 2.5, 0.35, 1.0);
    rotation.y = normalizeYaw(rotation.y + steer * TURN_DEGREES * reverseFactor * speedFactor);
    try { vehicle.setRotation({ x: 0, y: rotation.y }); } catch {}
  }

  // Kill sideways drift while retaining the forward component and vertical physics.
  // This converts touch-left/right into steering instead of strafing/gliding.
  if (horizontalSpeed > 0.001) {
    const yaw = rotation.y * Math.PI / 180;
    const forward = { x: -Math.sin(yaw), z: Math.cos(yaw) };
    const longitudinal = velocity.x * forward.x + velocity.z * forward.z;
    const lateralX = velocity.x - forward.x * longitudinal;
    const lateralZ = velocity.z - forward.z * longitudinal;

    try {
      vehicle.applyImpulse({
        x: -lateralX * LATERAL_DAMPING,
        y: 0,
        z: -lateralZ * LATERAL_DAMPING
      });
    } catch {}

    if (Math.abs(throttle) < DEADZONE) {
      try {
        vehicle.applyImpulse({
          x: -forward.x * longitudinal * COAST_BRAKE,
          y: 0,
          z: -forward.z * longitudinal * COAST_BRAKE
        });
      } catch {}
    }
  }
}

system.runInterval(() => {
  const seen = new Set();

  for (const player of world.getAllPlayers()) {
    seen.add(player.id);
    const vehicle = drivenVehicle(player);

    if (!vehicle) {
      if (activeDrivers.delete(player.id)) leaveDriverView(player);
      continue;
    }

    if (!activeDrivers.has(player.id)) {
      enterDriverView(player);
      activeDrivers.add(player.id);
    }

    steerVehicle(player, vehicle);
  }

  for (const id of [...activeDrivers]) {
    if (!seen.has(id)) activeDrivers.delete(id);
  }
}, 1);

world.afterEvents.playerSpawn.subscribe(({ player }) => {
  system.run(() => {
    if (!drivenVehicle(player)) {
      leaveDriverView(player);
      activeDrivers.delete(player.id);
    }
  });
});
