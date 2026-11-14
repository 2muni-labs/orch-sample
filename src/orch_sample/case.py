"""Convert text between identifier cases."""

import re

_WORDS = re.compile(r"[A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z]+|[A-Z]+|[0-9]+")


def snake_case(text: str) -> str:
    """Return the words of text in lowercase, joined by underscores."""
    return "_".join(word.lower() for word in _WORDS.findall(text))


def camel_case(text: str) -> str:
    """Return the words of text joined in camelCase."""
    words = _WORDS.findall(text)
    if not words:
        return ""
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])
