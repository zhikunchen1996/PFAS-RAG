from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

import common
import run_reference_revision_v2 as revision


PACKETS = (
    common.PACKAGE
    / "reference_build/inputs/reference_packets_repair5.jsonl"
)
SOURCE_REVISIONS = (
    common.PACKAGE
    / "reference_build/revisions/model_a_revisions_v2_repair4.jsonl"
)
SOURCE_REVIEWS = (
    common.PACKAGE
    / "reference_build/reviews/model_b_group_reviews_v2_repair4.jsonl"
)
PREAUDIT = (
    common.PACKAGE
    / "human_review_v2/AI_ASSISTED_PREAUDIT_2026-07-29.md"
)
OUTPUT = (
    common.PACKAGE
    / "reference_build/revisions/model_a_revisions_v2_repair5.jsonl"
)
MANIFEST = OUTPUT.with_name("model_a_revisions_v2_repair5_manifest.json")


def content_group(ledger: dict[str, Any], group_id: str) -> dict[str, Any]:
    matches = [
        row
        for row in ledger["claim_groups"]
        if row["claim_group_id"] == group_id
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one content group: {group_id}")
    return matches[0]


def update_group(
    ledger: dict[str, Any],
    group_id: str,
    **fields: Any,
) -> None:
    content_group(ledger, group_id).update(fields)


def set_reference(
    ledger: dict[str, Any],
    clauses: list[tuple[str, list[str]]],
) -> None:
    ledger["reference_answer"] = " ".join(text for text, _ in clauses)
    ledger["reference_answer_claim_map"] = [
        {
            "sentence_or_clause": text,
            "claim_group_ids": group_ids,
        }
        for text, group_ids in clauses
    ]


def sync_exact_spans(
    ledger: dict[str, Any],
    packet: dict[str, Any],
) -> None:
    evidence_by_id = {
        row["evidence_id"]: row for row in packet["gold_evidence"]
    }
    for group in ledger["claim_groups"] + ledger["constraint_groups"]:
        evidence_ids = [str(value) for value in group.get("evidence_ids", [])]
        if not evidence_ids and group.get("scoring_role") == "constraint_only":
            group["exact_spans"] = []
            continue
        old_support = {
            str(row.get("evidence_id", "")): str(
                row.get("supports", "")
            ).strip()
            for row in group.get("exact_spans", [])
            if isinstance(row, dict)
        }
        group["exact_spans"] = [
            {
                "evidence_id": evidence_id,
                "exact_evidence_span": evidence_by_id[evidence_id][
                    "exact_evidence_span"
                ],
                "supports": (
                    old_support.get(evidence_id)
                    or evidence_by_id[evidence_id]["exact_evidence_span"]
                ),
            }
            for evidence_id in evidence_ids
        ]


def repair_nq10(ledger: dict[str, Any]) -> None:
    update_group(
        ledger,
        "NQ10-G05",
        canonical_proposition=(
            "In one PFAS extraction workflow, elution into a 0.5 mL "
            "methanolic extract produced an effective 500-fold concentration "
            "of target analytes relative to the initial sample."
        ),
        central_proposition=(
            "A 0.5 mL methanolic extract produced about 500-fold enrichment "
            "of target PFAS analytes."
        ),
        material_qualifiers=[
            "eluted extract volume is 0.5 mL",
            "effective concentration factor is about 500-fold",
            (
                "the exact span does not independently identify the source "
                "water matrix, so no groundwater qualifier is required"
            ),
        ],
        full_rule=(
            "Award full if the answer reports both the 0.5 mL methanolic "
            "extract and the approximately 500-fold concentration factor "
            "without adding an unsupported matrix attribution."
        ),
        partial_rule=(
            "Award partial if the answer reports only one of the two "
            "numerical details or describes a large enrichment without both."
        ),
        contradiction_rule=(
            "Mark contradicted if the answer gives incompatible values or "
            "denies that the workflow produced substantial enrichment."
        ),
    )
    update_group(
        ledger,
        "NQ10-G04",
        canonical_proposition=(
            "Some PFAS analytical workflows use dilution-based preparation "
            "rather than a separately described extraction step: EPA Method "
            "8327 uses dilute-and-shoot for drinking water, while the cited "
            "foam-concentrate excerpt describes dilution and reagent mixing "
            "before HPLC injection without explicitly describing SPE or LLE."
        ),
        central_proposition=(
            "Dilution-based PFAS workflows include EPA Method 8327 "
            "dilute-and-shoot and a foam-concentrate preparation excerpt that "
            "does not describe a separate SPE or LLE step."
        ),
        material_qualifiers=[
            (
                "EPA Method 8327 is a drinking-water dilute-and-shoot "
                "workflow covering 24 PFAS compounds."
            ),
            (
                "The foam-concentrate excerpt directly reports dilution, "
                "reagent mixing, and HPLC injection; absence of a separate "
                "extraction step is limited to what that excerpt describes."
            ),
        ],
        full_rule=(
            "Award full if the answer identifies both the EPA Method 8327 "
            "dilute-and-shoot example and the foam-concentrate "
            "dilution/reagent-mixing example, while framing the latter only "
            "as having no separate extraction step described in the cited "
            "excerpt. A complete reagent inventory is not required."
        ),
        partial_rule=(
            "Award partial if the answer correctly describes one of the two "
            "dilution-based examples or describes both but omits the excerpt-"
            "limited hedge for the foam-concentrate workflow."
        ),
        contradiction_rule=(
            "Mark contradicted if the answer says EPA Method 8327 requires "
            "SPE/LLE or claims that the foam-concentrate excerpt explicitly "
            "proves no extraction occurred anywhere in the full workflow."
        ),
    )
    set_reference(
        ledger,
        [
            (
                "PFAS sample preparation before mass spectrometry varies with "
                "matrix, analyte scope, and analytical workflow rather than "
                "following one universal protocol.",
                ["NQ10-B01"],
            ),
            (
                "For parts-per-trillion determinations, reported "
                "preconcentration approaches include solid-phase extraction "
                "(SPE) and liquid-liquid extraction (LLE).",
                ["NQ10-G01"],
            ),
            (
                "Sorptive formats include an SPME method applied to river, "
                "lake, tap, and bottled water and an SBSE-TD-GC-MS method for "
                "PFCAs.",
                ["NQ10-G02", "NQ10-G03"],
            ),
            (
                "Dilution-based alternatives include EPA Method 8327 "
                "dilute-and-shoot and a foam-concentrate excerpt that reports "
                "dilution and reagent mixing before HPLC injection but does "
                "not explicitly describe a separate SPE or LLE step.",
                ["NQ10-G04"],
            ),
            (
                "Study-specific examples include a 0.5 mL methanolic extract "
                "with about 500-fold enrichment, lower SPE recovery when "
                "sample volume increased from 10 to 100 mL with a 150 mg "
                "cartridge, and compound-dependent recoveries for C8-C14 PFAS.",
                ["NQ10-G05", "NQ10-G06", "NQ10-G07"],
            ),
            (
                "In the developed SPME protocol, preconcentration was higher "
                "and matrix effects were less frequent than for very rapid "
                "methods such as dilute-and-shoot.",
                ["NQ10-G08"],
            ),
            (
                "Other cited methods showed substantial matrix effects in "
                "complex samples, so recovery and robustness must be "
                "evaluated for the specific matrix and analyte set.",
                ["NQ10-G09", "NQ10-B01"],
            ),
        ],
    )


def repair_nq12(ledger: dict[str, Any]) -> None:
    update_group(
        ledger,
        "NQ12-G02",
        canonical_proposition=(
            "In the reported SBSE-TD-GC-MS performance table for PFCAs "
            "PFHpA, PFOA, PFNA, PFDA, PFUnA, PFDoA, and PFTeDA, sensitivity "
            "is compound-specific, with LODs of about 21-74 ng/L and LOQs of "
            "about 91-192 ng/L."
        ),
        central_proposition=(
            "The SBSE-TD-GC-MS PFCA table reports compound-specific LODs of "
            "about 21-74 ng/L and LOQs of about 91-192 ng/L."
        ),
        material_qualifiers=[
            "method is SBSE-TD-GC-MS",
            (
                "compounds are PFHpA, PFOA, PFNA, PFDA, PFUnA, PFDoA, "
                "and PFTeDA"
            ),
            "LOD values span approximately 21-74 ng/L",
            "LOQ values span approximately 91-192 ng/L",
            (
                "the expanded exact span does not independently identify the "
                "sample matrix, so no matrix-specific claim is required"
            ),
        ],
        full_rule=(
            "Award full if the answer identifies the SBSE-TD-GC-MS PFCA "
            "table and reports compound-specific LOD and LOQ ranges "
            "equivalent to about 21-74 and 91-192 ng/L, respectively."
        ),
        partial_rule=(
            "Award partial if the answer correctly reports only one range or "
            "states that sensitivity varies by compound without both ranges."
        ),
        contradiction_rule=(
            "Mark contradicted if the answer swaps LOD and LOQ, gives "
            "incompatible ranges, or claims one identical detection limit for "
            "all listed PFCAs."
        ),
    )
    update_group(
        ledger,
        "NQ12-G03",
        canonical_proposition=(
            "The two reported method tables show different absolute "
            "sensitivity ranges: SPE-UHPLC-MS/MS reports LODs of 3-8 ng/L and "
            "LOQs of 9-25 ng/L for its C8-C14 PFAS set, whereas "
            "SBSE-TD-GC-MS reports LODs of 21.17-73.96 ng/L and LOQs of "
            "90.80-192.01 ng/L for a different C7-C14 PFCA set. This is a "
            "descriptive cross-study comparison and does not isolate method "
            "choice as the cause because analyte sets and protocols differ."
        ),
        central_proposition=(
            "The two method tables report different LOD/LOQ ranges, but the "
            "cross-study difference is descriptive and confounded."
        ),
        material_qualifiers=[
            (
                "SPE-UHPLC-MS/MS table: LOD 3-8 ng/L and LOQ 9-25 "
                "ng/L for its listed C8-C14 PFAS"
            ),
            (
                "SBSE-TD-GC-MS table: LOD 21.17-73.96 ng/L and LOQ "
                "90.80-192.01 ng/L for its listed C7-C14 PFCAs"
            ),
            (
                "the studies use different analyte sets and protocols, so "
                "the comparison does not establish method-only causation"
            ),
        ],
        full_rule=(
            "Award full if the answer correctly compares both LOD/LOQ ranges "
            "and explicitly notes that different analyte sets and protocols "
            "prevent attributing the difference solely to method choice."
        ),
        partial_rule=(
            "Award partial if the ranges are compared correctly but the "
            "cross-study confounding caveat is omitted, or if the caveat is "
            "given without both numerical ranges."
        ),
        contradiction_rule=(
            "Mark contradicted if the ranges are reversed or if the answer "
            "claims the comparison proves that method choice alone caused "
            "the difference."
        ),
    )
    update_group(
        ledger,
        "NQ12-G06",
        canonical_proposition=(
            "In the SBSE-TD-GC-MS table, individual LOD/LOQ pairs were PFHpA "
            "21.17/138.27 ng/L, PFOA 21.20/103.13 ng/L, PFNA "
            "30.12/90.80 ng/L, PFDA 54.29/169.85 ng/L, PFUnA "
            "34.39/132.90 ng/L, PFDoA 73.96/192.01 ng/L, and PFTeDA "
            "35.02/107.10 ng/L."
        ),
        central_proposition=(
            "The SBSE-TD-GC-MS table reports a distinct LOD/LOQ pair for "
            "each listed PFCA."
        ),
        material_qualifiers=[
            "method is SBSE-TD-GC-MS",
            "LOD/LOQ values are in ng/L",
            "each listed PFCA is paired with its tabulated values",
            "no sample-matrix qualifier is required from this exact span",
        ],
        full_rule=(
            "Award optional full credit if all listed compound-specific "
            "LOD/LOQ pairs are reported correctly for the SBSE-TD-GC-MS table."
        ),
        partial_rule=(
            "Award optional partial credit if at least two listed pairs are "
            "reported correctly without incompatible values."
        ),
        contradiction_rule=(
            "Mark contradicted if LOD and LOQ are swapped or a listed pair is "
            "materially misstated."
        ),
    )
    update_group(
        ledger,
        "NQ12-G07",
        canonical_proposition=(
            "In the SBSE-TD-GC-MS PFCA table, retention time and parent-ion "
            "m/z increase from PFHpA to PFTeDA, whereas LOD and LOQ values "
            "vary without a simple monotonic trend."
        ),
        central_proposition=(
            "Retention time and parent-ion mass increase across the listed "
            "PFCAs, while LOD/LOQ values are non-monotonic."
        ),
        material_qualifiers=[
            "applies to PFHpA through PFTeDA in the reported table",
            "method is SBSE-TD-GC-MS",
            "retention time and parent-ion m/z increase across the series",
            "LOD/LOQ values do not change monotonically",
            "no sample-matrix qualifier is required from this exact span",
        ],
        full_rule=(
            "Award optional full credit if the answer reports both the "
            "monotonic retention-time/parent-ion trend and the non-monotonic "
            "LOD/LOQ pattern."
        ),
        partial_rule=(
            "Award optional partial credit if only one of those two patterns "
            "is reported correctly."
        ),
        contradiction_rule=(
            "Mark contradicted if the answer claims LOD/LOQ changes "
            "monotonically across all listed PFCAs."
        ),
    )
    update_group(
        ledger,
        "NQ12-G04",
        canonical_proposition=(
            "In a fragmentor-voltage test for carboxylic acids, setting the "
            "fragmentor to 60 V almost eliminated the signal of short-chain "
            "PFAS (C < 5), so that setting was discarded; the excerpt reports "
            "signal loss rather than numerical LOD or LOQ values."
        ),
        central_proposition=(
            "A 60 V fragmentor setting almost eliminated short-chain PFAS "
            "signal and was discarded."
        ),
        material_qualifiers=[
            "instrument variable is fragmentor voltage",
            "setting is 60 V",
            "affected analytes are short-chain PFAS with C < 5",
            "endpoint is near-loss of signal, not a reported LOD/LOQ",
        ],
        full_rule=(
            "Award full if the answer states that 60 V almost eliminated "
            "C < 5 PFAS signal and was discarded, while not inventing a "
            "numeric LOD or LOQ."
        ),
        partial_rule=(
            "Award partial if the answer identifies fragmentor-voltage "
            "sensitivity for short-chain PFAS but omits either 60 V or the "
            "decision to discard the setting."
        ),
        contradiction_rule=(
            "Mark contradicted if the answer says 60 V improved short-chain "
            "signal or assigns a numerical LOD/LOQ not present in the span."
        ),
    )
    update_group(
        ledger,
        "NQ12-G08",
        canonical_proposition=(
            "The tabulated patterns are compound- and protocol-specific: "
            "within-table LOD/LOQ values are non-monotonic, and cross-study "
            "differences cannot be assigned solely to chain length or method "
            "because the analyte sets and protocols differ."
        ),
        central_proposition=(
            "The observed sensitivity patterns are non-monotonic and "
            "protocol-specific rather than a universal chain-length rule."
        ),
        material_qualifiers=[
            "applies only to the two reported tables",
            "cross-study comparison is confounded by analyte and protocol differences",
        ],
        full_rule=(
            "Award full if the answer rejects a universal monotonic "
            "chain-length rule and identifies compound/protocol specificity."
        ),
        partial_rule=(
            "Award partial if the answer gives only one of the two "
            "limitations without making a universal claim."
        ),
        contradiction_rule=(
            "Mark contradicted if the answer asserts a universal monotonic "
            "LOD/LOQ relationship across PFAS and methods."
        ),
    )
    update_group(
        ledger,
        "NQ12-G09",
        canonical_proposition=(
            "The quantitative findings are limited to the listed C8-C14 PFAS "
            "and C7-C14 PFCA sets under the two reported methods; only the "
            "SPE-UHPLC-MS/MS span explicitly identifies water samples, so the "
            "combined evidence must not be generalized to all matrices."
        ),
        central_proposition=(
            "The ranges are limited to the listed compounds and methods and "
            "do not establish performance in all matrices."
        ),
        material_qualifiers=[
            "compound and method scope must be retained",
            (
                "water is explicit for the SPE-UHPLC-MS/MS table but is not "
                "required for the SBSE-TD-GC-MS exact span"
            ),
        ],
        full_rule=(
            "Award full if the answer limits the ranges to the listed "
            "compound sets and methods and avoids generalizing them to all "
            "PFAS or matrices."
        ),
        partial_rule=(
            "Award partial if the answer gives a general scope caveat but "
            "does not distinguish the two compound sets."
        ),
        contradiction_rule=(
            "Mark contradicted if the answer treats the values as universal "
            "across PFAS classes, methods, or matrices."
        ),
    )
    set_reference(
        ledger,
        [
            (
                "The SPE-UHPLC-MS/MS table for C8-C14 PFAS in water reports "
                "compound-specific LODs of 3-8 ng/L and LOQs of 9-25 ng/L.",
                ["NQ12-G01", "NQ12-G05"],
            ),
            (
                "The SBSE-TD-GC-MS PFCA table reports LODs of 21.17-73.96 "
                "ng/L and LOQs of 90.80-192.01 ng/L, with retention time and "
                "parent-ion mass increasing across the listed homologues but "
                "LOD/LOQ values not following a simple monotonic pattern.",
                ["NQ12-G02", "NQ12-G06", "NQ12-G07"],
            ),
            (
                "These two tables have different sensitivity ranges, but the "
                "comparison is descriptive because their analyte sets and "
                "protocols differ and therefore does not isolate method "
                "choice as the cause.",
                ["NQ12-G03", "NQ12-G08"],
            ),
            (
                "Separately, a 60 V fragmentor setting almost eliminated the "
                "signal of short-chain PFAS (C < 5) and was discarded, "
                "showing an instrument-setting effect without reporting a "
                "numerical LOD or LOQ.",
                ["NQ12-G04"],
            ),
            (
                "The findings remain limited to the listed compounds and "
                "methods and do not support a universal chain-length, method, "
                "or matrix rule.",
                ["NQ12-G08", "NQ12-G09", "NQ12-B01"],
            ),
        ],
    )


def repair_nq15(ledger: dict[str, Any]) -> None:
    update_group(
        ledger,
        "NQ15-G01",
        canonical_proposition=(
            "Across PFAS electro-oxidation studies, there is no reported "
            "consensus on the effects of pH."
        ),
        central_proposition=(
            "There is no reported consensus on pH effects in the cited PFAS "
            "electro-oxidation literature."
        ),
        material_qualifiers=[
            "the statement is limited to the cited review",
            (
                "the span does not itself explain why consensus is absent or "
                "quantify between-study disagreement"
            ),
        ],
        full_rule=(
            "Award full if the answer states that the cited literature reports "
            "no consensus on pH effects without inventing a consensus trend."
        ),
        partial_rule=(
            "Award partial if the answer describes pH effects as uncertain or "
            "inconsistent but does not explicitly state the lack of consensus."
        ),
        contradiction_rule=(
            "Mark contradicted if the answer claims the cited review reports "
            "one settled pH-effect direction."
        ),
    )
    update_group(
        ledger,
        "NQ15-G03",
        canonical_proposition=(
            "Across the cited electro-oxidation, electro-coagulation, and "
            "non-thermal-plasma examples, electrolyte composition or ion "
            "identity changes PFAS removal or degradation behavior, so the "
            "electrolyte is a mechanistically active experimental variable."
        ),
        central_proposition=(
            "Electrolyte composition can change PFAS treatment performance "
            "and should be treated as mechanistically active."
        ),
        material_qualifiers=[
            "evidence spans three different treatment configurations",
            "effects are study- and mechanism-specific",
            "no named pH buffer is directly tested in the supplied evidence",
        ],
        full_rule=(
            "Award full if the answer states that electrolyte composition or "
            "ion identity can change PFAS treatment performance and treats "
            "the effect as system-specific rather than universal."
        ),
        partial_rule=(
            "Award partial if the answer notes an electrolyte effect but does "
            "not state that the direction or mechanism depends on the system."
        ),
        contradiction_rule=(
            "Mark contradicted if the answer treats electrolyte composition "
            "as inert or claims one observed ordering is universal."
        ),
    )
    update_group(
        ledger,
        "NQ15-G09",
        importance="core",
        scoring_role="required_content",
        canonical_proposition=(
            "The supplied evidence does not directly compare named pH "
            "buffers, so it cannot establish a buffer-specific performance "
            "rule. Electrolyte results motivate testing whether ions used for "
            "pH control interfere with a treatment system, but that extension "
            "is an explicitly identified inference rather than a measured "
            "buffer result."
        ),
        central_proposition=(
            "No named buffer is directly compared, so buffer-specific effects "
            "cannot be claimed from these records."
        ),
        material_qualifiers=[
            "the limitation concerns the supplied evidence set",
            "buffer-specific behavior is not directly measured",
            (
                "using electrolyte evidence to motivate buffer-interference "
                "testing is an inference, not a reported result"
            ),
        ],
        full_rule=(
            "Award full if the answer explicitly states that no named buffer "
            "is directly compared and therefore avoids a buffer-specific "
            "recommendation, while allowing a clearly labeled inference that "
            "pH-control ions should be tested for interference."
        ),
        partial_rule=(
            "Award partial if the answer avoids recommending a universal "
            "buffer but does not explicitly identify the buffer-evidence gap."
        ),
        contradiction_rule=(
            "Mark contradicted if the answer presents a specific buffer as "
            "experimentally proven optimal by these records."
        ),
    )
    set_reference(
        ledger,
        [
            (
                "The cited review reports no consensus on pH effects and "
                "warns that relying only on initial pH can mislead "
                "interpretation of PFAS degradation.",
                ["NQ15-G01", "NQ15-G02"],
            ),
            (
                "In one electro-oxidation study, degradation of 6:2 "
                "fluorotelomer sulfonic acid decreased in the order NaClO4 > "
                "NaCl > Na2SO4.",
                ["NQ15-G06"],
            ),
            (
                "In Fe-anode electro-coagulation, PFOS removal was 99.6% in "
                "NaCl, 93.7% in Na2SO4, 63.5% in NaNO3, and 45.4% in "
                "NaH2PO4.",
                ["NQ15-G07"],
            ),
            (
                "A non-thermal-plasma comparison also attributed differing "
                "PFOS breakdown rates in solutions of similar conductivity "
                "to a possible difference in monovalent and divalent ions.",
                ["NQ15-G08"],
            ),
            (
                "Together, these examples show that electrolyte composition "
                "is mechanistically active and that its effect is specific to "
                "the treatment configuration rather than transferable as one "
                "universal ordering.",
                ["NQ15-G03", "NQ15-G05"],
            ),
            (
                "No supplied span directly compares named pH buffers, so a "
                "buffer-specific recommendation is unsupported; at most, the "
                "electrolyte evidence motivates explicitly testing whether "
                "ions introduced for pH control interfere with the selected "
                "system.",
                ["NQ15-G09", "NQ15-B01"],
            ),
        ],
    )


def repair_nq23(ledger: dict[str, Any]) -> None:
    update_group(
        ledger,
        "NQ23-G09",
        canonical_proposition=(
            "A consolidated comparison presented reported EE/O values "
            "together with water type, initial PFAS concentration, reactor "
            "scale, reaction time, and removal or defluorination efficiency "
            "to support transparent, context-aware evaluation across "
            "technologies."
        ),
        central_proposition=(
            "EE/O is more transparently interpreted when reported with key "
            "experimental parameters and treatment outcomes."
        ),
        material_qualifiers=[
            "the source describes a consolidated comparison in Table S1",
            (
                "listed context includes water type, concentration, scale, "
                "time, and removal or defluorination efficiency"
            ),
            (
                "the source supports context-aware comparison but does not "
                "state that comparison is impossible without every field"
            ),
        ],
        full_rule=(
            "Award full if the answer says the source paired EE/O with key "
            "experimental parameters to support transparent context-aware "
            "comparison, without making the absolute claim that every "
            "comparison lacking all fields is meaningless."
        ),
        partial_rule=(
            "Award partial if the answer generally recommends contextualizing "
            "EE/O but omits most of the listed parameters."
        ),
        contradiction_rule=(
            "Mark contradicted if the answer says EE/O values are directly "
            "comparable without experimental context or claims the source "
            "proved comparison is impossible unless every listed field is "
            "present."
        ),
    )
    update_group(
        ledger,
        "NQ23-G10",
        importance="supplementary",
        scoring_role="optional_content",
        canonical_proposition=(
            "Taken together, the different energy metrics, broad reported "
            "ranges, nonuniform conditions, and use of contextual comparison "
            "tables indicate that no single energy-consumption value "
            "represents all PFAS degradation methods."
        ),
        central_proposition=(
            "No single energy value represents all PFAS degradation methods."
        ),
        full_rule=(
            "Award optional full credit if the answer synthesizes metric "
            "differences, variability, and contextual conditions into a "
            "non-universal conclusion."
        ),
        partial_rule=(
            "Award optional partial credit if the answer gives the "
            "non-universal conclusion with only one supporting reason."
        ),
        contradiction_rule=(
            "Mark contradicted if the answer proposes one universal "
            "energy-consumption value for all PFAS degradation methods."
        ),
    )
    set_reference(
        ledger,
        [
            (
                "PFAS degradation studies report non-interchangeable energy "
                "metrics, including electrical energy per order in kWh/m3 or "
                "kWh/m3/order and energy yield in mg/kWh.",
                ["NQ23-G01"],
            ),
            (
                "A hydrodynamic-cavitation PFOS study reported EEO values of "
                "7-598 kWh/m3/order and energy yields of 17-286 mg/kWh, while "
                "other plasma examples reported different ranges and "
                "compound-specific values.",
                ["NQ23-G02", "NQ23-G03", "NQ23-G04"],
            ),
            (
                "Pilot examples also differ in how energy is defined or "
                "reported, including explicit equipment loads or a referenced "
                "calculation equation without values in the selected excerpt.",
                ["NQ23-G06", "NQ23-G07"],
            ),
            (
                "A review attributes the broad ranges to uncertainty and "
                "nonuniform experimental conditions, which limits direct "
                "cross-study comparison.",
                ["NQ23-G08"],
            ),
            (
                "Another comparison paired EE/O with water type, initial PFAS "
                "concentration, reactor scale, reaction time, and removal or "
                "defluorination efficiency to support transparent "
                "context-aware interpretation.",
                ["NQ23-G09"],
            ),
            (
                "Consequently, no single energy-consumption number represents "
                "all PFAS degradation methods.",
                ["NQ23-G10", "NQ23-B01"],
            ),
        ],
    )


def repair_nq24(ledger: dict[str, Any]) -> None:
    for group_id in ["NQ24-G01", "NQ24-G02", "NQ24-G03"]:
        group = content_group(ledger, group_id)
        group["evidence_ids"] = [
            "NQ24_L3CTX001",
            "NQ24_MMG001",
        ]
    set_reference(
        ledger,
        [
            (
                "The source study concerns PFOA adsorption from aqueous media "
                "using CTAB-impregnated activated carbon.",
                ["NQ24-G01", "NQ24-G02", "NQ24-G03"],
            ),
            (
                "Its batch Langmuir result was 6.85 mg/g with 125-250 um "
                "particles.",
                ["NQ24-G01"],
            ),
            (
                "Its fixed-bed Thomas-model result was 5.71 mg/g with "
                "125-500 um particles and a background water matrix.",
                ["NQ24-G02"],
            ),
            (
                "The authors attributed the marginally lower column value "
                "mainly to the background matrix and larger particles, so the "
                "two modeled capacities are study-specific and do not define "
                "a universal batch-column relationship.",
                ["NQ24-G03", "NQ24-B01"],
            ),
        ],
    )


def repair_nq26(ledger: dict[str, Any]) -> None:
    update_group(
        ledger,
        "NQ26-G04",
        canonical_proposition=(
            "Simple PFAS concentration or separation routes such as "
            "filtration, membrane distillation, and forward osmosis do not "
            "themselves degrade PFAS. This limitation does not include "
            "membrane-assisted systems in which PFAS are first accumulated on "
            "a membrane and then degraded under light or an electric field."
        ),
        central_proposition=(
            "Simple membrane concentration routes do not themselves degrade "
            "PFAS, whereas coupled membrane-assisted degradation is a "
            "distinct category."
        ),
        material_qualifiers=[
            (
                "the non-degradation statement is restricted to simple "
                "separation or concentration routes"
            ),
            (
                "membrane-assisted degradation is explicitly excluded from "
                "the simple-route limitation"
            ),
        ],
        evidence_ids=["NQ26_MMG002", "NQ26_MMG005"],
        full_rule=(
            "Award full if the answer states that simple membrane "
            "separation/concentration routes do not themselves degrade PFAS "
            "and explicitly distinguishes coupled membrane-assisted "
            "degradation."
        ),
        partial_rule=(
            "Award partial if the answer correctly describes simple membrane "
            "routes as concentration without explicitly exempting coupled "
            "membrane-assisted degradation."
        ),
        contradiction_rule=(
            "Mark contradicted if the answer equates membrane separation with "
            "destruction or says no membrane-coupled system can degrade PFAS."
        ),
    )
    set_reference(
        ledger,
        [
            (
                "High-pressure nanofiltration and reverse osmosis are "
                "separation routes that can reject both short- and long-chain "
                "PFAS and produce a concentrated waste stream.",
                ["NQ26-G01"],
            ),
            (
                "Simple filtration, membrane distillation, and forward-osmosis "
                "routes concentrate or separate PFAS but do not themselves "
                "degrade it.",
                ["NQ26-G02", "NQ26-G04"],
            ),
            (
                "That limitation does not apply to the distinct "
                "membrane-assisted degradation category, in which PFAS are "
                "first accumulated on a membrane and then degraded under "
                "light or an electric field.",
                ["NQ26-G03", "NQ26-G04"],
            ),
            (
                "Concentrated PFAS streams can therefore be paired with a "
                "separate destruction or degradation step.",
                ["NQ26-G05"],
            ),
            (
                "The evidence also notes poor removal by some low-pressure "
                "membranes and an example in which concentrate residue is "
                "incinerated downstream.",
                ["NQ26-G06", "NQ26-G07"],
            ),
            (
                "Separation or retention must not be reported as destruction "
                "unless an explicit degradation step is present.",
                ["NQ26-B01", "NQ26-B02"],
            ),
        ],
    )


def repair_wf10_002(ledger: dict[str, Any]) -> None:
    update_group(
        ledger,
        "WF10_002-G03",
        function="affirmative",
        canonical_proposition=(
            "For membrane filtration, high-pressure NF and RO report "
            "separation or rejection of both short- and long-chain PFAS, "
            "typically above 90%, while filtration and membrane distillation "
            "are concentration routes rather than degradation endpoints."
        ),
        central_proposition=(
            "Membrane filtration reports separation/rejection and "
            "concentration, not degradation by the membrane step itself."
        ),
        material_qualifiers=[
            "high-pressure membrane examples are NF and RO",
            "endpoint is rejection or separation, typically above 90%",
            "simple filtration and membrane distillation concentrate PFAS",
        ],
        evidence_ids=["WF10_002_L3X001", "WF10_002_L3X002"],
        full_rule=(
            "Award full if the answer identifies membrane separation or "
            "rejection as distinct from degradation, mentions NF/RO rejection "
            "of short- and long-chain PFAS, and notes that simple membrane "
            "routes concentrate PFAS."
        ),
        partial_rule=(
            "Award partial if the answer correctly identifies membrane "
            "separation/concentration but omits either NF/RO scope or the "
            "reported rejection level."
        ),
        contradiction_rule=(
            "Mark contradicted if the answer treats membrane rejection as "
            "PFAS degradation or destruction."
        ),
    )
    update_group(
        ledger,
        "WF10_002-G04",
        canonical_proposition=(
            "The GAP study reports parent-analyte disappearance, degradation-"
            "product formation, and defluorination as separate measurements; "
            "the listed endpoints should not be collapsed into one measured "
            "quantity."
        ),
        central_proposition=(
            "GAP reports disappearance, degradation products, and "
            "defluorination as separate measurements."
        ),
        material_qualifiers=[
            "applies to the cited GAP system",
            (
                "the span lists the measurements but does not itself state "
                "that any one is formally insufficient"
            ),
        ],
        full_rule=(
            "Award full if the answer identifies all three GAP chemical "
            "measurements and keeps them distinct without claiming the source "
            "explicitly proved a formal sufficiency rule."
        ),
        partial_rule=(
            "Award partial if the answer identifies at least two of the three "
            "GAP chemical measurements as distinct."
        ),
        contradiction_rule=(
            "Mark contradicted if the answer treats parent disappearance, "
            "degradation-product formation, and defluorination as the same "
            "measured endpoint."
        ),
    )
    update_group(
        ledger,
        "WF10_002-G05",
        canonical_proposition=(
            "Across the three represented treatment contexts, membrane "
            "filtration reports separation/rejection or concentration, GAP "
            "reports disappearance, degradation products, and defluorination, "
            "and SCWO reports mineralization and short-chain byproduct "
            "formation; these are different endpoint categories and should be "
            "reported separately."
        ),
        central_proposition=(
            "Membrane, GAP, and SCWO studies report different endpoint "
            "categories that are not interchangeable."
        ),
        material_qualifiers=[
            "membrane: separation/rejection and concentration",
            "GAP: disappearance, degradation products, and defluorination",
            "SCWO: mineralization and short-chain byproduct formation",
        ],
        evidence_ids=[
            "WF10_002_MMG001",
            "WF10_002_MMG002",
            "WF10_002_L3X001",
            "WF10_002_L3X002",
        ],
        full_rule=(
            "Award full if the answer distinguishes the endpoint categories "
            "for all three treatment contexts rather than using removal, "
            "degradation, defluorination, and mineralization interchangeably."
        ),
        partial_rule=(
            "Award partial if the answer correctly distinguishes endpoints "
            "for two of the three treatment contexts."
        ),
        contradiction_rule=(
            "Mark contradicted if the answer equates membrane rejection, GAP "
            "disappearance, or SCWO mineralization as one identical endpoint."
        ),
    )
    update_group(
        ledger,
        "WF10_002-G06",
        canonical_proposition=(
            "Overall destruction and fluorine mass balance are interpretive "
            "outcomes distinct from individual measurements. In SCWO, a low "
            "fluorine mass balance at 425 and 450 C was interpreted as "
            "possible undetected fluorinated species in gas or liquid "
            "products, showing why target disappearance alone does not close "
            "fluorine fate."
        ),
        central_proposition=(
            "Destruction and mass balance are distinct from individual "
            "endpoints, and incomplete SCWO fluorine balance can indicate "
            "undetected fluorinated products."
        ),
        material_qualifiers=[
            "SCWO temperatures are 425 and 450 C",
            (
                "undetected fluorinated gas or liquid products are an "
                "inference from low fluorine mass-balance closure"
            ),
            "the evidence does not identify or quantify those species",
        ],
        evidence_ids=["WF10_002_MMG001", "WF10_002_L3X003"],
        full_rule=(
            "Award full if the answer keeps overall destruction and fluorine "
            "mass balance separate from individual endpoints and uses the "
            "425/450 C SCWO example with the appropriate uncertainty about "
            "undetected fluorinated products."
        ),
        partial_rule=(
            "Award partial if the answer generally distinguishes mass balance "
            "from individual endpoints but omits the SCWO example or its "
            "uncertainty."
        ),
        contradiction_rule=(
            "Mark contradicted if the answer treats target disappearance as "
            "complete fluorine mass-balance closure or claims the undetected "
            "species were identified and quantified."
        ),
    )
    set_reference(
        ledger,
        [
            (
                "Membrane filtration reports separation or rejection: "
                "high-pressure NF and RO can reject both short- and long-chain "
                "PFAS, while simple membrane routes concentrate PFAS rather "
                "than degrading it.",
                ["WF10_002-G03"],
            ),
            (
                "The GAP study separately reports parent-analyte "
                "disappearance, degradation-product formation, "
                "defluorination, and energy cost.",
                ["WF10_002-G01", "WF10_002-G04"],
            ),
            (
                "The SCWO discussion reports mineralization, temperature "
                "dependence, and minimal short-chain byproduct formation as "
                "separate outcomes.",
                ["WF10_002-G02"],
            ),
            (
                "Therefore membrane separation, GAP disappearance or "
                "degradation measurements, and SCWO mineralization should not "
                "be treated as interchangeable endpoints.",
                ["WF10_002-G05"],
            ),
            (
                "Overall destruction and fluorine mass balance are additional "
                "interpretive outcomes: in one SCWO example, low fluorine "
                "balance at 425 and 450 C suggested undetected fluorinated gas "
                "or liquid products rather than proving complete fate closure.",
                ["WF10_002-G06"],
            ),
            (
                "All of these distinctions remain condition-specific and do "
                "not establish a universal endpoint pattern for every PFAS "
                "technology.",
                ["WF10_002-B01"],
            ),
        ],
    )


def repair_wf10_021(ledger: dict[str, Any]) -> None:
    update_group(
        ledger,
        "WF10_021-G04",
        task_component_id="WF10_021-T01",
        importance="core",
        scoring_role="required_content",
        canonical_proposition=(
            "The supplied matrix-limitation evidence is biochar-specific; it "
            "does not establish analogous matrix effects for activated carbon."
        ),
        central_proposition=(
            "Activated-carbon matrix gaps are not established by the supplied "
            "biochar evidence."
        ),
        material_qualifiers=[
            "scope is the supplied evidence set",
            "affirmative matrix evidence concerns biochar",
            "no activated-carbon matrix result is inferred",
        ],
        evidence_ids=["WF10_021_MMG001"],
        full_rule=(
            "Award full if the answer explicitly states that the matrix "
            "evidence is biochar-specific and does not establish the "
            "activated-carbon case."
        ),
        partial_rule=(
            "Award partial if the answer discusses biochar matrix limitations "
            "without explicitly identifying the activated-carbon evidence gap."
        ),
        contradiction_rule=(
            "Mark contradicted if the answer generalizes the biochar matrix "
            "finding to activated carbon as a demonstrated result."
        ),
    )
    source = copy.deepcopy(content_group(ledger, "WF10_021-G04"))
    source.update(
        {
            "claim_group_id": "WF10_021-G05",
            "task_component_id": "WF10_021-T02",
            "canonical_proposition": (
                "The supplied regeneration and reuse limitations are "
                "biochar-specific; they do not establish analogous "
                "regeneration behavior for activated carbon."
            ),
            "central_proposition": (
                "Activated-carbon regeneration gaps are not established by "
                "the supplied biochar evidence."
            ),
            "material_qualifiers": [
                "scope is the supplied evidence set",
                "affirmative regeneration evidence concerns biochar",
                "no activated-carbon regeneration result is inferred",
            ],
            "evidence_ids": ["WF10_021_MMG002", "WF10_021_MMG003"],
            "full_rule": (
                "Award full if the answer explicitly states that the "
                "regeneration evidence is biochar-specific and does not "
                "establish the activated-carbon case."
            ),
            "partial_rule": (
                "Award partial if the answer discusses biochar regeneration "
                "limitations without identifying the activated-carbon "
                "evidence gap."
            ),
            "contradiction_rule": (
                "Mark contradicted if the answer generalizes the biochar "
                "regeneration finding to activated carbon as a demonstrated "
                "result."
            ),
        }
    )
    ledger["claim_groups"].append(source)
    set_reference(
        ledger,
        [
            (
                "For biochar, organic matter can have highly variable effects "
                "on PFAS sorption across water matrices, leaving a need for "
                "matrix-specific optimization.",
                ["WF10_021-G01"],
            ),
            (
                "Biochar regeneration has been studied too infrequently for "
                "definitive efficacy conclusions, and repeated cycles can "
                "alter morphology, functionality, and porosity.",
                ["WF10_021-G02", "WF10_021-G03"],
            ),
            (
                "The supplied matrix evidence is biochar-specific and does "
                "not establish analogous matrix behavior for activated carbon.",
                ["WF10_021-G04"],
            ),
            (
                "Likewise, the supplied regeneration evidence is "
                "biochar-specific and does not establish activated-carbon "
                "regeneration behavior.",
                ["WF10_021-G05"],
            ),
            (
                "These evidence gaps should be reported rather than filled by "
                "generalizing biochar findings to activated carbon.",
                ["WF10_021-B01"],
            ),
        ],
    )


def repair_wf10_004b(ledger: dict[str, Any]) -> None:
    update_group(
        ledger,
        "WF10_004b-G07",
        canonical_proposition=(
            "In the reported laser-made [Ni0.75Fe0.25]-(OH)2 hydrophilic "
            "carbon-fiber-paper anode study, PFAS headgroup identity did not "
            "govern adsorption; available adsorption sites and oxidant "
            "generation instead imposed a concentration limit on efficient "
            "defluorination under those study conditions."
        ),
        central_proposition=(
            "Headgroup identity did not govern adsorption at the reported "
            "anode; anode-site and oxidant constraints limited efficient "
            "defluorination."
        ),
        material_qualifiers=[
            (
                "anode is laser-made [Ni0.75Fe0.25]-(OH)2 on hydrophilic "
                "carbon fiber paper"
            ),
            "the finding is condition-specific",
            (
                "the expanded span discusses similar concentration dependence "
                "for GenX and PFOS but does not support a universal PFAS rule"
            ),
            (
                "pulsed-electrolysis and LiOH details are not required by "
                "this claim group"
            ),
        ],
        full_rule=(
            "Award full if the answer states that headgroup identity did not "
            "govern adsorption at the specified anode and identifies "
            "available sites or oxidant generation as the limiting anode "
            "characteristics, without adding unsupported process conditions."
        ),
        partial_rule=(
            "Award partial if the answer reports the negative headgroup "
            "finding but omits the anode-specific limiting characteristics."
        ),
        contradiction_rule=(
            "Mark contradicted if the answer says headgroup identity governed "
            "adsorption in this study or universalizes the finding."
        ),
    )
    set_reference(
        ledger,
        [
            (
                "Several foam-fractionation studies reported higher removal "
                "of sulfonate PFAS than carboxylate PFAS under their specific "
                "conditions.",
                ["WF10_004b-G01"],
            ),
            (
                "Iron-based batch and column systems likewise showed stronger "
                "removal or retention of sulfonates than matched carboxylates "
                "in the cited examples.",
                ["WF10_004b-G04"],
            ),
            (
                "In nanofiltration, neutral FHxSA showed lower rejection than "
                "anionic PFHxS because the neutral compound lacked an "
                "electrostatic-repulsion mechanism.",
                ["WF10_004b-G05"],
            ),
            (
                "All-silica zeolite beta showed the opposite class trend, "
                "with lower capacity and affinity for sulfonic-acid PFAS than "
                "for carboxylic-acid PFAS.",
                ["WF10_004b-G06"],
            ),
            (
                "At a laser-made [Ni0.75Fe0.25]-(OH)2 hydrophilic "
                "carbon-fiber-paper anode, headgroup identity did not govern "
                "adsorption; available sites and oxidant generation instead "
                "limited efficient defluorination at higher concentration.",
                ["WF10_004b-G07"],
            ),
            (
                "The direction of headgroup effects is therefore specific to "
                "the process, material, charge state, and conditions, and no "
                "universal headgroup rule is supported.",
                ["WF10_004b-G08", "WF10_004b-B01"],
            ),
        ],
    )


REPAIR_FUNCTIONS = {
    "NQ10": repair_nq10,
    "NQ12": repair_nq12,
    "NQ15": repair_nq15,
    "NQ23": repair_nq23,
    "NQ24": repair_nq24,
    "NQ26": repair_nq26,
    "WF10_002": repair_wf10_002,
    "WF10_021": repair_wf10_021,
    "WF10_004b": repair_wf10_004b,
}


def main() -> None:
    packet_by_qid = {
        row["question_id"]: row for row in common.read_jsonl(PACKETS)
    }
    component_by_qid = {
        row["question_id"]: row
        for row in common.read_jsonl(revision.TASK_COMPONENTS)
    }
    draft_by_qid = {
        row["question_id"]: row["draft"]
        for row in common.read_jsonl(common.DRAFTS)
    }
    review_by_qid = {
        row["question_id"]: row
        for row in common.read_jsonl(SOURCE_REVIEWS)
    }
    source_rows = common.read_jsonl(SOURCE_REVISIONS)
    output_rows = []
    changed_qids = []
    for source_row in source_rows:
        qid = str(source_row["question_id"])
        ledger = copy.deepcopy(source_row["revision"])
        repair_function = REPAIR_FUNCTIONS.get(qid)
        if repair_function is not None:
            repair_function(ledger)
            changed_qids.append(qid)
        # WF10_025 requires no wording change, but its complete original chunk
        # is now normative evidence and therefore changes the ledger payload.
        if qid == "WF10_025":
            changed_qids.append(qid)
        sync_exact_spans(ledger, packet_by_qid[qid])
        revision.normalize_disposition_targets(ledger)
        revision.validate_revision(
            ledger,
            packet_by_qid[qid],
            component_by_qid[qid],
            draft_by_qid[qid],
        )
        output_rows.append(
            {
                "question_id": qid,
                "packet_sha256": common.payload_sha256(packet_by_qid[qid]),
                "task_components_sha256": common.payload_sha256(
                    component_by_qid[qid]
                ),
                "previous_revision_sha256": common.payload_sha256(
                    source_row["revision"]
                ),
                "previous_group_review_sha256": common.payload_sha256(
                    review_by_qid[qid]["review"]
                ),
                "prompt_sha256": common.sha256(PREAUDIT),
                "revision": ledger,
                "generation": {
                    "repair_method": "deterministic_assistant_preaudit_repair5",
                    "repair_skipped": qid not in changed_qids,
                    "source_revision": str(
                        SOURCE_REVISIONS.relative_to(common.ROOT)
                    ),
                    "source_review": str(
                        SOURCE_REVIEWS.relative_to(common.ROOT)
                    ),
                    "preaudit": str(PREAUDIT.relative_to(common.ROOT)),
                },
            }
        )
    common.write_jsonl(OUTPUT, output_rows)
    common.write_json(
        MANIFEST,
        {
            "stage": "Deterministic L3 repair5 ledger repair",
            "question_count": len(output_rows),
            "changed_question_ids": sorted(changed_qids),
            "changed_question_count": len(changed_qids),
            "unchanged_question_ids": sorted(
                set(packet_by_qid) - set(changed_qids)
            ),
            "source_revisions_file": str(
                SOURCE_REVISIONS.relative_to(common.ROOT)
            ),
            "source_revisions_sha256": common.sha256(SOURCE_REVISIONS),
            "source_reviews_sha256": common.sha256(SOURCE_REVIEWS),
            "packets_file": str(PACKETS.relative_to(common.ROOT)),
            "packets_sha256": common.sha256(PACKETS),
            "preaudit_sha256": common.sha256(PREAUDIT),
            "output_sha256": common.sha256(OUTPUT),
            "candidate_answers_used": False,
            "test40_used": False,
        },
    )
    print(
        json.dumps(
            {
                "questions": len(output_rows),
                "changed": sorted(changed_qids),
                "output": str(OUTPUT),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
