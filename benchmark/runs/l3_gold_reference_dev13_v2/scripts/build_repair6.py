from __future__ import annotations

import copy
import json
from typing import Any

import common
import run_reference_revision_v2 as revision


PACKETS = (
    common.PACKAGE
    / "reference_build/inputs/reference_packets_repair6.jsonl"
)
SOURCE_REVISIONS = (
    common.PACKAGE
    / "reference_build/revisions/model_a_revisions_v2_repair5.jsonl"
)
SOURCE_REVIEWS = (
    common.PACKAGE
    / "reference_build/reviews/model_b_group_reviews_v2_repair5.jsonl"
)
OUTPUT = (
    common.PACKAGE
    / "reference_build/revisions/model_a_revisions_v2_repair6.jsonl"
)
MANIFEST = OUTPUT.with_name("model_a_revisions_v2_repair6_manifest.json")


def remove_group(ledger: dict[str, Any], group_id: str) -> None:
    before = len(ledger["claim_groups"])
    ledger["claim_groups"] = [
        row
        for row in ledger["claim_groups"]
        if row["claim_group_id"] != group_id
    ]
    if len(ledger["claim_groups"]) != before - 1:
        raise RuntimeError(f"Expected one content group to remove: {group_id}")


def content_group(
    ledger: dict[str, Any],
    group_id: str,
) -> dict[str, Any]:
    matches = [
        row
        for row in ledger["claim_groups"]
        if row["claim_group_id"] == group_id
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one content group: {group_id}")
    return matches[0]


def disposition(
    ledger: dict[str, Any],
    atomic_claim_id: str,
) -> dict[str, Any]:
    matches = [
        row
        for row in ledger["atomic_claim_dispositions"]
        if row["atomic_claim_id"] == atomic_claim_id
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one disposition: {atomic_claim_id}")
    return matches[0]


def remove_claim_map_id(
    ledger: dict[str, Any],
    group_id: str,
) -> None:
    for row in ledger["reference_answer_claim_map"]:
        row["claim_group_ids"] = [
            value
            for value in row["claim_group_ids"]
            if value != group_id
        ]
    ledger["reference_answer_claim_map"] = [
        row
        for row in ledger["reference_answer_claim_map"]
        if row["claim_group_ids"]
    ]


def repair_nq26(ledger: dict[str, Any]) -> None:
    remove_group(ledger, "NQ26-G04")
    remove_claim_map_id(ledger, "NQ26-G04")
    g02 = content_group(ledger, "NQ26-G02")
    g02["source_atomic_claim_ids"] = ["NQ26-C02", "NQ26-C03"]
    ledger["answerability_rationale"] = (
        "The evidence describes high-pressure NF/RO separation, simple "
        "filtration or membrane-distillation concentration routes, a "
        "distinct membrane-assisted degradation route, and examples in "
        "which concentrated streams are paired with downstream destruction. "
        "This supports the requested classification while restricting the "
        "non-degradation limitation to simple separation or concentration "
        "routes. No evidence is provided for dedicated electrical membrane "
        "separation technologies or for specific modified membranes beyond "
        "the represented NF/RO and membrane-assisted examples."
    )

    updates = {
        "NQ26-C01": (
            ["NQ26-B01", "NQ26-G01"],
            (
                "The NF/RO separation and concentrated-waste-stream content "
                "is scored once in G01. B01 separately prevents treating "
                "separation as destruction without adding coverage weight."
            ),
        ),
        "NQ26-C02": (
            ["NQ26-B01", "NQ26-G02", "NQ26-G05"],
            (
                "G02 scores the concentration-only route classification, "
                "G05 scores demonstrated or proposed pairing with a separate "
                "degradation step, and B01 enforces non-conflation."
            ),
        ),
        "NQ26-C03": (
            ["NQ26-B01", "NQ26-G02"],
            (
                "The original class-level statement overlapped with the "
                "route-specific concentration evidence. It is merged into "
                "G02 and the non-scored B01 boundary rather than retained as "
                "a second required-content group."
            ),
        ),
        "NQ26-C06": (
            ["NQ26-B01", "NQ26-G03"],
            (
                "The membrane-adsorption first step is represented in G03; "
                "B01 prevents equating retention with destruction. No "
                "additional scored limitation group is needed."
            ),
        ),
    }
    for atomic_claim_id, (targets, rationale) in updates.items():
        row = disposition(ledger, atomic_claim_id)
        row["action"] = "merged" if atomic_claim_id == "NQ26-C03" else "revised"
        row["target_claim_group_ids"] = targets
        row["rationale"] = rationale

    ledger["boundary_check"]["notes"] = (
        "The ledger distinguishes high-pressure NF/RO separation, simple "
        "concentration routes, membrane-assisted degradation, and separate "
        "downstream destruction. The simple-route limitation is not "
        "generalized to every membrane-coupled process, and electrical or "
        "otherwise unrepresented membrane variants remain unresolved."
    )


def repair_wf10_002(ledger: dict[str, Any]) -> None:
    remove_group(ledger, "WF10_002-G04")
    remove_claim_map_id(ledger, "WF10_002-G04")
    g01 = content_group(ledger, "WF10_002-G01")
    g01["source_atomic_claim_ids"] = [
        "WF10_002-C01",
        "WF10_002-C02",
        "WF10_002-C03",
        "WF10_002-S01",
    ]

    ledger["answerability"] = "supported"
    ledger["answerability_rationale"] = (
        "The evidence now covers the endpoint categories named by the "
        "question: membrane NF/RO separation or rejection; concentration by "
        "filtration, adsorption, and membrane distillation; GAP parent "
        "disappearance, degradation-product formation, defluorination, and "
        "energy cost; and SCWO mineralization, short-chain byproduct "
        "formation, temperature dependence, and an example of incomplete "
        "fluorine mass-balance closure. These records support a conceptual "
        "comparison of endpoint meaning. They do not support a quantitative "
        "cross-technology performance ranking or complete mass-balance "
        "closure for every system."
    )

    g03 = content_group(ledger, "WF10_002-G03")
    g03.update(
        {
            "canonical_proposition": (
                "High-pressure NF and RO report separation or rejection of "
                "short- and long-chain PFAS, while filtration, adsorption, "
                "and membrane distillation are described as concentration "
                "treatments rather than degradation endpoints."
            ),
            "central_proposition": (
                "Membrane rejection or separation and adsorption-based "
                "concentration are distinct from PFAS degradation."
            ),
            "material_qualifiers": [
                "high-pressure membrane examples are NF and RO",
                (
                    "the membrane endpoint is separation or rejection of "
                    "short- and long-chain PFAS"
                ),
                (
                    "filtration, adsorption, and membrane distillation are "
                    "described as concentration treatments"
                ),
            ],
            "full_rule": (
                "Award full if the answer identifies membrane separation or "
                "rejection as distinct from degradation and also keeps "
                "adsorption or concentration distinct from destruction."
            ),
            "partial_rule": (
                "Award partial if the answer correctly distinguishes either "
                "membrane separation/rejection or adsorption/concentration "
                "from degradation but does not cover both."
            ),
            "contradiction_rule": (
                "Mark contradicted if the answer treats membrane rejection, "
                "adsorption, or concentration as PFAS degradation or "
                "destruction."
            ),
        }
    )

    for atomic_claim_id in ["WF10_002-C02", "WF10_002-C03"]:
        row = disposition(ledger, atomic_claim_id)
        row["action"] = "merged"
        row["target_claim_group_ids"] = ["WF10_002-G01"]
        row["rationale"] = (
            "The atomic claim describes the separateness of GAP chemical "
            "measurements already scored in G01. It is merged there rather "
            "than counted again under a second required-content group."
        )
    limitation = disposition(ledger, "WF10_002-L01")
    limitation["action"] = "revised"
    limitation["target_claim_group_ids"] = ["WF10_002-G03"]
    limitation["rationale"] = (
        "The original draft marked membrane evidence as absent. Repair5 "
        "added already audited membrane evidence, so G03 now positively "
        "represents membrane separation/rejection and concentration "
        "endpoints."
    )

    ledger["reference_answer"] = (
        "Membrane filtration reports separation or rejection: high-pressure "
        "NF and RO separate short- and long-chain PFAS, while filtration, "
        "adsorption, and membrane distillation are concentration endpoints "
        "rather than degradation endpoints. The GAP study separately "
        "reports parent-analyte disappearance, degradation-product "
        "formation, defluorination, and energy cost. The SCWO discussion "
        "reports mineralization, temperature dependence, and minimal "
        "short-chain byproduct formation as separate outcomes. Therefore "
        "membrane separation, adsorption or concentration, GAP degradation "
        "measurements, and SCWO mineralization should not be treated as "
        "interchangeable endpoints. Overall destruction and fluorine mass "
        "balance are additional interpretive outcomes: in one SCWO example, "
        "low fluorine balance at 425 and 450 C suggested undetected "
        "fluorinated gas or liquid products rather than proving complete "
        "fate closure. These distinctions are condition-specific and do not "
        "establish a universal endpoint pattern for every PFAS technology."
    )
    ledger["reference_answer_claim_map"] = [
        {
            "sentence_or_clause": (
                "Membrane filtration reports separation or rejection: "
                "high-pressure NF and RO separate short- and long-chain PFAS, "
                "while filtration, adsorption, and membrane distillation are "
                "concentration endpoints rather than degradation endpoints."
            ),
            "claim_group_ids": ["WF10_002-G03"],
        },
        {
            "sentence_or_clause": (
                "The GAP study separately reports parent-analyte "
                "disappearance, degradation-product formation, "
                "defluorination, and energy cost."
            ),
            "claim_group_ids": ["WF10_002-G01"],
        },
        {
            "sentence_or_clause": (
                "The SCWO discussion reports mineralization, temperature "
                "dependence, and minimal short-chain byproduct formation as "
                "separate outcomes."
            ),
            "claim_group_ids": ["WF10_002-G02"],
        },
        {
            "sentence_or_clause": (
                "Therefore membrane separation, adsorption or concentration, "
                "GAP degradation measurements, and SCWO mineralization should "
                "not be treated as interchangeable endpoints."
            ),
            "claim_group_ids": ["WF10_002-G05"],
        },
        {
            "sentence_or_clause": (
                "Overall destruction and fluorine mass balance are additional "
                "interpretive outcomes: in one SCWO example, low fluorine "
                "balance at 425 and 450 C suggested undetected fluorinated "
                "gas or liquid products rather than proving complete fate "
                "closure."
            ),
            "claim_group_ids": ["WF10_002-G06"],
        },
        {
            "sentence_or_clause": (
                "These distinctions are condition-specific and do not "
                "establish a universal endpoint pattern for every PFAS "
                "technology."
            ),
            "claim_group_ids": ["WF10_002-B01"],
        },
    ]
    ledger["unresolved_or_unsupported"] = [
        (
            "Complete quantitative mass-balance closure, including fluorine "
            "and carbon across parent PFAS, products, and mineralized species, "
            "is not reported for every represented system."
        ),
        (
            "Quantitative performance cannot be compared directly across "
            "membrane filtration, GAP, and SCWO because the excerpts report "
            "different endpoints and operating contexts."
        ),
    ]
    ledger["boundary_check"]["notes"] = (
        "The ledger separately represents membrane separation/rejection, "
        "adsorption or concentration, GAP disappearance, degradation "
        "products, defluorination and energy cost, SCWO mineralization and "
        "byproducts, and interpretive destruction or mass-balance outcomes. "
        "No condition-specific result is generalized to all PFAS treatments."
    )


def main() -> None:
    packets = {
        row["question_id"]: row for row in common.read_jsonl(PACKETS)
    }
    ledgers = {
        row["question_id"]: copy.deepcopy(row["revision"])
        for row in common.read_jsonl(SOURCE_REVISIONS)
    }
    tasks = {
        row["question_id"]: row
        for row in common.read_jsonl(revision.TASK_COMPONENTS)
    }
    drafts = {
        row["question_id"]: row["draft"]
        for row in common.read_jsonl(common.DRAFTS)
    }

    repair_nq26(ledgers["NQ26"])
    repair_wf10_002(ledgers["WF10_002"])

    for question_id, ledger in ledgers.items():
        revision.validate_revision(
            ledger,
            packets[question_id],
            tasks[question_id],
            drafts[question_id],
        )

    rows = [
        {"question_id": question_id, "revision": ledgers[question_id]}
        for question_id in sorted(ledgers)
    ]
    common.write_jsonl(OUTPUT, rows)
    common.write_json(
        MANIFEST,
        {
            "stage": "Model A deterministic repair6 claim-ledger revision",
            "source_revisions_file": str(
                SOURCE_REVISIONS.relative_to(common.ROOT)
            ),
            "source_revisions_sha256": common.sha256(SOURCE_REVISIONS),
            "source_reviews_file": str(SOURCE_REVIEWS.relative_to(common.ROOT)),
            "source_reviews_sha256": common.sha256(SOURCE_REVIEWS),
            "packets_file": str(PACKETS.relative_to(common.ROOT)),
            "packets_sha256": common.sha256(PACKETS),
            "output_file": str(OUTPUT.relative_to(common.ROOT)),
            "output_sha256": common.sha256(OUTPUT),
            "question_count": len(rows),
            "changed_question_ids": ["NQ26", "WF10_002"],
            "repairs": [
                {
                    "question_id": "NQ26",
                    "removed_group": "NQ26-G04",
                    "reason": (
                        "Removed duplicate required-content weighting; G02 "
                        "scores simple concentration routes, G03 describes "
                        "membrane-assisted degradation, and B01 enforces the "
                        "distinction without adding coverage weight."
                    ),
                },
                {
                    "question_id": "WF10_002",
                    "removed_group": "WF10_002-G04",
                    "reason": (
                        "Merged the duplicate GAP endpoint-separation group "
                        "into G01 and corrected stale pre-transfer statements "
                        "about missing membrane evidence."
                    ),
                },
            ],
            "candidate_answers_used": False,
            "project_author_decisions_written": False,
        },
    )
    print(
        json.dumps(
            {
                "questions": len(rows),
                "changed_question_ids": ["NQ26", "WF10_002"],
                "output": str(OUTPUT),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
