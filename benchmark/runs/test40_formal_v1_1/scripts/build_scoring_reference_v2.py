from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[2]
SOURCE = (
    ROOT
    / "benchmark/runs/l3_gold_reference_test40_v1/frozen/"
    "reference_claim_ledgers_test40_v1.jsonl"
)
OUT = PACKAGE / "frozen/reference_claim_ledgers_test40_scoring_v2.jsonl"
MANIFEST = PACKAGE / "frozen/scoring_reference_v2_manifest.json"
FREEZE_RECORD = PACKAGE / "frozen/SCORING_REFERENCE_V2_FREEZE.md"
AUDIT_PACKET = PACKAGE / "frozen/scoring_reference_v2_audit_packet.json"
AUDIT_BATCH_DIR = PACKAGE / "frozen/scoring_reference_v2_audit_batches"
EXPECTED_SOURCE_SHA256 = (
    "7a805a79a72333d21fd381fc43498ffc9ebe2ea6c367f1afe0b1528cafc50b76"
)
RELEVANT_UNRESOLVED_INDEXES = {
    ("WF10_012", "WF10_012-T01"): [0],
    ("WF10_015", "WF10_015-T01"): [0],
    ("WF10_016", "WF10_016-T03"): [0],
    ("WF10_034", "WF10_034-T03"): [1],
    ("NQ07a", "NQ07a-T03"): [0],
    ("NQ07a", "NQ07a-T04"): [1],
    ("WF10_031", "WF10_031-T02"): [2],
}
AUDIT_SOURCE_GROUP_IDS = {
    ("NQ01", "NQ01-G08"): [
        "NQ01-G01",
        "NQ01-G03",
        "NQ01-G04",
        "NQ01-X01",
    ],
    ("WF10_015", "WF10_015-G05"): ["WF10_015-X01"],
    ("WF10_015", "WF10_015-G04"): ["WF10_015-G04"],
    ("WF10_016", "WF10_016-G05"): ["WF10_016-X01"],
    ("WF10_034", "WF10_034-G04"): ["WF10_034-G04"],
    ("WF10_031", "WF10_031-G03"): ["WF10_031-G01", "WF10_031-G02"],
}


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def jsonl_bytes(rows: list[dict[str, Any]]) -> bytes:
    return (
        "".join(
            json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n"
            for row in rows
        )
    ).encode("utf-8")


def group_by_id(ledger: dict[str, Any], group_id: str) -> dict[str, Any]:
    for key in ("claim_groups", "constraint_groups"):
        for group in ledger[key]:
            if group["claim_group_id"] == group_id:
                return group
    raise KeyError(group_id)


def unique_list(values: list[Any]) -> list[Any]:
    result = []
    seen = set()
    for value in values:
        marker = json.dumps(value, ensure_ascii=False, sort_keys=True)
        if marker not in seen:
            seen.add(marker)
            result.append(copy.deepcopy(value))
    return result


def limitation_group(
    *,
    claim_group_id: str,
    task_component_id: str,
    canonical_proposition: str,
    central_proposition: str,
    material_qualifiers: list[str],
    full_rule: str,
    partial_rule: str,
    contradiction_rule: str,
    source_group: dict[str, Any] | None = None,
) -> dict[str, Any]:
    source_group = source_group or {}
    return {
        "claim_group_id": claim_group_id,
        "task_component_id": task_component_id,
        "canonical_proposition": canonical_proposition,
        "central_proposition": central_proposition,
        "material_qualifiers": material_qualifiers,
        "importance": "core",
        "function": "limitation",
        "scoring_role": "required_content",
        "evidence_ids": copy.deepcopy(source_group.get("evidence_ids", [])),
        "synthesis_required": False,
        "numeric_required": False,
        "accepted_numeric_equivalents": [],
        "full_rule": full_rule,
        "partial_rule": partial_rule,
        "contradiction_rule": contradiction_rule,
        "source_atomic_claim_ids": copy.deepcopy(
            source_group.get("source_atomic_claim_ids", [])
        ),
        "exact_spans": copy.deepcopy(source_group.get("exact_spans", [])),
        "scoring_successor_basis": (
            "Candidate-blind mapping of an explicit limitation already "
            "present in the frozen reference answer, constraint groups, or "
            "unresolved_or_unsupported field. This is not a claim that no "
            "such evidence exists outside the frozen reference packet."
        ),
    }


