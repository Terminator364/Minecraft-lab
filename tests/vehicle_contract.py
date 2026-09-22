from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
BP = ROOT / "packs" / "behavior_pack"
RP = ROOT / "packs" / "resource_pack"

def load(path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

bp_manifest = load(BP / "manifest.json")
rp_manifest = load(RP / "manifest.json")
entity = load(BP / "entities" / "vehicle.json")["minecraft:entity"]
components = entity["components"]
item_doc = load(BP / "items" / "vehicle_item.json")
item = item_doc["minecraft:item"]
catalog = load(BP / "item_catalog" / "crafting_item_catalog.json")
camera = load(BP / "cameras" / "presets" / "driver.camera.json")["minecraft:camera_preset"]
client = load(RP / "entity" / "vehicle.entity.json")["minecraft:client_entity"]["description"]
render = load(RP / "render_controllers" / "vehicle.render_controllers.json")["render_controllers"]["controller.render.minecraft_lab.vehicle"]
geo = load(RP / "models" / "entity" / "simple_car.geo.json")
anim = load(RP / "animations" / "simple_car.animation.json")
ctrl = load(RP / "animation_controllers" / "simple_car.rp.ac.json")
script = (BP / "scripts" / "driver_camera.js").read_text(encoding="utf-8")

assert bp_manifest["header"]["version"] == [0,4,0]
assert rp_manifest["header"]["version"] == [0,4,0]
assert bp_manifest["dependencies"][0]["version"] == [0,4,0]
assert any(m["type"] == "script" and m["entry"] == "scripts/driver_camera.js" for m in bp_manifest["modules"])
assert any(d.get("module_name") == "@minecraft/server" and d.get("version") == "2.0.0" for d in bp_manifest["dependencies"])

forbidden = [
    "minecraft:horse.jump_strength", "minecraft:can_power_jump", "minecraft:can_climb",
    "minecraft:tameable", "minecraft:breedable", "minecraft:healable",
    "minecraft:inventory", "minecraft:is_saddled"
]
present = sorted(set(forbidden) & set(components))
assert not present, f"Forbidden horse/mob components present: {present}"

assert "minecraft:input_ground_controlled" in components
ride = components["minecraft:rideable"]
assert ride["controlling_seat"] == 0
assert ride["seat_count"] == 2
assert len(ride["seats"]) == 2

step = components["minecraft:variable_max_auto_step"]
assert max(step.values()) <= 0.0625

assert client.get("spawn_egg") is None
assert item_doc["format_version"] == "1.21.60"
menu = item["description"]["menu_category"]
assert menu["category"] == "equipment"
assert menu["group"] == "minecraft:itemGroup.name.minecart"
assert menu["is_hidden_in_commands"] is False
assert item["components"]["minecraft:entity_placer"]["entity"] == "minecraft_lab:vehicle"
assert item["components"]["minecraft:icon"]["texture"] == "minecart_normal"

cats = catalog["minecraft:crafting_items_catalog"]["categories"]
minecart_items = []
for cat in cats:
    if cat["category_name"] == "equipment":
        for group in cat["groups"]:
            if group.get("group_identifier", {}).get("name") == "minecraft:itemGroup.name.minecart":
                minecart_items.extend(group["items"])
assert "minecraft_lab:vehicle_item" in minecart_items

assert camera["identifier"] == "minecraft_lab:driver"
assert camera["inherit_from"] == "minecraft:follow_orbit"
assert 4.0 <= camera["radius"] <= 7.0
assert "EntityComponentTypes.Riding" in script
assert 'player.camera.setCamera(CAMERA_ID)' in script
assert 'player.camera.clear()' in script

assert client["render_controllers"] == ["controller.render.minecraft_lab.vehicle"]
vis_text = json.dumps(render.get("part_visibility", []))
assert "query.is_first_person" in vis_text
for bone in ["body", "top", "door*", "steering_wheel", "lever"]:
    assert bone in vis_text

geo_ids = [g["description"]["identifier"] for g in geo["minecraft:geometry"]]
assert "geometry.simple_car" in geo_ids
assert "animation.simple_car.turn" in anim["animations"]
assert "animation.simple_car.move" in anim["animations"]
assert "controller.animation.simple_car.move_general" in ctrl["animation_controllers"]
assert (RP / "textures" / "entity" / "simple_car.png").is_file()

fr = (RP / "texts" / "fr_FR.lang").read_text(encoding="utf-8")
en = (RP / "texts" / "en_US.lang").read_text(encoding="utf-8")
assert "Voiture Minecraft Lab" in fr
assert "Minecraft Lab Car" in en

print("vehicle_contract_v040: PASS")
