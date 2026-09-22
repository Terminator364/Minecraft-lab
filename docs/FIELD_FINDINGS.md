# Field findings — Road Car

## C-008 — lateral glide / no steering
1.0.0 Android field test: left/right produced lateral sliding instead of car-like yaw.
Root cause class: the built-in third-person preset defaults to locked-player-relative-strafe. Microsoft documents that strafe schemes move left/right without turning.
1.1.0 response: custom follow-orbit camera uses control_scheme=player_relative, where Microsoft documents that left/right rotates the player. Command fallback repeats player_relative.

## C-009 — forced exterior third person
1.0.0 improved visibility but lost the desired cockpit sensation.
1.1.0 response: near-zero follow-orbit radius (0.12) with a forward camera anchor near the windshield. The camera remains a follow-orbit preset so it can use player_relative steering semantics.

## C-010 — road car vs 4x4 semantics
A normal car should remain road-oriented. Off-road auto-climb becomes a separate vehicle class.
1.1.0 baseline road car max auto-step: 0.50 block.
Dedicated 4x4 requirement moved to A-P1-010.