def add_group(
    ledger: dict[str, Any],
    group: dict[str, Any],
    reference_excerpt: str,
) -> None:
    ids = {
        row["claim_group_id"]
        for row in ledger["claim_groups"] + ledger["constraint_groups"]
    }
    if group["claim_group_id"] in ids:
        raise RuntimeError(f"Duplicate group ID {group['claim_group_id']}")
    ledger["claim_groups"].append(group)
    ledger["reference_answer_claim_map"].append(
        {
            "claim_group_id": group["claim_group_id"],
            "reference_answer_excerpt": reference_excerpt,
        }
    )


def promote_group(
    ledger: dict[str, Any],
    group_id: str,
) -> None:
    group = group_by_id(ledger, group_id)
    if group not in ledger["claim_groups"]:
        raise RuntimeError(f"{group_id} is not a content claim group")
    if (
        group["importance"] != "supplementary"
        or group["scoring_role"] != "supplementary_content"
    ):
        raise RuntimeError(f"{group_id} does not have the expected source role")
    group["importance"] = "core"
    group["scoring_role"] = "required_content"
    group["scoring_successor_basis"] = (
        "Promoted from supplementary to required content because it is the "
        "existing human-audited claim that answers an otherwise unscored "
        "frozen task component."
    )


def build_nq01_group(ledger: dict[str, Any]) -> dict[str, Any]:
    sources = [
        group_by_id(ledger, group_id)
        for group_id in ("NQ01-G01", "NQ01-G03", "NQ01-G04", "NQ01-X01")
    ]
    return {
        "claim_group_id": "NQ01-G08",
        "task_component_id": "NQ01-T03",
        "canonical_proposition": (
            "Analytical-method suitability is conditional on analyte scope, "
            "matrix, and study goal: targeted LC-MS/MS supports defined-list "
            "quantification and regulatory monitoring in water; "
            "high-resolution suspect or non-target methods support broader "
            "screening in complex mixtures; and no single method is "
            "established as universally suitable across PFAS and matrices, "
            "including sludge and biosolids."
        ),
        "central_proposition": (
            "PFAS analytical methods should be selected according to target "
            "analytes, matrix, and intended use rather than treated as one "
            "universal gold standard."
        ),
        "material_qualifiers": [
            "targeted LC-MS/MS for predefined analytes and water-focused "
            "regulatory quantification",
            "high-resolution suspect or non-target analysis for broader "
            "screening in complex matrices",
            "matrix- and goal-specific suitability",
            "no universal method across all PFAS and matrices",
            "no widely recognized standard broadly applicable across "
            "sludge and biosolid matrices",
        ],
        "importance": "core",
        "function": "synthesis",
        "scoring_role": "required_content",
        "evidence_ids": unique_list(
            [value for group in sources for value in group["evidence_ids"]]
        ),
        "synthesis_required": True,
        "numeric_required": False,
        "accepted_numeric_equivalents": [],
        "full_rule": (
            "Award full credit if the answer explicitly links method "
            "suitability to analyte scope, matrix, and study goal; contrasts "
            "defined-list targeted LC-MS/MS monitoring with broader "
            "high-resolution suspect or non-target screening; and avoids a "
            "universal gold-standard claim by noting matrix limitations, "
            "including the lack of a broadly applicable recognized standard "
            "for sludge or biosolids."
        ),
        "partial_rule": (
            "Award partial credit if the answer correctly makes method "
            "selection conditional on at least two of analyte scope, matrix, "
            "and study goal, but omits either the targeted-versus-broad-"
            "screening distinction or the sludge/biosolid limitation."
        ),
        "contradiction_rule": (
            "Mark as contradictory if the answer presents one method as "
            "universally suitable or as the gold standard for all PFAS, "
            "matrices, and study goals."
        ),
        "source_atomic_claim_ids": unique_list(
            [
                value
                for group in sources
                for value in group["source_atomic_claim_ids"]
            ]
        ),
        "exact_spans": unique_list(
            [value for group in sources for value in group["exact_spans"]]
        ),
        "scoring_successor_basis": (
            "Candidate-blind synthesis of distinctions already stated in the "
            "human-audited frozen reference answer and source groups."
        ),
    }


