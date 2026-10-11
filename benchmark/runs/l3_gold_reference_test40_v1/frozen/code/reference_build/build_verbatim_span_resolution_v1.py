from __future__ import annotations

import copy
import json
import re

import common
import build_final_resolution_v1 as prior


SOURCE = (
    common.PACKAGE
    / "reference_build/revisions/model_a_ledgers_resolution1.jsonl"
)
OUTPUT = (
    common.PACKAGE
    / "reference_build/revisions/model_a_ledgers_resolution2.jsonl"
)
RESOLUTIONS = (
    common.PACKAGE / "reference_build/revisions/verbatim_span_resolution_v1.jsonl"
)


def verbatim_whitespace_match(span: str, full_chunk: str) -> str | None:
    tokens = span.split()
    if not tokens:
        return None
    pattern = r"\s+".join(re.escape(token) for token in tokens)
    match = re.search(pattern, full_chunk)
    return match.group(0) if match else None


def main() -> None:
    packets = {
        row["question_id"]: row for row in common.read_jsonl(common.REFERENCE_PACKETS)
    }
    output_rows = []
    resolution_rows = []
    for source_row in common.read_jsonl(SOURCE):
        row = copy.deepcopy(source_row)
        qid = row["question_id"]
        ledger = row["draft_ledger"]
        evidence = {
            item["evidence_id"]: item
            for item in packets[qid]["approved_source_evidence"]
        }
        changes = []
        for group in ledger["claim_groups"] + ledger["constraint_groups"]:
            resolved_spans = []
            for span in group.get("exact_spans", []):
                source = evidence[span["evidence_id"]]
                text = span["exact_evidence_span"]
                if text in source["full_chunk_text"]:
                    resolved_spans.append(span)
                    continue
                matched = verbatim_whitespace_match(text, source["full_chunk_text"])
                if matched is not None:
                    updated = copy.deepcopy(span)
                    updated["exact_evidence_span"] = matched
                    resolved_spans.append(updated)
                    changes.append(
                        {
                            "claim_group_id": group["claim_group_id"],
                            "evidence_id": span["evidence_id"],
                            "action": "restored_original_chunk_whitespace",
                            "old_span_sha256": common.payload_sha256(text),
                            "new_span_sha256": common.payload_sha256(matched),
                        }
                    )
                    continue
                if (
                    qid == "NQ07a"
                    and group["claim_group_id"] == "NQ07a-G01"
                    and span["evidence_id"] == "NQ07a_MMG001"
                ):
                    first = (
                        "sate traps along the gas pipeline using HDPE bottles "
                        "(refer to Smallwood et al., 2023 for a detailed description "
                        "of a landfill gas collection system similar to the studied site)."
                    )
                    second = (
                        "Groundwater was sampled from a monitoring well using a "
                        "Waterra ® inertial hand pump connected to HDPE tubing."
                    )
                    if (
                        first not in source["full_chunk_text"]
                        or second not in source["full_chunk_text"]
                    ):
                        raise RuntimeError("NQ07a split spans are not verbatim")
                    for exact, support in [
                        (
                            first,
                            "HDPE bottles were used in condensate traps along the "
                            "landfill gas pipeline.",
                        ),
                        (
                            second,
                            "Groundwater was sampled through an inertial hand pump "
                            "connected to HDPE tubing.",
                        ),
                    ]:
                        resolved_spans.append(
                            {
                                "evidence_id": span["evidence_id"],
                                "exact_evidence_span": exact,
                                "supports": support,
                            }
                        )
                    changes.append(
                        {
                            "claim_group_id": group["claim_group_id"],
                            "evidence_id": span["evidence_id"],
                            "action": "split_noncontiguous_span_into_two_verbatim_spans",
                            "old_span_sha256": common.payload_sha256(text),
                            "new_span_sha256": common.payload_sha256([first, second]),
                        }
                    )
                    continue
                raise RuntimeError(
                    f"{qid} {group['claim_group_id']}: unresolved non-verbatim span"
                )
            group["exact_spans"] = resolved_spans
        prior.validate_with_documented_component_amendment(
            ledger, packets[qid], qid
        )
        row["verbatim_resolution_provenance"] = {
            "source_ledger_sha256": common.payload_sha256(source_row["draft_ledger"]),
            "change_count": len(changes),
            "changes": changes,
        }
        output_rows.append(row)
        if changes:
            resolution_rows.append(
                {
                    "question_id": qid,
                    "source_ledger_sha256": common.payload_sha256(
                        source_row["draft_ledger"]
                    ),
                    "resolved_ledger_sha256": common.payload_sha256(ledger),
                    "changes": changes,
                    "candidate_test40_inputs_used": False,
                    "scientific_propositions_changed": False,
                    "project_author_audit_required": True,
                }
            )
    common.write_jsonl(OUTPUT, output_rows)
    common.write_jsonl(RESOLUTIONS, resolution_rows)
    manifest = {
        "stage": "Test40 verbatim-span resolution v1",
        "question_count": len(output_rows),
        "affected_question_count": len(resolution_rows),
        "span_change_count": sum(len(row["changes"]) for row in resolution_rows),
        "source_sha256": common.sha256(SOURCE),
        "output_sha256": common.sha256(OUTPUT),
        "resolutions_sha256": common.sha256(RESOLUTIONS),
        "candidate_test40_inputs_used": False,
        "scientific_propositions_changed": False,
        "project_author_audit_required": True,
    }
    common.write_json(
        common.PACKAGE
        / "reference_build/revisions/verbatim_span_resolution_v1_manifest.json",
        manifest,
    )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
