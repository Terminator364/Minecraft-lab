import copy

def validate_scale(v):
    assert 0.55 <= v <= 0.75

def validate_step(v):
    assert 1.0 <= v <= 1.25

def validate_icon(item_key,atlas):
    assert item_key in atlas

tests=[
 ("oversized_model",lambda:validate_scale(1.0)),
 ("tiny_model",lambda:validate_scale(0.3)),
 ("not_4x4",lambda:validate_step(0.5)),
 ("wall_climber",lambda:validate_step(2.0)),
 ("missing_icon",lambda:validate_icon("missing",{"minecraft_lab_4x4_icon":{}}))
]
caught=0
for name,fn in tests:
    try: fn()
    except AssertionError:
        caught+=1
        print("NEGATIVE CONTROL CAUGHT",name)
    else:
        raise AssertionError("escaped mutation: "+name)
assert caught==len(tests)
print(f"negative_controls_v100: PASS ({caught}/{len(tests)})")
