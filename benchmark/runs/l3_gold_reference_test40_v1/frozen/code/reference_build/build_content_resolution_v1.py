from __future__ import annotations

import copy
import json

import common
import build_final_resolution_v1 as final_resolution
import build_verbatim_span_resolution_v1 as verbatim


SOURCE = (
    common.PACKAGE
    / "reference_build/revisions/model_a_ledgers_resolution2.jsonl"
)
OUTPUT = (
    common.PACKAGE
    / "reference_build/revisions/model_a_ledgers_resolution3.jsonl"
)
RESOLUTIONS = (
    common.PACKAGE / "reference_build/revisions/content_resolution_v1.jsonl"
)


def resolve_nq28(ledger: dict, packet: dict) -> list[str]:
    evidence = {
        row["evidence_id"]: row for row in packet["approved_source_evidence"]
    }
    energy_span = evidence["NQ28_MMG001"]["unit_exact_spans"][2]
    replacements = 0
    for group_id in ["NQ28-G04", "NQ28-G06"]:
        group = next(
            row for row in ledger["claim_groups"] if row["claim_group_id"] == group_id
        )
        for span in group["exact_spans"]:
            support = span.get("supports", "").lower()
            if span["evidence_id"] == "NQ28_MMG001" and (
                "order of magnitude" in support
                or "very different energy inputs" in support
            ):
                span["exact_evidence_span"] = energy_span
                replacements += 1
    if replacements != 2:
        raise RuntimeError("NQ28 energy-span replacements did not occur twice")
    disposition = next(
        row
        for row in ledger["atomic_claim_dispositions"]
        if row["atomic_claim_id"] == "NQ28-A02"
    )
    disposition["evidence_ids"] = ["NQ28_MMG002"]
    disposition["rationale"] = (
        "The approved NQ28_MMG002 context distinguishes hydrated electrons from "
        "hydroxyl and sulfate radicals and situates them within reduction versus "
        "oxidation-process discussion; NQ28_MMG003 is not used for this claim."
    )
    return [
        "Replaced two misattributed NQ28_MMG001 quotes with its approved "
        "energy-density unit span.",
        "Removed unsupported NQ28_MMG003 linkage from atomic disposition NQ28-A02.",
    ]


def resolve_wf10_009(ledger: dict, packet: dict) -> list[str]:
    evidence = {
        row["evidence_id"]: row for row in packet["approved_source_evidence"]
    }
    calcium = (
        "The concentration of Ca 2 + was increased from 0.1 mM to 2 mM, and the "
        "level of PFOS rejection was raised from 97.10 % to 99.40 %."
    )
    reach_99 = (
        "Overall, available commercial NF and RO membranes exhibited a good PFAS "
        "rejection in water and wastewater with efficiencies that could reach "
        "up to 99 %."
    )
    if calcium not in evidence["WF10_009_MMG002"]["full_chunk_text"]:
        raise RuntimeError("WF10_009 calcium span is not verbatim")
    if reach_99 not in evidence["WF10_009_MMG001"]["full_chunk_text"]:
        raise RuntimeError("WF10_009 99-percent span is not verbatim")
    group = next(
        row for row in ledger["claim_groups"] if row["claim_group_id"] == "WF10_009-G02"
    )
    calcium_updates = 0
    for span in group["exact_spans"]:
        if span["evidence_id"] == "WF10_009_MMG002" and "97.10" in span.get(
            "supports", ""
        ):
            span["exact_evidence_span"] = calcium
            calcium_updates += 1
    constraint = next(
        row
        for row in ledger["constraint_groups"]
        if row["claim_group_id"] == "WF10_009-X01"
    )
    limit_updates = 0
    for span in constraint["exact_spans"]:
        if span["evidence_id"] == "WF10_009_MMG001" and "99" in span.get(
            "supports", ""
        ):
            span["exact_evidence_span"] = reach_99
            limit_updates += 1
    if calcium_updates != 1 or limit_updates != 1:
        raise RuntimeError("WF10_009 quote/support repairs did not occur exactly once")
    return [
        "Replaced the duplicated pH quote with the verbatim Ca2+ sentence in G02.",
        "Replaced the duplicated CCMF quote with the verbatim up-to-99% sentence in X01.",
    ]


