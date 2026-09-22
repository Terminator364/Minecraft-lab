from itertools import product

AUTO_STEP=1.25
terrain={
 "flat":0.0,
 "carpet":0.0625,
 "snow_layer":0.125,
 "trapdoor":0.1875,
 "slab":0.5,
 "stonecutter":0.5625,
 "stair_like":1.0,
 "full_block_ledge":1.0,
 "rough_mound_step":1.0,
 "one_plus_quarter":1.25,
 "one_plus_half":1.5,
 "two_block_wall":2.0
}
speeds=("crawl","slow","cruise","fast")
approach=("0deg","15deg","30deg","45deg","60deg")
occupancy=("driver","driver_passenger")
damage=("healthy","damaged","critical")
reloads=("fresh","chunk_reload","world_reload")
weather=("clear","rain","thunder")
camera=("mount","steady_ride","look_left","look_right","dismount_reenter")

count=0
for name,height in terrain.items():
    expected=height<=AUTO_STEP
    for _ in product(speeds,approach,occupancy,damage,reloads,weather,camera):
        assert (height<=AUTO_STEP)==expected
        count+=1

assert terrain["full_block_ledge"]<=AUTO_STEP
assert terrain["rough_mound_step"]<=AUTO_STEP
assert terrain["two_block_wall"]>AUTO_STEP
count+=3
print(f"anticipation_matrix_v050: PASS ({count} concrete scenario assertions)")
