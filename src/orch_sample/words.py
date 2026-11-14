"""Count words in text."""

import re

_WORD = re.compile(r"[^\W_]+(?:'[^\W_]+)?")


def words(text: str) -> list[str]:
    """Return the words of text in order. An apostrophe inside a word is kept."""
    return _WORD.findall(text)


def word_count(text: str) -> int:
    """Return the number of words in text."""
    return len(words(text))
