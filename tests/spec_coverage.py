from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
registry = json.loads((ROOT/"spec"/"requirements.json").read_text(encoding="utf-8"))
reqs = registry["requirements"]

assert reqs, "No requirements"
ids = [r["id"] for r in reqs]
assert len(ids) == len(set(ids)), "Duplicate requirement IDs"

allowed = {"UNTESTED","STATIC_PASS","RUNTIME_PASS","VISUAL_PASS","DEVICE_PASS","PARTIAL","FAIL","BLOCKED_EXTERNAL","SUPERSEDED"}
for r in reqs:
    assert r["priority"] in {"P0","P1","P2"}
    assert r["current_status"] in allowed
    assert r["acceptance"].strip()
    assert r["required_evidence"], f"{r['id']} missing required evidence"

p0 = [r for r in reqs if r["priority"] == "P0"]
blocking = [r["id"] for r in p0 if r["current_status"] in {"UNTESTED","PARTIAL","FAIL","BLOCKED_EXTERNAL"}]
print("P0 requirements:", len(p0))
print("Blocking READY:", blocking)
assert "A-P0-004" in blocking, "Known Android camera failure must remain blocking"
print("spec_coverage: PASS (truthful candidate state)")
