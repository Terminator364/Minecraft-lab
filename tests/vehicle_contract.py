from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
BP = ROOT / "packs" / "behavior_pack"
RP = ROOT / "packs" / "resource_pack"

def load(path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

entity = load(BP / "entities" / "vehicle.json")["minecraft:entity"]
components = entity["components"]
client = load(RP / "entity" / "vehicle.entity.json")["minecraft:client_entity"]["description"]
item = load(BP / "items" / "vehicle_item.json")["minecraft:item"]
geo = load(RP / "models" / "entity" / "simple_car.geo.json")
anim = load(RP / "animations" / "simple_car.animation.json")
ctrl = load(RP / "animation_controllers" / "simple_car.rp.ac.json")

forbidden = [
    "minecraft:horse.jump_strength",
    "minecraft:can_power_jump",
    "minecraft:can_climb",
    "minecraft:tameable",
    "minecraft:breedable",
    "minecraft:healable",
    "minecraft:inventory",
    "minecraft:is_saddled",
]
present = sorted(set(forbidden) & set(components))
assert not present, f"Forbidden horse/mob components present: {present}"

assert "minecraft:input_ground_controlled" in components
ride = components["minecraft:rideable"]
assert ride["controlling_seat"] == 0
assert ride["seat_count"] >= 1
assert len(ride["seats"]) >= 1

step = components["minecraft:variable_max_auto_step"]
assert max(step.values()) <= 0.0625, f"Auto-step too high: {step}"

assert client.get("spawn_egg") is None, "Spawn egg must not be exposed"
assert item["components"]["minecraft:entity_placer"]["entity"] == "minecraft_lab:vehicle"

geo_ids = [g["description"]["identifier"] for g in geo["minecraft:geometry"]]
assert "geometry.simple_car" in geo_ids
assert "animation.simple_car.turn" in anim["animations"]
assert "animation.simple_car.move" in anim["animations"]
assert "controller.animation.simple_car.move_general" in ctrl["animation_controllers"]

assert (RP / "textures" / "entity" / "simple_car.png").is_file()
assert (RP / "textures" / "items" / "vehicle_item.png").is_file()

fr = (RP / "texts" / "fr_FR.lang").read_text(encoding="utf-8")
en = (RP / "texts" / "en_US.lang").read_text(encoding="utf-8")
assert "action.minecraft_lab.drive=Conduire" in fr
assert "action.minecraft_lab.drive=Drive" in en

print("vehicle_contract: PASS")
