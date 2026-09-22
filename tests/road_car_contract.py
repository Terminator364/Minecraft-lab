from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
BP=ROOT/"packs"/"behavior_pack"
RP=ROOT/"packs"/"resource_pack"

def load(p): return json.loads(p.read_text(encoding="utf-8"))

bp=load(BP/"manifest.json")
rp=load(RP/"manifest.json")
ent=load(BP/"entities"/"vehicle.json")["minecraft:entity"]
item=load(BP/"items"/"vehicle_item.json")["minecraft:item"]
script=(BP/"scripts"/"road_car.js").read_text(encoding="utf-8")

assert bp["header"]["version"]==[1,1,0]
assert rp["header"]["version"]==[1,1,0]
assert bp["dependencies"][0]["version"]==[1,1,0]
assert any(m.get("entry")=="scripts/road_car.js" for m in bp["modules"])

c=ent["components"]
assert c["minecraft:friction_modifier"]["value"]==2.0
step=c["minecraft:variable_max_auto_step"]
assert step["controlled_value"]<=0.5625
assert step["base_value"]<=0.5625
assert "minecraft:input_ground_controlled" in c

forbidden={"minecraft:horse.jump_strength","minecraft:can_power_jump","minecraft:can_climb","minecraft:tameable","minecraft:breedable","minecraft:inventory","minecraft:is_saddled"}
assert not(forbidden & set(c))

ride=c["minecraft:rideable"]
assert ride["controlling_seat"]==0 and ride["seat_count"]==4
driver=ride["seats"][0]["position"]
assert driver[2] <= -0.55, "driver must be forward-biased for windscreen visibility"

assert "inputInfo.getMovementVector()" in script
assert "vehicle.setRotation" in script
assert "vehicle.getVelocity()" in script
assert "LATERAL_DAMPING" in script
assert 'minecraft:third_person' not in script
assert "player.camera.clear()" in script

icon=item["components"]["minecraft:icon"]["textures"]["default"]
atlas=load(RP/"textures"/"item_texture.json")
assert icon in atlas["texture_data"]

print("road_car_contract_1_1_0: PASS")
