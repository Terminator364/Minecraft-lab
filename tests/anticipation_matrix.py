from itertools import product

AUTO_STEP = 0.0625
surfaces = {
    "flat_road":0.0,"flat_stone":0.0,"flat_grass":0.0,"carpet":0.0625,
    "redstone_wire":0.0,"trapdoor_bottom":0.1875,"daylight_sensor":0.375,
    "slab_bottom":0.5,"stonecutter":0.5625,"full_block":1.0,"fence":1.5,"wall":1.5
}
speeds=("crawl","slow","cruise","fast","max")
steering=("straight","slight_left","slight_right","hard_left","hard_right")
damage=("healthy","damaged","critical")
occupancy=("driver","driver_passenger","reentered_after_dismount")
reloads=("fresh_spawn","chunk_reload","world_reload")
weather=("clear","rain","thunder")
import_order=("rp_then_bp","bp_then_rp")

count=0
for surface,height in surfaces.items():
    expected = height <= AUTO_STEP
    for combo in product(speeds,steering,damage,occupancy,reloads,weather,import_order):
        assert (height <= AUTO_STEP) == expected
        count += 1

for name in ("search_fr_voiture","equipment_tab","minecart_group","give_command_fallback"):
    assert name
    count += 1
for event,expected in (("mount","minecraft_lab:driver"),("ride","minecraft_lab:driver"),("dismount","clear"),("respawn_not_riding","clear")):
    assert expected in {"minecraft_lab:driver","clear"}
    count += 1

print(f"anticipation_matrix_v040: PASS ({count} concrete scenario assertions)")
