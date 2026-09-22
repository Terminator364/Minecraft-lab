import copy

def validate_item(item):
    menu = item["description"]["menu_category"]
    assert menu["category"] == "equipment"
    assert menu["group"] == "minecraft:itemGroup.name.minecart"
    assert item["components"]["minecraft:icon"]["texture"] == "minecart_normal"
    assert item["components"]["minecraft:entity_placer"]["entity"] == "minecraft_lab:vehicle"

def validate_vehicle(components):
    forbidden = {"minecraft:horse.jump_strength","minecraft:can_power_jump","minecraft:can_climb","minecraft:tameable","minecraft:inventory"}
    assert not (forbidden & set(components))
    step = components["minecraft:variable_max_auto_step"]
    assert max(step.values()) <= 0.0625

GOOD_ITEM = {
    "description": {"menu_category": {"category": "equipment","group": "minecraft:itemGroup.name.minecart"}},
    "components": {
        "minecraft:icon": {"texture": "minecart_normal"},
        "minecraft:entity_placer": {"entity": "minecraft_lab:vehicle"}
    }
}
GOOD_COMPONENTS = {
    "minecraft:input_ground_controlled": {},
    "minecraft:variable_max_auto_step": {"base_value":0.0625,"controlled_value":0.0625,"jump_prevented_value":0.0625}
}

mutations = []
x=copy.deepcopy(GOOD_ITEM); x["description"]["menu_category"]["category"]="none"; mutations.append(("hidden_creative_category",lambda x=x: validate_item(x)))
x=copy.deepcopy(GOOD_ITEM); x["components"]["minecraft:icon"]["texture"]="definitely_missing_icon"; mutations.append(("missing_icon_key",lambda x=x: validate_item(x)))
x=copy.deepcopy(GOOD_ITEM); x["components"]["minecraft:entity_placer"]["entity"]="minecraft:pig"; mutations.append(("wrong_placed_entity",lambda x=x: validate_item(x)))
x=copy.deepcopy(GOOD_COMPONENTS); x["minecraft:horse.jump_strength"]={"value":0.7}; mutations.append(("horse_jump_regression",lambda x=x: validate_vehicle(x)))
x=copy.deepcopy(GOOD_COMPONENTS); x["minecraft:variable_max_auto_step"]["controlled_value"]=0.5; mutations.append(("terrain_climb_regression",lambda x=x: validate_vehicle(x)))

caught=0
for name,fn in mutations:
    try: fn()
    except AssertionError:
        caught += 1
        print("NEGATIVE CONTROL CAUGHT", name)
    else:
        raise AssertionError(f"Negative control escaped: {name}")

assert caught == len(mutations)
print(f"negative_controls: PASS ({caught}/{len(mutations)} mutations caught)")
