from pathlib import Path
import json, struct, zlib

ROOT=Path(__file__).resolve().parents[1]
BP=ROOT/"packs"/"behavior_pack"
RP=ROOT/"packs"/"resource_pack"

def load(p):
    return json.loads(p.read_text(encoding="utf-8"))

bp=load(BP/"manifest.json")
rp=load(RP/"manifest.json")
ent=load(BP/"entities"/"vehicle.json")["minecraft:entity"]
item=load(BP/"items"/"vehicle_item.json")["minecraft:item"]
atlas=load(RP/"textures"/"item_texture.json")
script=(BP/"scripts"/"driver_camera.js").read_text(encoding="utf-8")

assert bp["header"]["version"]==[0,5,0]
assert rp["header"]["version"]==[0,5,0]
assert bp["dependencies"][0]["version"]==[0,5,0]

comp=ent["components"]
forbidden={"minecraft:horse.jump_strength","minecraft:can_power_jump","minecraft:can_climb","minecraft:tameable","minecraft:breedable","minecraft:inventory","minecraft:is_saddled"}
assert not (forbidden & set(comp))

step=comp["minecraft:variable_max_auto_step"]
assert 1.0 <= step["controlled_value"] <= 1.25
assert step["base_value"] <= 1.25
assert step["jump_prevented_value"] <= 1.0

ride=comp["minecraft:rideable"]
assert ride["controlling_seat"]==0 and ride["seat_count"]==2
assert ride["seats"][0]["position"][1] >= 1.0
assert ride["seats"][1]["position"][1] >= 1.0

icon_key=item["components"]["minecraft:icon"]
assert icon_key=="minecraft_lab_4x4_icon"
tex=atlas["texture_data"][icon_key]["textures"]
assert tex=="textures/items/minecraft_lab_4x4_icon"
png=RP/(tex+".png")
assert png.is_file()
data=png.read_bytes()
assert data[:8]==b"\x89PNG\r\n\x1a\n"
width,height=struct.unpack(">II",data[16:24])
assert (width,height)==(64,64)
assert len(data)>300

assert 'player.camera.setCamera("minecraft:third_person")' in script
assert 'camera @s set minecraft:third_person' in script
assert 'player.camera.clear()' in script
assert '}, 10);' in script

print("vehicle_contract_v050: PASS")
