def validate_control_scheme(v):
    assert v=="player_relative"

def validate_radius(v):
    assert 0.10 <= v <= 0.20

def validate_road_step(v):
    assert 0.25 <= v <= 0.50

tests=[
 ("strafe_regression",lambda:validate_control_scheme("player_relative_strafe")),
 ("locked_strafe_regression",lambda:validate_control_scheme("locked_player_relative_strafe")),
 ("forced_chase_camera",lambda:validate_radius(5.0)),
 ("camera_inside_player_zero",lambda:validate_radius(0.0)),
 ("4x4_leak_into_road_car",lambda:validate_road_step(1.25)),
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
print(f"negative_controls_1_1_0: PASS ({caught}/{len(tests)})")
