from __future__ import annotations

from collections import Counter
import json
import math
import os
import re

from openai import OpenAI

from .config import Settings
from .ingest import get_collection


SYSTEM_PROMPT = """You are a careful scientific literature assistant for PFAS treatment research.
Answer the user's question using only the provided context.

Requirements:
1. Use only the supplied context. Do not use outside knowledge.
2. If the context is fully insufficient, say:
   "Based on the provided information, I cannot answer this question."
   If the context is only partially sufficient, provide the narrowest answer supported by the evidence and explicitly state what is missing.
3. Do not fabricate information or citations.
4. Do not treat related technical terms as interchangeable unless the context explicitly supports it.
   In particular, distinguish between removal, separation, degradation, destruction, defluorination, and mineralization.
5. If the evidence is conditional, limited, or conflicting, state this explicitly.
6. Support each major claim with the corresponding citation(s) immediately after the claim whenever possible.
   Do not attach citations that do not directly support the specific statement.
7. Do not generalize a finding from a single study into a field-wide conclusion unless multiple retrieved sources support it.
8. If the retrieved evidence supports only a weaker or narrower claim, state that weaker claim instead of a stronger one.
   For example, do not state mineralization when the evidence supports only degradation or defluorination.
9. If the question contains ambiguous evaluative terms such as "best", "most mature", "most effective", or "most promising",
   interpret them cautiously based on the retrieved evidence, and do not claim a universal answer unless the context clearly supports one.
10. Prefer synthesis over quotation. Use short quotations only when necessary."""
RERANK_SYSTEM_PROMPT = """You are a document relevance evaluator for PFAS treatment literature question answering.

Your task is to score whether each retrieved chunk contains useful evidence for answering the research question.

Evaluate each chunk on these criteria:
1. Question relevance:
   Does the chunk directly address the question or one of its core concepts?
2. Evidence value:
   Does the chunk contain concrete evidence such as findings, comparisons, mechanisms, treatment performance, limitations, or conditions?
3. Answer usefulness:
   Would this chunk help produce a precise, evidence-grounded answer rather than only broad background?

Scoring guidance:
- 9-10: Directly answers the question with concrete evidence.
- 7-8: Strongly relevant and useful, but incomplete or indirect.
- 5-6: Partially relevant; may provide context or supporting detail.
- 3-4: Weak relevance; mostly background, methods-only detail, or marginal context.
- 0-2: Not useful for answering the question.

Important rules:
- Prefer chunks with direct findings, comparisons, limitations, treatment conditions, PFAS-specific behavior, water matrix effects, defluorination, destruction, or mineralization evidence.
- Score background-only chunks lower unless the question explicitly asks for background or overview.
- Score methods-only chunks lower unless they directly help answer the question.
- Score references sections very low unless they contain uniquely useful evidence.
- Do not reward a chunk simply for containing overlapping keywords.

Return valid JSON only.
For each chunk, include:
- score
- short_reason
- evidence_type (e.g., direct finding, comparison, mechanism, limitation, background, methods-only, references)
- covered_evidence: a list of short labels for distinct evidence points this chunk helps cover
- redundancy_risk: low, medium, or high compared with other candidate chunks"""
FIELD_TAGGER_SYSTEM_PROMPT = """You are an evidence-field tagger for a PFAS literature-grounded RAG benchmark.

Your task is NOT to write the answer and NOT to use outside knowledge.
For each candidate chunk, decide whether it contains explicit evidence useful for answering the benchmark question.

Classify each chunk:
- direct_support: explicitly supports a required answer element.
- partial_support: useful but missing key fields.
- negative_support: helps show a claim is unsupported, limited, or not generalizable.
- decoy: looks relevant but would mislead if used as support.
- background: general background only.
- irrelevant: not useful.

Important rules:
- Do not reward superficial keyword overlap.
- Do not infer missing values, units, compounds, matrices, methods, endpoints, or protocol details.
- For numeric_extraction, exact values and units are high priority.
- For protocol_extraction, concrete protocol steps, reagents, volumes, conditions, cartridges, blanks, standards, QA/QC, or containers are high priority.
- For endpoint_distinction, chunks distinguishing removal, adsorption, separation, degradation, defluorination, mineralization, or destruction are high priority.
- For unsupported_claim_detection, limitations, verification gaps, negative evidence, and overgeneralization risks are high priority.
- Methods-only chunks should be high priority if the task asks for protocols, LOD/LOQ, QA/QC, blanks, standards, containers, or analytical workflows.
- Background-only chunks should be low priority unless the question asks for general background.
- References sections should be low priority.

Return valid JSON only."""


