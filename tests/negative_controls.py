def steering_contract(script):
    assert "inputInfo.getMovementVector()" in script
    assert "vehicle.setRotation" in script
    assert "LATERAL_DAMPING" in script
    assert "minecraft:third_person" not in script

good='inputInfo.getMovementVector() vehicle.setRotation LATERAL_DAMPING player.camera.clear()'
mutations=[
 ("no_input",good.replace("inputInfo.getMovementVector()","")),
 ("no_yaw",good.replace("vehicle.setRotation","")),
 ("no_anti_slip",good.replace("LATERAL_DAMPING","")),
 ("forced_third_person",good+" minecraft:third_person")
]
caught=0
for name,text in mutations:
    try: steering_contract(text)
    except AssertionError:
        caught+=1
        print("NEGATIVE CONTROL CAUGHT",name)
    else:
        raise AssertionError("escaped mutation "+name)
assert caught==len(mutations)
print(f"negative_controls_1_1_0: PASS ({caught}/{len(mutations)})")
