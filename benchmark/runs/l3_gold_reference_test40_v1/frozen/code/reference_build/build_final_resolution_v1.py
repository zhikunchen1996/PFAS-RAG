from __future__ import annotations

import copy
import json

import common
import run_reference_drafts as drafts


SOURCE = common.PACKAGE / "reference_build/revisions/model_a_ledgers_repair3.jsonl"
OUTPUT = (
    common.PACKAGE
    / "reference_build/revisions/model_a_ledgers_resolution1.jsonl"
)
RESOLUTIONS = (
    common.PACKAGE / "reference_build/revisions/final_resolution_v1.jsonl"
)


WF10_028_T01 = (
    "Extract how increasing membrane-modifier loading is reported to affect "
    "PFAS rejection, including the available PFOA, total-PFAS, and PFOS "
    "examples; report the direction and extent of change, any plateau or loss "
    "of improvement, and any stated limitations or tradeoffs at higher loadings."
)

NQ25_G05_REFERENCE = (
    "There is also substantial variability within adsorbent classes. Franke "
    "et al. describe two commercial GACs, noting that \"the Filtrasorb 400 "
    "material is prepared from steam-activated bituminous coal that was "
    "pulverized and reagglomerated whereas Norit 1240 W is prepared from "
    "steam-activated coal,\" and that this preparation difference is a main "
    "distinction between the materials. These distinct preparation routes show "
    "that the broad GAC label can encompass different commercial materials. "
    "Cross-study comparisons that treat all GAC materials as interchangeable "
    "may therefore reflect product-specific preparation differences rather "
    "than class-wide behavior."
)


def resolve_wf10_028(ledger: dict) -> list[str]:
    component = next(
        row
        for row in ledger["task_components"]
        if row["task_component_id"] == "WF10_028-T01"
    )
    component["component_text"] = WF10_028_T01
    return [
        "Broadened T01 to match the visible question and the already-supported "
        "PFOA, total-PFAS, and PFOS claim groups."
    ]


def resolve_nq25(ledger: dict) -> list[str]:
    group = next(
        row for row in ledger["claim_groups"] if row["claim_group_id"] == "NQ25-G05"
    )
    group["canonical_proposition"] = (
        "Different preparation routes among commercial granular activated "
        "carbons complicate class-wide generalization and cross-study comparison."
    )
    group["central_proposition"] = (
        "Commercial granular activated carbons can use different preparation "
        "routes, so comparisons reported broadly as 'GAC' may partly reflect "
        "the specific products being compared rather than class-wide behavior."
    )
    group["full_rule"] = (
        "Award full credit if the answer notes that the cited commercial GAC "
        "products use different preparation routes and explains that this "
        "product-level variation complicates class-wide performance comparisons."
    )
    group["partial_rule"] = (
        "Award partial credit if the answer mentions that different GAC products "
        "or preparation routes exist but does not connect that variation to the "
        "difficulty of cross-study comparison."
    )
    group["contradiction_rule"] = (
        "Flag a contradiction if the answer states that all commercial GAC "
        "products have the same preparation route or can be assumed to be "
        "interchangeable in cross-study comparisons."
    )
    old_paragraph = next(
        row["reference_answer_excerpt"]
        for row in ledger["reference_answer_claim_map"]
        if row["claim_group_id"] == "NQ25-G05"
    )
    if old_paragraph not in ledger["reference_answer"]:
        raise RuntimeError("NQ25-G05 mapped paragraph is absent from reference prose")
    ledger["reference_answer"] = ledger["reference_answer"].replace(
        old_paragraph, NQ25_G05_REFERENCE
    )
    for row in ledger["reference_answer_claim_map"]:
        if row["claim_group_id"] == "NQ25-G05":
            row["reference_answer_excerpt"] = NQ25_G05_REFERENCE
    stale_prefix = (
        "Specific experimental and reporting choices such as Freundlich "
        "isotherm parameters"
    )
    before = len(ledger["unresolved_or_unsupported"])
    ledger["unresolved_or_unsupported"] = [
        row
        for row in ledger["unresolved_or_unsupported"]
        if not row.startswith(stale_prefix)
    ]
    if len(ledger["unresolved_or_unsupported"]) != before - 1:
        raise RuntimeError("NQ25 stale unresolved item was not removed exactly once")
    return [
        "Trimmed G05 and its prose to the directly supported preparation-route "
        "comparison; removed the stale unresolved item about deleted prose."
    ]


def validate_with_documented_component_amendment(
    ledger: dict, packet: dict, question_id: str
) -> None:
    if question_id != "WF10_028":
        drafts.validate(ledger, packet)
        return
    validation_copy = copy.deepcopy(ledger)
    validation_copy["task_components"] = copy.deepcopy(packet["task_components"])
    drafts.validate(validation_copy, packet)
    component = next(
        row
        for row in ledger["task_components"]
        if row["task_component_id"] == "WF10_028-T01"
    )
    if component["component_text"] != WF10_028_T01:
        raise RuntimeError("WF10_028 task-component amendment differs")


def main() -> None:
    packets = {
        row["question_id"]: row for row in common.read_jsonl(common.REFERENCE_PACKETS)
    }
    source_rows = common.read_jsonl(SOURCE)
    output_rows = []
    resolutions = []
    for source_row in source_rows:
        row = copy.deepcopy(source_row)
        qid = row["question_id"]
        ledger = row["draft_ledger"]
        changes: list[str] = []
        if qid == "WF10_028":
            changes = resolve_wf10_028(ledger)
        elif qid == "NQ25":
            changes = resolve_nq25(ledger)
        elif qid == "WF10_035":
            changes = [
                "Retained MMG001 and MMG003 in the immutable source packet "
                "because they preserve distinct human-audited required-gold and "
                "negative-gold provenance roles; the normative ledger uses the "
                "duplicated source content only once and does not double-weight it."
            ]
        validate_with_documented_component_amendment(ledger, packets[qid], qid)
        row["resolution_provenance"] = {
            "source_ledger_sha256": common.payload_sha256(source_row["draft_ledger"]),
            "status": "deterministic_resolution" if changes else "unchanged",
            "changes": changes,
        }
        output_rows.append(row)
        if changes:
            resolutions.append(
                {
                    "question_id": qid,
                    "source_ledger_sha256": common.payload_sha256(
                        source_row["draft_ledger"]
                    ),
                    "resolved_ledger_sha256": common.payload_sha256(ledger),
                    "resolution_type": (
                        "source_packet_provenance_adjudication"
                        if qid == "WF10_035"
                        else "deterministic_ledger_repair"
                    ),
                    "changes": changes,
                    "candidate_test40_inputs_used": False,
                    "project_author_audit_required": True,
                }
            )
    common.write_jsonl(OUTPUT, output_rows)
    common.write_jsonl(RESOLUTIONS, resolutions)
    manifest = {
        "stage": "Test40 deterministic final resolution1",
        "question_count": len(output_rows),
        "resolution_count": len(resolutions),
        "source_sha256": common.sha256(SOURCE),
        "output_sha256": common.sha256(OUTPUT),
        "resolutions_sha256": common.sha256(RESOLUTIONS),
        "candidate_test40_inputs_used": False,
        "project_author_audit_required": True,
    }
    common.write_json(
        common.PACKAGE / "reference_build/revisions/final_resolution_v1_manifest.json",
        manifest,
    )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