STOPWORDS = {
    "about",
    "after",
    "also",
    "and",
    "are",
    "can",
    "for",
    "from",
    "has",
    "have",
    "how",
    "into",
    "its",
    "the",
    "their",
    "this",
    "what",
    "when",
    "which",
    "with",
}
def tokenize(text: str) -> set[str]:
    terms = re.findall(r"[a-z0-9][a-z0-9-]{2,}", text.lower())
    return {term for term in terms if term not in STOPWORDS}


def tokenize_list(text: str) -> list[str]:
    terms = re.findall(r"[a-z0-9][a-z0-9-]{2,}", text.lower())
    return [term for term in terms if term not in STOPWORDS]


def metadata_to_hit(document: str, metadata: dict | None, distance: float | None = None) -> dict:
    metadata = metadata or {}
    hit = {
        "text": document,
        "source": metadata.get("source", "unknown"),
        "chunk": metadata.get("chunk"),
        "section": metadata.get("section"),
        "year": metadata.get("year"),
        "first_author": metadata.get("first_author"),
        "title": metadata.get("title"),
        "doi": metadata.get("doi"),
        "journal": metadata.get("journal"),
        "volume": metadata.get("volume"),
        "issue": metadata.get("issue"),
        "pages": metadata.get("pages"),
        "citation_apa": metadata.get("citation_apa"),
        "citation_acs": metadata.get("citation_acs"),
        "distance": distance if distance is not None else 1.0,
        "dense_rank": None,
        "bm25_rank": None,
        "bm25_score": 0.0,
        "retrieval_source": "",
    }
    return hit


def hit_key(hit: dict) -> tuple[str, int | str | None]:
    return hit.get("source", "unknown"), hit.get("chunk")


def is_article_front_matter(hit: dict, lower: str) -> bool:
    chunk = hit.get("chunk")
    try:
        chunk_number = int(chunk)
    except (TypeError, ValueError):
        chunk_number = None

    front_matter_markers = {
        "abstract",
        "received",
        "accepted",
        "correspondence",
        "cite this",
        "original research",
        "research article",
        "paper",
    }
    article_identity_markers = {
        "doi",
        "journal",
        "rsc.li",
        "environmental science",
        "water research",
    }
    marker_count = sum(1 for marker in front_matter_markers if marker in lower[:1800])
    identity_count = sum(1 for marker in article_identity_markers if marker in lower[:1800])
    if chunk_number == 0 and marker_count >= 1 and identity_count >= 1:
        return True
    return marker_count >= 2 and "abstract" in lower[:1800]


