from __future__ import annotations

import re


TOKEN_PATTERN = re.compile(r"\w+|[^\w\s]", re.UNICODE)
SENTENCE_END_PATTERN = re.compile(r"(?<=[.!?])\s+")


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def estimate_token_count(text: str) -> int:
    return len(TOKEN_PATTERN.findall(text))


def split_sentences(text: str) -> list[str]:
    paragraphs = [paragraph.strip() for paragraph in normalize_text(text).split("\n") if paragraph.strip()]
    sentences: list[str] = []
    for paragraph in paragraphs:
        parts = SENTENCE_END_PATTERN.split(paragraph)
        sentences.extend(part.strip() for part in parts if part.strip())
    return sentences


def split_long_sentence(sentence: str, max_tokens: int) -> list[str]:
    tokens = TOKEN_PATTERN.findall(sentence)
    if len(tokens) <= max_tokens:
        return [sentence]

    chunks = []
    for index in range(0, len(tokens), max_tokens):
        chunks.append(" ".join(tokens[index : index + max_tokens]).strip())
    return [chunk for chunk in chunks if chunk]


def fit_overlap_sentences(sentences: list[str], max_tokens: int) -> list[str]:
    overlap = list(sentences)
    while overlap and sum(estimate_token_count(sentence) for sentence in overlap) > max_tokens:
        overlap.pop(0)
    return overlap


def chunk_text(text: str, chunk_size: int, overlap: int = 0, overlap_sentences: int = 2) -> list[str]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    if overlap < 0:
        raise ValueError("overlap must be non-negative")
    if overlap_sentences < 0:
        raise ValueError("overlap_sentences must be non-negative")

    text = normalize_text(text)
    if not text:
        return []

    sentences: list[str] = []
    for sentence in split_sentences(text):
        sentences.extend(split_long_sentence(sentence, chunk_size))

    chunks: list[str] = []
    current_sentences: list[str] = []
    current_tokens = 0

    for sentence in sentences:
        sentence_tokens = estimate_token_count(sentence)
        if current_sentences and current_tokens + sentence_tokens > chunk_size:
            chunks.append(" ".join(current_sentences).strip())
            current_sentences = (
                fit_overlap_sentences(current_sentences[-overlap_sentences:], chunk_size)
                if overlap_sentences
                else []
            )
            current_tokens = sum(estimate_token_count(item) for item in current_sentences)
            while current_sentences and current_tokens + sentence_tokens > chunk_size:
                removed = current_sentences.pop(0)
                current_tokens -= estimate_token_count(removed)

        current_sentences.append(sentence)
        current_tokens += sentence_tokens

    if current_sentences:
        chunks.append(" ".join(current_sentences).strip())

    return [chunk for chunk in chunks if chunk]
