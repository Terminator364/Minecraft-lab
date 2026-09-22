# Minecraft Lab — Road Car 1.1.0

This release directly addresses the Android field regression where the previous chase camera caused left/right strafing instead of steering.

Core decisions:
- standard car = road car, max auto-step 0.50 block;
- dedicated 4x4 becomes a separate later class;
- cockpit-like camera = custom follow_orbit radius 0.12;
- control scheme = player_relative so left/right rotates instead of strafes;
- camera anchor shifted toward windshield for forward visibility;
- one-click .mcaddon preserved.

Device acceptance for this release is intentionally narrow:
left steer, right steer, forward/reverse, cockpit visibility, slab/road behavior.