def is_reference_like(hit: dict) -> bool:
    section = str(hit.get("section") or "").lower()
    text = hit.get("text") or ""
    sample = text[:2500]
    lower = sample.lower()
    stripped = lower.lstrip()
    if stripped.startswith(("references", "bibliography", "literature cited")):
        return True
    if is_article_front_matter(hit, lower):
        return False

    doi_count = len(re.findall(r"\bdoi\b|https?://doi\s*\.?\s*org|doi\s*:", lower))
    crossref_count = lower.count("[crossref]") + lower.count("crossref")
    pubmed_count = lower.count("[pubmed]") + lower.count("pubmed")
    et_al_count = lower.count(" et al.")
    year_count = len(re.findall(r"\b(?:19|20)\d{2}\b", lower))
    numbered_reference_count = len(
        re.findall(r"(?:^|\s)(?:\[\d{1,3}\]|\(\d{1,3}\)|\d{1,3}\.?)\s+[A-Z]", sample)
    )
    semicolon_count = sample.count(";")
    journal_marker_count = len(
        re.findall(
            r"\b(?:water res|j\.|journal|environ|chem|sci|technol|hazard|adsorption|removal)\b",
            lower,
        )
    )
    author_year_reference_count = len(
        re.findall(r"[A-Z][A-Za-z-]+,\s+(?:[A-Z]\.,\s+){0,6}(?:19|20)\d{2}[a-z]?\.", sample)
    )
    author_initial_count = len(re.findall(r"[A-Z][A-Za-z-]+,\s+(?:[A-Z]\.\s*){1,4}", sample))

    if section == "references" and (
        doi_count >= 1
        or crossref_count >= 1
        or numbered_reference_count >= 2
        or author_year_reference_count >= 2
        or year_count >= 5
    ):
        return True
    if "view article online" in lower and (crossref_count or doi_count) and not is_article_front_matter(hit, lower):
        return True
    if crossref_count >= 3 or pubmed_count >= 3:
        return True
    if doi_count >= 3 and et_al_count >= 3:
        return True
    if doi_count >= 2 and year_count >= 4:
        return True
    if doi_count >= 2 and year_count >= 4 and journal_marker_count >= 4:
        return True
    if numbered_reference_count >= 2 and doi_count >= 1:
        return True
    if numbered_reference_count >= 3 and (year_count >= 3 or semicolon_count >= 8):
        return True
    if year_count >= 6 and journal_marker_count >= 5 and semicolon_count >= 12:
        return True
    if author_year_reference_count >= 3 and journal_marker_count >= 5:
        return True
    if author_initial_count >= 8 and year_count >= 3 and (journal_marker_count >= 3 or doi_count >= 1):
        return True
    if year_count >= 3 and journal_marker_count >= 6 and stripped[:80].startswith(("j.", "water res")):
        return True
    if year_count >= 10 and et_al_count >= 6:
        return True
    if numbered_reference_count >= 5:
        return True
    return False


def reference_penalty(text: str) -> float:
    lower = text[:2000].lower()
    reference_markers = lower.count(" doi:") + lower.count(" et al.") + lower.count(" references")
    if lower.lstrip().startswith(("references", "bibliography")):
        return 0.25
    if reference_markers >= 8:
        return 0.15
    return 0.0


def bm25_search(collection, question: str, n_results: int) -> list[dict]:
    query_terms = tokenize_list(question)
    if not query_terms or n_results <= 0:
        return []

    data = collection.get(include=["documents", "metadatas"])
    documents = data.get("documents", []) or []
    metadatas = data.get("metadatas", []) or []
    if not documents:
        return []

    tokenized_docs = [tokenize_list(document) for document in documents]
    doc_freq: Counter[str] = Counter()
    for terms in tokenized_docs:
        doc_freq.update(set(terms))

    avg_doc_len = sum(len(terms) for terms in tokenized_docs) / max(len(tokenized_docs), 1)
    query_counts = Counter(query_terms)
    scores: list[tuple[float, int]] = []
    k1 = 1.5
    b = 0.75
    total_docs = len(documents)

    for index, terms in enumerate(tokenized_docs):
        if not terms:
            continue
        term_counts = Counter(terms)
        doc_len = len(terms)
        score = 0.0
        for term, query_count in query_counts.items():
            if term not in term_counts:
                continue
            idf = math.log(1 + (total_docs - doc_freq[term] + 0.5) / (doc_freq[term] + 0.5))
            tf = term_counts[term]
            denom = tf + k1 * (1 - b + b * doc_len / avg_doc_len)
            score += query_count * idf * (tf * (k1 + 1) / denom)
        if score > 0:
            scores.append((score, index))

    top = sorted(scores, key=lambda item: item[0], reverse=True)[:n_results]
    hits = []
    for rank, (score, index) in enumerate(top, start=1):
        hit = metadata_to_hit(documents[index], metadatas[index], distance=1.0)
        hit["bm25_rank"] = rank
        hit["bm25_score"] = score
        hit["retrieval_source"] = "bm25"
        hits.append(hit)
    return hits


def merge_hits(dense_hits: list[dict], bm25_hits: list[dict]) -> list[dict]:
    merged: dict[tuple[str, int | str | None], dict] = {}
    for rank, hit in enumerate(dense_hits, start=1):
        hit["dense_rank"] = rank
        hit["retrieval_source"] = "dense"
        merged[hit_key(hit)] = hit

    for hit in bm25_hits:
        key = hit_key(hit)
        if key in merged:
            existing = merged[key]
            existing["bm25_rank"] = hit.get("bm25_rank")
            existing["bm25_score"] = hit.get("bm25_score", 0.0)
            existing["retrieval_source"] = "hybrid"
        else:
            merged[key] = hit

    return list(merged.values())


