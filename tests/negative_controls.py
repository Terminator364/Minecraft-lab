import copy

def icon_ok(item,atlas):
    key=item["components"]["minecraft:icon"]
    assert key in atlas["texture_data"]
    assert atlas["texture_data"][key]["textures"].endswith("minecraft_lab_4x4_icon")

def terrain_ok(step):
    assert 1.0 <= step["controlled_value"] <= 1.25
    assert step["jump_prevented_value"] <= 1.0

GOOD_ITEM={"components":{"minecraft:icon":"minecraft_lab_4x4_icon"}}
GOOD_ATLAS={"texture_data":{"minecraft_lab_4x4_icon":{"textures":"textures/items/minecraft_lab_4x4_icon"}}}
GOOD_STEP={"controlled_value":1.25,"base_value":1.25,"jump_prevented_value":1.0}

tests=[]
x=copy.deepcopy(GOOD_ITEM); x["components"]["minecraft:icon"]="missing"; tests.append(("wrong_icon_key",lambda x=x:icon_ok(x,GOOD_ATLAS)))
a=copy.deepcopy(GOOD_ATLAS); a["texture_data"]["minecraft_lab_4x4_icon"]["textures"]="textures/items/missing"; tests.append(("wrong_icon_path",lambda a=a:icon_ok(GOOD_ITEM,a)))
s=copy.deepcopy(GOOD_STEP); s["controlled_value"]=0.0625; tests.append(("not_offroad",lambda s=s:terrain_ok(s)))
s=copy.deepcopy(GOOD_STEP); s["controlled_value"]=2.0; tests.append(("wall_climber",lambda s=s:terrain_ok(s)))

caught=0
for name,fn in tests:
    try: fn()
    except AssertionError:
        caught+=1
        print("NEGATIVE CONTROL CAUGHT",name)
    else:
        raise AssertionError("escaped mutation: "+name)
assert caught==len(tests)
print(f"negative_controls_v050: PASS ({caught}/{len(tests)})")
