from __future__ import annotations

import json

import common


def main() -> None:
    paths = [
        common.PACKAGE / "prompts/reference_repair_v2.txt",
        common.PACKAGE / "scripts/run_reference_repairs_v2.py",
        common.PACKAGE / "reference_build/revisions/model_a_ledgers_repair2.jsonl",
        common.PACKAGE
        / "reference_build/reviews/model_b_reviews_v1_rereview1.jsonl",
        common.REFERENCE_PACKETS,
    ]
    manifest = {
        "stage": "pre-repair2 frozen inputs",
        "repair_question_count": 13,
        "artifacts": {
            str(path.relative_to(common.ROOT)): common.sha256(path) for path in paths
        },
        "candidate_test40_inputs_used": False,
    }
    output = common.PACKAGE / "pre_repair2_manifest.json"
    common.write_json(output, manifest)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