def resolve_wf10_011(ledger: dict, packet: dict) -> list[str]:
    evidence = {
        row["evidence_id"]: row for row in packet["approved_source_evidence"]
    }
    requested = (
        "More importantly, the author found that the bound PFOA could be "
        "effectively desorbed due to the charge repulsion when a negative bias "
        "was applied (e.g., regeneration of > 80 % at –1.5 V) ( Fig. 6(b))."
    )
    regeneration_span = verbatim.verbatim_whitespace_match(
        requested, evidence["WF10_011_MMG003"]["full_chunk_text"]
    )
    if regeneration_span is None:
        raise RuntimeError("WF10_011 regeneration sentence could not be matched")
    if any(row["claim_group_id"] == "WF10_011-G03" for row in ledger["claim_groups"]):
        raise RuntimeError("WF10_011-G03 already exists")
    ledger["claim_groups"].append(
        {
            "claim_group_id": "WF10_011-G03",
            "task_component_id": "WF10_011-T02",
            "canonical_proposition": (
                "In the cited electro-adsorption study, applying a negative bias "
                "desorbed bound PFOA through charge repulsion and achieved more "
                "than 80% regeneration at -1.5 V."
            ),
            "central_proposition": (
                "A negative applied bias can desorb bound PFOA and regenerate the "
                "electro-adsorption electrode in the reported system."
            ),
            "material_qualifiers": [
                "PFOA",
                "electro-adsorption electrode",
                "negative bias",
                "reported regeneration at -1.5 V",
            ],
            "importance": "core",
            "function": "affirmative",
            "scoring_role": "required_content",
            "evidence_ids": ["WF10_011_MMG003"],
            "synthesis_required": False,
            "numeric_required": False,
            "accepted_numeric_equivalents": [],
            "full_rule": (
                "Award full credit if the answer states that applying a negative "
                "bias caused charge-repulsion-driven desorption of bound PFOA and "
                "thereby regenerated the electrode in the reported system; the "
                "reported >80% regeneration at -1.5 V may be included."
            ),
            "partial_rule": (
                "Award partial credit if the answer links negative or reversed "
                "bias to PFOA desorption or electrode regeneration but omits the "
                "charge-repulsion explanation or the condition-specific nature."
            ),
            "contradiction_rule": (
                "Mark contradiction if the answer states that negative bias "
                "prevented PFOA desorption or regeneration in the cited system."
            ),
            "source_atomic_claim_ids": ["WF10_011-A03"],
            "exact_spans": [
                {
                    "evidence_id": "WF10_011_MMG003",
                    "exact_evidence_span": regeneration_span,
                    "supports": (
                        "Reports charge-repulsion-driven desorption of bound PFOA "
                        "under negative bias and >80% regeneration at -1.5 V."
                    ),
                }
            ],
        }
    )
    disposition = {
        "atomic_claim_id": "WF10_011-A03",
        "atomic_claim": (
            "Applying a negative bias enables desorption of bound PFOA through "
            "charge repulsion and substantial electrode regeneration."
        ),
        "evidence_ids": ["WF10_011_MMG003"],
        "action": "retained",
        "target_claim_group_ids": ["WF10_011-G03"],
        "rationale": (
            "The approved full chunk directly reports PFOA desorption under "
            "negative bias and more than 80% regeneration at -1.5 V."
        ),
    }
    insert_at = next(
        index
        for index, row in enumerate(ledger["atomic_claim_dispositions"])
        if row["atomic_claim_id"] == "WF10_011-A04"
    )
    ledger["atomic_claim_dispositions"].insert(insert_at, disposition)
    ledger["answerability_rationale"] = (
        "The approved evidence directly describes how applied voltage influences "
        "PFAS electro-adsorption rate and capacity and how negative bias enables "
        "PFOA desorption and electrode regeneration. These adsorption and "
        "regeneration endpoints are kept distinct from degradation, removal, and "
        "coagulation evidence."
    )
    stale_prefix = "The full text describes potential-controlled desorption"
    ledger["unresolved_or_unsupported"] = [
        row
        for row in ledger["unresolved_or_unsupported"]
        if not row.startswith(stale_prefix)
    ]
    regeneration_paragraph = (
        "For regeneration behavior (Task T02), the same review reports that bound "
        "PFOA was effectively desorbed by charge repulsion when a negative bias "
        "was applied, with more than 80% regeneration at -1.5 V."
        "[WF10_011_MMG003] This is a potential-controlled desorption and electrode-"
        "regeneration result, not evidence of PFAS degradation or mineralization."
    )
    anchor = "\n\nOther parts of the supplied evidence discuss"
    if anchor not in ledger["reference_answer"]:
        raise RuntimeError("WF10_011 reference-answer insertion anchor is absent")
    ledger["reference_answer"] = ledger["reference_answer"].replace(
        anchor, "\n\n" + regeneration_paragraph + anchor, 1
    )
    ledger["reference_answer_claim_map"].append(
        {
            "claim_group_id": "WF10_011-G03",
            "reference_answer_excerpt": regeneration_paragraph,
        }
    )
    ledger["boundary_check"]["notes"] = (
        "The answer covers adsorption rate/capacity and condition-specific "
        "negative-bias regeneration while explicitly separating these endpoints "
        "from degradation, bulk removal, electrocoagulation, byproduct, and "
        "mass-balance claims."
    )
    return [
        "Added core regeneration group WF10_011-G03 from a verbatim approved "
        "full-chunk sentence and restored atomic disposition WF10_011-A03.",
        "Updated answerability, unresolved boundaries, prose, and claim map to "
        "cover Task T02 without conflating regeneration with destruction endpoints.",
    ]


def main() -> None:
    packets = {
        row["question_id"]: row for row in common.read_jsonl(common.REFERENCE_PACKETS)
    }
    resolvers = {
        "NQ28": resolve_nq28,
        "WF10_009": resolve_wf10_009,
        "WF10_011": resolve_wf10_011,
    }
    output_rows = []
    resolution_rows = []
    for source_row in common.read_jsonl(SOURCE):
        row = copy.deepcopy(source_row)
        qid = row["question_id"]
        changes = []
        if qid in resolvers:
            changes = resolvers[qid](row["draft_ledger"], packets[qid])
        final_resolution.validate_with_documented_component_amendment(
            row["draft_ledger"], packets[qid], qid
        )
        row["content_resolution_provenance"] = {
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
                    "resolved_ledger_sha256": common.payload_sha256(
                        row["draft_ledger"]
                    ),
                    "changes": changes,
                    "candidate_test40_inputs_used": False,
                    "project_author_audit_required": True,
                }
            )
    common.write_jsonl(OUTPUT, output_rows)
    common.write_jsonl(RESOLUTIONS, resolution_rows)
    manifest = {
        "stage": "Test40 content resolution v1 after verbatim review",
        "question_count": len(output_rows),
        "affected_question_count": len(resolution_rows),
        "source_sha256": common.sha256(SOURCE),
        "output_sha256": common.sha256(OUTPUT),
        "resolutions_sha256": common.sha256(RESOLUTIONS),
        "candidate_test40_inputs_used": False,
        "project_author_audit_required": True,
    }
    common.write_json(
        common.PACKAGE / "reference_build/revisions/content_resolution_v1_manifest.json",
        manifest,
    )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