def rerank_hits(settings: Settings, question: str, hits: list[dict], top_k: int) -> list[dict]:
    query_terms = tokenize(question)
    if not hits:
        return []

    max_distance = max(float(hit.get("distance") or 0.0) for hit in hits) or 1.0
    max_bm25 = max(float(hit.get("bm25_score") or 0.0) for hit in hits) or 1.0
    for index, hit in enumerate(hits):
        text = " ".join(
            str(value or "")
            for value in (hit.get("title"), hit.get("source"), hit.get("text"))
        )
        text_terms = tokenize(text)
        lexical_score = (
            len(query_terms & text_terms) / len(query_terms)
            if query_terms
            else 0.0
        )
        vector_score = 1.0 - (float(hit.get("distance") or 0.0) / max_distance)
        bm25_score = float(hit.get("bm25_score") or 0.0) / max_bm25
        score = (
            (0.65 * vector_score)
            + (0.2 * bm25_score)
            + (0.15 * lexical_score)
            - reference_penalty(hit["text"])
        )
        hit["retrieval_rank"] = index + 1
        hit["rerank_score"] = score
        hit["reference_like"] = is_reference_like(hit)

    ranked = sorted(hits, key=lambda hit: hit["rerank_score"], reverse=True)
    if not settings.reference_filter:
        return ranked[:top_k]

    evidence_hits = [hit for hit in ranked if not hit.get("reference_like")]
    reference_hits = [hit for hit in ranked if hit.get("reference_like")]
    return (evidence_hits + reference_hits)[:top_k]


def compact_text(text: str, max_chars: int = 900) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rsplit(" ", 1)[0] + "..."


def parse_rerank_json(content: str) -> dict:
    content = content.strip()
    try:
        return json.loads(content, strict=False)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", content, re.DOTALL)
        if not match:
            return {}
        try:
            return json.loads(match.group(0), strict=False)
        except json.JSONDecodeError:
            return {}


def document_id_to_int(document_id: str) -> int | None:
    match = re.search(r"\d+", document_id)
    return int(match.group(0)) if match else None


def normalize_evidence_label(label: str) -> str:
    label = re.sub(r"[^a-z0-9 -]+", " ", str(label).lower())
    label = re.sub(r"\s+", " ", label).strip()
    return label[:80]


def parse_covered_evidence(value) -> list[str]:
    if isinstance(value, list):
        labels = value
    elif isinstance(value, str):
        labels = re.split(r"[;,|]\s*", value)
    else:
        labels = []
    normalized = []
    seen = set()
    for label in labels:
        cleaned = normalize_evidence_label(label)
        if cleaned and cleaned not in seen:
            normalized.append(cleaned)
            seen.add(cleaned)
    return normalized[:6]


FIELD_COVERAGE_KEYS = [
    "compound",
    "matrix",
    "method_or_material",
    "endpoint",
    "numerical_value",
    "unit",
    "protocol_detail",
    "limitation",
    "negative_evidence",
    "comparison",
]


def parse_bool(value) -> bool:
    if isinstance(value, bool):
        return value
    return str(value or "").strip().lower() in {"1", "true", "yes", "y"}


def parse_field_coverage(value) -> dict[str, bool]:
    if not isinstance(value, dict):
        value = {}
    return {key: parse_bool(value.get(key)) for key in FIELD_COVERAGE_KEYS}


def parse_risk_flags(value) -> dict[str, bool]:
    keys = [
        "background_only",
        "methods_only",
        "references_section",
        "decoy_risk",
        "overgeneralization_risk",
        "redundant_with_prior_chunks",
    ]
    if not isinstance(value, dict):
        value = {}
    return {key: parse_bool(value.get(key)) for key in keys}


