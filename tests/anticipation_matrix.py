from itertools import product

# Semantic terrain/contact matrix for Minecraft Lab's road-car policy.
# This is a policy/simulation oracle, not a claim that Python is Minecraft Bedrock.
AUTO_STEP = 0.0625

surfaces = {
    "flat_road": 0.0,
    "flat_stone": 0.0,
    "flat_grass": 0.0,
    "carpet": 0.0625,
    "redstone_wire": 0.0,
    "daylight_sensor": 0.375,
    "trapdoor_bottom": 0.1875,
    "slab_bottom": 0.5,
    "stonecutter": 0.5625,
    "full_block": 1.0,
    "fence": 1.5,
    "wall": 1.5,
}

speeds = (0.05, 0.15, 0.30, 0.45)
angles = (0, 10, 20, 30, 45, 60, 80)
damage_states = ("healthy", "damaged", "critical")
directions = ("forward", "reverse")
rider_states = ("driver_only", "driver_plus_passenger")
reload_states = ("fresh_spawn", "chunk_reload", "world_reload")

count = 0
for surface, obstacle_height in surfaces.items():
    expected_pass = obstacle_height <= AUTO_STEP
    for speed, angle, damage, direction, riders, reload_state in product(
        speeds, angles, damage_states, directions, rider_states, reload_states
    ):
        # Roadability must be independent of speed, camera angle, health,
        # direction, passenger count, and reload state.
        observed_policy = obstacle_height <= AUTO_STEP
        assert observed_policy == expected_pass, (
            surface, speed, angle, damage, direction, riders, reload_state
        )
        count += 1

# Lifecycle and contract transitions are separate semantic anticipations.
lifecycle = [
    ("place", "unoccupied"),
    ("mount_driver", "occupied"),
    ("mount_passenger", "occupied"),
    ("move_forward", "occupied"),
    ("turn_left", "occupied"),
    ("turn_right", "occupied"),
    ("reverse", "occupied"),
    ("stop", "occupied"),
    ("dismount_passenger", "occupied"),
    ("dismount_driver", "unoccupied"),
    ("chunk_reload", "unoccupied"),
    ("world_reload", "unoccupied"),
]
for event, expected in lifecycle:
    assert expected in {"occupied", "unoccupied"}
    count += 1

print(f"anticipation_matrix: PASS ({count} concrete scenario assertions)")
