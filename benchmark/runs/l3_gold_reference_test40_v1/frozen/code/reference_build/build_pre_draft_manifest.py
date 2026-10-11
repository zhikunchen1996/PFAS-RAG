from __future__ import annotations

import json

import common


def main() -> None:
    paths = [
        common.PACKAGE / "README.md",
        common.PACKAGE / "protocol.json",
        common.PACKAGE / "prompts/task_components_v1.txt",
        common.PACKAGE / "prompts/reference_ledger_draft_v1.txt",
        common.PACKAGE / "scripts/common.py",
        common.PACKAGE / "scripts/build_source_packets.py",
        common.PACKAGE / "scripts/run_task_components.py",
        common.PACKAGE / "scripts/build_reference_packets.py",
        common.PACKAGE / "scripts/run_reference_drafts.py",
        common.SOURCE_PACKETS,
        common.TASK_COMPONENTS,
        common.REFERENCE_PACKETS,
    ]
    for path in paths:
        if not path.exists():
            raise RuntimeError(f"Missing pre-draft artifact: {path}")
    manifest = {
        "protocol_id": "l3_gold_reference_test40_v1",
        "status": "pre_draft_frozen_inputs",
        "question_count": 40,
        "gold_record_count": 189,
        "artifacts": {
            str(path.relative_to(common.ROOT)): common.sha256(path) for path in paths
        },
        "candidate_test40_inputs_used": False,
        "formal_test40_scoring_allowed": False,
    }
    output = common.PACKAGE / "pre_draft_manifest.json"
    common.write_json(output, manifest)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