def required_fields_for_question(question_metadata: dict | None) -> set[str]:
    metadata = question_metadata or {}
    task_type = str(metadata.get("task_type") or "").lower()
    fields: set[str] = {"compound", "matrix", "method_or_material", "limitation"}
    if "numeric" in task_type or parse_bool(metadata.get("requires_numeric_extraction")):
        fields.update({"compound", "matrix", "method_or_material", "endpoint", "numerical_value", "unit"})
    if "protocol" in task_type or parse_bool(metadata.get("requires_protocol_extraction")):
        fields.update({"method_or_material", "protocol_detail", "matrix", "compound", "limitation"})
    if "endpoint" in task_type or parse_bool(metadata.get("requires_endpoint_distinction")):
        fields.update({"endpoint", "limitation", "negative_evidence"})
    if "unsupported_claim" in task_type:
        fields.update({"negative_evidence", "limitation"})
    if "comparison" in task_type or "cross_study" in task_type:
        fields.update({"comparison", "compound", "matrix", "method_or_material", "endpoint"})
    return fields


def redundancy_penalty(value: str) -> float:
    risk = str(value or "").strip().lower()
    if risk.startswith("high"):
        return 1.0
    if risk.startswith("med"):
        return 0.45
    return 0.0


def select_coverage_aware_hits(scored_hits: list[dict], candidates: list[dict], top_k: int) -> list[dict]:
    """Select relevant, complementary chunks without hand-tuned linear weights.

    The intent is a pre-registered, explainable strategy:
    filter out clearly weak chunks, greedily maximize newly covered evidence labels,
    then tie-break by LLM relevance and the original hybrid rank.
    """
    remaining = list(scored_hits)
    selected_hits = []
    selected_ids = set()
    covered_labels: set[str] = set()
    selected_evidence_types: set[str] = set()
    relevance_threshold = 5.0

    while remaining and len(selected_hits) < top_k:
        relevant_remaining = [
            hit for hit in remaining if float(hit.get("llm_relevance_score", 0.0)) >= relevance_threshold
        ]
        pool = relevant_remaining or remaining

        def coverage_key(hit: dict) -> tuple[int, int, int, float, float, int]:
            labels = set(hit.get("llm_covered_evidence") or [])
            new_label_count = len(labels - covered_labels)
            evidence_type = str(hit.get("llm_evidence_type") or "").lower()
            new_type = 1 if evidence_type and evidence_type not in selected_evidence_types else 0
            score = float(hit.get("llm_relevance_score", 0.0))
            redundant_without_gain = (
                1
                if new_label_count == 0
                and redundancy_penalty(hit.get("llm_redundancy_risk", "")) > 0
                else 0
            )
            original_rank = int(hit.get("retrieval_rank") or hit.get("dense_rank") or hit.get("bm25_rank") or 999999)
            return (
                new_label_count,
                new_type,
                -redundant_without_gain,
                score,
                float(hit.get("rerank_score", 0.0)),
                -original_rank,
            )

        best = max(pool, key=coverage_key)
        selected_hits.append(best)
        selected_ids.add(id(best))
        covered_labels.update(best.get("llm_covered_evidence") or [])
        if best.get("llm_evidence_type"):
            selected_evidence_types.add(str(best.get("llm_evidence_type")).lower())
        remaining = [hit for hit in remaining if id(hit) != id(best)]

    for hit in candidates:
        if len(selected_hits) >= top_k:
            break
        if id(hit) not in selected_ids:
            selected_hits.append(hit)
            selected_ids.add(id(hit))

    for rank, hit in enumerate(selected_hits, start=1):
        hit["llm_rerank_rank"] = rank
    return selected_hits


def protect_count_from_mode(mode: str) -> int:
    match = re.search(r"protect[_-]?(\d+)", mode)
    if match:
        return max(0, int(match.group(1)))
    return 5


def support_priority(hit: dict, task_type: str) -> int:
    label = str(hit.get("llm_support_label") or "").lower()
    if label == "direct_support":
        return 5
    if label == "negative_support":
        return 5 if "unsupported_claim" in task_type else 4
    if label == "partial_support":
        return 3
    if label == "decoy":
        return -3
    if label == "background":
        return -1
    if label == "irrelevant":
        return -5
    return 0


