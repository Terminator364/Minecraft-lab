from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
BP=ROOT/"packs"/"behavior_pack"

def load(p):
    return json.loads(p.read_text(encoding="utf-8"))

ent=load(BP/"entities"/"vehicle.json")["minecraft:entity"]["components"]
cam=load(BP/"cameras"/"presets"/"cockpit_drive.camera.json")["minecraft:camera_preset"]
script=(BP/"scripts"/"driver_camera.js").read_text(encoding="utf-8")
ants=load(ROOT/"spec"/"anticipations.json")

# Steering contract: the exact regression was strafe. Player-relative is the
# official scheme where left/right ROTATES rather than strafes.
assert cam["inherit_from"]=="minecraft:follow_orbit"
assert cam["control_scheme"]=="player_relative"
assert cam["radius"] <= 0.20
assert 0.30 <= cam["entity_offset"][2] <= 0.80
assert "controlscheme @s set player_relative" in script
assert "player_relative_strafe" not in script

# Baseline road car, not the 4x4 variant.
step=ent["minecraft:variable_max_auto_step"]
assert step["controlled_value"]==0.50
assert step["base_value"]==0.50
assert step["jump_prevented_value"]==0.50
assert "road_car" in ent["minecraft:type_family"]["family"]
assert "offroad_4x4" not in ent["minecraft:type_family"]["family"]

# No horse mechanics.
forbidden={"minecraft:horse.jump_strength","minecraft:can_power_jump","minecraft:can_climb","minecraft:tameable","minecraft:breedable","minecraft:inventory","minecraft:is_saddled"}
assert not(forbidden & set(ent))

ids=[a["id"] for a in ants["families"]]
assert len(ids)==len(set(ids))
assert any(a["id"]=="STEER-001" and a["status"]=="PENDING_DEVICE" for a in ants["families"])
assert any(a["id"]=="CAMERA-002" and a["status"]=="PENDING_DEVICE" for a in ants["families"])
print("road_car_qa_1_1_0: PASS")
