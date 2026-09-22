from pathlib import Path
import json, io, zipfile, struct

ROOT=Path(__file__).resolve().parents[1]
BP=ROOT/"packs"/"behavior_pack"
RP=ROOT/"packs"/"resource_pack"

def load(p):
    return json.loads(p.read_text(encoding="utf-8"))

entity=load(BP/"entities"/"vehicle.json")["minecraft:entity"]
item=load(BP/"items"/"vehicle_item.json")["minecraft:item"]
atlas=load(RP/"textures"/"item_texture.json")
geo=load(RP/"models"/"entity"/"simple_car.geo.json")["minecraft:geometry"][0]
ants=load(ROOT/"spec"/"anticipations.json")

# Icon chain
key=item["components"]["minecraft:icon"]["textures"]["default"]
assert key=="minecraft_lab_4x4_icon"
assert key in atlas["texture_data"]
tex=atlas["texture_data"][key]["textures"]
png=RP/(tex+".png")
data=png.read_bytes()
assert data[:8]==b"\x89PNG\r\n\x1a\n"
w,h=struct.unpack(">II",data[16:24])
assert (w,h)==(64,64)
assert len(data)>300

# Geometry visual bounds after scale
mins=[10**9,10**9,10**9]
maxs=[-10**9,-10**9,-10**9]
for bone in geo["bones"]:
    for cube in bone.get("cubes",[]):
        o=cube["origin"]; s=cube["size"]
        for i in range(3):
            mins[i]=min(mins[i],o[i])
            maxs[i]=max(maxs[i],o[i]+s[i])
raw=[(maxs[i]-mins[i])/16 for i in range(3)]
scale=entity["components"]["minecraft:scale"]["value"]
scaled=[x*scale for x in raw]
print("raw_bbox_blocks",raw)
print("scaled_bbox_blocks",scaled)
assert scaled[0] < 2.3
assert scaled[1] < 2.6
assert scaled[2] < 4.5

# 4x4 policy
step=entity["components"]["minecraft:variable_max_auto_step"]
assert 1.0 <= step["controlled_value"] <= 1.25
assert 1.0 <= step["base_value"] <= 1.25
assert step["jump_prevented_value"] <= 1.0

# No horse UX
forbidden={
 "minecraft:horse.jump_strength","minecraft:can_power_jump","minecraft:can_climb",
 "minecraft:tameable","minecraft:breedable","minecraft:inventory","minecraft:is_saddled"
}
assert not(forbidden & set(entity["components"]))

# Seats
ride=entity["components"]["minecraft:rideable"]
assert ride["seat_count"]==4
assert ride["controlling_seat"]==0
assert len(ride["seats"])==4

# Semantic anticipation discipline
ids=[a["id"] for a in ants["families"]]
assert len(ids)==len(set(ids))
assert all(a["requirement_id"] for a in ants["families"])
device_pending=[a for a in ants["families"] if a["oracle"]=="DEVICE" and a["status"]=="PENDING_DEVICE"]
assert len(device_pending)>=3
print("semantic_families",len(ants["families"]))
print("device_pending",len(device_pending))
print("production_qa_v100: PASS")