def selected_field_set(hits: list[dict]) -> set[str]:
    fields: set[str] = set()
    for hit in hits:
        coverage = hit.get("llm_field_coverage") or {}
        fields.update(key for key, present in coverage.items() if present)
    return fields


def select_filterfill_hits(
    scored_hits: list[dict],
    candidates: list[dict],
    top_k: int,
    question_metadata: dict | None,
    protect_n: int,
) -> list[dict]:
    protected = list(candidates[: min(protect_n, top_k, len(candidates))])
    selected_hits = list(protected)
    selected_ids = {id(hit) for hit in selected_hits}
    task_type = str((question_metadata or {}).get("task_type") or "").lower()
    required_fields = required_fields_for_question(question_metadata)
    covered_fields = selected_field_set(selected_hits)
    remaining = [hit for hit in scored_hits if id(hit) not in selected_ids]

    def selectable(hit: dict) -> bool:
        label = str(hit.get("llm_support_label") or "").lower()
        risks = hit.get("llm_risk_flags") or {}
        if label in {"irrelevant", "decoy"}:
            return False
        if risks.get("references_section"):
            return False
        if label == "background" and risks.get("background_only"):
            return False
        return True

    while remaining and len(selected_hits) < top_k:
        pool = [hit for hit in remaining if selectable(hit)] or remaining

        def fill_key(hit: dict) -> tuple[int, int, int, int, int, float, float, int]:
            coverage = hit.get("llm_field_coverage") or {}
            hit_fields = {key for key, present in coverage.items() if present}
            new_required = len((hit_fields & required_fields) - covered_fields)
            new_any = len(hit_fields - covered_fields)
            exact_value_bonus = int(coverage.get("numerical_value", False) and coverage.get("unit", False))
            protocol_bonus = int(coverage.get("protocol_detail", False))
            endpoint_bonus = int(coverage.get("endpoint", False))
            score = float(hit.get("llm_relevance_score", 0.0))
            original_rank = int(hit.get("retrieval_rank") or hit.get("dense_rank") or hit.get("bm25_rank") or 999999)
            return (
                new_required,
                support_priority(hit, task_type),
                exact_value_bonus,
                protocol_bonus,
                endpoint_bonus,
                score,
                float(hit.get("rerank_score", 0.0)),
                -original_rank,
            )

        best = max(pool, key=fill_key)
        selected_hits.append(best)
        selected_ids.add(id(best))
        covered_fields.update(selected_field_set([best]))
        remaining = [hit for hit in remaining if id(hit) != id(best)]

    for hit in candidates:
        if len(selected_hits) >= top_k:
            break
        if id(hit) not in selected_ids:
            selected_hits.append(hit)
            selected_ids.add(id(hit))

    for rank, hit in enumerate(selected_hits, start=1):
        hit["llm_rerank_rank"] = rank
        hit["llm_rerank_strategy"] = f"filterfill_protect{protect_n}"
    return selected_hits


