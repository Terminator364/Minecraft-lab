# Minecraft Lab — 4x4

Current candidate: **v0.5.0**.

This version treats the Android screenshots as failed gates, not cosmetic feedback.

Changes:
- real 64x64 custom item icon with explicit item_texture.json mapping;
- third-person camera forced and periodically reasserted while riding;
- higher driver/passenger seat as camera fallback;
- off-road auto-step raised to 1.25 blocks;
- one-click mcaddon remains the only user-facing install file.

4x4 policy:
- full 1-block ledges: supported by policy;
- rough mounds made of successive block-height steps: supported by policy;
- vertical 2-block walls: intentionally not supported.

Sources and licensing: docs/SOURCES.md.
Field failures: docs/FIELD_FINDINGS.md.
