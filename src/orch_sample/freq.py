"""Count how often each word occurs."""

from collections import Counter

from orch_sample.words import words


def word_frequencies(text: str, top: int | None = None) -> list[tuple[str, int]]:
    """Return (word, count) pairs, most frequent first, ignoring case."""
    if top is not None and top < 0:
        raise ValueError("top must not be negative")
    counts = Counter(word.lower() for word in words(text))
    # Counter keeps first-seen order and sorted() is stable, so ties keep it.
    ordered = sorted(counts.items(), key=lambda item: -item[1])
    if top is not None:
        return ordered[:top]
    return ordered