def llm_rerank_hits(
    settings: Settings,
    question: str,
    hits: list[dict],
    top_k: int,
    question_metadata: dict | None = None,
) -> list[dict]:
    if not hits or not os.getenv("OPENAI_API_KEY"):
        return hits[:top_k]

    candidates = hits[: settings.llm_rerank_k]
    blocks = []
    id_to_hit = {}
    for index, hit in enumerate(candidates, start=1):
        id_to_hit[index] = hit
        citation = hit.get("citation_acs") or hit.get("title") or hit.get("source", "unknown")
        section = hit.get("section") or "unknown"
        blocks.append(
            f"ID: {index}\n"
            f"Section: {section}\n"
            f"Source: {citation}\n"
            f"Chunk: {compact_text(hit['text'])}"
        )

    client = OpenAI(timeout=120.0, max_retries=0)
    mode = settings.llm_rerank_mode.lower()
    use_field_tagger = mode.startswith("filterfill") or mode.startswith("field")
    metadata = question_metadata or {}
    if use_field_tagger:
        user_prompt = (
            f"Question:\n{question}\n\n"
            "Question metadata:\n"
            f"task_type: {metadata.get('task_type', '')}\n"
            f"answerability_type: {metadata.get('answerability_type', '')}\n"
            f"must_include: {metadata.get('must_include', '')}\n"
            f"must_not_claim: {metadata.get('must_not_claim', '')}\n"
            f"requires_numeric_extraction: {metadata.get('requires_numeric_extraction', '')}\n"
            f"requires_protocol_extraction: {metadata.get('requires_protocol_extraction', '')}\n"
            f"requires_endpoint_distinction: {metadata.get('requires_endpoint_distinction', '')}\n\n"
            "For each candidate chunk, classify support and mark field coverage. "
            "Mark a field true only if it is explicitly present in the chunk.\n\n"
            "Return valid JSON in exactly this format:\n"
            "{\n"
            '  "Document 1": {\n'
            '    "support_label": "direct_support | partial_support | negative_support | decoy | background | irrelevant",\n'
            '    "relevance_score": 0,\n'
            '    "field_coverage": {\n'
            '      "compound": false,\n'
            '      "matrix": false,\n'
            '      "method_or_material": false,\n'
            '      "endpoint": false,\n'
            '      "numerical_value": false,\n'
            '      "unit": false,\n'
            '      "protocol_detail": false,\n'
            '      "limitation": false,\n'
            '      "negative_evidence": false,\n'
            '      "comparison": false\n'
            "    },\n"
            '    "extracted_values": [],\n'
            '    "extracted_units": [],\n'
            '    "endpoint_labels": [],\n'
            '    "risk_flags": {\n'
            '      "background_only": false,\n'
            '      "methods_only": false,\n'
            '      "references_section": false,\n'
            '      "decoy_risk": false,\n'
            '      "overgeneralization_risk": false,\n'
            '      "redundant_with_prior_chunks": false\n'
            "    },\n"
            '    "short_reason": ""\n'
            "  }\n"
            "}\n\n"
            "Candidate documents:\n\n"
            + "\n\n".join(blocks)
        )
        system_prompt = FIELD_TAGGER_SYSTEM_PROMPT
    else:
        user_prompt = (
            f"Question:\n{question}\n\n"
            "Evaluate each retrieved chunk for relevance to this research question.\n\n"
            "Return valid JSON in exactly this format:\n"
            "{\n"
            '  "Document 1": {\n'
            '    "score": 0,\n'
            '    "short_reason": "brief explanation of why it is useful or not useful",\n'
            '    "evidence_type": "direct finding | comparison | mechanism | limitation | background | methods-only | references",\n'
            '    "covered_evidence": ["short evidence point label"],\n'
            '    "redundancy_risk": "low | medium | high"\n'
            "  }\n"
            "}\n\n"
            "For covered_evidence, prefer specific labels such as endpoint distinction, matrix effect, "
            "PFAS class difference, residual stream, regeneration limitation, mineralization evidence, "
            "defluorination evidence, byproduct/PID evidence, treatment condition, or uncertainty/overgeneralization.\n"
            "Do not add a label for superficial keyword overlap.\n\n"
            "Candidate documents:\n\n"
            + "\n\n".join(blocks)
        )
        system_prompt = RERANK_SYSTEM_PROMPT

    response = client.chat.completions.create(
        model=settings.openai_model,
        response_format={"type": "json_object"},
        temperature=0,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    evaluations = parse_rerank_json(response.choices[0].message.content or "")
    scored_hits = []
    for document_id, evaluation in evaluations.items():
        candidate_id = document_id_to_int(document_id)
        if candidate_id not in id_to_hit or not isinstance(evaluation, dict):
            continue
        hit = id_to_hit[candidate_id]
        try:
            score = float(evaluation.get("score", evaluation.get("relevance_score", 0)))
        except (TypeError, ValueError):
            score = 0.0
        hit["llm_relevance_score"] = max(0.0, min(10.0, score))
        hit["llm_reason"] = str(evaluation.get("short_reason", evaluation.get("reason", ""))).strip()
        hit["llm_evidence_type"] = str(evaluation.get("evidence_type", "")).strip()
        hit["llm_covered_evidence"] = parse_covered_evidence(evaluation.get("covered_evidence", []))
        hit["llm_redundancy_risk"] = str(evaluation.get("redundancy_risk", "")).strip().lower()
        hit["llm_support_label"] = str(evaluation.get("support_label", "")).strip().lower()
        hit["llm_field_coverage"] = parse_field_coverage(evaluation.get("field_coverage", {}))
        hit["llm_extracted_values"] = evaluation.get("extracted_values", []) if isinstance(evaluation.get("extracted_values", []), list) else []
        hit["llm_extracted_units"] = evaluation.get("extracted_units", []) if isinstance(evaluation.get("extracted_units", []), list) else []
        hit["llm_endpoint_labels"] = evaluation.get("endpoint_labels", []) if isinstance(evaluation.get("endpoint_labels", []), list) else []
        hit["llm_risk_flags"] = parse_risk_flags(evaluation.get("risk_flags", {}))
        scored_hits.append(hit)

    scored_hits.sort(
        key=lambda hit: (
            hit.get("llm_relevance_score", 0.0),
            hit.get("rerank_score", 0.0),
        ),
        reverse=True,
    )

    if mode.startswith("filterfill") or mode.startswith("field"):
        return select_filterfill_hits(
            scored_hits,
            candidates,
            top_k,
            question_metadata,
            protect_count_from_mode(mode),
        )

    if mode in {"coverage", "coverage_tag", "coverage-aware", "coverage_aware"}:
        return select_coverage_aware_hits(scored_hits, candidates, top_k)

    selected_hits = []
    seen_hit_ids = set()
    for hit in scored_hits:
        hit["llm_rerank_rank"] = len(selected_hits) + 1
        selected_hits.append(hit)
        seen_hit_ids.add(id(hit))
        if len(selected_hits) >= top_k:
            break

    for hit in candidates:
        if len(selected_hits) >= top_k:
            break
        if id(hit) not in seen_hit_ids:
            hit["llm_rerank_rank"] = len(selected_hits) + 1
            selected_hits.append(hit)
            seen_hit_ids.add(id(hit))

    return selected_hits


def retrieve(settings: Settings, question: str, question_metadata: dict | None = None) -> list[dict]:
    collection = get_collection(settings)
    candidate_count = max(settings.retrieval_k, settings.top_k)
    results = collection.query(query_texts=[question], n_results=candidate_count)

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    hits = []
    for document, metadata, distance in zip(documents, metadatas, distances):
        hits.append(metadata_to_hit(document, metadata, distance))

    if settings.retrieval_mode.lower() == "hybrid":
        bm25_hits = bm25_search(collection, question, settings.bm25_k)
        hits = merge_hits(hits, bm25_hits)

    reranked = rerank_hits(settings, question, hits, max(settings.top_k, settings.llm_rerank_k))
    if settings.llm_rerank:
        return llm_rerank_hits(settings, question, reranked, settings.top_k, question_metadata=question_metadata)
    return reranked[: settings.top_k]


def build_context(hits: list[dict]) -> str:
    blocks = []
    for index, hit in enumerate(hits, start=1):
        source = hit["source"]
        chunk = hit["chunk"]
        section = hit.get("section") or "unknown"
        title = hit.get("title") or source
        year = hit.get("year")
        first_author = hit.get("first_author")
        doi = hit.get("doi")
        citation_text = hit.get("citation_acs") or hit.get("citation_apa")
        text = hit["text"]
        citation = citation_text or ", ".join(
            str(value) for value in (first_author, year, title) if value
        )
        doi_text = "" if citation_text or not doi else f", doi={doi}"
        blocks.append(
            f"[{index}] {citation}{doi_text}, source={source}, "
            f"section={section}, chunk={chunk}\n{text}"
        )
    return "\n\n".join(blocks)


def answer(settings: Settings, question: str) -> tuple[str, list[dict]]:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not set. Add it to .env before using ask.")

    hits = retrieve(settings, question)
    context = build_context(hits)
    client = OpenAI()

    response = client.chat.completions.create(
        model=settings.openai_model,
        temperature=0,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": (
                    "Answer the question based only on the provided context.\n\n"
                    "Use this structure:\n"
                    "1. Direct answer\n"
                    "2. Supporting evidence\n"
                    "3. Key limitations or uncertainty\n"
                    "4. Citations for major claims\n\n"
                    f"Context:\n{context}\n\nQuestion:\n{question}"
                ),
            },
        ],
    )

    return response.choices[0].message.content or "", hits