def build_rows() -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    if sha256(SOURCE) != EXPECTED_SOURCE_SHA256:
        raise RuntimeError("Frozen Test40 v1 source hash changed")
    source_rows = [
        json.loads(line)
        for line in SOURCE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    rows = copy.deepcopy(source_rows)
    by_id = {row["question_id"]: row for row in rows}
    if len(rows) != 40 or len(by_id) != 40:
        raise RuntimeError("Expected 40 unique Test40 source ledgers")

    operations: list[dict[str, str]] = []

    ledger = by_id["NQ01"]["draft_ledger"]
    add_group(
        ledger,
        build_nq01_group(ledger),
        (
            "The suitability and generalizability of these methods are "
            "constrained by matrix and study goals... None of the sources "
            "claim any single method as universally optimal across all PFAS "
            "analytes, matrices, and applications."
        ),
    )
    operations.append(
        {
            "question_id": "NQ01",
            "task_component_id": "NQ01-T03",
            "claim_group_id": "NQ01-G08",
            "operation": "add candidate-blind synthesis group NQ01-G08",
        }
    )

    ledger = by_id["WF10_012"]["draft_ledger"]
    add_group(
        ledger,
        limitation_group(
            claim_group_id="WF10_012-G06",
            task_component_id="WF10_012-T01",
            canonical_proposition=(
                "The frozen evidence does not describe how a base membrane "
                "was modified with PVA/MOF layers or provide PVA/MOF-specific "
                "protocol steps, reagents, or materials."
            ),
            central_proposition=(
                "No PVA/MOF modification protocol can be extracted from the "
                "frozen evidence."
            ),
            material_qualifiers=[
                "limited to the frozen evidence packet",
                "PVA/MOF-specific modification protocol",
                "protocol steps, reagents, and materials are unavailable",
                "other membrane modifications must not be substituted",
            ],
            full_rule=(
                "Award full credit if the answer explicitly states that the "
                "frozen evidence does not provide PVA/MOF modification steps, "
                "reagents, or materials and does not substitute details from "
                "MXene-TiO2, PDA, PEI, or other membrane modifications."
            ),
            partial_rule=(
                "Award partial credit if the answer notes that PVA/MOF "
                "protocol evidence is missing but does not identify which "
                "requested protocol details are unavailable."
            ),
            contradiction_rule=(
                "Mark as contradictory if the answer attributes a specific "
                "PVA/MOF preparation protocol, reagent set, or modification "
                "sequence to the frozen evidence."
            ),
        ),
        (
            "The evidence set, however, does not include protocols, reagents, "
            "or operating conditions for PVA/MOF layer modifications, so no "
            "PVA/MOF-specific preparation steps or performance data can be "
            "extracted from these excerpts."
        ),
    )
    operations.append(
        {
            "question_id": "WF10_012",
            "task_component_id": "WF10_012-T01",
            "claim_group_id": "WF10_012-G06",
            "operation": "add evidence-limitation group WF10_012-G06",
        }
    )

    ledger = by_id["WF10_015"]["draft_ledger"]
    source = group_by_id(ledger, "WF10_015-X01")
    add_group(
        ledger,
        limitation_group(
            claim_group_id="WF10_015-G05",
            task_component_id="WF10_015-T01",
            canonical_proposition=(
                "The frozen evidence identifies comparison variables but "
                "does not report a start-to-finish PFAS adsorption-column "
                "protocol, so detailed operating steps cannot be extracted."
            ),
            central_proposition=(
                "No explicit stepwise adsorption-column protocol is "
                "available in the frozen evidence."
            ),
            material_qualifiers=[
                "limited to the frozen evidence packet",
                "start-to-finish adsorption-column procedure",
                "no inferred start-up, equilibration, sampling, or shutdown",
            ],
            full_rule=(
                "Award full credit if the answer explicitly distinguishes "
                "reported comparison variables from an unavailable "
                "start-to-finish protocol and states that detailed operating "
                "steps cannot be extracted."
            ),
            partial_rule=(
                "Award partial credit if the answer generally notes that "
                "procedural detail is incomplete but does not clearly state "
                "that a stepwise protocol is unavailable."
            ),
            contradiction_rule=(
                "Mark as contradictory if the answer presents unsupported "
                "start-up, equilibration, dosing, sampling, or shutdown steps "
                "as reported by the frozen evidence."
            ),
            source_group=source,
        ),
        (
            "Within the provided text, no detailed stepwise column protocol "
            "is given."
        ),
    )
    promote_group(ledger, "WF10_015-G04")
    operations.extend(
        [
            {
                "question_id": "WF10_015",
                "task_component_id": "WF10_015-T01",
                "claim_group_id": "WF10_015-G05",
                "operation": "add evidence-limitation group WF10_015-G05",
            },
            {
                "question_id": "WF10_015",
                "task_component_id": "WF10_015-T04",
                "claim_group_id": "WF10_015-G04",
                "operation": "promote WF10_015-G04 to core required content",
            },
        ]
    )

    ledger = by_id["WF10_016"]["draft_ledger"]
    source = group_by_id(ledger, "WF10_016-X01")
    add_group(
        ledger,
        limitation_group(
            claim_group_id="WF10_016-G05",
            task_component_id="WF10_016-T03",
            canonical_proposition=(
                "The frozen plasma-treatment evidence does not report "
                "mass-balance accounting of PFAS or transformation products "
                "across phases or system components."
            ),
            central_proposition=(
                "Mass-balance closure cannot be assessed from the frozen "
                "plasma-treatment evidence."
            ),
            material_qualifiers=[
                "limited to the frozen evidence span",
                "PFAS and transformation-product accounting",
                "across phases or system components",
                "distinct from degradation, defluorination, and energy use",
            ],
            full_rule=(
                "Award full credit if the answer explicitly states that "
                "mass-balance evidence is not reported and keeps this absence "
                "distinct from the reported degradation, defluorination, "
                "kinetic, and energy-use metrics."
            ),
            partial_rule=(
                "Award partial credit if the answer notes missing mass-balance "
                "information but does not distinguish it from at least one "
                "reported performance or energy metric."
            ),
            contradiction_rule=(
                "Mark as contradictory if the answer claims that the frozen "
                "span establishes PFAS or transformation-product mass-balance "
                "closure."
            ),
            source_group=source,
        ),
        (
            "Within this span, there is no explicit mass-balance accounting "
            "of PFAS or its transformation products across phases or system "
            "components."
        ),
    )
    operations.append(
        {
            "question_id": "WF10_016",
            "task_component_id": "WF10_016-T03",
            "claim_group_id": "WF10_016-G05",
            "operation": "add evidence-limitation group WF10_016-G05",
        }
    )

    ledger = by_id["WF10_034"]["draft_ledger"]
    promote_group(ledger, "WF10_034-G04")
    add_group(
        ledger,
        limitation_group(
            claim_group_id="WF10_034-G05",
            task_component_id="WF10_034-T03",
            canonical_proposition=(
                "The frozen matched-condition plating-wastewater evidence "
                "does not report how activated-carbon treatment performance "
                "or capacity changes with influent PFAS concentration."
            ),
            central_proposition=(
                "No activated-carbon concentration-response or capacity "
                "trend can be extracted from the frozen evidence."
            ),
            material_qualifiers=[
                "activated carbon in plating wastewater",
                "influent PFAS concentration dependence",
                "performance or capacity trend",
                "limited to the frozen matched-condition evidence",
            ],
            full_rule=(
                "Award full credit if the answer states that the frozen "
                "matched-condition study does not provide activated-carbon "
                "performance or capacity trends as influent PFAS "
                "concentration changes."
            ),
            partial_rule=(
                "Award partial credit if the answer notes insufficient carbon "
                "data but does not identify concentration dependence or "
                "capacity as the missing relationship."
            ),
            contradiction_rule=(
                "Mark as contradictory if the answer attributes a specific "
                "activated-carbon concentration-response, loading limit, or "
                "capacity trend to the frozen evidence."
            ),
        ),
        (
            "The study, however, does not describe how the efficiency or "
            "capacity of ion exchange or activated carbon change as influent "
            "PFAS concentrations vary."
        ),
    )
    operations.extend(
        [
            {
                "question_id": "WF10_034",
                "task_component_id": "WF10_034-T02",
                "claim_group_id": "WF10_034-G04",
                "operation": "promote WF10_034-G04 to core required content",
            },
            {
                "question_id": "WF10_034",
                "task_component_id": "WF10_034-T03",
                "claim_group_id": "WF10_034-G05",
                "operation": "add evidence-limitation group WF10_034-G05",
            },
        ]
    )

    ledger = by_id["NQ07a"]["draft_ledger"]
    add_group(
        ledger,
        limitation_group(
            claim_group_id="NQ07a-G05",
            task_component_id="NQ07a-T03",
            canonical_proposition=(
                "The frozen evidence reports water-sample containers but not "
                "the container materials used to store post-extraction PFAS "
                "extracts."
            ),
            central_proposition=(
                "Post-extraction PFAS extract-container materials cannot be "
                "specified from the frozen evidence."
            ),
            material_qualifiers=[
                "post-extraction extracts rather than collected water samples",
                "container, cap, or liner material",
                "limited to the frozen evidence packet",
            ],
            full_rule=(
                "Award full credit if the answer clearly distinguishes "
                "water-sample containers from post-extraction extracts and "
                "states that extract-container materials are not reported."
            ),
            partial_rule=(
                "Award partial credit if the answer notes missing extract "
                "container information but does not clearly distinguish the "
                "post-extraction stage from sample collection."
            ),
            contradiction_rule=(
                "Mark as contradictory if the answer transfers HDPE, glass, "
                "or polypropylene water-sample container details to "
                "post-extraction extracts as though the frozen evidence "
                "reported that use."
            ),
        ),
        (
            "No information in the provided evidence explicitly describes "
            "container materials ... for post-extraction PFAS extracts."
        ),
    )
    add_group(
        ledger,
        limitation_group(
            claim_group_id="NQ07a-G06",
            task_component_id="NQ07a-T04",
            canonical_proposition=(
                "The frozen evidence reports pre-extraction water-sample "
                "storage but not storage temperature, duration, light "
                "protection, or evaporation control for post-extraction PFAS "
                "extracts."
            ),
            central_proposition=(
                "Post-extraction PFAS extract-storage conditions cannot be "
                "specified from the frozen evidence."
            ),
            material_qualifiers=[
                "post-extraction extracts rather than collected water samples",
                "temperature, duration, light, or evaporation controls",
                "limited to the frozen evidence packet",
            ],
            full_rule=(
                "Award full credit if the answer clearly states that reported "
                "cold-storage practices concern water samples before "
                "extraction and that post-extraction extract-storage "
                "conditions are not provided."
            ),
            partial_rule=(
                "Award partial credit if the answer notes missing extract "
                "storage information but does not distinguish it from "
                "pre-extraction water-sample storage."
            ),
            contradiction_rule=(
                "Mark as contradictory if the answer applies reported "
                "pre-extraction water-sample storage conditions to "
                "post-extraction extracts as a study-reported protocol."
            ),
        ),
        (
            "No information in the provided evidence explicitly describes "
            "storage conditions for post-extraction PFAS extracts."
        ),
    )
    operations.extend(
        [
            {
                "question_id": "NQ07a",
                "task_component_id": "NQ07a-T03",
                "claim_group_id": "NQ07a-G05",
                "operation": "add evidence-limitation group NQ07a-G05",
            },
            {
                "question_id": "NQ07a",
                "task_component_id": "NQ07a-T04",
                "claim_group_id": "NQ07a-G06",
                "operation": "add evidence-limitation group NQ07a-G06",
            },
        ]
    )

    ledger = by_id["WF10_031"]["draft_ledger"]
    add_group(
        ledger,
        limitation_group(
            claim_group_id="WF10_031-G03",
            task_component_id="WF10_031-T02",
            canonical_proposition=(
                "The frozen evidence shows that natural or complex water "
                "matrices hamper comparison, but it does not provide "
                "supported detail on how individual small PFAS behave "
                "differently across natural and simpler matrices."
            ),
            central_proposition=(
                "Small-PFAS-specific matrix behavior cannot be characterized "
                "from the frozen evidence beyond the general comparability "
                "limitation."
            ),
            material_qualifiers=[
                "individual small PFAS",
                "natural raw water versus simpler matrices",
                "general matrix comparability limitation remains supported",
                "no unsupported mechanistic or quantitative detail",
            ],
            full_rule=(
                "Award full credit if the answer states that matrix "
                "differences hamper comparison while explicitly recognizing "
                "that the frozen evidence does not support a detailed "
                "small-PFAS-specific behavior claim."
            ),
            partial_rule=(
                "Award partial credit if the answer recognizes uncertainty "
                "for small PFAS but does not clearly separate it from the "
                "supported general matrix-comparability limitation."
            ),
            contradiction_rule=(
                "Mark as contradictory if the answer attributes a specific "
                "small-PFAS mechanism, direction of change, or quantitative "
                "difference across matrices to the frozen evidence."
            ),
        ),
        (
            "The available evidence does not provide approved detail on how "
            "individual small PFAS behave differently in natural raw water "
            "versus simpler matrices."
        ),
    )
    operations.append(
        {
            "question_id": "WF10_031",
            "task_component_id": "WF10_031-T02",
            "claim_group_id": "WF10_031-G03",
            "operation": "add evidence-limitation group WF10_031-G03",
        }
    )

    for row in rows:
        row["scoring_successor_provenance"] = {
            "release_id": "test40_scoring_reference_v2_2026-07-29",
            "source_release": "l3_test40_reference_v1_2026-07-29",
            "source_ledger_sha256": EXPECTED_SOURCE_SHA256,
            "candidate_test40_answers_used": False,
            "candidate_test40_contexts_used": False,
            "system_identities_used": False,
            "purpose": (
                "Make every frozen task component scoreable under the "
                "component-balanced L3 metric without changing questions, "
                "gold evidence, task components, or reference answers."
            ),
        }
    return rows, operations


def validate_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    if len(rows) != 40:
        raise RuntimeError("Scoring reference must contain 40 rows")
    missing = []
    for row in rows:
        ledger = row["draft_ledger"]
        claim_ids = [group["claim_group_id"] for group in ledger["claim_groups"]]
        constraint_ids = [
            group["claim_group_id"] for group in ledger["constraint_groups"]
        ]
        if len(claim_ids + constraint_ids) != len(set(claim_ids + constraint_ids)):
            raise RuntimeError(f"{row['question_id']}: duplicate group IDs")
        for component in ledger["task_components"]:
            component_id = component["task_component_id"]
            core = [
                group
                for group in ledger["claim_groups"]
                if group["task_component_id"] == component_id
                and group["importance"] == "core"
                and group["scoring_role"] == "required_content"
            ]
            if not core:
                missing.append(f"{row['question_id']}/{component_id}")
    if missing:
        raise RuntimeError(f"Unscoreable task components remain: {missing}")
    return {
        "question_count": len(rows),
        "task_component_count": sum(
            len(row["draft_ledger"]["task_components"]) for row in rows
        ),
        "claim_group_count": sum(
            len(row["draft_ledger"]["claim_groups"]) for row in rows
        ),
        "constraint_group_count": sum(
            len(row["draft_ledger"]["constraint_groups"]) for row in rows
        ),
        "unscoreable_task_component_count": 0,
    }


def freeze_record_text(output_hash: str) -> str:
    return f"""# Test40 scoring reference V2 freeze

Date: 2026-07-29

This is a candidate-blind scoring-compatible successor to the frozen Test40
reference release. The original release remains unchanged.

- Source ledger SHA-256: `{EXPECTED_SOURCE_SHA256}`
- Scoring ledger SHA-256: `{output_hash}`
- Candidate Test40 answers used: no
- Candidate Test40 retrieved contexts used: no
- System identities used: no
- Questions, gold chunks, task components, and reference answers changed: no
- Existing supplementary groups promoted to required core: 2
- Existing audited content mapped to new required core groups: 8

The successor fixes a structural incompatibility between the Test40 reference
ledger and component-balanced L3 scoring: ten task components previously had
no `core` + `required_content` claim. Evidence-limitation groups are explicitly
limited to the frozen reference packet and must not be interpreted as claims
that no relevant evidence exists outside that packet.
"""


def build_audit_packet(
    successor_rows: list[dict[str, Any]],
    operations: list[dict[str, str]],
) -> dict[str, Any]:
    source_rows = {
        row["question_id"]: row
        for row in [
            json.loads(line)
            for line in SOURCE.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
    }
    successor_by_id = {row["question_id"]: row for row in successor_rows}
    comparisons = []
    for operation in operations:
        qid = operation["question_id"]
        component_id = operation["task_component_id"]
        group_id = operation["claim_group_id"]
        source_ledger = source_rows[qid]["draft_ledger"]
        successor_ledger = successor_by_id[qid]["draft_ledger"]
        task_component = next(
            row
            for row in source_ledger["task_components"]
            if row["task_component_id"] == component_id
        )
        original_component_groups = [
            {
                key: copy.deepcopy(group.get(key))
                for key in (
                    "claim_group_id",
                    "canonical_proposition",
                    "importance",
                    "function",
                    "scoring_role",
                    "evidence_ids",
                )
            }
            for group in (
                source_ledger["claim_groups"]
                + source_ledger["constraint_groups"]
            )
            if group["task_component_id"] == component_id
        ]
        successor_group = next(
            group
            for group in successor_ledger["claim_groups"]
            if group["claim_group_id"] == group_id
        )
        all_unresolved = source_ledger.get("unresolved_or_unsupported", [])
        unresolved_indexes = RELEVANT_UNRESOLVED_INDEXES.get(
            (qid, component_id),
            [],
        )
        source_group_ids = AUDIT_SOURCE_GROUP_IDS.get((qid, group_id), [])
        source_groups_used = []
        for source_group_id in source_group_ids:
            source_group = group_by_id(source_ledger, source_group_id)
            source_groups_used.append(
                {
                    "claim_group_id": source_group_id,
                    "task_component_id": source_group["task_component_id"],
                    "canonical_proposition": source_group[
                        "canonical_proposition"
                    ],
                    "central_proposition": source_group[
                        "central_proposition"
                    ],
                    "importance": source_group["importance"],
                    "scoring_role": source_group["scoring_role"],
                    "evidence_ids": copy.deepcopy(source_group["evidence_ids"]),
                    "exact_span_support_summaries": [
                        span.get("supports", "")
                        for span in source_group.get("exact_spans", [])
                    ],
                }
            )
        comparisons.append(
            {
                **operation,
                "original_task_component": task_component,
                "original_component_groups": original_component_groups,
                "original_source_groups_used": source_groups_used,
                "original_unresolved_or_unsupported": [
                    copy.deepcopy(all_unresolved[index])
                    for index in unresolved_indexes
                ],
                "successor_claim_group": {
                    key: copy.deepcopy(successor_group.get(key))
                    for key in (
                        "claim_group_id",
                        "canonical_proposition",
                        "central_proposition",
                        "material_qualifiers",
                        "importance",
                        "function",
                        "scoring_role",
                        "full_rule",
                        "partial_rule",
                        "scoring_successor_basis",
                    )
                },
            }
        )
    return {
        "purpose": (
            "Compact candidate-blind review packet for the ten scoring-role "
            "repairs. It contains no candidate answer, candidate retrieved "
            "context, system identity, or Test40 outcome."
        ),
        "source_ledger_sha256": EXPECTED_SOURCE_SHA256,
        "candidate_test40_answers_used": False,
        "candidate_test40_contexts_used": False,
        "system_identities_used": False,
        "comparisons": comparisons,
    }


def expected_artifacts(
) -> tuple[bytes, dict[str, Any], str, str, list[tuple[Path, str]]]:
    rows, operations = build_rows()
    validation = validate_rows(rows)
    output_bytes = jsonl_bytes(rows)
    output_hash = sha256_bytes(output_bytes)
    freeze_text = freeze_record_text(output_hash)
    audit_packet = build_audit_packet(rows, operations)
    audit_text = json.dumps(audit_packet, indent=2, ensure_ascii=False) + "\n"
    audit_batches = []
    comparisons = audit_packet["comparisons"]
    for batch_index, start in enumerate(range(0, len(comparisons), 5), start=1):
        batch_path = AUDIT_BATCH_DIR / f"batch_{batch_index:02d}.json"
        batch_value = {
            key: copy.deepcopy(value)
            for key, value in audit_packet.items()
            if key != "comparisons"
        }
        batch_value["batch_index"] = batch_index
        batch_value["comparisons"] = comparisons[start : start + 5]
        batch_text = json.dumps(
            batch_value,
            indent=2,
            ensure_ascii=False,
        ) + "\n"
        audit_batches.append((batch_path, batch_text))
    manifest = {
        "release_id": "test40_scoring_reference_v2_2026-07-29",
        "status": "FROZEN_CANDIDATE_BLIND_SCORING_SUCCESSOR",
        "freeze_date": "2026-07-29",
        "source": {
            "path": str(SOURCE.relative_to(ROOT)),
            "sha256": EXPECTED_SOURCE_SHA256,
        },
        "output": {
            "path": str(OUT.relative_to(ROOT)),
            "sha256": output_hash,
        },
        "audit_packet": {
            "path": str(AUDIT_PACKET.relative_to(ROOT)),
            "sha256": sha256_bytes(audit_text.encode("utf-8")),
        },
        "audit_batches": {
            str(path.relative_to(ROOT)): sha256_bytes(text.encode("utf-8"))
            for path, text in audit_batches
        },
        "candidate_test40_answers_used": False,
        "candidate_test40_contexts_used": False,
        "system_identities_used": False,
        "question_text_changed": False,
        "gold_evidence_changed": False,
        "task_components_changed": False,
        "reference_answers_changed": False,
        "operations": operations,
        "validation": validation,
    }
    return output_bytes, manifest, freeze_text, audit_text, audit_batches


def write() -> None:
    (
        output_bytes,
        manifest,
        freeze_text,
        audit_text,
        audit_batches,
    ) = expected_artifacts()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(output_bytes)
    FREEZE_RECORD.write_text(freeze_text, encoding="utf-8")
    AUDIT_PACKET.write_text(audit_text, encoding="utf-8")
    AUDIT_BATCH_DIR.mkdir(parents=True, exist_ok=True)
    for path, text in audit_batches:
        path.write_text(text, encoding="utf-8")
    MANIFEST.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def verify() -> None:
    (
        output_bytes,
        manifest,
        freeze_text,
        audit_text,
        audit_batches,
    ) = expected_artifacts()
    if not OUT.exists() or OUT.read_bytes() != output_bytes:
        raise RuntimeError("Scoring reference output differs from builder")
    if not FREEZE_RECORD.exists() or FREEZE_RECORD.read_text(
        encoding="utf-8"
    ) != freeze_text:
        raise RuntimeError("Scoring reference freeze record differs")
    if not AUDIT_PACKET.exists() or AUDIT_PACKET.read_text(
        encoding="utf-8"
    ) != audit_text:
        raise RuntimeError("Scoring reference audit packet differs")
    for path, text in audit_batches:
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            raise RuntimeError(f"Scoring reference audit batch differs: {path}")
    if not MANIFEST.exists():
        raise RuntimeError("Scoring reference manifest is missing")
    actual_manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if actual_manifest != manifest:
        raise RuntimeError("Scoring reference manifest differs")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.write == args.verify:
        raise RuntimeError("Choose exactly one of --write or --verify")
    if args.write:
        write()
    else:
        verify()
    print("Test40 scoring reference V2: PASS")


if __name__ == "__main__":
    main()
