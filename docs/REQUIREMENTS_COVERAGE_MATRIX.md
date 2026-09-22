# Requirements ↔ Sources ↔ Tests ↔ Proof matrix

| Requirement | Source A/B/C | Test family | Required oracle | Current truth |
|---|---|---|---|---|
| A-P0-001 One-click install | A + C-006/C-007 | INSTALL-* | PACKAGE + DEVICE | DEVICE_PASS |
| A-P0-002 Visible item/icon | A + C-003/C-004 | ICON-* / INVENTORY-* | STATIC + VISUAL + DEVICE | PARTIAL |
| A-P0-003 Vehicle controls | A + C-001 | CONTROL-* | RUNTIME + DEVICE | PARTIAL |
| A-P0-004 Driver visibility | A + C-005 | CAMERA-* | VISUAL + DEVICE | FAIL |
| A-P0-005 4x4 terrain | A + C-002 | TERRAIN-* | RUNTIME + DEVICE | PARTIAL |
| A-P0-006 Reuse-first | A + B | SOURCE-* | STATIC | STATIC_PASS |
| A-P0-007 Provenance | A + B | LICENSE-* | STATIC | STATIC_PASS |
| A-P0-008 Semantic anticipations | A | META-* | STATIC | UNTESTED |
| A-P0-009 Truthful release gate | A + BCP/KINLINK method | RELEASE-* | STATIC | STATIC_PASS |

## Important
La V0.5 n'est pas marquée READY. Elle est **CANDIDATE_FIELD** parce que A-P0-002, A-P0-004 et A-P0-005 n'ont pas encore les niveaux de preuve requis.
